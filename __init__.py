bl_info = {
    "name": "Qlab Virtual Lighting Environment",
    "author": "Daniel W",
    "version": (0, 1),
    "blender": (4, 10, 0),
    "location": "3D View > Sidebar > Virual Lighting Environment",
    "description": "Visualize stage lighting in a 3D space; Works with Qlab",
    "category": "3D View"
}

import bpy
from bpy.types import Panel, Operator, PropertyGroup, FloatProperty, PointerProperty, StringProperty
import time
import math
import json
import numpy as np

class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    @property
    def in_first_quadrant(self):
        return self.x > 0 and self.y > 0

    @property
    def in_second_quadrant(self):
        return self.x < 0 and self.y > 0
    
    @property
    def in_third_quadrant(self):
        return self.x < 0 and self.y < 0
    
    @property
    def in_fourth_quadrant(self):
        return self.x > 0 and self.y < 0
    
    @property
    def length(self):
        return math.sqrt(((self.x) ** 2) + ((self.y) ** 2) + ((self.z) ** 2))

def change_color(color1, color2, color3, light):
    
    cyc = [
    '17',
    '18',
    '19',
    '20',
    '21',
    '22'
    ]
    
    par_ds = [
    '15',
    '16'
    ]
    
    par_us = [
    '7',
    '8',
    '9',
    '10',
    '11',
    '12',
    '13',
    '14'
    ]
    
    movers = [
    '25',
    '36'
    ]
    
    foh = [
    '1',
    '2',
    '3',
    '4',
    '5',
    '6'
    ]
    
    context = bpy.context
    scene = context.scene
    mytool = scene.settings
    
    group = mytool.groups
    
    if group == 'OP1':
        color = (color1, color2, color3)
        selected_light = scene.objects[light]
        selected_light.data.color = color
        
    if group == 'OP2':
        color = (color1, color2, color3)
        
        for lights in scene.objects:
            if lights.name in cyc:
                selected_light = scene.objects[lights.name]
                selected_light.data.color = color
                
    if group == 'OP5':
        color = (color1, color2, color3)
        
        for lights in scene.objects:
            if lights.name in foh:
                selected_light = scene.objects[lights.name]
                selected_light.data.color = color
                
    if group == 'OP3':
        color = (color1, color2, color3)
        
        for lights in scene.objects:
            if lights.name in par_ds:
                selected_light = scene.objects[lights.name]
                selected_light.data.color = color
                
    if group == 'OP4':
        color = (color1, color2, color3)
        
        for lights in scene.objects:
            if lights.name in par_us:
                selected_light = scene.objects[lights.name]
                selected_light.data.color = color
                
    if group == 'OP6':
        color = (color1, color2, color3)
        
        for lights in scene.objects:
            if lights.name in movers:
                selected_light = scene.objects[lights.name]
                selected_light.data.color = color
    
    
    
def open_front_curtain():
    
    bpy.data.scenes[0].frame_current = 0

    context = bpy.context
    scene = context.scene
    mytool = scene.settings

    bpy.data.shape_keys["Key"].key_blocks["Key"].value = 0

    for single_shapekey in scene.objects["Front Curtain"].data.shape_keys.key_blocks:
        single_shapekey.keyframe_insert(data_path='value', frame=0)
        
    bpy.data.shape_keys["Key"].key_blocks["Key"].value = 1

    for single_shapekey in scene.objects["Front Curtain"].data.shape_keys.key_blocks:
        single_shapekey.keyframe_insert(data_path='value', frame=30)
        
    def stop_playback(scene):
        context = bpy.context
        scene = context.scene
        mytool = scene.settings

        if scene.frame_current == 30:
            bpy.ops.screen.animation_cancel(restore_frame=False)
            
            for single_shapekey in scene.objects["Front Curtain"].data.shape_keys.key_blocks:
                single_shapekey.keyframe_delete(data_path='value', frame=0)
                
            for single_shapekey in scene.objects["Front Curtain"].data.shape_keys.key_blocks:
                single_shapekey.keyframe_delete(data_path='value', frame=30)
    
    bpy.app.handlers.frame_change_pre.append(stop_playback)

    bpy.ops.screen.animation_play()
    



     
