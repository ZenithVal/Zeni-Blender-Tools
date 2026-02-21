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
import bmesh
import math
import mathutils
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

class ZeniTools_OP_Mesh_SetVertexColor(bpy.types.Operator):
    bl_idname = "zenitools.mesh_set_vertex_color"
    bl_label = "Set Vertex Color"
    bl_description = "Sets the vertex color of the selected mesh(es)."
    bl_options = {'REGISTER', 'UNDO', 'INTERNAL'}

    def execute(self, context):
        props = context.scene
        vertColor = props.ZeniTools_VertexColorToSet

        target_meshes = []
        for obj in bpy.context.selected_objects:
            if isinstance(obj.data, bpy.types.Mesh):
                target_meshes.append(obj)
        if len(target_meshes) == 0:
            self.report({'ERROR'},  "No mesh selected")
            return {'CANCELLED'}
        
        for target_mesh in target_meshes:
            if target_mesh is None:
                self.report({'WARNING'},  "Target mesh cannot be null.")
                continue
            
            # Ensure the mesh has a vertex color layer
            if not target_mesh.data.vertex_colors:
                target_mesh.data.vertex_colors.new(name="VertexColors")

            # Set the vertex color
            color_layer = target_mesh.data.vertex_colors.active
            for poly in target_mesh.data.polygons:
                for loop_index in poly.loop_indices:
                    color_layer.data[loop_index].color = vertColor[:4]

        return {'FINISHED'}


class ZeniTools_OP_Mesh_RemoveVertexColor(bpy.types.Operator):
    bl_idname = "zenitools.mesh_remove_vertex_color"
    bl_label = "Remove Vertex Color"
    bl_description = "Removes the vertex color attributes from the selected mesh(es)."
    bl_options = {'REGISTER', 'UNDO', 'INTERNAL'}

    def execute(self, context):
        target_meshes = []
        for obj in bpy.context.selected_objects:
            if isinstance(obj.data, bpy.types.Mesh):
                target_meshes.append(obj)
        if len(target_meshes) == 0:
            self.report({'ERROR'},  "No mesh selected")
            return {'CANCELLED'}
        
        for target_mesh in target_meshes:
            if target_mesh is None:
                self.report({'WARNING'},  "Target mesh cannot be null.")
                continue
            
        for col_attr in obj.data.vertex_colors:
            obj.data.vertex_colors.remove(col_attr)

        return {'FINISHED'}


# Python port of Blender's internal is_poly_convex_v2 C function. Returns False if the polygon is concave.
def is_poly_convex_v2(face):

    coords = [v.co for v in face.verts]
    nr = len(coords)
    
    if nr < 3:
        return False
        
    sign_flag = 0
    normal = face.normal
    
    for a in range(nr):
        v_prev2 = coords[a - 2]
        v_prev1 = coords[a - 1]
        v_curr = coords[a]
        
        dir_prev = v_prev1 - v_prev2
        dir_curr = v_curr - v_prev1
        
        cross_scalar = dir_prev.cross(dir_curr).dot(normal)
        
        if cross_scalar < -1e-6:
            sign_flag |= 1
        elif cross_scalar > 1e-6:
            sign_flag |= 2
        if sign_flag == 3: 
            return False 
            
    return True

def is_face_concave_or_invalid(face):
    coords = [v.co for v in face.verts]
    nr = len(coords)
    
    if nr < 3:
        return True
        
    if not is_poly_convex_v2(face):
        return True 

    # Edge Overlap/parallel check
    prev_prev_co = coords[nr - 2]
    prev_co = coords[nr - 1]
    
    prev_vec = prev_co - prev_prev_co
    if prev_vec.length < 1e-6:
        return True 
    prev_vec.normalize()

    for i in range(nr):
        curr_co = coords[i]
        curr_vec = curr_co - prev_co
        
        curr_len = curr_vec.length
        if curr_len < 1e-6:
            return True
            
        curr_vec.normalize()
        if (curr_co - prev_prev_co).length_squared < 1e-12:
            return True
            
        if 1.0 - prev_vec.dot(curr_vec) < 1e-6:
            return True
            
        prev_prev_co = prev_co
        prev_co = curr_co
        prev_vec = curr_vec

    # Degenerate Projection Check
    centroid = sum(coords, mathutils.Vector()) / nr
    normal = face.normal
    
    if normal.length < 1e-6:
        return True # Face has zero area
        
    for j in range(nr):
        v_prev = coords[j - 1]
        v_curr = coords[j]
        v_next = coords[(j + 1) % nr]
        
        # Calculate midpoints of adjacent edges
        mid_prev = (v_prev + v_curr) / 2.0
        mid_next = (v_curr + v_next) / 2.0
        
        # Vectors from centroid to midpoints, projected onto the face plane
        vec_mid_prev = mid_prev - centroid
        vec_mid_next = mid_next - centroid
        vec_mid_prev -= vec_mid_prev.project(normal)
        vec_mid_next -= vec_mid_next.project(normal)
        
        len_prev = vec_mid_prev.length
        len_next = vec_mid_next.length
        if len_prev < 1e-6 or len_next < 1e-6:
            return True
            
        vec_mid_prev /= len_prev
        vec_mid_next /= len_next
        
        # bpoly->scales[0] and [1] (Distance from centroid to the edges)
        edge1_dir = v_curr - v_prev
        len_edge1 = edge1_dir.length
        if len_edge1 < 1e-6: return True
        edge1_dir /= len_edge1
        scale0 = (centroid - v_prev).cross(edge1_dir).length
        
        edge2_dir = v_next - v_curr
        len_edge2 = edge2_dir.length
        if len_edge2 < 1e-6: return True
        edge2_dir /= len_edge2
        scale1 = (centroid - v_curr).cross(edge2_dir).length
        
        if scale0 < 1e-6 or scale1 < 1e-6:
            return True
            
        # bpoly->edgemid_angle (Angle between the two mid-vectors)
        dot_val = max(-1.0, min(1.0, vec_mid_prev.dot(vec_mid_next)))
        edgemid_angle = math.acos(dot_val)
        
        if edgemid_angle < 1e-6:
            return True
            
        # bpoly->corner_edgemid_angles
        vec_corner = v_curr - centroid
        vec_corner -= vec_corner.project(normal)
        len_corner = vec_corner.length
        if len_corner < 1e-6:
            return True
        vec_corner /= len_corner
        
        dot_c0 = max(-1.0, min(1.0, vec_corner.dot(vec_mid_prev)))
        dot_c1 = max(-1.0, min(1.0, vec_corner.dot(vec_mid_next)))
        corner_angle_0 = math.acos(dot_c0)
        corner_angle_1 = math.acos(dot_c1)
        
        if corner_angle_0 < 1e-6 or corner_angle_1 < 1e-6:
            return True

        # bpoly->scale_mid
        area_tri = 0.5 * (v_curr - v_prev).cross(v_next - v_prev).length
        base_len = (v_next - v_prev).length
        if base_len < 1e-6:
            return True
        scale_mid = (area_tri / base_len) * 1.41421356 # sqrt(2)
        if scale_mid < 1e-6:
            return True
    return False


