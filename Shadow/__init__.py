#
# @file    tools/plugin/blender/Shadow/__init__.py
# @author  Luke Tokheim, luke@motionshadow.com
# @version 2.4
#
# (C) Copyright Motion Workshop 2016. All rights reserved.
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
    "name": "Shadow",
    "author": "Luke Tokheim",
    "version": (2, 4),
    "description": "Stream Shadow animation data from the Motion Service into "
                   "the Blender scene. Use MotionSDK to handle socket "
                   "communication.",
    "category": "Animation"
}

from .mDevice import ModalOperator
from .mPanel import LuaOperator, ImportOperator, ShadowPanel

import bpy


def register():
    bpy.utils.register_class(ModalOperator)
    bpy.utils.register_class(LuaOperator)
    bpy.utils.register_class(ImportOperator)
    bpy.utils.register_class(ShadowPanel)


def unregister():
    bpy.utils.unregister_class(ModalOperator)
    bpy.utils.unregister_class(LuaOperator)
    bpy.utils.unregister_class(ImportOperator)
    bpy.utils.unregister_class(ShadowPanel)

if __name__ == "__main__":
    register()