def close_front_curtain():
    
    bpy.data.scenes[0].frame_current = 0

    context = bpy.context
    scene = context.scene
    mytool = scene.settings

    bpy.data.shape_keys["Key"].key_blocks["Key"].value = 1

    for single_shapekey in scene.objects["Front Curtain"].data.shape_keys.key_blocks:
        single_shapekey.keyframe_insert(data_path='value', frame=0)
        
    bpy.data.shape_keys["Key"].key_blocks["Key"].value = 0

    for single_shapekey in scene.objects["Front Curtain"].data.shape_keys.key_blocks:
        single_shapekey.keyframe_insert(data_path='value', frame=30)
        
    def stop_playback(scene):
        context = bpy.context
        scene = context.scene
        mytool = scene.settings

        if scene.frame_current == 30:
            bpy.ops.screen.animation_cancel(restore_frame=False)
            
            for single_shapekey in scene.objects["Front Curtain"].data.shape_keys.key_blocks:
                single_shapekey.keyframe_delete(data_path='value', frame=30)
                
            for single_shapekey in scene.objects["Front Curtain"].data.shape_keys.key_blocks:
                single_shapekey.keyframe_delete(data_path='value', frame=0)
    
    bpy.app.handlers.frame_change_pre.append(stop_playback)

    bpy.ops.screen.animation_play()


def open_middle_curtain():
    
    bpy.data.scenes[0].frame_current = 0

    context = bpy.context
    scene = context.scene
    mytool = scene.settings

    bpy.data.shape_keys["Key.001"].key_blocks["Key.001"].value = 0

    for single_shapekey in scene.objects["Middle Curtain"].data.shape_keys.key_blocks:
        single_shapekey.keyframe_insert(data_path='value', frame=0)
        
    bpy.data.shape_keys["Key.001"].key_blocks["Key.001"].value = 1

    for single_shapekey in scene.objects["Middle Curtain"].data.shape_keys.key_blocks:
        single_shapekey.keyframe_insert(data_path='value', frame=30)
        
    def stop_playback(scene):
        context = bpy.context
        scene = context.scene
        mytool = scene.settings

        if scene.frame_current == 30:
            bpy.ops.screen.animation_cancel(restore_frame=False)
            
            for single_shapekey in scene.objects["Middle Curtain"].data.shape_keys.key_blocks:
                single_shapekey.keyframe_delete(data_path='value', frame=30)
                
            for single_shapekey in scene.objects["Middle Curtain"].data.shape_keys.key_blocks:
                single_shapekey.keyframe_delete(data_path='value', frame=0)
    
    bpy.app.handlers.frame_change_pre.append(stop_playback)

    bpy.ops.screen.animation_play()

     
def close_middle_curtain():
    
    bpy.data.scenes[0].frame_current = 0

    context = bpy.context
    scene = context.scene
    mytool = scene.settings

    bpy.data.shape_keys["Key.001"].key_blocks["Key.001"].value = 1

    for single_shapekey in scene.objects["Middle Curtain"].data.shape_keys.key_blocks:
        single_shapekey.keyframe_insert(data_path='value', frame=0)
        
    bpy.data.shape_keys["Key.001"].key_blocks["Key.001"].value = 0

    for single_shapekey in scene.objects["Middle Curtain"].data.shape_keys.key_blocks:
        single_shapekey.keyframe_insert(data_path='value', frame=30)
        
    def stop_playback(scene):
        context = bpy.context
        scene = context.scene
        mytool = scene.settings

        if scene.frame_current == 30:
            bpy.ops.screen.animation_cancel(restore_frame=False)
            
            for single_shapekey in scene.objects["Middle Curtain"].data.shape_keys.key_blocks:
                single_shapekey.keyframe_delete(data_path='value', frame=30)
                
            for single_shapekey in scene.objects["Middle Curtain"].data.shape_keys.key_blocks:
                single_shapekey.keyframe_delete(data_path='value', frame=0)
    
    bpy.app.handlers.frame_change_pre.append(stop_playback)

    bpy.ops.screen.animation_play()
    


def open_back_curtain():
    
    bpy.data.scenes[0].frame_current = 0

    context = bpy.context
    scene = context.scene
    mytool = scene.settings

    bpy.data.shape_keys["Key.002"].key_blocks["Key.002"].value = 0

    for single_shapekey in scene.objects["Back Curtain"].data.shape_keys.key_blocks:
        single_shapekey.keyframe_insert(data_path='value', frame=0)
        
    bpy.data.shape_keys["Key.002"].key_blocks["Key.002"].value = 1

    for single_shapekey in scene.objects["Back Curtain"].data.shape_keys.key_blocks:
        single_shapekey.keyframe_insert(data_path='value', frame=30)
        
    def stop_playback(scene):
        context = bpy.context
        scene = context.scene
        mytool = scene.settings

        if scene.frame_current == 30:
            bpy.ops.screen.animation_cancel(restore_frame=False)
            
            for single_shapekey in scene.objects["Back Curtain"].data.shape_keys.key_blocks:
                single_shapekey.keyframe_delete(data_path='value', frame=30)
                
            for single_shapekey in scene.objects["Back Curtain"].data.shape_keys.key_blocks:
                single_shapekey.keyframe_delete(data_path='value', frame=0)
    
    bpy.app.handlers.frame_change_pre.append(stop_playback)

    bpy.ops.screen.animation_play()

     
