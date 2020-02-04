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

import bpy

class BMC_PT_Make_Sphere_Panel(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Make Sphere"
    bl_label = "Make Sphere"
    bl_idname = "bmc.make_sphere_panel"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        props = scene.BMC_MS

        row = layout.row()
        layout.prop(props, "obj", text="Object")

        row = layout.row()
        row.operator('bmc.make_sphere', text="Make Sphere")

        
