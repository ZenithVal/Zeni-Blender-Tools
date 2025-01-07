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

from .operators import ShapeKeysOps
from .panels import ShapeKeysPanel

from .operators import ModelOps
from .panels import ModelPanel

modules = [
    ShapeKeysOps,
    ShapeKeysPanel,

    ModelOps,
    ModelPanel,
]

classes = (
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    for module in modules:
        print(f"Registering {module.__name__}")
        module.register()

    bpy.types.Scene.ZeniTools_ShapeKeys_Props = bpy.props.PointerProperty(type=ShapeKeysOps.Properties)
    # byp.types.Scene.ZeniTools_Model_Props = bpy.props.PointerProperty(type=ModelOps.Properties)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

    for module in reversed(modules):
        print(f"Unregistering {module.__name__}")
        module.unregister()

    del bpy.types.Scene.ZeniTools_ShapeKeys_Props
    # del bpy.types.Scene.ZeniTools_Model_Props