def close_back_curtain():
    
    bpy.data.scenes[0].frame_current = 0

    context = bpy.context
    scene = context.scene
    mytool = scene.settings
    
    bpy.data.shape_keys["Key.002"].key_blocks["Key.002"].value = 1

    for single_shapekey in scene.objects["Back Curtain"].data.shape_keys.key_blocks:
        single_shapekey.keyframe_insert(data_path='value', frame=0)
        
    bpy.data.shape_keys["Key.002"].key_blocks["Key.002"].value = 0

    for single_shapekey in scene.objects["Back Curtain"].data.shape_keys.key_blocks:
        single_shapekey.keyframe_insert(data_path='value', frame=30)
        
    def stop_playback(scene):
        context = bpy.context
        scene = context.scene
        mytool = scene.settings

        if scene.frame_current == 30:
            bpy.ops.screen.animation_cancel(restore_frame=False)
            
            for single_shapekey in scene.objects["Back Curtain"].data.shape_keys.key_blocks:
                single_shapekey.keyframe_delete(data_path='value', frame=30)
                
            for single_shapekey in scene.objects["Back Curtain"].data.shape_keys.key_blocks:
                single_shapekey.keyframe_delete(data_path='value', frame=0)
    
    bpy.app.handlers.frame_change_pre.append(stop_playback)

    bpy.ops.screen.animation_play()
    

        
def mover_intensity():
    
    context = bpy.context
    scene = context.scene
    mytool = scene.settings
    
    intensity = mytool.intensity
    
    if mytool.selected_light == '25':
        selected_mover = scene.objects[mytool.selected_light]
        selected_mover.data.energy = (intensity * 100000)
        
    if mytool.selected_light == '26':
        selected_mover = scene.objects[mytool.selected_light]
        selected_mover.data.energy = (intensity * 100000)
    

def mover_zoom():
    
    context = bpy.context
    scene = context.scene
    mytool = scene.settings
    
    zoom = math.radians((mytool.zoom / 5) + 5)
    blend = (mytool.zoom / 100)
    intensity = mytool.intensity
    fade = intensity / (zoom * 1000)
    
    if mytool.selected_light == '25':
        selected_mover = scene.objects[mytool.selected_light]
        selected_mover.data.spot_size = zoom
        selected_mover.data.spot_blend = blend
        selected_mover.data.energy = (intensity * 100000 )
        
    if mytool.selected_light == '26':
        selected_mover = scene.objects[mytool.selected_light]
        selected_mover.data.spot_size = zoom
        selected_mover.data.spot_blend = blend
        selected_mover.data.energy = (intensity * 100000 )
        
        
        
