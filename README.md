Motion Shadow for Blender
=======

Blender support for the Shadow motion capture system.

Install
-------

The folder Motion in this repository is the Blender add-on. Copy the entire
folder into your Blender installation or user folder. Refer to the Blender
manual for more details.

http://wiki.blender.org/index.php/Doc:2.6/Manual/Extensions/Python/Add-Ons

Note that you must copy the folder manually rather than using the Blender
Add-Ons window. The window only supports installation of single file add-ons.

Usage
------

1. Open the Shadow.blend scene file in Blender. This contains the Shadow skeleton
   model defined as a Blender armature.

2. Enable the "Motion Shadow" add-on using the add-ons window.

3. Start streaming data from the Shadow motion capture system.

4. Send the command "mDevice: Start Device" from Blender. This will start to update
   the scene with live preview data.
