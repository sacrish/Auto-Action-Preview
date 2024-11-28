bl_info = {
    "name": "Auto Action Preview",
    "author": "Zakrich",
    "version": (1, 0, 1),
    "blender": (4, 2, 0),
    "description": "Auto set preview frame range to match current action, for more convenient animation loop preview.",
    "warning": "",
    "doc_url": "https://github.com/sacrish/Auto-Action-Preview",
    "tracker_url": "https://github.com/sacrish/Auto-Action-Preview/issues",
    "category": "Animation",
}

import bpy

from . import auto_set_preview_range

def register():
    auto_set_preview_range.register()

def unregister():
    auto_set_preview_range.unregister()

if __name__ == "__main__":
    register()