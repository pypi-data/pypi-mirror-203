import sys
import typing


def delete():
    ''' Delete active scene

    '''

    pass


def freestyle_add_edge_marks_to_keying_set():
    ''' Add the data paths to the Freestyle Edge Mark property of selected edges to the active keying set :File: startup/bl_operators/freestyle.py\:134 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/freestyle.py#L134> __

    '''

    pass


def freestyle_add_face_marks_to_keying_set():
    ''' Add the data paths to the Freestyle Face Mark property of selected polygons to the active keying set :File: startup/bl_operators/freestyle.py\:165 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/freestyle.py#L165> __

    '''

    pass


def freestyle_alpha_modifier_add(
        type: typing.Union[int, str] = 'ALONG_STROKE'):
    ''' Add an alpha transparency modifier to the line style associated with the active lineset

    :param type: Type
    :type type: typing.Union[int, str]
    '''

    pass


def freestyle_color_modifier_add(
        type: typing.Union[int, str] = 'ALONG_STROKE'):
    ''' Add a line color modifier to the line style associated with the active lineset

    :param type: Type
    :type type: typing.Union[int, str]
    '''

    pass


def freestyle_fill_range_by_selection(type: typing.Union[int, str] = 'COLOR',
                                      name: str = ""):
    ''' Fill the Range Min/Max entries by the min/max distance between selected mesh objects and the source object (either a user-specified object or the active camera) :File: startup/bl_operators/freestyle.py\:40 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/freestyle.py#L40> __

    :param type: Type, Type of the modifier to work on * COLOR Color -- Color modifier type. * ALPHA Alpha -- Alpha modifier type. * THICKNESS Thickness -- Thickness modifier type.
    :type type: typing.Union[int, str]
    :param name: Name, Name of the modifier to work on
    :type name: str
    '''

    pass


def freestyle_geometry_modifier_add(
        type: typing.Union[int, str] = '2D_OFFSET'):
    ''' Add a stroke geometry modifier to the line style associated with the active lineset

    :param type: Type
    :type type: typing.Union[int, str]
    '''

    pass


def freestyle_lineset_add():
    ''' Add a line set into the list of line sets

    '''

    pass


def freestyle_lineset_copy():
    ''' Copy the active line set to a buffer

    '''

    pass


def freestyle_lineset_move(direction: typing.Union[int, str] = 'UP'):
    ''' Change the position of the active line set within the list of line sets

    :param direction: Direction, Direction to move the active line set towards
    :type direction: typing.Union[int, str]
    '''

    pass


def freestyle_lineset_paste():
    ''' Paste the buffer content to the active line set

    '''

    pass


def freestyle_lineset_remove():
    ''' Remove the active line set from the list of line sets

    '''

    pass


def freestyle_linestyle_new():
    ''' Create a new line style, reusable by multiple line sets

    '''

    pass


def freestyle_modifier_copy():
    ''' Duplicate the modifier within the list of modifiers

    '''

    pass


def freestyle_modifier_move(direction: typing.Union[int, str] = 'UP'):
    ''' Move the modifier within the list of modifiers

    :param direction: Direction, Direction to move the chosen modifier towards
    :type direction: typing.Union[int, str]
    '''

    pass


def freestyle_modifier_remove():
    ''' Remove the modifier from the list of modifiers

    '''

    pass


def freestyle_module_add():
    ''' Add a style module into the list of modules

    '''

    pass


def freestyle_module_move(direction: typing.Union[int, str] = 'UP'):
    ''' Change the position of the style module within in the list of style modules

    :param direction: Direction, Direction to move the chosen style module towards
    :type direction: typing.Union[int, str]
    '''

    pass


def freestyle_module_open(filepath: str = "", make_internal: bool = True):
    ''' Open a style module file :File: startup/bl_operators/freestyle.py\:209 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/freestyle.py#L209> __

    :param filepath: filepath
    :type filepath: str
    :param make_internal: Make internal, Make module file internal after loading
    :type make_internal: bool
    '''

    pass


def freestyle_module_remove():
    ''' Remove the style module from the stack

    '''

    pass