def mover_position():
    
    context = bpy.context
    scene = context.scene
    mytool = scene.settings
    
    selected_mover = scene.objects[mytool.selected_light]

    mover_groups = mytool.mover_groups
    
    circle = scene.objects[f"Spot {selected_mover.name}"]
    
    global pan_25
    global pan_26
    global tilt_25
    global tilt_26
    

    if mover_groups == 'OP1':
        if selected_mover.name == "25":
            circle.location = scene.objects["25"].location
            pan_25 = 0
            tilt_25 = 0
        if selected_mover.name == "26":
            circle.location = scene.objects["26"].location
            pan_26 = 0
            tilt_26 = 0

    if mover_groups == 'OP2':
        if selected_mover.name == "25":
            circle.location = (0, -5, 0.7)
            pan_25 = 43.44
            tilt_25 = 29.34
        if selected_mover.name == "26":
            circle.location = (0, -5, 0.7)
            pan_26 = 55.84
            tilt_26 = 29.06

    if mover_groups == 'OP3':
        if selected_mover.name == "25":
            circle.location = (1, -2.5, 0.7)
            pan_25 = 44.34
            tilt_25 = 27.52
        if selected_mover.name == "26":
            circle.location = (-1, -2.5, 0.7)
            pan_26 = 54.83
            tilt_26 = 27.45

    if mover_groups == 'OP4':
        if selected_mover.name == "25":
            circle.location = (2.25, -2.5, 0.7)
            pan_25 = 44.74
            tilt_25 = 27.69
        if selected_mover.name == "26":
            circle.location = (-2.25, -2.5, 0.7)
            pan_26 = 54.40
            tilt_26 = 27.63

    if mover_groups == 'OP5':
        if selected_mover.name == "25":
            circle.location = (3.5, -5, 0.7)
            pan_25 = 46.13
            tilt_25 = 28.37
        if selected_mover.name == "26":
            circle.location = (3.5, -5, 0.7)
            pan_26 = 56.50
            tilt_26 = 26.58

    if mover_groups == 'OP6':
        if selected_mover.name == "25":
            circle.location = (-3.5, -5, 0.7)
            pan_25 = 42.63
            tilt_25 = 26.67
        if selected_mover.name == "26":
            circle.location = (-3.5, -5, 0.7)
            pan_26 = 53.16
            tilt_26 = 28.28
            
    if mover_groups == 'OP7':
        if selected_mover.name == "25":
            circle.location = (4.25, -5, 0.7)
            pan_25 = 47.04
            tilt_25 = 28.57
        if selected_mover.name == "26":
            circle.location = (4.25, -5, 0.7)
            pan_26 = 56.95
            tilt_26 = 26.01

    if mover_groups == 'OP8':
        if selected_mover.name == "25":
            circle.location = (-4.25, -5, 0.7)
            pan_25 = 42.22
            tilt_25 = 26.24
        if selected_mover.name == "26":
            circle.location = (-4.25, -5, 0.7)
            pan_26 = 52.24
            tilt_26 = 28.56

    if mover_groups == 'OP9':
        if selected_mover.name == "25":
            circle.location = (7.75, -5, 0.7)
            pan_25 = 48.62
            tilt_25 = 29.76
        if selected_mover.name == "26":
            circle.location = (7.75, -5, 0.7)
            pan_26 = 58.36
            tilt_26 = 25.59

    if mover_groups == 'OP10':
        if selected_mover.name == "25":
            circle.location = (-7.75, -5, 0.7)
            pan_25 = 40.73
            tilt_25 = 25.99
        if selected_mover.name == "26":
            circle.location = (-7.75, -5, 0.7)
            pan_26 = 50.92
            tilt_26 = 29.77

    if mover_groups == 'OP11':
        if selected_mover.name == "25":
            circle.location = (10.35, -5, 0.7)
            pan_25 = 49.89
            tilt_25 = 29.93
        if selected_mover.name == "26":
            circle.location = (10.35, -5, 0.7)
            pan_26 = 59.04
            tilt_26 = 25.47

    if mover_groups == 'OP12':
        if selected_mover.name == "25":
            circle.location = (-10.35, -5, 0.7)
            pan_25 = 40.36
            tilt_25 = 25.51
        if selected_mover.name == "26":
            circle.location = (-10.35, -5, 0.7)
            pan_26 = 49.50
            tilt_26 = 29.32

    if mover_groups == 'OP13':
        if selected_mover.name == "25":
            circle.location = (0, 2.7, 0.7)
            pan_25 = 44.34
            tilt_25 = 26.00
        if selected_mover.name == "Spot 26":
            circle.location = (0, 2.7, 0.7)
            pan_26 = 54.83
            tilt_26 = 26.00

    if mover_groups == 'OP14':
        if selected_mover.name == "25":
            circle.location = (3.5, 2.7, 0.7)
            pan_25 = 46.13
            tilt_25 = 26.50
        if selected_mover.name == "26":
            circle.location = (3.5, 2.7, 0.7)
            pan_26 = 56.00
            tilt_26 = 25.21

    if mover_groups == 'OP15':
        if selected_mover.name == "25":
            circle.location = (-3.5, 2.7, 0.7)
            pan_25 = 42.38
            tilt_25 = 24.68
        if selected_mover.name == "26":
            circle.location = (-3.5, 2.7, 0.7)
            pan_26 = 52.24
            tilt_26 = 26.50
            
    try:        
        mytool.pan_25_settings = pan_25
        mytool.pan_26_settings = pan_26
    except:
        mytool.pan_25_settings = 0
        mytool.pan_26_settings = 0
        
    try:        
        mytool.tilt_25_settings = tilt_25
        mytool.tilt_26_settings = tilt_26
    except:
        mytool.tilt_25_settings = 0
        mytool.tilt_26_settings = 0
        
        
