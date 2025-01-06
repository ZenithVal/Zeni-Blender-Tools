# menus/TopBar.py

import bpy
from bpy.types import Menu

class TOPBAR_MT_custom_menu(bpy.types.Menu):
    bl_idname = "TOPBAR_MT_ZeniTools_Menu"
    bl_label = "Zeni"

    def draw(self, context):
        layout = self.layout
        layout.menu("TOPBAR_MT_zeni_General")

def menu_draw_func(self, context):
    layout = self.layout
    layout.menu(TOPBAR_MT_custom_menu.bl_idname)

classes = [
    TOPBAR_MT_custom_menu,
]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.TOPBAR_MT_editor_menus.append(menu_draw_func)

def unregister():
    bpy.types.TOPBAR_MT_editor_menus.remove(menu_draw_func)
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
