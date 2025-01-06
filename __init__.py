# Main __init__.py - this is where we determine addon info, import all the main py modules so everything else works, then import everything from the rest of the folder structure.

bl_info = {
    "name": "Zeni's Blender Tools",
    "author": "ZenithVal",
    "version": (1, 0, 0), 
    "blender": (4, 3, 2),
    "location": "View3D > Sidebar > Zeni",
    "description": "Misc Tools Zeni Uses",
    "doc_url": "https://github.com/ZenithVal/Zeni-Blender-Tools",
    "category": "General",
}

import bpy
import os
import sys
import importlib
import textwrap
import re
import json
import math
import mathutils

from .operators import ShapekeyOps
from .panels import ShapekeysPanel

modules = [
    ShapekeyOps,
    ShapekeysPanel,
]

classes = (
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    for module in modules:
        print(f"Registering {module.__name__}")
        module.register()

    # I'd like to put this in a property group but every time I do, it all breaks so
    bpy.types.Scene.ZeniTools_Shapekeys_Source_Object = bpy.props.PointerProperty(
        name="Source Object",
        type=bpy.types.Object,
        description="Mesh with shapekeys you want trasnfered",
    )
    bpy.types.Scene.ZeniTools_Shapekeys_Vertex_Group = bpy.props.StringProperty(
        name="Vertex Group Mask",
        description="Optional vertex Group mask for shapekey transfer. Ignored if applying to selected is enabled.",
    )
    bpy.types.Scene.ZeniTools_Shapekeys_Vertex_Group_Invert = bpy.props.BoolProperty(
        name="Invert Vertex Group",
        description="Invert the vertex group mask",
    )
    bpy.types.Scene.ZeniTools_Shapekeys_ApplyToAllSelected = bpy.props.BoolProperty(
        name="Apply to all selected objects",
        description="Transfers the shapkeys from the source to all selected objects",
    )


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

    for module in reversed(modules):
        print(f"Unregistering {module.__name__}")
        module.unregister()

    del bpy.types.Scene.ZeniTools_Shapekeys_Source_Object
    del bpy.types.Scene.ZeniTools_Shapekeys_Vertex_Group
    del bpy.types.Scene.ZeniTools_Shapekeys_Vertex_Group_Invert
    del bpy.types.Scene.ZeniTools_Shapekeys_ApplyToAllSelected