bl_info = {
    "name" : "Floating Camera to View",
    "author" : "Claromes",
    "description" : "Fast access to Camera to View",
    "blender" : (3, 2, 2),
    "version" : (0, 0, 4),
    "location" : "View3D",
    "category" : "3D View",
    "doc_url": "https://github.com/claromes/floating_camera_to_view",
    "tracker_url": "https://github.com/claromes/floating_camera_to_view/issues"
}

import bpy
from . float_op import FLOAT_Btn_Settings, FLOAT_OT_Btn
from . float_pnl import FLOAT_PT_Panel

classes = (
    FLOAT_Btn_Settings,
    FLOAT_OT_Btn,
    FLOAT_PT_Panel
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.Scene.float_set = bpy.props.PointerProperty(type=FLOAT_Btn_Settings)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

    del bpy.types.Scene.float_set