#operators/ShapeKeysOps.py
# Duin was here. If there is code to blame, it's Zeni's fault. 

import bpy
from bpy.types import Operator

class ZeniTools_OP_BatchShapeKeyTransfer(bpy.types.Operator):
    bl_idname = "zenitools.batch_shape_key_transfer"
    bl_label = "Batch Shape Key Transfer"
    bl_description = "Transfers all Shape Keys from the source mesh to the selected mesh using surface deform."
    bl_options = {'REGISTER', 'UNDO', 'INTERNAL'}

    @classmethod
    def poll(cls, context):
        return context.area.type == 'VIEW_3D' and context.mode == 'OBJECT'

    def execute(self, context):
        props = context.scene
        source_mesh = props.ZeniTools_ShapeKeys_Source_Object
        
        if source_mesh == None:
            self.report({'INFO'}, "No source mesh selected")
            return {'CANCELLED'}

        target_meshes = []
        for obj in bpy.context.selected_objects:
            if isinstance(obj.data, bpy.types.Mesh):
                if obj == source_mesh:
                    self.report({'WARNING'},  "Can't transfer Shape Keys to self. Skipping")
                    continue
                target_meshes.append(obj)

        if len(target_meshes) == 0:
            self.report({'ERROR'},  "No mesh selected")
            return {'CANCELLED'}

        shapeKeysSkipped = 0
        for target_mesh in target_meshes:
            try:
                if target_mesh == None: # This should be impossible. If it happens uhhhh. Explode.
                    self.report({'WARNING'},  "Target and/or source cannot be null.")

                self.report({'INFO'},  f"Transfering Shape Keys from {source_mesh.name} to {target_mesh.name}.")

                # Select the target mesh
                target_mesh.select_set(True)
                bpy.context.view_layer.objects.active = target_mesh
                
                # Create a surface deform modifier
                modifierName = "ZeniBatchShapeKeyTransfer"
                target_mesh.select_set(True)
                surf_def_mod = target_mesh.modifiers.new(name=modifierName, type='SURFACE_DEFORM')

                # Define properties
                surf_def_mod.target = source_mesh
                if not props.ZeniTools_ShapeKeys_ApplyToAllSelected and props.ZeniTools_ShapeKeys_Vertex_Group != "":
                    surf_def_mod.vertex_group = props.ZeniTools_ShapeKeys_Vertex_Group
                    if props.ZeniTools_ShapeKeys_Vertex_Group_Invert:
                        surf_def_mod.invert_vertex_group = True
                # Bind
                bpy.ops.object.surfacedeform_bind(modifier=surf_def_mod.name)

                # Apply shape keys
                for shapekey in source_mesh.data.shape_keys.key_blocks:
                    try:
                        if shapekey.name == "Basis":
                            continue
                        if (shapekey.value != 0):
                            self.report({'WARNING'},  f'Shape key "{shapekey.name}" on {source_mesh.name} is not 0. Skipped')
                            shapeKeysSkipped += 1
                            continue
                        
                        shapekey.value = 1
                        surf_def_mod.name = shapekey.name

                        bpy.ops.object.modifier_apply_as_shapekey(keep_modifier=True, modifier=surf_def_mod.name) 
                        shapekey.value = 0 # reset
                    except Exception as ex: 
                        self.report({'ERROR'},  f'Error occured while tyrying to copy a shape key: \n {ex}') 
                        shapeKeysSkipped += 1

                surf_def_mod.name = modifierName
                bpy.ops.object.modifier_remove(modifier=modifierName)
            except Exception as ex: 
                self.report({'ERROR'},  f'Error occured while trying to interact with a mesh: \n {ex}') 
                return {'CANCELLED'}
            
        endTextSkip = f" {shapeKeysSkipped} Shape Keys were skipped." if shapeKeysSkipped > 0 else ""
        endTextMode = "selected meshes" if props.ZeniTools_ShapeKeys_ApplyToAllSelected else target_meshes[0].name
        self.report({'INFO'},  f"Shape Keys transferred from {source_mesh.name} to {endTextMode}. {endTextSkip}")
        
        return {'FINISHED'}

class Properties(bpy.types.PropertyGroup):
    bpy.types.Scene.ZeniTools_ShapeKeys_Source_Object = bpy.props.PointerProperty(
        name="Source Object",
        type=bpy.types.Object,
        description="Mesh with shapekeys you want transfered.",
    )
    bpy.types.Scene.ZeniTools_ShapeKeys_Vertex_Group = bpy.props.StringProperty(
        name="Vertex Group Mask",
        description="Optional vertex Group mask for shapekey transfer.",
    )
    bpy.types.Scene.ZeniTools_ShapeKeys_Vertex_Group_Invert = bpy.props.BoolProperty(
        name="Invert Vertex Group",
        description="Invert the vertex group mask",
    )
    bpy.types.Scene.ZeniTools_ShapeKeys_ApplyToAllSelected = bpy.props.BoolProperty(
        name="Apply to all selected objects",
        description="Transfers the shapkeys from the source to all selected objects",
    )

classes = [
    ZeniTools_OP_BatchShapeKeyTransfer,
    Properties,
]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)