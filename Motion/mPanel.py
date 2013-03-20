#
# @file    tools/plugin/blender/Motion/mPanel.py
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

import bpy
from . import MotionSDK as SDK

class ShadowPanel(bpy.types.Panel):
    """
    Basic Blender control panel for the Shadow commands. Just provide
    convenient access to preview, pose, and recording commands from the
    3D View > Tools (T) panel.
    """
    bl_idname = "ShadowPanel"
    bl_label = "Shadow"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"

    def draw(self, context):
        col = self.layout.column(align=True)
        col.operator("mdevice.start",
                     text="Start Preview")

        col = self.layout.column(align=True)
        col.operator("motion.lua",
                     text="Set Pose").command = "set_pose"
        col.operator("motion.lua",
                     text="Create Rest Pose").command = "set_pose_marker"

        col = self.layout.column(align=True)
        col.operator("motion.lua",
                     text="Start Take").command = "start_take"
        col.operator("motion.lua",
                     text="Stop Take").command = "stop_take"

class LuaOperator(bpy.types.Operator):
    """
    Generic wrapper for Lua calls to the Motion Service as a Blender Operator.
    Suitable for incorporation into a UI Panel. See the ShadowPanel class for
    example usage.
    """
    bl_idname = "motion.lua"
    bl_label = "Send a Lua command to the Motion Service"
    command = bpy.props.StringProperty()

    # Static class member, MotionSDK.Client.
    client = None
    host = "127.0.0.1"
    port = 32075
 
    def execute(self, context):
        """
        Send the Lua command store in self.command to the Motion Service. For
        example, to start a take send:
          bpy.ops.motion.lua('EXEC_DEFAULT', command="start_take")
        """
        if len(self.command) > 0:
            node = self.__lua_node()
            getattr(node, self.command)()

        return {'FINISHED'}

    def __client(self):
        """
        Internal use. Return a LuaConsole scripting node to send remote
        commands to the server.
        """
        if None == LuaOperator.client:
            try:
                LuaOperator.client = SDK.Client(LuaOperator.host,
                                                LuaOperator.port)

                print("Connected to device server at \"%s\""
                      % LuaOperator.host)
            except:
                LuaOperator.client = None
                report('ERROR', "Failed to connect device server at \"%s\""
                       % LuaOperator.host)

        return LuaOperator.client

    def __lua_node(self):
        """
        Internal use. Return a LuaConsole scripting node to send remote
        commands to the server.
        """
        return SDK.LuaConsole.Node(self.__client())

