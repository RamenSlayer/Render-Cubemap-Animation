bl_info = {
    "name": "ReCuAn",
    "author": "RamenSlayer",
    "version": (1, 0),
    "blender": (2, 92, 0),
    "location": "View3D > UI",
    "description": "Render an animation with a cubemap",
    "category": "Render",
}

import bpy

class RECUAN_OT_OP(bpy.types.Operator):
    bl_idname = "view3d.recuan"
    bl_label = "ReCuAn"
    bl_description = "Render an animation rebaking the cubemap every frame"

    # (filepath, framename, render_scene)

    def execute(self, context):
        fpath = str(context.scene.filepath)
        rscene = str(context.scene.render_scene).split()[1].split('"')[1]
        fname = str(context.scene.framename)

        for i in range (bpy.context.scene.frame_start, bpy.context.scene.frame_end + 1):
            bpy.data.scenes[rscene].frame_current = i
            bpy.ops.scene.light_cache_bake()
            bpy.data.scenes[rscene].render.filepath = fpath + fname + str(bpy.data.scenes[rscene].frame_current)
            bpy.ops.render.render(write_still=1)
        
        return {"FINISHED"}


class RECUAN_PT_Panel(bpy.types.Panel):
    bl_idname = "RECUAN_PT_Panel"
    bl_label = "ReCuAn Panel"
    bl_category = "ReCuAn"
    bl_space_type = "VIEW_3D"
    bl_register_type = "UI"
    bl_region_type = "UI"
    
    # @classmethod
    # def poll(cls, context):
    #     return (context.object is not None)


    def draw(self, context):
        self.layout.prop(context.scene, "filepath")

        self.layout.prop(context.scene, "framename")

        self.layout.prop(context.scene, "render_scene")

        self.layout.operator('view3d.recuan', text="Render animation")

classes = (RECUAN_OT_OP, RECUAN_PT_Panel)

def register():
    for c in classes:
        bpy.utils.register_class(c)

    bpy.types.Scene.filepath = bpy.props.StringProperty(
        name = "path",
        subtype = "DIR_PATH",
        default = "../renderframes/",
        description = "Path saying where the animation should be rendered to."
        )

    bpy.types.Scene.framename = bpy.props.StringProperty(
        name = "name",
        default = "frame",
        description = "Name for the frame sequence"
        )

    bpy.types.Scene.render_scene = bpy.props.PointerProperty(
        name = "scene",
        type = bpy.types.Scene,
        # default = "Scene",
        description = "Pick which scene should be rendered. Usually doesn't need to be changed unless you have multiple scenes or renamed one"
        )

def unregister():
    for c in classes:
        bpy.utils.unregister_class(c)
