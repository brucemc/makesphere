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

bl_info = {
    "name" : "MakeSphere",
    "author" : "Bruce McIntosh",
	"description": "Make duplicates of selected object in a spherical arrangement",
    "blender" : (2, 80, 0),
    "version" : (0, 0, 1),
    "warning" : "",
   	"location": "3D View > Properties> Make Sphere",
	"category": "Object"}

import bpy
from bpy.props import *

class BMC_Make_Sphere_Properties(bpy.types.PropertyGroup):
    obj : bpy.props.PointerProperty(name="Source Object", type=bpy.types.Object)


from . bmc_make_sphere import BMC_OT_Make_Sphere
from . bmc_make_sphere_panel import BMC_PT_Make_Sphere_Panel
	
classes = (
        BMC_Make_Sphere_Properties,
        BMC_OT_Make_Sphere,
        BMC_PT_Make_Sphere_Panel,
)

def register():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)

    bpy.types.Scene.BMC_MS = bpy.props.PointerProperty(type=BMC_Make_Sphere_Properties)

def unregister():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)
    del bpy.types.Scene.BMC_MS
