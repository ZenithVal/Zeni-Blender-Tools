#operators/ModelOps.py

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

def get_objects():
    return bpy.context.view_layer.objects

def get_armature(armature_name=None):
    if not armature_name:
        armature_name = bpy.context.scene.armature
    for obj in get_objects():
        if obj.type == 'ARMATURE':
            if (armature_name and obj.name == armature_name) or not armature_name:
                return obj
    return None

def get_armature_objects():
    armatures = []
    for obj in get_objects():
        if obj.type == 'ARMATURE':
            armatures.append(obj)
    return armatures

class ZeniTools_OP_ExportFBX(bpy.types.Operator):
    bl_idname = "zenitools.export_fbx"
    bl_label = "Export Model"
    bl_description = "Exports the selected model with optimal settings"
    bl_options = {'REGISTER', 'UNDO', 'INTERNAL'}

    @classmethod
    def poll(cls, context):
        return context.area.type == 'VIEW_3D'

    def execute(self, context):

        return {'FINISHED'}


# Pose Mode
class ZeniTools_OP_PoseMode_Start(bpy.types.Operator):
    bl_idname = "zenitools.pose_mode_start"
    bl_label = "Start Pose Mode"
    bl_description = "Starts Pose Mode from the default pose."
    bl_options = {'REGISTER', 'UNDO', 'INTERNAL'}

    def execute(self, context):
        return {'FINISHED'}
    
class ZeniTools_OP_PoseMode_Stop(bpy.types.Operator):
    bl_idname = "zenitools.pose_mode_stop"
    bl_label = "Stop Pose Mode"
    bl_description = "Exits Pose Mode and resets the pose."
    bl_options = {'REGISTER', 'UNDO', 'INTERNAL'}

    def execute(self, context):
        return {'FINISHED'}
    
class ZeniTools_OP_PoseMode_StartNoReset(bpy.types.Operator):
    bl_idname = "zenitools.pose_mode_start_no_reset"
    bl_label = "Start Pose Mode (No Reset)"
    bl_description = "Starts Pose Mode and keeps the current pose."
    bl_options = {'REGISTER', 'UNDO', 'INTERNAL'}

    def execute(self, context):
        return {'FINISHED'}
    
class ZeniTools_OP_PoseMode_StopNoReset(bpy.types.Operator):
    bl_idname = "zenitools.pose_mode_stop_no_reset"
    bl_label = "Stop Pose mode (No Reset)"
    bl_description = "Exits Pose Mode and keeps the current pose."
    bl_options = {'REGISTER', 'UNDO', 'INTERNAL'}

    def execute(self, context):
        return {'FINISHED'}
    
class ZeniTools_OP_PoseMode_Reset(bpy.types.Operator):
    bl_idname = "zenitools.pose_mode_reset"
    bl_label = "Reset Pose"
    bl_description = "Resets the pose for the selected armature."
    bl_options = {'REGISTER', 'UNDO', 'INTERNAL'}

    def execute(self, context):
        return {'FINISHED'}
    
class ZeniTools_OP_PoseMode_ApplyAsRestPose(bpy.types.Operator):
    bl_idname = "zenitools.pose_mode_apply_as_rest_pose"
    bl_label = "Apply Pose as Rest Pose"
    bl_description = "Applies the current pose as the rest pose."
    bl_options = {'REGISTER', 'UNDO', 'INTERNAL'}

    def execute(self, context):
        return {'FINISHED'}
    
class ZeniTools_OP_PoseMode_ApplyAsShapeKey(bpy.types.Operator):
    bl_idname = "zenitools.pose_mode_apply_as_shape_key"
    bl_label = "Apply Pose as Shape Key"
    bl_description = "Applies the current pose as a shape key."
    bl_options = {'REGISTER', 'UNDO', 'INTERNAL'}

    def execute(self, context):
        return {'FINISHED'}


# Mesh Cleanup
class ZeniTools_OP_Mesh_CleanupVertexGroups(bpy.types.Operator):
    bl_idname = "zenitools.mesh_cleanup_vertex_groups"
    bl_label = "Remove unused Vertex Groups"
    bl_description = "Removes unused vertex groups from the selected mesh(es)."
    bl_options = {'REGISTER', 'UNDO', 'INTERNAL'}

    def execute(self, context):
        return {'FINISHED'}

class ZeniTools_OP_Mesh_CleanupMaterials(bpy.types.Operator):
    bl_idname = "zenitools.mesh_cleanup_materials"
    bl_label = "Remove unused Materials"
    bl_description = "Removes unused materials from the selected mesh(es)."
    bl_options = {'REGISTER', 'UNDO', 'INTERNAL'}

    def execute(self, context):
        return {'FINISHED'}

class ZeniTools_OP_Mesh_CleanupShapekeys(bpy.types.Operator):
    bl_idname = "zenitools.mesh_cleanup_shapekeys"
    bl_label = "Remove unused shapekeys"
    bl_description = "Removes unused shapekeys from the selected mesh. (Ignores shapekeys that start with ==)"
    bl_options = {'REGISTER', 'UNDO', 'INTERNAL'}

    def execute(self, context):
        return {'FINISHED'}


# Mesh Operators
class ZeniTools_OP_Mesh_SeparateByMaterials(bpy.types.Operator):
    bl_idname = "zenitools.mesh_separate_by_materials"
    bl_label = "Separate by Materials"
    bl_description = "Separates the selected mesh by materials."
    bl_options = {'REGISTER', 'UNDO', 'INTERNAL'}

    def execute(self, context):
        return {'FINISHED'}


