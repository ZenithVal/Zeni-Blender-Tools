# panels/ShapeKeysPanel.py

import bpy
from bpy.types import Panel

class ZeniTools_PT_ShapeKeys(Panel):
    bl_label = "Shape Keys"
    bl_idname = "ZeniTools_PT_ShapeKeys"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Zeni'

    def draw(self, context):
        layout = self.layout
        box = layout.box()

        box.label(text="Transfer Shape Keys")
        active_obj = context.object
        props = context.scene

        box.prop(props, "ZeniTools_ShapeKeys_Source_Object", text="Source")

        row = box.row(align=True)
        row.label(text='Transfer Mask:')
        if active_obj != None:
            row.prop_search(props, "ZeniTools_ShapeKeys_Vertex_Group", active_obj, "vertex_groups", text='')  
            row.prop (props, "ZeniTools_ShapeKeys_Vertex_Group_Invert",text="", toggle=True, icon='ARROW_LEFTRIGHT')
        else:
            row.label(text='No object selected')
            row.enabled = False
        row.enabled = not props.ZeniTools_ShapeKeys_ApplyToAllSelected

        row = box.row(align=True)
        row.prop(props, 'ZeniTools_ShapeKeys_ApplyToAllSelected', text='', icon='RESTRICT_SELECT_OFF')
        row.operator("zenitools.batch_shape_key_transfer", text="Transfer ShapeKeys")

classes = [
    ZeniTools_PT_ShapeKeys,
]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
