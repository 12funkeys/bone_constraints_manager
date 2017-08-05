import bpy
from bl_ui.properties_constraint import ConstraintButtonsPanel

bl_info = {
    "name" : "Bone Constraints Manager",
    "author" : "12funkeys",
    "version" : (0,1),
    "blender" : (2, 7, 8),
    "location" : "PROPERTIES > data",
    "description" : "Bone Constraints Controll in one view",
    "warning" : "",
    "wiki_url" : "",
    "tracker_url" : "",
    "category" : "Rigging"
}


class addonUI(bpy.types.Panel):
    bl_label = "Bone Constraints Manager"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "data"
  
    def draw(self, context):
        layout = self.layout
        
        row = layout.row(align=False)
        row.alignment = 'RIGHT'
        row.label("All Controll")
        row.operator(FuncMuteOFF.bl_idname, text="", icon='RESTRICT_VIEW_OFF', emboss=True)
        row.operator(FuncMuteON.bl_idname, text="", icon='RESTRICT_VIEW_ON', emboss=True)
        row.operator(FuncOpen.bl_idname, text="", icon='ZOOMIN', emboss=True)
        row.operator(FuncClose.bl_idname, text="", icon='ZOOMOUT', emboss=True)
        
        obj = bpy.context.active_object
        
        for bone in obj.data.bones:

            layout.label(bone.name, icon='BONE_DATA')
       
            if obj.pose.bones[bone.name].constraints:
       
                for con in obj.pose.bones[bone.name].constraints:   

                    box = layout.template_constraint(con)

                    if box:
                        getattr(ConstraintButtonsPanel, con.type)(ConstraintButtonsPanel, context, box, con)    
                        #getattr(self, con.type)(context, box, con)

#mute
class FuncMuteON(bpy.types.Operator):
    bl_idname = "bone_constraints_manager.muteon"
    bl_label = "constraint muteon"
    bl_description = "all constraints mute off"
    bl_options = {'REGISTER', 'UNDO'}
  
    def execute(self, context):

        obj = bpy.context.active_object

        for bone in obj.data.bones:
            for con in obj.pose.bones[bone.name].constraints: 
                con.mute = True
                print("ok")

        return{'FINISHED'}

class FuncMuteOFF(bpy.types.Operator):
    bl_idname = "bone_constraints_manager.muteoff"
    bl_label = "constraint muteoff"
    bl_description = "all constraints mute on"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        obj = bpy.context.active_object

        for bone in obj.data.bones:
            for con in obj.pose.bones[bone.name].constraints: 
                con.mute = False
                print("ok")

        return{'FINISHED'}

#close
class FuncOpen(bpy.types.Operator):
    bl_idname = "bone_constraints_manager.open"
    bl_label = "constraint close"
    bl_description = "all constraints expand open"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        obj = bpy.context.active_object

        for bone in obj.data.bones:
            for con in obj.pose.bones[bone.name].constraints: 
                con.show_expanded = True
                print("ok")
            
        return{'FINISHED'}

class FuncClose(bpy.types.Operator):
    bl_idname = "bone_constraints_manager.close"
    bl_label = "constraint close"
    bl_description = "all constraints expand close"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        obj = bpy.context.active_object

        for bone in obj.data.bones:
            for con in obj.pose.bones[bone.name].constraints: 
                con.show_expanded = False
                print("ok")
            
        return{'FINISHED'}


def register():
    bpy.utils.register_module(__name__)


def unregister():
    bpy.utils.unregister_module(__name__)


if __name__ == '__main__':
    register()


#thanks
#https://blender.stackexchange.com/questions/46882/what-draws-the-constraint-menu-completely