def freestyle_stroke_material_create():
    ''' Create Freestyle stroke material for testing

    '''

    pass


def freestyle_thickness_modifier_add(
        type: typing.Union[int, str] = 'ALONG_STROKE'):
    ''' Add a line thickness modifier to the line style associated with the active lineset

    :param type: Type
    :type type: typing.Union[int, str]
    '''

    pass


def gpencil_brush_preset_add(name: str = "",
                             remove_name: bool = False,
                             remove_active: bool = False):
    ''' Add or remove grease pencil brush preset :File: startup/bl_operators/presets.py\:73 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/presets.py#L73> __

    :param name: Name, Name of the preset, used to make the path name
    :type name: str
    :param remove_name: remove_name
    :type remove_name: bool
    :param remove_active: remove_active
    :type remove_active: bool
    '''

    pass


def gpencil_material_preset_add(name: str = "",
                                remove_name: bool = False,
                                remove_active: bool = False):
    ''' Add or remove grease pencil material preset :File: startup/bl_operators/presets.py\:73 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/presets.py#L73> __

    :param name: Name, Name of the preset, used to make the path name
    :type name: str
    :param remove_name: remove_name
    :type remove_name: bool
    :param remove_active: remove_active
    :type remove_active: bool
    '''

    pass


def light_cache_bake(delay: int = 0, subset: typing.Union[int, str] = 'ALL'):
    ''' Bake the active view layer lighting

    :param delay: Delay, Delay in millisecond before baking starts
    :type delay: int
    :param subset: Subset, Subset of probes to update * ALL All Light Probes -- Bake both irradiance grids and reflection cubemaps. * DIRTY Dirty Only -- Only bake light probes that are marked as dirty. * CUBEMAPS Cubemaps Only -- Try to only bake reflection cubemaps if irradiance grids are up to date.
    :type subset: typing.Union[int, str]
    '''

    pass


def light_cache_free():
    ''' Delete cached indirect lighting

    '''

    pass


def new(type: typing.Union[int, str] = 'NEW'):
    ''' Add new scene by type

    :param type: Type * NEW New -- Add a new, empty scene with default settings. * EMPTY Copy Settings -- Add a new, empty scene, and copy settings from the current scene. * LINK_COPY Linked Copy -- Link in the collections from the current scene (shallow copy). * FULL_COPY Full Copy -- Make a full copy of the current scene.
    :type type: typing.Union[int, str]
    '''

    pass


def new_sequencer(type: typing.Union[int, str] = 'NEW'):
    ''' Add new scene by type in the sequence editor and assign to active strip

    :param type: Type * NEW New -- Add a new, empty scene with default settings. * EMPTY Copy Settings -- Add a new, empty scene, and copy settings from the current scene. * LINK_COPY Linked Copy -- Link in the collections from the current scene (shallow copy). * FULL_COPY Full Copy -- Make a full copy of the current scene.
    :type type: typing.Union[int, str]
    '''

    pass


def render_view_add():
    ''' Add a render view

    '''

    pass


def render_view_remove():
    ''' Remove the selected render view

    '''

    pass


def view_layer_add(type: typing.Union[int, str] = 'NEW'):
    ''' Add a view layer

    :param type: Type * NEW New -- Add a new view layer. * COPY Copy Settings -- Copy settings of current view layer. * EMPTY Blank -- Add a new view layer with all collections disabled.
    :type type: typing.Union[int, str]
    '''

    pass


def view_layer_add_aov():
    ''' Add a Shader AOV

    '''

    pass


def view_layer_add_lightgroup(name: str = ""):
    ''' Add a Light Group

    :param name: Name, Name of newly created lightgroup
    :type name: str
    '''

    pass


def view_layer_add_used_lightgroups():
    ''' Add all used Light Groups

    '''

    pass


def view_layer_remove():
    ''' Remove the selected view layer

    '''

    pass


def view_layer_remove_aov():
    ''' Remove Active AOV

    '''

    pass


def view_layer_remove_lightgroup():
    ''' Remove Active Lightgroup

    '''

    pass


def view_layer_remove_unused_lightgroups():
    ''' Remove all unused Light Groups

    '''

    pass
