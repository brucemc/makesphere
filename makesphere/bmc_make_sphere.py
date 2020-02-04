# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import bpy, bpy_extras, math, random
from bpy.props import *
from mathutils import *

class BMC_OT_Make_Sphere(bpy.types.Operator):
    """ Make a sphere """
    bl_label = 'Make a sphere'
    bl_idname = "bmc.make_sphere"
    bl_options = {'REGISTER', 'UNDO'}

    dup_number: bpy.props.IntProperty(
        name = "Number of Duplicates",
        default = 16,
        min = 1,
        max = 1024,
        description = "The number of duplicates to place in sphere",
    )

    radius: bpy.props.FloatProperty(
        name = "Radius",
        default = 2.0,
        min = 0.0001,
        max = 1024.0,
        description = "Radius of sphere",
    )

    def execute(self, context):
        scene = context.scene
        obj = scene.BMC_MS.obj

        points = fibonacci_sphere(self.dup_number, True)

        v0 = Vector((0,0,1))

        for i in range(self.dup_number):
            obj_new = obj.copy()
            scene.collection.objects.link(obj_new)
            x, y, z = map(lambda x: x * self.radius, points[i])
            v1 = Vector((x,y,z))
            rot = v0.rotation_difference(v1).to_euler()
            obj_new.rotation_euler = rot
            obj_new.location=(x,y,z)

        return {"FINISHED"}

# Credit for sphere positioning code:
# https://stackoverflow.com/users/1429402/fnord
# https://stackoverflow.com/questions/9600801/evenly-distributing-n-points-on-a-sphere

def fibonacci_sphere(samples=1,randomize=True):
    rnd = 1.
    if randomize:
        rnd = random.random() * samples

    points = []
    offset = 2./samples
    increment = math.pi * (3. - math.sqrt(5.));

    for i in range(samples):
        y = ((i * offset) - 1) + (offset / 2);
        r = math.sqrt(1 - pow(y,2))

        phi = ((i + rnd) % samples) * increment

        x = math.cos(phi) * r
        z = math.sin(phi) * r

        points.append([x,y,z])

    return points