def export_lights():

    context = bpy.context
    scene = context.scene
    mytool = scene.settings
    
    mover_groups = mytool.mover_groups
    
    bpy.ops.object.select_all(action='DESELECT')
    
    outfile = open((str(mytool.directory) + "/" + str(mytool.cue) + ".txt"), "a")
    
    pan_25 = mytool.pan_25_settings
    pan_26 = mytool.pan_26_settings
    tilt_25 = mytool.tilt_25_settings
    tilt_26 = mytool.tilt_26_settings
    
    
    data = (
    f"1.color = rgb({int(scene.objects['1'].data.color[0] * 100)},{int(scene.objects['1'].data.color[1] * 100)},{int(scene.objects['1'].data.color[2] * 100)})""\n"
    f"2.color = rgb({int(scene.objects['2'].data.color[0] * 100)},{int(scene.objects['2'].data.color[1] * 100)},{int(scene.objects['2'].data.color[2] * 100)})""\n"
    f"3.color = rgb({int(scene.objects['3'].data.color[0] * 100)},{int(scene.objects['3'].data.color[1] * 100)},{int(scene.objects['3'].data.color[2] * 100)})""\n"
    f"4.color = rgb({int(scene.objects['4'].data.color[0] * 100)},{int(scene.objects['4'].data.color[1] * 100)},{int(scene.objects['4'].data.color[2] * 100)})""\n"
    f"5.color = rgb({int(scene.objects['5'].data.color[0] * 100)},{int(scene.objects['5'].data.color[1] * 100)},{int(scene.objects['5'].data.color[2] * 100)})""\n"
    f"6.color = rgb({int(scene.objects['6'].data.color[0] * 100)},{int(scene.objects['6'].data.color[1] * 100)},{int(scene.objects['6'].data.color[2] * 100)})""\n"
    f"7.color = rgb({int(scene.objects['7'].data.color[0] * 100)},{int(scene.objects['7'].data.color[1] * 100)},{int(scene.objects['7'].data.color[2] * 100)})""\n"
    f"8.color = rgb({int(scene.objects['8'].data.color[0] * 100)},{int(scene.objects['8'].data.color[1] * 100)},{int(scene.objects['8'].data.color[2] * 100)})""\n"
    f"9.color = rgb({int(scene.objects['9'].data.color[0] * 100)},{int(scene.objects['9'].data.color[1] * 100)},{int(scene.objects['9'].data.color[2] * 100)})""\n"
    f"10.color = rgb({int(scene.objects['10'].data.color[0] * 100)},{int(scene.objects['10'].data.color[1] * 100)},{int(scene.objects['10'].data.color[2] * 100)})""\n"
    f"11.color = rgb({int(scene.objects['11'].data.color[0] * 100)},{int(scene.objects['11'].data.color[1] * 100)},{int(scene.objects['11'].data.color[2] * 100)})""\n"
    f"12.color = rgb({int(scene.objects['12'].data.color[0] * 100)},{int(scene.objects['12'].data.color[1] * 100)},{int(scene.objects['12'].data.color[2] * 100)})""\n"
    f"13.color = rgb({int(scene.objects['13'].data.color[0] * 100)},{int(scene.objects['13'].data.color[1] * 100)},{int(scene.objects['13'].data.color[2] * 100)})""\n"
    f"14.color = rgb({int(scene.objects['14'].data.color[0] * 100)},{int(scene.objects['14'].data.color[1] * 100)},{int(scene.objects['14'].data.color[2] * 100)})""\n"
    f"15.color = rgb({int(scene.objects['15'].data.color[0] * 100)},{int(scene.objects['15'].data.color[1] * 100)},{int(scene.objects['15'].data.color[2] * 100)})""\n"
    f"16.color = rgb({int(scene.objects['16'].data.color[0] * 100)},{int(scene.objects['16'].data.color[1] * 100)},{int(scene.objects['16'].data.color[2] * 100)})""\n"
    f"17.color = rgb({int(scene.objects['17'].data.color[0] * 100)},{int(scene.objects['17'].data.color[1] * 100)},{int(scene.objects['17'].data.color[2] * 100)})""\n"
    f"18.color = rgb({int(scene.objects['18'].data.color[0] * 100)},{int(scene.objects['18'].data.color[1] * 100)},{int(scene.objects['18'].data.color[2] * 100)})""\n"
    f"19.color = rgb({int(scene.objects['19'].data.color[0] * 100)},{int(scene.objects['19'].data.color[1] * 100)},{int(scene.objects['19'].data.color[2] * 100)})""\n"
    f"20.color = rgb({int(scene.objects['20'].data.color[0] * 100)},{int(scene.objects['20'].data.color[1] * 100)},{int(scene.objects['20'].data.color[2] * 100)})""\n"
    f"21.color = rgb({int(scene.objects['21'].data.color[0] * 100)},{int(scene.objects['21'].data.color[1] * 100)},{int(scene.objects['21'].data.color[2] * 100)})""\n"
    f"22.color = rgb({int(scene.objects['22'].data.color[0] * 100)},{int(scene.objects['22'].data.color[1] * 100)},{int(scene.objects['22'].data.color[2] * 100)})""\n"
    f"23.color = rgb({int(scene.objects['23'].data.color[0] * 100)},{int(scene.objects['23'].data.color[1] * 100)},{int(scene.objects['23'].data.color[2] * 100)})""\n"
    f"24.color = rgb({int(scene.objects['24'].data.color[0] * 100)},{int(scene.objects['24'].data.color[1] * 100)},{int(scene.objects['24'].data.color[2] * 100)})""\n"
    f"25.intensity = {int(scene.objects['25'].data.energy/100000)}""\n"
    f"25.color = cmy({int((scene.objects['25'].data.color[0]) * 100)},{int((scene.objects['25'].data.color[1]) * 100)},{int((scene.objects['25'].data.color[2]) * 100)})""\n"
    f"25.pan = {(pan_25)}""\n"
    f"25.tilt = {(tilt_25)}""\n"
    f"26.intensity = {int(scene.objects['26'].data.energy/100000)}""\n"
    f"26.color = cmy({int((scene.objects['26'].data.color[0]) * 100)},{int((scene.objects['26'].data.color[1]) * 100)},{int((scene.objects['26'].data.color[2]) * 100)})""\n"
    f"26.pan = {(pan_26)}""\n"
    f"26.tilt = {(tilt_26)}""\n"
    )
    
    
    
    
    outfile.write(data)
    
    bpy.ops.object.select_all(action='DESELECT')
    
    for frames in range(bpy.data.scenes[0].frame_end):
        for fc in scene.objects['25'].animation_data.action.fcurves:
            scene.objects['25'].keyframe_delete(data_path=fc.data_path, frame=frames)
        for fc in scene.objects['26'].animation_data.action.fcurves:
            scene.objects['26'].keyframe_delete(data_path=fc.data_path, frame=frames)
    
    

