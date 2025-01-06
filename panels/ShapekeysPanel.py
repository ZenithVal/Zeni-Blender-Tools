# panels/ShapekeysPanel.py

import bpy
from bpy.types import Panel

class ZeniTools_PA_Shapekeys(Panel):
    bl_label = "Shape Keys"
    bl_idname = "ZeniTools_PA_Shapekeys"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Zeni'

    def draw(self, context):
        layout = self.layout
        box = layout.box()

        box.label(text="Transfer Shape Keys")
        active_obj = context.active_object
        props = context.scene

        box.prop(props, "ZeniTools_Shapekeys_Source_Object", text="Source")

        row = box.row(align=True)
        row.label(text='Transfer Mask:')
        row.prop_search(props, "ZeniTools_Shapekeys_Vertex_Group", active_obj, "vertex_groups", text='')  
        row.prop (props, "ZeniTools_Shapekeys_Vertex_Group_Invert",text="", toggle=True, icon='ARROW_LEFTRIGHT')
        row.enabled = not props.ZeniTools_Shapekeys_ApplyToAllSelected

        row = box.row(align=True)
        row.prop(props, 'ZeniTools_Shapekeys_ApplyToAllSelected', text='', icon='RESTRICT_SELECT_OFF')
        row.operator("zenitools.batch_shape_key_transfer", text="Transfer Shapekeys")

classes = [
    ZeniTools_PA_Shapekeys,
]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