class ZeniTools_OP_Mesh_SeparateByLooseParts(bpy.types.Operator):
    bl_idname = "zenitools.mesh_separate_by_loose_parts"
    bl_label = "Separate by Loose Parts"
    bl_description = "Separates the selected mesh by loose parts."
    bl_options = {'REGISTER', 'UNDO', 'INTERNAL'}

    def execute(self, context):
        return {'FINISHED'}


class ZeniTools_OP_Mesh_SeperateByShapekeys(bpy.types.Operator):
    bl_idname = "zenitools.mesh_separate_by_shapekeys"
    bl_label = "Separate by Shapekeys"
    bl_description = "Separates the selected mesh by shapekeys."
    bl_options = {'REGISTER', 'UNDO', 'INTERNAL'}

    def execute(self, context):
        return {'FINISHED'}


class ZeniTools_OP_Mesh_JoinVisible(bpy.types.Operator):
    bl_idname = "zenitools.mesh_join_visible"
    bl_label = "Join Visible"
    bl_description = "Joins all visible meshes."
    bl_options = {'REGISTER', 'UNDO', 'INTERNAL'}

    def execute(self, context):
        return {'FINISHED'}

class ZeniTools_OP_Mesh_JoinSelected(bpy.types.Operator):
    bl_idname = "zenitools.mesh_join_selected"
    bl_label = "Join Selected"
    bl_description = "Joins all selected meshes."
    bl_options = {'REGISTER', 'UNDO', 'INTERNAL'}

    def execute(self, context):
        return {'FINISHED'}
    
# Armature

class ZeniTools_OP_Armature_MergeToActive(bpy.types.Operator):
    bl_idname = "zenitools.armature_merge_to_active"
    bl_label = "Merge Bones & Weights to Active"
    bl_description = "Merges all selected bones & weights to the active bone."
    bl_options = {'REGISTER', 'UNDO', 'INTERNAL'}

    def execute(self, context):
        return {'FINISHED'}
    
class ZeniTools_OP_Armature_MergeToParent(bpy.types.Operator):
    bl_idname = "zenitools.armature_merge_to_parent"
    bl_label = "Merge Bones & Weights to Parent"
    bl_description = "Merges all selected bones & Weights to their parent bone."
    bl_options = {'REGISTER', 'UNDO', 'INTERNAL'}

    def execute(self, context):
        return {'FINISHED'}
    
class ZeniTools_OP_Armature_Cleanup(bpy.types.Operator):
    bl_idname = "zenitools.armature_cleanup"
    bl_label = "Remove Zero Weight Bones"
    bl_description = "Removes all bones with no associated weights (Ignores Root_ & _Twist)"
    bl_options = {'REGISTER', 'UNDO', 'INTERNAL'}

    def execute(self, context):
        return {'FINISHED'}
    
class ZeniTools_OP_Armature_CreateRoot(bpy.types.Operator):
    bl_idname = "zenitools.armature_create_root"
    bl_label = "Create Root Bone"
    bl_description = "Creates a Root_ bone parent for the selected bones"
    bl_options = {'REGISTER', 'UNDO', 'INTERNAL'}

    def execute(self, context):
        return {'FINISHED'}


# Object Operators
class ZeniTools_OP_Global_ApplyTransformsVisible(bpy.types.Operator):
    bl_idname = "zenitools.global_apply_transforms"
    bl_label = "Apply Transforms to all visible objects"
    bl_description = "Applies all transforms to the selected objects."
    bl_options = {'REGISTER', 'UNDO', 'INTERNAL'}

    def execute(self, context):
        return {'FINISHED'}
    
class ZeniTools_OP_Global_ApplyTransformsSelected(bpy.types.Operator):
    bl_idname = "zenitools.global_apply_transforms_selected"
    bl_label = "Apply Transforms to selected objects"
    bl_description = "Applies all transforms to the selected objects."
    bl_options = {'REGISTER', 'UNDO', 'INTERNAL'}
    
    def execute(self, context):
        return {'FINISHED'}


# class Properties(bpy.types.PropertyGroup):


classes = [   
    ZeniTools_OP_ExportFBX,
    ZeniTools_OP_PoseMode_Start,
    ZeniTools_OP_PoseMode_Stop,
    ZeniTools_OP_PoseMode_StartNoReset,
    ZeniTools_OP_PoseMode_StopNoReset,
    ZeniTools_OP_PoseMode_Reset,
    ZeniTools_OP_PoseMode_ApplyAsRestPose,
    ZeniTools_OP_PoseMode_ApplyAsShapeKey,

    ZeniTools_OP_Mesh_SeparateByLooseParts,
    ZeniTools_OP_Mesh_SeparateByMaterials,
    ZeniTools_OP_Mesh_SeperateByShapekeys,
    ZeniTools_OP_Mesh_JoinSelected,
    ZeniTools_OP_Mesh_JoinVisible,

    ZeniTools_OP_Mesh_CleanupMaterials,
    ZeniTools_OP_Mesh_CleanupShapekeys,
    ZeniTools_OP_Mesh_CleanupVertexGroups,

    ZeniTools_OP_Armature_Cleanup,
    ZeniTools_OP_Armature_CreateRoot,
    ZeniTools_OP_Armature_MergeToActive,
    ZeniTools_OP_Armature_MergeToParent,

    ZeniTools_OP_Global_ApplyTransformsVisible,
    ZeniTools_OP_Global_ApplyTransformsSelected

    # Properties
]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)