class ZeniTools_OP_MESH_SelectInvalidPolys(bpy.types.Operator):
    bl_idname = "zenitools.mesh_select_invalid_polys"
    bl_label = "Select Invalid Polygons"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.mode == 'EDIT_MESH'

    def execute(self, context):
        obj = context.edit_object
        me = obj.data
        bm = bmesh.from_edit_mesh(me)

        # Deselect all
        for elem in bm.verts[:] + bm.edges[:] + bm.faces[:]:
            elem.select = False

        count = 0
        for f in bm.faces:
            if is_face_concave_or_invalid(f):
                f.select = True
                for v in f.verts:
                    v.select = True
                for e in f.edges:
                    e.select = True
                count += 1

        bmesh.update_edit_mesh(me)
        
        if count > 0:
            self.report({'INFO'}, f"Found {count} invalid polys.")
        else:
            self.report({'INFO'}, "No invalid polys.")
            
        return {'FINISHED'}


class ZeniTools_OP_Mesh_CreateVertexGroupWithObjectName(bpy.types.Operator):
    bl_idname = "zenitools.mesh_create_vertex_group_with_object_name"
    bl_label = "Add Vertex Group with Object Name"
    bl_description = "Adds a vertex group to the selected mesh(es) with the name of the object."
    bl_options = {'REGISTER', 'UNDO', 'INTERNAL'}

    def execute(self, context):
        target_meshes = []
        for obj in bpy.context.selected_objects:
            if isinstance(obj.data, bpy.types.Mesh):
                target_meshes.append(obj)
        if len(target_meshes) == 0:
            self.report({'ERROR'},  "No mesh selected")
            return {'CANCELLED'}
        
        for target_mesh in target_meshes:
            if target_mesh is None:
                self.report({'WARNING'},  "Target mesh cannot be null.")
                continue
            
            # Create a vertex group with the name of the object
            vertex_group_name = target_mesh.name
            if vertex_group_name not in target_mesh.vertex_groups:
                target_mesh.vertex_groups.new(name=vertex_group_name)
                vertex_group = target_mesh.vertex_groups[vertex_group_name]
                for vertex in target_mesh.data.vertices:
                    vertex_group.add([vertex.index], 1.0, 'ADD')
            else:
                self.report({'WARNING'}, f"Vertex group '{vertex_group_name}' already exists.")

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

class Properties(bpy.types.PropertyGroup):
    bpy.types.Scene.ZeniTools_VertexColorToSet = bpy.props.FloatVectorProperty(
                name = "Vertex Set Color Picker",
                subtype = "COLOR",
                size = 4,
                min = 0.0,
                max = 1.0,
                default = (0.0,0.0,0.0,1.0)
                )

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

    ZeniTools_OP_MESH_SelectInvalidPolys,

    ZeniTools_OP_Mesh_CleanupMaterials,
    ZeniTools_OP_Mesh_CleanupShapekeys,
    ZeniTools_OP_Mesh_CleanupVertexGroups,

    ZeniTools_OP_Armature_Cleanup,
    ZeniTools_OP_Armature_CreateRoot,
    ZeniTools_OP_Armature_MergeToActive,
    ZeniTools_OP_Armature_MergeToParent,

    ZeniTools_OP_Global_ApplyTransformsVisible,
    ZeniTools_OP_Global_ApplyTransformsSelected,

    ZeniTools_OP_Mesh_SetVertexColor,
    ZeniTools_OP_Mesh_RemoveVertexColor,

    ZeniTools_OP_Mesh_CreateVertexGroupWithObjectName,

    Properties,
]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)