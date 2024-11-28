import bpy

# Define a property to store the checkbox state
def register_properties():
    bpy.types.Scene.auto_set_preview_range = bpy.props.BoolProperty(
        name="Preview Range Matching Action",
        description="Automatically set preview frame range based on selected action",
        default=True
    )

def unregister_properties():
    del bpy.types.Scene.auto_set_preview_range

# Define the event listener function
@bpy.app.handlers.persistent
def update_preview_range(scene):
    obj = bpy.context.view_layer.objects.active
    if obj and obj.animation_data:
        action = obj.animation_data.action
        if action and scene.auto_set_preview_range:
            # print(f"New action selected: {action.name}")
            
            # Set the scene's frame range based on the action's frame range
            scene.frame_preview_start = int(action.frame_range[0])
            scene.frame_preview_end = int(action.frame_range[1])
            #print(f"Scene frame range set to: {scene.frame_start} - {scene.frame_end}")

# Register the event handler
def register_handler():
    bpy.app.handlers.animation_playback_pre.append(update_preview_range)
    bpy.app.handlers.load_post.append(update_preview_range)
    # bpy.app.handlers.depsgraph_update_post.append(update_preview_range)

def unregister_handler():
    bpy.app.handlers.animation_playback_pre.remove(update_preview_range)
    bpy.app.handlers.load_post.remove(update_preview_range)
    # bpy.app.handlers.depsgraph_update_post.remove(update_preview_range)

def draw(self, context):
    layout = self.layout
    scene = context.scene

    col = layout.column(heading="Preview Range")
    col.prop(scene, "auto_set_preview_range", text="Match Action")

# Add property checkbox to Playback menu
def register_menu():
    bpy.types.TIME_PT_playback.append(draw)

def unregister_menu():
    bpy.types.TIME_PT_playback.remove(draw)

# Register and unregister
def register():
    register_properties()
    register_handler()
    register_menu()

def unregister():
    unregister_properties()
    unregister_handler()
    unregister_menu()