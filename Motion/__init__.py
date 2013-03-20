#
# @file    tools/plugin/blender/Motion/__init__.py
# @author  Luke Tokheim, luke@motionnode.com
# @version 2.0
#
# (C) Copyright Motion Workshop 2013. All rights reserved.
#
# The coded instructions, statements, computer programs, and/or related
# material (collectively the "Data") in these files contain unpublished
# information proprietary to Motion Workshop, which is protected by
# US federal copyright law and by international treaties.
#
# The Data may not be disclosed or distributed to third parties, in whole
# or in part, without the prior written consent of Motion Workshop.
#
# The Data is provided "as is" without express or implied warranty, and
# with no claim as to its suitability for any purpose.
#

bl_info = {
    "name": "Motion Shadow",
    "author": "Luke Tokheim",
    "version": (1, 0),
    "description": "Stream animation data from the Motion Service into the"
                   " Blender scene. Use MotionSDK to handle socket "
                   "communication.",
    "category": "Animation"
}

from .mDevice import ModalOperator
from .mPanel import LuaOperator, ShadowPanel

import bpy

def register():
    bpy.utils.register_class(ModalOperator)
    bpy.utils.register_class(LuaOperator)
    bpy.utils.register_class(ShadowPanel)

def unregister():
    bpy.utils.unregister_class(ModalOperator)
    bpy.utils.unregister_class(LuaOperator)
    bpy.utils.unregister_class(ShadowPanel)

if __name__ == "__main__":
    register()