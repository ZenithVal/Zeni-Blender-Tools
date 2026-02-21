# panels/ModelPanel.py

# Snippits of code in this file are based on Cats Blender Plugin.
# MIT License

# Copyright (c) 2017 GiveMeAllYourCats

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the 'Software'), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# Code author: GiveMeAllYourCats
# Repo: https://github.com/michaeldegroot/cats-blender-plugin
# Edits by: GiveMeAllYourCats, Hotox

import bpy
from bpy.types import Panel
from ..operators import ModelOps

def layout_split(layout, factor=0.0, align=False):
    return layout.split(factor=factor, align=align)

class ZeniTools_PT_Model(Panel):
    bl_label = 'Model'
    bl_idname = 'ZeniTools_PT_Model'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Zeni'

    def draw(self, context):
        layout = self.layout
        box = layout.box()

        row = box.row(align=True)
        row.operator(ModelOps.ZeniTools_OP_ExportFBX.bl_idname, icon='EXPORT')
        row.scale_y = 1.4

        col = box.column(align=True)
        arm_count = len(ModelOps.get_armature_objects())

        # Armature Selector
        if arm_count > 1:
            row = col.row(align=True)
            row.scale_y = 1.1
            row.prop(context.scene, 'armature', icon='ARMATURE_DATA')

        col.separator()

        # Pose Mode Functions
        armature_obj = ModelOps.get_armature()
        if not armature_obj or armature_obj.mode != 'POSE':
            split = col.row(align=True)
            row = split.row(align=True)
            row.scale_y = 1.1
            row.operator(ModelOps.ZeniTools_OP_PoseMode_Start.bl_idname, icon='POSE_HLT')
            row = split.row(align=True)
            row.alignment = 'RIGHT'
            row.scale_y = 1.1
            row.operator(ModelOps.ZeniTools_OP_PoseMode_StartNoReset.bl_idname, text="", icon='POSE_HLT')
        else:
            split = col.row(align=True)
            row = split.row(align=True)
            row.scale_y = 1.1
            row.operator(ModelOps.ZeniTools_OP_PoseMode_Stop.bl_idname, icon='POSE_HLT')
            row = split.row(align=True)
            row.alignment = 'RIGHT'
            row.scale_y = 1.1
            row.operator(ModelOps.ZeniTools_OP_PoseMode_StopNoReset.bl_idname, text='', icon='POSE_HLT')
            row = col.row(align=True)
            row.scale_y = 0.9
            row.operator(ModelOps.ZeniTools_OP_PoseMode_ApplyAsShapeKey.bl_idname, icon='SHAPEKEY_DATA')
            row = col.row(align=True)
            row.scale_y = 0.9
            row.operator(ModelOps.ZeniTools_OP_PoseMode_ApplyAsRestPose.bl_idname, icon='POSE_HLT')

class ZeniTools_PT_ModelTools(Panel):
    bl_label = 'Model Tools'
    bl_idname = 'ZeniTools_PT_ModelTools'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Zeni'

    def draw(self, context):
        props = context.scene
        layout = self.layout

        # Vertex Color Stuff
        box = layout.box()
        box.label(text="Vertex Color")
        row = box.row(align=True)
        row.prop(props, "ZeniTools_VertexColorToSet", text="Color To Set")
        row = box.row(align=True)
        row.operator("zenitools.mesh_set_vertex_color", text="Set Vertex Color")
        row = box.row(align=True)
        row.operator("zenitools.mesh_remove_vertex_color", text="Remove Vertex Color")

        # Vertex Group Stuff
        box = layout.box()
        box.label(text="Vertex Groups")
        row = box.row(align=True)
        row.scale_y = 1.4
        row.operator("zenitools.mesh_create_vertex_group_with_object_name", text="Add Vertex Group With Object Name")
 

classes = [
    ZeniTools_PT_Model,
    ZeniTools_PT_ModelTools,
]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