class Settings(PropertyGroup):
    
    selected_light : bpy.props.StringProperty(name = "Lights")

#    x_axis : bpy.props.FloatProperty(name = "x_axis", min = -90, max = 90)
 #   y_axis : bpy.props.FloatProperty(name = "y_axis", min = -90, max = 90)
  #  z_axis : bpy.props.FloatProperty(name = "z_axis", min = -90, max = 90)
    
    intensity : bpy.props.IntProperty(name = "Intensity", min = 0, max = 100)
    
    zoom : bpy.props.IntProperty(name = "Zoom", min = 0, max = 100)
    
    directory : bpy.props.StringProperty(name = "Directory:")
    
    cue : bpy.props.StringProperty(name = "Cue Name:")
    
    pan_25_settings : bpy.props.FloatProperty(name = "Pan 25", min = 0, max = 100, default = 0)
    pan_26_settings : bpy.props.FloatProperty(name = "Pan 26", min = 0, max = 100, default = 0)
    
    tilt_25_settings : bpy.props.FloatProperty(name = "Tilt 25", min = 0, max = 100, default = 0)
    tilt_26_settings : bpy.props.FloatProperty(name = "Tilt 26", min = 0, max = 100, default = 0)
    
    
    groups : bpy.props.EnumProperty(
            name="Light Classes",
            description="Lighting Groups",
            items = [
                ('OP1', "None", ""),
                ('OP2', "CYC", ""),
                ('OP3', "PAR DS", ""),
                ('OP4', "PAR US", ""),
                ('OP5', "FOH", ""),
                ('OP6', "movers", "")
                ]
    )
    
    mover_groups : bpy.props.EnumProperty(
            name="Mover Presets",
            description="Mover Presets",
            items = [
                ('OP1', "None", ""),
                ('OP2', "Front-Center", ""),
                ('OP3', "Middle-Center-1", ""),
                ('OP4', "Middle-Center-2", ""),
                ('OP5', "Middle-Left-1", ""),
                ('OP6', "Middle-Right-1", ""),
                ('OP7', "Middle-Left-2", ""),
                ('OP8', "Middle-Right-2", ""),
                ('OP9', "Left-1", ""),
                ('OP10', "Right-1", ""),
                ('OP11', "Left-2", ""),
                ('OP12', "Right-2", ""),
                ('OP13', "Back-Center", ""),
                ('OP14', "Back-Left", ""),
                ('OP15', "Back-Right", "")
                ]
    )




class ExportLights(bpy.types.Operator):
    """ExportLights"""
    bl_idname = "object.export_lights"
    bl_label = "Export Lights"

    def execute(self, context): 
        context = bpy.context
        scene = context.scene
        export_lights()
        return {'FINISHED'}


class ChangeColor(bpy.types.Operator):
    """ChangeColor"""
    bl_idname = "object.change_color"
    bl_label = "Change Light Color"
    
    context = bpy.context
    scene = context.scene

    def execute(self, context):  
        context = bpy.context
        scene = context.scene
        mytool = scene.settings
        clr = context.scene.mytool_color
        change_color(float(clr[0]), float(clr[1]), float(clr[2]), mytool.selected_light)
        return {'FINISHED'}
    
class OpenFrontCurtain(bpy.types.Operator):
    """OpenFrontCurtian"""
    bl_idname = "object.open_front_curtian"
    bl_label = "Open Front Curtain"
    
    context = bpy.context
    scene = context.scene

    def execute(self, context): 
        open_front_curtain()
        return {'FINISHED'}
    
class CloseFrontCurtain(bpy.types.Operator):
    """CloseFrontCurtian"""
    bl_idname = "object.close_front_curtian"
    bl_label = "Close Front Curtain"
    
    context = bpy.context
    scene = context.scene

    def execute(self, context): 
        close_front_curtain()
        return {'FINISHED'}
    
class OpenMiddleCurtain(bpy.types.Operator):
    """OpenMiddleCurtian"""
    bl_idname = "object.open_middle_curtian"
    bl_label = "Open Middle Curtain"
    
    context = bpy.context
    scene = context.scene

    def execute(self, context): 
        open_middle_curtain()
        return {'FINISHED'}
    
class CloseMiddleCurtain(bpy.types.Operator):
    """CloseMiddleCurtian"""
    bl_idname = "object.close_middle_curtian"
    bl_label = "Close Middle Curtain"
    
    context = bpy.context
    scene = context.scene

    def execute(self, context): 
        close_middle_curtain()
        return {'FINISHED'}
    
    
class OpenBackCurtain(bpy.types.Operator):
    """OpenBackCurtian"""
    bl_idname = "object.open_back_curtian"
    bl_label = "Open Back Curtain"
    
    context = bpy.context
    scene = context.scene

    def execute(self, context): 
        open_back_curtain()
        return {'FINISHED'}
    
class CloseBackCurtain(bpy.types.Operator):
    """CloseBackCurtian"""
    bl_idname = "object.close_back_curtian"
    bl_label = "Close Back Curtain"
    
    context = bpy.context
    scene = context.scene

    def execute(self, context): 
        close_back_curtain()
        return {'FINISHED'}
"""    
class Movers(bpy.types.Operator):
    bl_idname = "object.movers"
    bl_label = "Change Mover Position"
    
    context = bpy.context
    scene = context.scene

    def execute(self, context): 
        change_mover_position()
        return {'FINISHED'}
    """
    
class MoversIntensity(bpy.types.Operator):
    """MoversIntensity"""
    bl_idname = "object.movers_intensity"
    bl_label = "Change Mover Intensity"
    
    context = bpy.context
    scene = context.scene

    def execute(self, context): 
        mover_intensity()
        return {'FINISHED'}
    
class MoversZoom(bpy.types.Operator):
    """MoversZoom"""
    bl_idname = "object.movers_zoom"
    bl_label = "Change Mover Zoom"
    
    context = bpy.context
    scene = context.scene

    def execute(self, context): 
        mover_zoom()
        return {'FINISHED'}
    
class MoversPosition(bpy.types.Operator):
    """MoversPosition"""
    bl_idname = "object.movers_position"
    bl_label = "Change Mover Position"
    
    context = bpy.context
    scene = context.scene

    def execute(self, context): 
        mover_position()
        return {'FINISHED'}


class VirtualLightingEnvironment(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Virtual Lighting Environment"
    bl_category = "Virtual Lighting Environment"
    bl_idname = "Virtual Lighting Environment"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_label = "Virtual Lighting Environment"
    

    def draw(self, context):
        layout = self.layout
        context = bpy.context
        settings = context.scene.settings
        scene = context.scene
        mytool = scene.settings
        lights_collection = bpy.data.collections["Lights"]
        
        
        self.prev_front_curtain = None 
        
        row = layout.row()
        layout.prop_search(mytool, "selected_light", lights_collection, "objects")
        
        row = layout.row()
        row.prop(context.scene, "mytool_color")
        
        row = layout.row()
        row.operator(ChangeColor.bl_idname, icon="LIGHT")
        
        layout.prop(mytool, "groups")
        
        layout.prop(mytool, "mover_groups")
        
        row = layout.row()
        row.operator(MoversPosition.bl_idname)
        
        
#        layout.prop(mytool, "x_axis")
 #       layout.prop(mytool, "y_axis")
  #      layout.prop(mytool, "z_axis")
        
#        row = layout.row()
 #       row.operator(Movers.bl_idname, icon="PIVOT_CURSOR")
        
        row = layout.row()
        row.label(text="Movers Intensity")
        
        layout.prop(mytool, "intensity")
        
        row = layout.row()
        row.operator(MoversIntensity.bl_idname, icon="LIGHT_POINT")
        
        row = layout.row()
        row.label(text="Movers Zoom")
        
        layout.prop(mytool, "zoom")
        
        row = layout.row()
        row.operator(MoversZoom.bl_idname, icon="LIGHT_POINT")
        
        row = layout.row()
        row.label(text="Export Cue")
        
        layout.prop(mytool, "directory")
        
        layout.prop(mytool, "cue")
        
        row = layout.row()
        row.operator(ExportLights.bl_idname, icon="LIGHT_POINT")
        
        row = layout.row()
        row.label(text="Front Curtain")
        
        row = layout.row()
        row.operator(OpenFrontCurtain.bl_idname)
        
        row = layout.row()
        row.operator(CloseFrontCurtain.bl_idname)
        
        row = layout.row()
        row.label(text="Middle Curtain")
        
        row = layout.row()
        row.operator(OpenMiddleCurtain.bl_idname)
        
        row = layout.row()
        row.operator(CloseMiddleCurtain.bl_idname)
        
        row = layout.row()
        row.label(text="Back Curtain")
        
        row = layout.row()
        row.operator(OpenBackCurtain.bl_idname)
        
        row = layout.row()
        row.operator(CloseBackCurtain.bl_idname)

        
def register():
    bpy.utils.register_class(VirtualLightingEnvironment)
    bpy.utils.register_class(ChangeColor)
    bpy.utils.register_class(OpenFrontCurtain)
    bpy.utils.register_class(CloseFrontCurtain)
    bpy.utils.register_class(OpenMiddleCurtain)
    bpy.utils.register_class(CloseMiddleCurtain)
    bpy.utils.register_class(OpenBackCurtain)
    bpy.utils.register_class(CloseBackCurtain)
    bpy.utils.register_class(Settings)
#    bpy.utils.register_class(Movers)
    bpy.utils.register_class(MoversIntensity)
    bpy.utils.register_class(MoversPosition)
    bpy.utils.register_class(MoversZoom)
    bpy.utils.register_class(ExportLights)
    bpy.types.Scene.settings = bpy.props.PointerProperty(type=Settings)
    
    
    # Register the property per Scene, Object or whatever
    bpy.types.Scene.mytool_color = bpy.props.FloatVectorProperty(
                 name = "Color Picker",
                 subtype = "COLOR",
                 size = 4,
                 min = 0.0,
                 max = 1.0,
                 default = (1.0,1.0,1.0,1.0))       
                 
    
def unregister():
    bpy.utils.unregister_class(ChangeColor)
    bpy.utils.unregister_class(VirtualLightingEnvironment)
    bpy.utils.unregister_class(OpenFrontCurtain)
    bpy.utils.unregister_class(CloseFrontCurtain)
    bpy.utils.unregister_class(OpenMiddleCurtain)
    bpy.utils.unregister_class(CloseMiddleCurtain)
    bpy.utils.unregister_class(OpenBackCurtain)
    bpy.utils.unregister_class(CloseBackCurtain)
#    bpy.utils.unregister_class(Movers)
    bpy.utils.unregister_class(MoversIntensity)
    bpy.utils.unregister_class(MoversPosition)
    bpy.utils.unregister_class(MoversZoom)
    bpy.utils.unregister_class(ExportLights)
    
    del bpy.types.Scene.mytool_color
    del bpy.types.Scene.settings

if __name__ == "__main__":
    register()
    
