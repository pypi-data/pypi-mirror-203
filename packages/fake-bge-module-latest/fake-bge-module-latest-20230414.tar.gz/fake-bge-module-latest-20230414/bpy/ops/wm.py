import sys
import typing
import bpy.types
import bl_operators.wm


def append(filepath: str = "",
           directory: str = "",
           filename: str = "",
           files: typing.
           Union[typing.Dict[str, 'bpy.types.OperatorFileListElement'], typing.
                 List['bpy.types.OperatorFileListElement'],
                 'bpy_prop_collection'] = None,
           check_existing: bool = False,
           filter_blender: bool = True,
           filter_backup: bool = False,
           filter_image: bool = False,
           filter_movie: bool = False,
           filter_python: bool = False,
           filter_font: bool = False,
           filter_sound: bool = False,
           filter_text: bool = False,
           filter_archive: bool = False,
           filter_btx: bool = False,
           filter_collada: bool = False,
           filter_alembic: bool = False,
           filter_usd: bool = False,
           filter_obj: bool = False,
           filter_volume: bool = False,
           filter_folder: bool = True,
           filter_blenlib: bool = True,
           filemode: int = 1,
           display_type: typing.Union[int, str] = 'DEFAULT',
           sort_method: typing.Union[int, str] = '',
           link: bool = False,
           do_reuse_local_id: bool = False,
           clear_asset_data: bool = False,
           autoselect: bool = True,
           active_collection: bool = True,
           instance_collections: bool = False,
           instance_object_data: bool = True,
           set_fake: bool = False,
           use_recursive: bool = True):
    ''' Append from a Library .blend file

    :param filepath: File Path, Path to file
    :type filepath: str
    :param directory: Directory, Directory of the file
    :type directory: str
    :param filename: File Name, Name of the file
    :type filename: str
    :param files: Files
    :type files: typing.Union[typing.Dict[str, 'bpy.types.OperatorFileListElement'], typing.List['bpy.types.OperatorFileListElement'], 'bpy_prop_collection']
    :param check_existing: Check Existing, Check and warn on overwriting existing files
    :type check_existing: bool
    :param filter_blender: Filter .blend files
    :type filter_blender: bool
    :param filter_backup: Filter .blend files
    :type filter_backup: bool
    :param filter_image: Filter image files
    :type filter_image: bool
    :param filter_movie: Filter movie files
    :type filter_movie: bool
    :param filter_python: Filter python files
    :type filter_python: bool
    :param filter_font: Filter font files
    :type filter_font: bool
    :param filter_sound: Filter sound files
    :type filter_sound: bool
    :param filter_text: Filter text files
    :type filter_text: bool
    :param filter_archive: Filter archive files
    :type filter_archive: bool
    :param filter_btx: Filter btx files
    :type filter_btx: bool
    :param filter_collada: Filter COLLADA files
    :type filter_collada: bool
    :param filter_alembic: Filter Alembic files
    :type filter_alembic: bool
    :param filter_usd: Filter USD files
    :type filter_usd: bool
    :param filter_obj: Filter OBJ files
    :type filter_obj: bool
    :param filter_volume: Filter OpenVDB volume files
    :type filter_volume: bool
    :param filter_folder: Filter folders
    :type filter_folder: bool
    :param filter_blenlib: Filter Blender IDs
    :type filter_blenlib: bool
    :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
    :type filemode: int
    :param display_type: Display Type * DEFAULT Default -- Automatically determine display type for files. * LIST_VERTICAL Short List -- Display files as short list. * LIST_HORIZONTAL Long List -- Display files as a detailed list. * THUMBNAIL Thumbnails -- Display files as thumbnails.
    :type display_type: typing.Union[int, str]
    :param sort_method: File sorting mode
    :type sort_method: typing.Union[int, str]
    :param link: Link, Link the objects or data-blocks rather than appending
    :type link: bool
    :param do_reuse_local_id: Re-Use Local Data, Try to re-use previously matching appended data-blocks instead of appending a new copy
    :type do_reuse_local_id: bool
    :param clear_asset_data: Clear Asset Data, Don't add asset meta-data or tags from the original data-block
    :type clear_asset_data: bool
    :param autoselect: Select, Select new objects
    :type autoselect: bool
    :param active_collection: Active Collection, Put new objects on the active collection
    :type active_collection: bool
    :param instance_collections: Instance Collections, Create instances for collections, rather than adding them directly to the scene
    :type instance_collections: bool
    :param instance_object_data: Instance Object Data, Create instances for object data which are not referenced by any objects
    :type instance_object_data: bool
    :param set_fake: Fake User, Set "Fake User" for appended items (except objects and collections)
    :type set_fake: bool
    :param use_recursive: Localize All, Localize all appended data, including those indirectly linked from other libraries
    :type use_recursive: bool
    '''

    pass


def batch_rename(
        data_type: typing.Union[int, str] = 'OBJECT',
        data_source: typing.Union[int, str] = 'SELECT',
        actions: typing.
        Union[typing.Dict[str, 'bl_operators.wm.BatchRenameAction'], typing.
              List['bl_operators.wm.BatchRenameAction'],
              'bpy_prop_collection'] = None):
    ''' Rename multiple items at once :File: startup/bl_operators/wm.py\:3087 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/wm.py#L3087> __

    :param data_type: Type, Type of data to rename
    :type data_type: typing.Union[int, str]
    :param data_source: Source
    :type data_source: typing.Union[int, str]
    :param actions: actions
    :type actions: typing.Union[typing.Dict[str, 'bl_operators.wm.BatchRenameAction'], typing.List['bl_operators.wm.BatchRenameAction'], 'bpy_prop_collection']
    '''

    pass


def blend_strings_utf8_validate():
    ''' Check and fix all strings in current .blend file to be valid UTF-8 Unicode (needed for some old, 2.4x area files) :File: startup/bl_operators/file.py\:288 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/file.py#L288> __

    '''

    pass


def blenderplayer_start():
    ''' Launch the blender-player with the current blend-file :File: startup/bl_operators/wm.py\:2125 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/wm.py#L2125> __

    '''

    pass


def call_menu(name: str = ""):
    ''' Open a predefined menu

    :param name: Name, Name of the menu
    :type name: str
    '''

    pass


def call_menu_pie(name: str = ""):
    ''' Open a predefined pie menu

    :param name: Name, Name of the pie menu
    :type name: str
    '''

    pass


def call_panel(name: str = "", keep_open: bool = True):
    ''' Open a predefined panel

    :param name: Name, Name of the menu
    :type name: str
    :param keep_open: Keep Open
    :type keep_open: bool
    '''

    pass


def context_collection_boolean_set(data_path_iter: str = "",
                                   data_path_item: str = "",
                                   type: typing.Union[int, str] = 'TOGGLE'):
    ''' Set boolean values for a collection of items :File: startup/bl_operators/wm.py\:858 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/wm.py#L858> __

    :param data_path_iter: data_path_iter, The data path relative to the context, must point to an iterable
    :type data_path_iter: str
    :param data_path_item: data_path_item, The data path from each iterable to the value (int or float)
    :type data_path_item: str
    :param type: Type
    :type type: typing.Union[int, str]
    '''

    pass


def context_cycle_array(data_path: str = "", reverse: bool = False):
    ''' Set a context array value (useful for cycling the active mesh edit mode) :File: startup/bl_operators/wm.py\:661 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/wm.py#L661> __

    :param data_path: Context Attributes, Context data-path (expanded using visible windows in the current .blend file)
    :type data_path: str
    :param reverse: Reverse, Cycle backwards
    :type reverse: bool
    '''

    pass


def context_cycle_enum(data_path: str = "",
                       reverse: bool = False,
                       wrap: bool = False):
    ''' Toggle a context value :File: startup/bl_operators/wm.py\:612 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/wm.py#L612> __

    :param data_path: Context Attributes, Context data-path (expanded using visible windows in the current .blend file)
    :type data_path: str
    :param reverse: Reverse, Cycle backwards
    :type reverse: bool
    :param wrap: Wrap, Wrap back to the first/last values
    :type wrap: bool
    '''

    pass


def context_cycle_int(data_path: str = "",
                      reverse: bool = False,
                      wrap: bool = False):
    ''' Set a context value (useful for cycling active material, shape keys, groups, etc.) :File: startup/bl_operators/wm.py\:572 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/wm.py#L572> __

    :param data_path: Context Attributes, Context data-path (expanded using visible windows in the current .blend file)
    :type data_path: str
    :param reverse: Reverse, Cycle backwards
    :type reverse: bool
    :param wrap: Wrap, Wrap back to the first/last values
    :type wrap: bool
    '''

    pass


def context_menu_enum(data_path: str = ""):
    ''' Undocumented, consider contributing <https://developer.blender.org/> __. :File: startup/bl_operators/wm.py\:690 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/wm.py#L690> __

    :param data_path: Context Attributes, Context data-path (expanded using visible windows in the current .blend file)
    :type data_path: str
    '''

    pass


def context_modal_mouse(data_path_iter: str = "",
                        data_path_item: str = "",
                        header_text: str = "",
                        input_scale: float = 0.01,
                        invert: bool = False,
                        initial_x: int = 0):
    ''' Adjust arbitrary values with mouse input :File: startup/bl_operators/wm.py\:995 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/wm.py#L995> __

    :param data_path_iter: data_path_iter, The data path relative to the context, must point to an iterable
    :type data_path_iter: str
    :param data_path_item: data_path_item, The data path from each iterable to the value (int or float)
    :type data_path_item: str
    :param header_text: Header Text, Text to display in header during scale
    :type header_text: str
    :param input_scale: input_scale, Scale the mouse movement by this value before applying the delta
    :type input_scale: float
    :param invert: invert, Invert the mouse input
    :type invert: bool
    :param initial_x: initial_x
    :type initial_x: int
    '''

    pass


def context_pie_enum(data_path: str = ""):
    ''' Undocumented, consider contributing <https://developer.blender.org/> __. :File: startup/bl_operators/wm.py\:721 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/wm.py#L721> __

    :param data_path: Context Attributes, Context data-path (expanded using visible windows in the current .blend file)
    :type data_path: str
    '''

    pass


def context_scale_float(data_path: str = "", value: float = 1.0):
    ''' Scale a float context value :File: startup/bl_operators/wm.py\:331 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/wm.py#L331> __

    :param data_path: Context Attributes, Context data-path (expanded using visible windows in the current .blend file)
    :type data_path: str
    :param value: Value, Assign value
    :type value: float
    '''

    pass


def context_scale_int(data_path: str = "",
                      value: float = 1.0,
                      always_step: bool = True):
    ''' Scale an int context value :File: startup/bl_operators/wm.py\:369 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/wm.py#L369> __

    :param data_path: Context Attributes, Context data-path (expanded using visible windows in the current .blend file)
    :type data_path: str
    :param value: Value, Assign value
    :type value: float
    :param always_step: Always Step, Always adjust the value by a minimum of 1 when 'value' is not 1.0
    :type always_step: bool
    '''

    pass


def context_set_boolean(data_path: str = "", value: bool = True):
    ''' Set a context value :File: startup/bl_operators/wm.py\:260 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/wm.py#L260> __

    :param data_path: Context Attributes, Context data-path (expanded using visible windows in the current .blend file)
    :type data_path: str
    :param value: Value, Assignment value
    :type value: bool
    '''

    pass


def context_set_enum(data_path: str = "", value: str = ""):
    ''' Set a context value :File: startup/bl_operators/wm.py\:260 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/wm.py#L260> __

    :param data_path: Context Attributes, Context data-path (expanded using visible windows in the current .blend file)
    :type data_path: str
    :param value: Value, Assignment value (as a string)
    :type value: str
    '''

    pass


def context_set_float(data_path: str = "",
                      value: float = 0.0,
                      relative: bool = False):
    ''' Set a context value :File: startup/bl_operators/wm.py\:260 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/wm.py#L260> __

    :param data_path: Context Attributes, Context data-path (expanded using visible windows in the current .blend file)
    :type data_path: str
    :param value: Value, Assignment value
    :type value: float
    :param relative: Relative, Apply relative to the current value (delta)
    :type relative: bool
    '''

    pass


def context_set_id(data_path: str = "", value: str = ""):
    ''' Set a context value to an ID data-block :File: startup/bl_operators/wm.py\:802 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/wm.py#L802> __

    :param data_path: Context Attributes, Context data-path (expanded using visible windows in the current .blend file)
    :type data_path: str
    :param value: Value, Assign value
    :type value: str
    '''

    pass


def context_set_int(data_path: str = "",
                    value: int = 0,
                    relative: bool = False):
    ''' Set a context value :File: startup/bl_operators/wm.py\:260 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/wm.py#L260> __

    :param data_path: Context Attributes, Context data-path (expanded using visible windows in the current .blend file)
    :type data_path: str
    :param value: Value, Assign value
    :type value: int
    :param relative: Relative, Apply relative to the current value (delta)
    :type relative: bool
    '''

    pass


def context_set_string(data_path: str = "", value: str = ""):
    ''' Set a context value :File: startup/bl_operators/wm.py\:260 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/wm.py#L260> __

    :param data_path: Context Attributes, Context data-path (expanded using visible windows in the current .blend file)
    :type data_path: str
    :param value: Value, Assign value
    :type value: str
    '''

    pass


def context_set_value(data_path: str = "", value: str = ""):
    ''' Set a context value :File: startup/bl_operators/wm.py\:472 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/wm.py#L472> __

    :param data_path: Context Attributes, Context data-path (expanded using visible windows in the current .blend file)
    :type data_path: str
    :param value: Value, Assignment value (as a string)
    :type value: str
    '''

    pass


def context_toggle(data_path: str = "", module: str = ""):
    ''' Toggle a context value :File: startup/bl_operators/wm.py\:496 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/wm.py#L496> __

    :param data_path: Context Attributes, Context data-path (expanded using visible windows in the current .blend file)
    :type data_path: str
    :param module: Module, Optionally override the context with a module
    :type module: str
    '''

    pass


def context_toggle_enum(data_path: str = "",
                        value_1: str = "",
                        value_2: str = ""):
    ''' Toggle a context value :File: startup/bl_operators/wm.py\:537 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/wm.py#L537> __

    :param data_path: Context Attributes, Context data-path (expanded using visible windows in the current .blend file)
    :type data_path: str
    :param value_1: Value, Toggle enum
    :type value_1: str
    :param value_2: Value, Toggle enum
    :type value_2: str
    '''

    pass


def debug_menu(debug_value: int = 0):
    ''' Open a popup to set the debug level

    :param debug_value: Debug Value
    :type debug_value: int
    '''

    pass


def doc_view(doc_id: str = ""):
    ''' Open online reference docs in a web browser :File: startup/bl_operators/wm.py\:1323 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/wm.py#L1323> __

    :param doc_id: Doc ID
    :type doc_id: str
    '''

    pass


def doc_view_manual(doc_id: str = ""):
    ''' Load online manual :File: startup/bl_operators/wm.py\:1293 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/wm.py#L1293> __

    :param doc_id: Doc ID
    :type doc_id: str
    '''

    pass


def doc_view_manual_ui_context():
    ''' View a context based online manual in a web browser

    '''

    pass


def drop_blend_file(filepath: str = ""):
    ''' Undocumented, consider contributing <https://developer.blender.org/> __. :File: startup/bl_operators/wm.py\:3318 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/wm.py#L3318> __

    :param filepath: filepath
    :type filepath: str
    '''

    pass


def gpencil_import_svg(
        filepath: str = "",
        directory: str = "",
        files: typing.
        Union[typing.Dict[str, 'bpy.types.OperatorFileListElement'], typing.
              List['bpy.types.OperatorFileListElement'],
              'bpy_prop_collection'] = None,
        check_existing: bool = False,
        filter_blender: bool = False,
        filter_backup: bool = False,
        filter_image: bool = False,
        filter_movie: bool = False,
        filter_python: bool = False,
        filter_font: bool = False,
        filter_sound: bool = False,
        filter_text: bool = False,
        filter_archive: bool = False,
        filter_btx: bool = False,
        filter_collada: bool = False,
        filter_alembic: bool = False,
        filter_usd: bool = False,
        filter_obj: bool = True,
        filter_volume: bool = False,
        filter_folder: bool = True,
        filter_blenlib: bool = False,
        filemode: int = 8,
        relative_path: bool = True,
        display_type: typing.Union[int, str] = 'DEFAULT',
        sort_method: typing.Union[int, str] = '',
        resolution: int = 10,
        scale: float = 10.0):
    ''' Import SVG into grease pencil

    :param filepath: File Path, Path to file
    :type filepath: str
    :param directory: Directory, Directory of the file
    :type directory: str
    :param files: Files
    :type files: typing.Union[typing.Dict[str, 'bpy.types.OperatorFileListElement'], typing.List['bpy.types.OperatorFileListElement'], 'bpy_prop_collection']
    :param check_existing: Check Existing, Check and warn on overwriting existing files
    :type check_existing: bool
    :param filter_blender: Filter .blend files
    :type filter_blender: bool
    :param filter_backup: Filter .blend files
    :type filter_backup: bool
    :param filter_image: Filter image files
    :type filter_image: bool
    :param filter_movie: Filter movie files
    :type filter_movie: bool
    :param filter_python: Filter python files
    :type filter_python: bool
    :param filter_font: Filter font files
    :type filter_font: bool
    :param filter_sound: Filter sound files
    :type filter_sound: bool
    :param filter_text: Filter text files
    :type filter_text: bool
    :param filter_archive: Filter archive files
    :type filter_archive: bool
    :param filter_btx: Filter btx files
    :type filter_btx: bool
    :param filter_collada: Filter COLLADA files
    :type filter_collada: bool
    :param filter_alembic: Filter Alembic files
    :type filter_alembic: bool
    :param filter_usd: Filter USD files
    :type filter_usd: bool
    :param filter_obj: Filter OBJ files
    :type filter_obj: bool
    :param filter_volume: Filter OpenVDB volume files
    :type filter_volume: bool
    :param filter_folder: Filter folders
    :type filter_folder: bool
    :param filter_blenlib: Filter Blender IDs
    :type filter_blenlib: bool
    :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
    :type filemode: int
    :param relative_path: Relative Path, Select the file relative to the blend file
    :type relative_path: bool
    :param display_type: Display Type * DEFAULT Default -- Automatically determine display type for files. * LIST_VERTICAL Short List -- Display files as short list. * LIST_HORIZONTAL Long List -- Display files as a detailed list. * THUMBNAIL Thumbnails -- Display files as thumbnails.
    :type display_type: typing.Union[int, str]
    :param sort_method: File sorting mode
    :type sort_method: typing.Union[int, str]
    :param resolution: Resolution, Resolution of the generated strokes
    :type resolution: int
    :param scale: Scale, Scale of the final strokes
    :type scale: float
    '''

    pass


def interface_theme_preset_add(name: str = "",
                               remove_name: bool = False,
                               remove_active: bool = False):
    ''' Add or remove a theme preset :File: startup/bl_operators/presets.py\:73 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/presets.py#L73> __

    :param name: Name, Name of the preset, used to make the path name
    :type name: str
    :param remove_name: remove_name
    :type remove_name: bool
    :param remove_active: remove_active
    :type remove_active: bool
    '''

    pass


def keyconfig_preset_add(name: str = "",
                         remove_name: bool = False,
                         remove_active: bool = False):
    ''' Add or remove a Key-config Preset :File: startup/bl_operators/presets.py\:73 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/presets.py#L73> __

    :param name: Name, Name of the preset, used to make the path name
    :type name: str
    :param remove_name: remove_name
    :type remove_name: bool
    :param remove_active: remove_active
    :type remove_active: bool
    '''

    pass


def lib_reload(library: str = "",
               filepath: str = "",
               directory: str = "",
               filename: str = "",
               hide_props_region: bool = True,
               check_existing: bool = False,
               filter_blender: bool = True,
               filter_backup: bool = False,
               filter_image: bool = False,
               filter_movie: bool = False,
               filter_python: bool = False,
               filter_font: bool = False,
               filter_sound: bool = False,
               filter_text: bool = False,
               filter_archive: bool = False,
               filter_btx: bool = False,
               filter_collada: bool = False,
               filter_alembic: bool = False,
               filter_usd: bool = False,
               filter_obj: bool = False,
               filter_volume: bool = False,
               filter_folder: bool = True,
               filter_blenlib: bool = False,
               filemode: int = 8,
               relative_path: bool = True,
               display_type: typing.Union[int, str] = 'DEFAULT',
               sort_method: typing.Union[int, str] = ''):
    ''' Reload the given library

    :param library: Library, Library to reload
    :type library: str
    :param filepath: File Path, Path to file
    :type filepath: str
    :param directory: Directory, Directory of the file
    :type directory: str
    :param filename: File Name, Name of the file
    :type filename: str
    :param hide_props_region: Hide Operator Properties, Collapse the region displaying the operator settings
    :type hide_props_region: bool
    :param check_existing: Check Existing, Check and warn on overwriting existing files
    :type check_existing: bool
    :param filter_blender: Filter .blend files
    :type filter_blender: bool
    :param filter_backup: Filter .blend files
    :type filter_backup: bool
    :param filter_image: Filter image files
    :type filter_image: bool
    :param filter_movie: Filter movie files
    :type filter_movie: bool
    :param filter_python: Filter python files
    :type filter_python: bool
    :param filter_font: Filter font files
    :type filter_font: bool
    :param filter_sound: Filter sound files
    :type filter_sound: bool
    :param filter_text: Filter text files
    :type filter_text: bool
    :param filter_archive: Filter archive files
    :type filter_archive: bool
    :param filter_btx: Filter btx files
    :type filter_btx: bool
    :param filter_collada: Filter COLLADA files
    :type filter_collada: bool
    :param filter_alembic: Filter Alembic files
    :type filter_alembic: bool
    :param filter_usd: Filter USD files
    :type filter_usd: bool
    :param filter_obj: Filter OBJ files
    :type filter_obj: bool
    :param filter_volume: Filter OpenVDB volume files
    :type filter_volume: bool
    :param filter_folder: Filter folders
    :type filter_folder: bool
    :param filter_blenlib: Filter Blender IDs
    :type filter_blenlib: bool
    :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
    :type filemode: int
    :param relative_path: Relative Path, Select the file relative to the blend file
    :type relative_path: bool
    :param display_type: Display Type * DEFAULT Default -- Automatically determine display type for files. * LIST_VERTICAL Short List -- Display files as short list. * LIST_HORIZONTAL Long List -- Display files as a detailed list. * THUMBNAIL Thumbnails -- Display files as thumbnails.
    :type display_type: typing.Union[int, str]
    :param sort_method: File sorting mode
    :type sort_method: typing.Union[int, str]
    '''

    pass


def lib_relocate(
        library: str = "",
        filepath: str = "",
        directory: str = "",
        filename: str = "",
        files: typing.
        Union[typing.Dict[str, 'bpy.types.OperatorFileListElement'], typing.
              List['bpy.types.OperatorFileListElement'],
              'bpy_prop_collection'] = None,
        hide_props_region: bool = True,
        check_existing: bool = False,
        filter_blender: bool = True,
        filter_backup: bool = False,
        filter_image: bool = False,
        filter_movie: bool = False,
        filter_python: bool = False,
        filter_font: bool = False,
        filter_sound: bool = False,
        filter_text: bool = False,
        filter_archive: bool = False,
        filter_btx: bool = False,
        filter_collada: bool = False,
        filter_alembic: bool = False,
        filter_usd: bool = False,
        filter_obj: bool = False,
        filter_volume: bool = False,
        filter_folder: bool = True,
        filter_blenlib: bool = False,
        filemode: int = 8,
        relative_path: bool = True,
        display_type: typing.Union[int, str] = 'DEFAULT',
        sort_method: typing.Union[int, str] = ''):
    ''' Relocate the given library to one or several others

    :param library: Library, Library to relocate
    :type library: str
    :param filepath: File Path, Path to file
    :type filepath: str
    :param directory: Directory, Directory of the file
    :type directory: str
    :param filename: File Name, Name of the file
    :type filename: str
    :param files: Files
    :type files: typing.Union[typing.Dict[str, 'bpy.types.OperatorFileListElement'], typing.List['bpy.types.OperatorFileListElement'], 'bpy_prop_collection']
    :param hide_props_region: Hide Operator Properties, Collapse the region displaying the operator settings
    :type hide_props_region: bool
    :param check_existing: Check Existing, Check and warn on overwriting existing files
    :type check_existing: bool
    :param filter_blender: Filter .blend files
    :type filter_blender: bool
    :param filter_backup: Filter .blend files
    :type filter_backup: bool
    :param filter_image: Filter image files
    :type filter_image: bool
    :param filter_movie: Filter movie files
    :type filter_movie: bool
    :param filter_python: Filter python files
    :type filter_python: bool
    :param filter_font: Filter font files
    :type filter_font: bool
    :param filter_sound: Filter sound files
    :type filter_sound: bool
    :param filter_text: Filter text files
    :type filter_text: bool
    :param filter_archive: Filter archive files
    :type filter_archive: bool
    :param filter_btx: Filter btx files
    :type filter_btx: bool
    :param filter_collada: Filter COLLADA files
    :type filter_collada: bool
    :param filter_alembic: Filter Alembic files
    :type filter_alembic: bool
    :param filter_usd: Filter USD files
    :type filter_usd: bool
    :param filter_obj: Filter OBJ files
    :type filter_obj: bool
    :param filter_volume: Filter OpenVDB volume files
    :type filter_volume: bool
    :param filter_folder: Filter folders
    :type filter_folder: bool
    :param filter_blenlib: Filter Blender IDs
    :type filter_blenlib: bool
    :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
    :type filemode: int
    :param relative_path: Relative Path, Select the file relative to the blend file
    :type relative_path: bool
    :param display_type: Display Type * DEFAULT Default -- Automatically determine display type for files. * LIST_VERTICAL Short List -- Display files as short list. * LIST_HORIZONTAL Long List -- Display files as a detailed list. * THUMBNAIL Thumbnails -- Display files as thumbnails.
    :type display_type: typing.Union[int, str]
    :param sort_method: File sorting mode
    :type sort_method: typing.Union[int, str]
    '''

    pass


def link(filepath: str = "",
         directory: str = "",
         filename: str = "",
         files: typing.
         Union[typing.Dict[str, 'bpy.types.OperatorFileListElement'], typing.
               List['bpy.types.OperatorFileListElement'],
               'bpy_prop_collection'] = None,
         check_existing: bool = False,
         filter_blender: bool = True,
         filter_backup: bool = False,
         filter_image: bool = False,
         filter_movie: bool = False,
         filter_python: bool = False,
         filter_font: bool = False,
         filter_sound: bool = False,
         filter_text: bool = False,
         filter_archive: bool = False,
         filter_btx: bool = False,
         filter_collada: bool = False,
         filter_alembic: bool = False,
         filter_usd: bool = False,
         filter_obj: bool = False,
         filter_volume: bool = False,
         filter_folder: bool = True,
         filter_blenlib: bool = True,
         filemode: int = 1,
         relative_path: bool = True,
         display_type: typing.Union[int, str] = 'DEFAULT',
         sort_method: typing.Union[int, str] = '',
         link: bool = True,
         do_reuse_local_id: bool = False,
         clear_asset_data: bool = False,
         autoselect: bool = True,
         active_collection: bool = True,
         instance_collections: bool = True,
         instance_object_data: bool = True):
    ''' Link from a Library .blend file

    :param filepath: File Path, Path to file
    :type filepath: str
    :param directory: Directory, Directory of the file
    :type directory: str
    :param filename: File Name, Name of the file
    :type filename: str
    :param files: Files
    :type files: typing.Union[typing.Dict[str, 'bpy.types.OperatorFileListElement'], typing.List['bpy.types.OperatorFileListElement'], 'bpy_prop_collection']
    :param check_existing: Check Existing, Check and warn on overwriting existing files
    :type check_existing: bool
    :param filter_blender: Filter .blend files
    :type filter_blender: bool
    :param filter_backup: Filter .blend files
    :type filter_backup: bool
    :param filter_image: Filter image files
    :type filter_image: bool
    :param filter_movie: Filter movie files
    :type filter_movie: bool
    :param filter_python: Filter python files
    :type filter_python: bool
    :param filter_font: Filter font files
    :type filter_font: bool
    :param filter_sound: Filter sound files
    :type filter_sound: bool
    :param filter_text: Filter text files
    :type filter_text: bool
    :param filter_archive: Filter archive files
    :type filter_archive: bool
    :param filter_btx: Filter btx files
    :type filter_btx: bool
    :param filter_collada: Filter COLLADA files
    :type filter_collada: bool
    :param filter_alembic: Filter Alembic files
    :type filter_alembic: bool
    :param filter_usd: Filter USD files
    :type filter_usd: bool
    :param filter_obj: Filter OBJ files
    :type filter_obj: bool
    :param filter_volume: Filter OpenVDB volume files
    :type filter_volume: bool
    :param filter_folder: Filter folders
    :type filter_folder: bool
    :param filter_blenlib: Filter Blender IDs
    :type filter_blenlib: bool
    :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
    :type filemode: int
    :param relative_path: Relative Path, Select the file relative to the blend file
    :type relative_path: bool
    :param display_type: Display Type * DEFAULT Default -- Automatically determine display type for files. * LIST_VERTICAL Short List -- Display files as short list. * LIST_HORIZONTAL Long List -- Display files as a detailed list. * THUMBNAIL Thumbnails -- Display files as thumbnails.
    :type display_type: typing.Union[int, str]
    :param sort_method: File sorting mode
    :type sort_method: typing.Union[int, str]
    :param link: Link, Link the objects or data-blocks rather than appending
    :type link: bool
    :param do_reuse_local_id: Re-Use Local Data, Try to re-use previously matching appended data-blocks instead of appending a new copy
    :type do_reuse_local_id: bool
    :param clear_asset_data: Clear Asset Data, Don't add asset meta-data or tags from the original data-block
    :type clear_asset_data: bool
    :param autoselect: Select, Select new objects
    :type autoselect: bool
    :param active_collection: Active Collection, Put new objects on the active collection
    :type active_collection: bool
    :param instance_collections: Instance Collections, Create instances for collections, rather than adding them directly to the scene
    :type instance_collections: bool
    :param instance_object_data: Instance Object Data, Create instances for object data which are not referenced by any objects
    :type instance_object_data: bool
    '''

    pass


def memory_statistics():
    ''' Print memory statistics to the console

    '''

    pass


def obj_export(filepath: str = "",
               check_existing: bool = True,
               filter_blender: bool = False,
               filter_backup: bool = False,
               filter_image: bool = False,
               filter_movie: bool = False,
               filter_python: bool = False,
               filter_font: bool = False,
               filter_sound: bool = False,
               filter_text: bool = False,
               filter_archive: bool = False,
               filter_btx: bool = False,
               filter_collada: bool = False,
               filter_alembic: bool = False,
               filter_usd: bool = False,
               filter_obj: bool = False,
               filter_volume: bool = False,
               filter_folder: bool = True,
               filter_blenlib: bool = False,
               filemode: int = 8,
               display_type: typing.Union[int, str] = 'DEFAULT',
               sort_method: typing.Union[int, str] = '',
               export_animation: bool = False,
               start_frame: int = -2147483648,
               end_frame: int = 2147483647,
               forward_axis: typing.Union[int, str] = 'NEGATIVE_Z',
               up_axis: typing.Union[int, str] = 'Y',
               global_scale: float = 1.0,
               apply_modifiers: bool = True,
               export_eval_mode: typing.Union[int, str] = 'DAG_EVAL_VIEWPORT',
               export_selected_objects: bool = False,
               export_uv: bool = True,
               export_normals: bool = True,
               export_colors: bool = False,
               export_materials: bool = True,
               export_pbr_extensions: bool = False,
               path_mode: typing.Union[int, str] = 'AUTO',
               export_triangulated_mesh: bool = False,
               export_curves_as_nurbs: bool = False,
               export_object_groups: bool = False,
               export_material_groups: bool = False,
               export_vertex_groups: bool = False,
               export_smooth_groups: bool = False,
               smooth_group_bitflags: bool = False,
               filter_glob: str = "*.obj;*.mtl"):
    ''' Save the scene to a Wavefront OBJ file

    :param filepath: File Path, Path to file
    :type filepath: str
    :param check_existing: Check Existing, Check and warn on overwriting existing files
    :type check_existing: bool
    :param filter_blender: Filter .blend files
    :type filter_blender: bool
    :param filter_backup: Filter .blend files
    :type filter_backup: bool
    :param filter_image: Filter image files
    :type filter_image: bool
    :param filter_movie: Filter movie files
    :type filter_movie: bool
    :param filter_python: Filter python files
    :type filter_python: bool
    :param filter_font: Filter font files
    :type filter_font: bool
    :param filter_sound: Filter sound files
    :type filter_sound: bool
    :param filter_text: Filter text files
    :type filter_text: bool
    :param filter_archive: Filter archive files
    :type filter_archive: bool
    :param filter_btx: Filter btx files
    :type filter_btx: bool
    :param filter_collada: Filter COLLADA files
    :type filter_collada: bool
    :param filter_alembic: Filter Alembic files
    :type filter_alembic: bool
    :param filter_usd: Filter USD files
    :type filter_usd: bool
    :param filter_obj: Filter OBJ files
    :type filter_obj: bool
    :param filter_volume: Filter OpenVDB volume files
    :type filter_volume: bool
    :param filter_folder: Filter folders
    :type filter_folder: bool
    :param filter_blenlib: Filter Blender IDs
    :type filter_blenlib: bool
    :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
    :type filemode: int
    :param display_type: Display Type * DEFAULT Default -- Automatically determine display type for files. * LIST_VERTICAL Short List -- Display files as short list. * LIST_HORIZONTAL Long List -- Display files as a detailed list. * THUMBNAIL Thumbnails -- Display files as thumbnails.
    :type display_type: typing.Union[int, str]
    :param sort_method: File sorting mode
    :type sort_method: typing.Union[int, str]
    :param export_animation: Export Animation, Export multiple frames instead of the current frame only
    :type export_animation: bool
    :param start_frame: Start Frame, The first frame to be exported
    :type start_frame: int
    :param end_frame: End Frame, The last frame to be exported
    :type end_frame: int
    :param forward_axis: Forward Axis * X X -- Positive X axis. * Y Y -- Positive Y axis. * Z Z -- Positive Z axis. * NEGATIVE_X -X -- Negative X axis. * NEGATIVE_Y -Y -- Negative Y axis. * NEGATIVE_Z -Z -- Negative Z axis.
    :type forward_axis: typing.Union[int, str]
    :param up_axis: Up Axis * X X -- Positive X axis. * Y Y -- Positive Y axis. * Z Z -- Positive Z axis. * NEGATIVE_X -X -- Negative X axis. * NEGATIVE_Y -Y -- Negative Y axis. * NEGATIVE_Z -Z -- Negative Z axis.
    :type up_axis: typing.Union[int, str]
    :param global_scale: Scale, Value by which to enlarge or shrink the objects with respect to the world's origin
    :type global_scale: float
    :param apply_modifiers: Apply Modifiers, Apply modifiers to exported meshes
    :type apply_modifiers: bool
    :param export_eval_mode: Object Properties, Determines properties like object visibility, modifiers etc., where they differ for Render and Viewport * DAG_EVAL_RENDER Render -- Export objects as they appear in render. * DAG_EVAL_VIEWPORT Viewport -- Export objects as they appear in the viewport.
    :type export_eval_mode: typing.Union[int, str]
    :param export_selected_objects: Export Selected Objects, Export only selected objects instead of all supported objects
    :type export_selected_objects: bool
    :param export_uv: Export UVs
    :type export_uv: bool
    :param export_normals: Export Normals, Export per-face normals if the face is flat-shaded, per-face-per-loop normals if smooth-shaded
    :type export_normals: bool
    :param export_colors: Export Colors, Export per-vertex colors
    :type export_colors: bool
    :param export_materials: Export Materials, Export MTL library. There must be a Principled-BSDF node for image textures to be exported to the MTL file
    :type export_materials: bool
    :param export_pbr_extensions: Export Materials with PBR Extensions, Export MTL library using PBR extensions (roughness, metallic, sheen, clearcoat, anisotropy, transmission)
    :type export_pbr_extensions: bool
    :param path_mode: Path Mode, Method used to reference paths * AUTO Auto -- Use relative paths with subdirectories only. * ABSOLUTE Absolute -- Always write absolute paths. * RELATIVE Relative -- Write relative paths where possible. * MATCH Match -- Match absolute/relative setting with input path. * STRIP Strip -- Write filename only. * COPY Copy -- Copy the file to the destination path.
    :type path_mode: typing.Union[int, str]
    :param export_triangulated_mesh: 4
    :type export_triangulated_mesh: bool
    :param export_curves_as_nurbs: Export Curves as NURBS, Export curves in parametric form instead of exporting as mesh
    :type export_curves_as_nurbs: bool
    :param export_object_groups: Export Object Groups, Append mesh name to object name, separated by a '_'
    :type export_object_groups: bool
    :param export_material_groups: Export Material Groups, Generate an OBJ group for each part of a geometry using a different material
    :type export_material_groups: bool
    :param export_vertex_groups: Export Vertex Groups, Export the name of the vertex group of a face. It is approximated by choosing the vertex group with the most members among the vertices of a face
    :type export_vertex_groups: bool
    :param export_smooth_groups: Export Smooth Groups, Every smooth-shaded face is assigned group "1" and every flat-shaded face "off"
    :type export_smooth_groups: bool
    :param smooth_group_bitflags: Generate Bitflags for Smooth Groups
    :type smooth_group_bitflags: bool
    :param filter_glob: Extension Filter
    :type filter_glob: str
    '''

    pass


def obj_import(
        filepath: str = "",
        directory: str = "",
        files: typing.
        Union[typing.Dict[str, 'bpy.types.OperatorFileListElement'], typing.
              List['bpy.types.OperatorFileListElement'],
              'bpy_prop_collection'] = None,
        check_existing: bool = False,
        filter_blender: bool = False,
        filter_backup: bool = False,
        filter_image: bool = False,
        filter_movie: bool = False,
        filter_python: bool = False,
        filter_font: bool = False,
        filter_sound: bool = False,
        filter_text: bool = False,
        filter_archive: bool = False,
        filter_btx: bool = False,
        filter_collada: bool = False,
        filter_alembic: bool = False,
        filter_usd: bool = False,
        filter_obj: bool = False,
        filter_volume: bool = False,
        filter_folder: bool = True,
        filter_blenlib: bool = False,
        filemode: int = 8,
        display_type: typing.Union[int, str] = 'DEFAULT',
        sort_method: typing.Union[int, str] = '',
        global_scale: float = 1.0,
        clamp_size: float = 0.0,
        forward_axis: typing.Union[int, str] = 'NEGATIVE_Z',
        up_axis: typing.Union[int, str] = 'Y',
        use_split_objects: bool = True,
        use_split_groups: bool = False,
        import_vertex_groups: bool = False,
        validate_meshes: bool = False,
        filter_glob: str = "*.obj;*.mtl"):
    ''' Load a Wavefront OBJ scene

    :param filepath: File Path, Path to file
    :type filepath: str
    :param directory: Directory, Directory of the file
    :type directory: str
    :param files: Files
    :type files: typing.Union[typing.Dict[str, 'bpy.types.OperatorFileListElement'], typing.List['bpy.types.OperatorFileListElement'], 'bpy_prop_collection']
    :param check_existing: Check Existing, Check and warn on overwriting existing files
    :type check_existing: bool
    :param filter_blender: Filter .blend files
    :type filter_blender: bool
    :param filter_backup: Filter .blend files
    :type filter_backup: bool
    :param filter_image: Filter image files
    :type filter_image: bool
    :param filter_movie: Filter movie files
    :type filter_movie: bool
    :param filter_python: Filter python files
    :type filter_python: bool
    :param filter_font: Filter font files
    :type filter_font: bool
    :param filter_sound: Filter sound files
    :type filter_sound: bool
    :param filter_text: Filter text files
    :type filter_text: bool
    :param filter_archive: Filter archive files
    :type filter_archive: bool
    :param filter_btx: Filter btx files
    :type filter_btx: bool
    :param filter_collada: Filter COLLADA files
    :type filter_collada: bool
    :param filter_alembic: Filter Alembic files
    :type filter_alembic: bool
    :param filter_usd: Filter USD files
    :type filter_usd: bool
    :param filter_obj: Filter OBJ files
    :type filter_obj: bool
    :param filter_volume: Filter OpenVDB volume files
    :type filter_volume: bool
    :param filter_folder: Filter folders
    :type filter_folder: bool
    :param filter_blenlib: Filter Blender IDs
    :type filter_blenlib: bool
    :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
    :type filemode: int
    :param display_type: Display Type * DEFAULT Default -- Automatically determine display type for files. * LIST_VERTICAL Short List -- Display files as short list. * LIST_HORIZONTAL Long List -- Display files as a detailed list. * THUMBNAIL Thumbnails -- Display files as thumbnails.
    :type display_type: typing.Union[int, str]
    :param sort_method: File sorting mode
    :type sort_method: typing.Union[int, str]
    :param global_scale: Scale, Value by which to enlarge or shrink the objects with respect to the world's origin
    :type global_scale: float
    :param clamp_size: Clamp Bounding Box, Resize the objects to keep bounding box under this value. Value 0 disables clamping
    :type clamp_size: float
    :param forward_axis: Forward Axis * X X -- Positive X axis. * Y Y -- Positive Y axis. * Z Z -- Positive Z axis. * NEGATIVE_X -X -- Negative X axis. * NEGATIVE_Y -Y -- Negative Y axis. * NEGATIVE_Z -Z -- Negative Z axis.
    :type forward_axis: typing.Union[int, str]
    :param up_axis: Up Axis * X X -- Positive X axis. * Y Y -- Positive Y axis. * Z Z -- Positive Z axis. * NEGATIVE_X -X -- Negative X axis. * NEGATIVE_Y -Y -- Negative Y axis. * NEGATIVE_Z -Z -- Negative Z axis.
    :type up_axis: typing.Union[int, str]
    :param use_split_objects: Split By Object, Import each OBJ 'o' as a separate object
    :type use_split_objects: bool
    :param use_split_groups: Split By Group, Import each OBJ 'g' as a separate object
    :type use_split_groups: bool
    :param import_vertex_groups: Vertex Groups, Import OBJ groups as vertex groups
    :type import_vertex_groups: bool
    :param validate_meshes: Validate Meshes, Check imported mesh objects for invalid data (slow)
    :type validate_meshes: bool
    :param filter_glob: Extension Filter
    :type filter_glob: str
    '''

    pass


def open_mainfile(filepath: str = "",
                  hide_props_region: bool = True,
                  check_existing: bool = False,
                  filter_blender: bool = True,
                  filter_backup: bool = False,
                  filter_image: bool = False,
                  filter_movie: bool = False,
                  filter_python: bool = False,
                  filter_font: bool = False,
                  filter_sound: bool = False,
                  filter_text: bool = False,
                  filter_archive: bool = False,
                  filter_btx: bool = False,
                  filter_collada: bool = False,
                  filter_alembic: bool = False,
                  filter_usd: bool = False,
                  filter_obj: bool = False,
                  filter_volume: bool = False,
                  filter_folder: bool = True,
                  filter_blenlib: bool = False,
                  filemode: int = 8,
                  display_type: typing.Union[int, str] = 'DEFAULT',
                  sort_method: typing.Union[int, str] = '',
                  load_ui: bool = True,
                  use_scripts: bool = True,
                  display_file_selector: bool = True,
                  state: int = 0):
    ''' Open a Blender file

    :param filepath: File Path, Path to file
    :type filepath: str
    :param hide_props_region: Hide Operator Properties, Collapse the region displaying the operator settings
    :type hide_props_region: bool
    :param check_existing: Check Existing, Check and warn on overwriting existing files
    :type check_existing: bool
    :param filter_blender: Filter .blend files
    :type filter_blender: bool
    :param filter_backup: Filter .blend files
    :type filter_backup: bool
    :param filter_image: Filter image files
    :type filter_image: bool
    :param filter_movie: Filter movie files
    :type filter_movie: bool
    :param filter_python: Filter python files
    :type filter_python: bool
    :param filter_font: Filter font files
    :type filter_font: bool
    :param filter_sound: Filter sound files
    :type filter_sound: bool
    :param filter_text: Filter text files
    :type filter_text: bool
    :param filter_archive: Filter archive files
    :type filter_archive: bool
    :param filter_btx: Filter btx files
    :type filter_btx: bool
    :param filter_collada: Filter COLLADA files
    :type filter_collada: bool
    :param filter_alembic: Filter Alembic files
    :type filter_alembic: bool
    :param filter_usd: Filter USD files
    :type filter_usd: bool
    :param filter_obj: Filter OBJ files
    :type filter_obj: bool
    :param filter_volume: Filter OpenVDB volume files
    :type filter_volume: bool
    :param filter_folder: Filter folders
    :type filter_folder: bool
    :param filter_blenlib: Filter Blender IDs
    :type filter_blenlib: bool
    :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
    :type filemode: int
    :param display_type: Display Type * DEFAULT Default -- Automatically determine display type for files. * LIST_VERTICAL Short List -- Display files as short list. * LIST_HORIZONTAL Long List -- Display files as a detailed list. * THUMBNAIL Thumbnails -- Display files as thumbnails.
    :type display_type: typing.Union[int, str]
    :param sort_method: File sorting mode
    :type sort_method: typing.Union[int, str]
    :param load_ui: Load UI, Load user interface setup in the .blend file
    :type load_ui: bool
    :param use_scripts: Trusted Source, Allow .blend file to execute scripts automatically, default available from system preferences
    :type use_scripts: bool
    :param display_file_selector: Display File Selector
    :type display_file_selector: bool
    :param state: State
    :type state: int
    '''

    pass


def operator_cheat_sheet():
    ''' List all the operators in a text-block, useful for scripting :File: startup/bl_operators/wm.py\:2175 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/wm.py#L2175> __

    '''

    pass


def operator_defaults():
    ''' Set the active operator to its default values

    '''

    pass


def operator_pie_enum(data_path: str = "", prop_string: str = ""):
    ''' Undocumented, consider contributing <https://developer.blender.org/> __. :File: startup/bl_operators/wm.py\:762 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/wm.py#L762> __

    :param data_path: Operator, Operator name (in python as string)
    :type data_path: str
    :param prop_string: Property, Property name (as a string)
    :type prop_string: str
    '''

    pass


def operator_preset_add(name: str = "",
                        remove_name: bool = False,
                        remove_active: bool = False,
                        operator: str = ""):
    ''' Add or remove an Operator Preset :File: startup/bl_operators/presets.py\:73 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/presets.py#L73> __

    :param name: Name, Name of the preset, used to make the path name
    :type name: str
    :param remove_name: remove_name
    :type remove_name: bool
    :param remove_active: remove_active
    :type remove_active: bool
    :param operator: Operator
    :type operator: str
    '''

    pass


def owner_disable(owner_id: str = ""):
    ''' Disable add-on for workspace :File: startup/bl_operators/wm.py\:2223 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/wm.py#L2223> __

    :param owner_id: UI Tag
    :type owner_id: str
    '''

    pass


def owner_enable(owner_id: str = ""):
    ''' Enable add-on for workspace :File: startup/bl_operators/wm.py\:2208 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/wm.py#L2208> __

    :param owner_id: UI Tag
    :type owner_id: str
    '''

    pass


def path_open(filepath: str = ""):
    ''' Open a path in a file browser :File: startup/bl_operators/wm.py\:1122 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/wm.py#L1122> __

    :param filepath: filepath
    :type filepath: str
    '''

    pass


def ply_export(filepath: str = "",
               check_existing: bool = True,
               filter_blender: bool = False,
               filter_backup: bool = False,
               filter_image: bool = False,
               filter_movie: bool = False,
               filter_python: bool = False,
               filter_font: bool = False,
               filter_sound: bool = False,
               filter_text: bool = False,
               filter_archive: bool = False,
               filter_btx: bool = False,
               filter_collada: bool = False,
               filter_alembic: bool = False,
               filter_usd: bool = False,
               filter_obj: bool = False,
               filter_volume: bool = False,
               filter_folder: bool = True,
               filter_blenlib: bool = False,
               filemode: int = 8,
               display_type: typing.Union[int, str] = 'DEFAULT',
               sort_method: typing.Union[int, str] = '',
               forward_axis: typing.Union[int, str] = 'Y',
               up_axis: typing.Union[int, str] = 'Z',
               global_scale: float = 1.0,
               apply_modifiers: bool = True,
               export_selected_objects: bool = False,
               export_uv: bool = True,
               export_normals: bool = False,
               export_colors: typing.Union[int, str] = 'SRGB',
               export_triangulated_mesh: bool = False,
               ascii_format: bool = False,
               filter_glob: str = "*.ply"):
    ''' Save the scene to a PLY file

    :param filepath: File Path, Path to file
    :type filepath: str
    :param check_existing: Check Existing, Check and warn on overwriting existing files
    :type check_existing: bool
    :param filter_blender: Filter .blend files
    :type filter_blender: bool
    :param filter_backup: Filter .blend files
    :type filter_backup: bool
    :param filter_image: Filter image files
    :type filter_image: bool
    :param filter_movie: Filter movie files
    :type filter_movie: bool
    :param filter_python: Filter python files
    :type filter_python: bool
    :param filter_font: Filter font files
    :type filter_font: bool
    :param filter_sound: Filter sound files
    :type filter_sound: bool
    :param filter_text: Filter text files
    :type filter_text: bool
    :param filter_archive: Filter archive files
    :type filter_archive: bool
    :param filter_btx: Filter btx files
    :type filter_btx: bool
    :param filter_collada: Filter COLLADA files
    :type filter_collada: bool
    :param filter_alembic: Filter Alembic files
    :type filter_alembic: bool
    :param filter_usd: Filter USD files
    :type filter_usd: bool
    :param filter_obj: Filter OBJ files
    :type filter_obj: bool
    :param filter_volume: Filter OpenVDB volume files
    :type filter_volume: bool
    :param filter_folder: Filter folders
    :type filter_folder: bool
    :param filter_blenlib: Filter Blender IDs
    :type filter_blenlib: bool
    :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
    :type filemode: int
    :param display_type: Display Type * DEFAULT Default -- Automatically determine display type for files. * LIST_VERTICAL Short List -- Display files as short list. * LIST_HORIZONTAL Long List -- Display files as a detailed list. * THUMBNAIL Thumbnails -- Display files as thumbnails.
    :type display_type: typing.Union[int, str]
    :param sort_method: File sorting mode
    :type sort_method: typing.Union[int, str]
    :param forward_axis: Forward Axis * X X -- Positive X axis. * Y Y -- Positive Y axis. * Z Z -- Positive Z axis. * NEGATIVE_X -X -- Negative X axis. * NEGATIVE_Y -Y -- Negative Y axis. * NEGATIVE_Z -Z -- Negative Z axis.
    :type forward_axis: typing.Union[int, str]
    :param up_axis: Up Axis * X X -- Positive X axis. * Y Y -- Positive Y axis. * Z Z -- Positive Z axis. * NEGATIVE_X -X -- Negative X axis. * NEGATIVE_Y -Y -- Negative Y axis. * NEGATIVE_Z -Z -- Negative Z axis.
    :type up_axis: typing.Union[int, str]
    :param global_scale: Scale, Value by which to enlarge or shrink the objects with respect to the world's origin
    :type global_scale: float
    :param apply_modifiers: Apply Modifiers, Apply modifiers to exported meshes
    :type apply_modifiers: bool
    :param export_selected_objects: Export Selected Objects, Export only selected objects instead of all supported objects
    :type export_selected_objects: bool
    :param export_uv: Export UVs
    :type export_uv: bool
    :param export_normals: Export Vertex Normals, Export specific vertex normals if available, export calculated normals otherwise
    :type export_normals: bool
    :param export_colors: Export Vertex Colors, Export vertex color attributes * NONE None -- Do not import/export color attributes. * SRGB sRGB -- Vertex colors in the file are in sRGB color space. * LINEAR Linear -- Vertex colors in the file are in linear color space.
    :type export_colors: typing.Union[int, str]
    :param export_triangulated_mesh: 4
    :type export_triangulated_mesh: bool
    :param ascii_format: ASCII Format, Export file in ASCII format, export as binary otherwise
    :type ascii_format: bool
    :param filter_glob: Extension Filter
    :type filter_glob: str
    '''

    pass


def ply_import(
        filepath: str = "",
        directory: str = "",
        files: typing.
        Union[typing.Dict[str, 'bpy.types.OperatorFileListElement'], typing.
              List['bpy.types.OperatorFileListElement'],
              'bpy_prop_collection'] = None,
        check_existing: bool = False,
        filter_blender: bool = False,
        filter_backup: bool = False,
        filter_image: bool = False,
        filter_movie: bool = False,
        filter_python: bool = False,
        filter_font: bool = False,
        filter_sound: bool = False,
        filter_text: bool = False,
        filter_archive: bool = False,
        filter_btx: bool = False,
        filter_collada: bool = False,
        filter_alembic: bool = False,
        filter_usd: bool = False,
        filter_obj: bool = False,
        filter_volume: bool = False,
        filter_folder: bool = True,
        filter_blenlib: bool = False,
        filemode: int = 8,
        display_type: typing.Union[int, str] = 'DEFAULT',
        sort_method: typing.Union[int, str] = '',
        global_scale: float = 1.0,
        use_scene_unit: bool = False,
        forward_axis: typing.Union[int, str] = 'Y',
        up_axis: typing.Union[int, str] = 'Z',
        merge_verts: bool = False,
        import_colors: typing.Union[int, str] = 'SRGB',
        filter_glob: str = "*.ply"):
    ''' Import an PLY file as an object

    :param filepath: File Path, Path to file
    :type filepath: str
    :param directory: Directory, Directory of the file
    :type directory: str
    :param files: Files
    :type files: typing.Union[typing.Dict[str, 'bpy.types.OperatorFileListElement'], typing.List['bpy.types.OperatorFileListElement'], 'bpy_prop_collection']
    :param check_existing: Check Existing, Check and warn on overwriting existing files
    :type check_existing: bool
    :param filter_blender: Filter .blend files
    :type filter_blender: bool
    :param filter_backup: Filter .blend files
    :type filter_backup: bool
    :param filter_image: Filter image files
    :type filter_image: bool
    :param filter_movie: Filter movie files
    :type filter_movie: bool
    :param filter_python: Filter python files
    :type filter_python: bool
    :param filter_font: Filter font files
    :type filter_font: bool
    :param filter_sound: Filter sound files
    :type filter_sound: bool
    :param filter_text: Filter text files
    :type filter_text: bool
    :param filter_archive: Filter archive files
    :type filter_archive: bool
    :param filter_btx: Filter btx files
    :type filter_btx: bool
    :param filter_collada: Filter COLLADA files
    :type filter_collada: bool
    :param filter_alembic: Filter Alembic files
    :type filter_alembic: bool
    :param filter_usd: Filter USD files
    :type filter_usd: bool
    :param filter_obj: Filter OBJ files
    :type filter_obj: bool
    :param filter_volume: Filter OpenVDB volume files
    :type filter_volume: bool
    :param filter_folder: Filter folders
    :type filter_folder: bool
    :param filter_blenlib: Filter Blender IDs
    :type filter_blenlib: bool
    :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
    :type filemode: int
    :param display_type: Display Type * DEFAULT Default -- Automatically determine display type for files. * LIST_VERTICAL Short List -- Display files as short list. * LIST_HORIZONTAL Long List -- Display files as a detailed list. * THUMBNAIL Thumbnails -- Display files as thumbnails.
    :type display_type: typing.Union[int, str]
    :param sort_method: File sorting mode
    :type sort_method: typing.Union[int, str]
    :param global_scale: Scale
    :type global_scale: float
    :param use_scene_unit: Scene Unit, Apply current scene's unit (as defined by unit scale) to imported data
    :type use_scene_unit: bool
    :param forward_axis: Forward Axis * X X -- Positive X axis. * Y Y -- Positive Y axis. * Z Z -- Positive Z axis. * NEGATIVE_X -X -- Negative X axis. * NEGATIVE_Y -Y -- Negative Y axis. * NEGATIVE_Z -Z -- Negative Z axis.
    :type forward_axis: typing.Union[int, str]
    :param up_axis: Up Axis * X X -- Positive X axis. * Y Y -- Positive Y axis. * Z Z -- Positive Z axis. * NEGATIVE_X -X -- Negative X axis. * NEGATIVE_Y -Y -- Negative Y axis. * NEGATIVE_Z -Z -- Negative Z axis.
    :type up_axis: typing.Union[int, str]
    :param merge_verts: Merge Vertices, Merges vertices by distance
    :type merge_verts: bool
    :param import_colors: Import Vertex Colors, Import vertex color attributes * NONE None -- Do not import/export color attributes. * SRGB sRGB -- Vertex colors in the file are in sRGB color space. * LINEAR Linear -- Vertex colors in the file are in linear color space.
    :type import_colors: typing.Union[int, str]
    :param filter_glob: Extension Filter
    :type filter_glob: str
    '''

    pass


def previews_batch_clear(
        files: typing.
        Union[typing.Dict[str, 'bpy.types.OperatorFileListElement'], typing.
              List['bpy.types.OperatorFileListElement'],
              'bpy_prop_collection'] = None,
        directory: str = "",
        filter_blender: bool = True,
        filter_folder: bool = True,
        use_scenes: bool = True,
        use_collections: bool = True,
        use_objects: bool = True,
        use_intern_data: bool = True,
        use_trusted: bool = False,
        use_backups: bool = True):
    ''' Clear selected .blend file's previews :File: startup/bl_operators/file.py\:203 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/file.py#L203> __

    :param files: files
    :type files: typing.Union[typing.Dict[str, 'bpy.types.OperatorFileListElement'], typing.List['bpy.types.OperatorFileListElement'], 'bpy_prop_collection']
    :param directory: directory
    :type directory: str
    :param filter_blender: filter_blender
    :type filter_blender: bool
    :param filter_folder: filter_folder
    :type filter_folder: bool
    :param use_scenes: Scenes, Clear scenes' previews
    :type use_scenes: bool
    :param use_collections: Collections, Clear collections' previews
    :type use_collections: bool
    :param use_objects: Objects, Clear objects' previews
    :type use_objects: bool
    :param use_intern_data: Materials & Textures, Clear 'internal' previews (materials, textures, images, etc.)
    :type use_intern_data: bool
    :param use_trusted: Trusted Blend Files, Enable python evaluation for selected files
    :type use_trusted: bool
    :param use_backups: Save Backups, Keep a backup (.blend1) version of the files when saving with cleared previews
    :type use_backups: bool
    '''

    pass


def previews_batch_generate(
        files: typing.
        Union[typing.Dict[str, 'bpy.types.OperatorFileListElement'], typing.
              List['bpy.types.OperatorFileListElement'],
              'bpy_prop_collection'] = None,
        directory: str = "",
        filter_blender: bool = True,
        filter_folder: bool = True,
        use_scenes: bool = True,
        use_collections: bool = True,
        use_objects: bool = True,
        use_intern_data: bool = True,
        use_trusted: bool = False,
        use_backups: bool = True):
    ''' Generate selected .blend file's previews :File: startup/bl_operators/file.py\:93 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/file.py#L93> __

    :param files: Collection of file paths with common directory root
    :type files: typing.Union[typing.Dict[str, 'bpy.types.OperatorFileListElement'], typing.List['bpy.types.OperatorFileListElement'], 'bpy_prop_collection']
    :param directory: Root path of all files listed in files collection
    :type directory: str
    :param filter_blender: Show Blender files in the File Browser
    :type filter_blender: bool
    :param filter_folder: Show folders in the File Browser
    :type filter_folder: bool
    :param use_scenes: Scenes, Generate scenes' previews
    :type use_scenes: bool
    :param use_collections: Collections, Generate collections' previews
    :type use_collections: bool
    :param use_objects: Objects, Generate objects' previews
    :type use_objects: bool
    :param use_intern_data: Materials & Textures, Generate 'internal' previews (materials, textures, images, etc.)
    :type use_intern_data: bool
    :param use_trusted: Trusted Blend Files, Enable python evaluation for selected files
    :type use_trusted: bool
    :param use_backups: Save Backups, Keep a backup (.blend1) version of the files when saving with generated previews
    :type use_backups: bool
    '''

    pass


def previews_clear(
        id_type: typing.Union[typing.Set[int], typing.Set[str]] = {}):
    ''' Clear data-block previews (only for some types like objects, materials, textures, etc.)

    :param id_type: Data-Block Type, Which data-block previews to clear * ALL All Types. * GEOMETRY All Geometry Types -- Clear previews for scenes, collections and objects. * SHADING All Shading Types -- Clear previews for materials, lights, worlds, textures and images. * SCENE Scenes. * COLLECTION Collections. * OBJECT Objects. * MATERIAL Materials. * LIGHT Lights. * WORLD Worlds. * TEXTURE Textures. * IMAGE Images.
    :type id_type: typing.Union[typing.Set[int], typing.Set[str]]
    '''

    pass


def previews_ensure():
    ''' Ensure data-block previews are available and up-to-date (to be saved in .blend file, only for some types like materials, textures, etc.)

    '''

    pass


def properties_add(data_path: str = ""):
    ''' Add your own property to the data-block :File: startup/bl_operators/wm.py\:2017 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/wm.py#L2017> __

    :param data_path: Property Edit, Property data_path edit
    :type data_path: str
    '''

    pass


def properties_context_change(context: str = ""):
    ''' Jump to a different tab inside the properties editor :File: startup/bl_operators/wm.py\:2060 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/wm.py#L2060> __

    :param context: Context
    :type context: str
    '''

    pass


def properties_edit(
        data_path: str = "",
        property_name: str = "",
        property_type: typing.Union[int, str] = 'FLOAT',
        is_overridable_library: bool = False,
        description: str = "",
        use_soft_limits: bool = False,
        array_length: int = 3,
        default_int: typing.List[int] = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                         0, 0, 0, 0, 0, 0),
        min_int: int = -10000,
        max_int: int = 10000,
        soft_min_int: int = -10000,
        soft_max_int: int = 10000,
        step_int: int = 1,
        default_bool: typing.List[bool] = (False, False, False, False, False,
                                           False, False, False, False, False,
                                           False, False, False, False, False,
                                           False, False, False, False, False,
                                           False, False, False, False, False,
                                           False, False, False, False, False,
                                           False, False),
        default_float: typing.List[float] = (0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                                             0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                                             0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                                             0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                                             0.0, 0.0, 0.0, 0.0),
        min_float: float = -10000.0,
        max_float: float = -10000.0,
        soft_min_float: float = -10000.0,
        soft_max_float: float = -10000.0,
        precision: int = 3,
        step_float: float = 0.1,
        subtype: typing.Union[int, str] = 'NONE',
        default_string: str = "",
        eval_string: str = ""):
    ''' Change a custom property's type, or adjust how it is displayed in the interface :File: startup/bl_operators/wm.py\:1757 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/wm.py#L1757> __

    :param data_path: Property Edit, Property data_path edit
    :type data_path: str
    :param property_name: Property Name, Property name edit
    :type property_name: str
    :param property_type: Type * FLOAT Float -- A single floating-point value. * FLOAT_ARRAY Float Array -- An array of floating-point values. * INT Integer -- A single integer. * INT_ARRAY Integer Array -- An array of integers. * BOOL Boolean -- A true or false value. * BOOL_ARRAY Boolean Array -- An array of true or false values. * STRING String -- A string value. * PYTHON Python -- Edit a python value directly, for unsupported property types.
    :type property_type: typing.Union[int, str]
    :param is_overridable_library: Library Overridable, Allow the property to be overridden when the data-block is linked
    :type is_overridable_library: bool
    :param description: Description
    :type description: str
    :param use_soft_limits: Soft Limits, Limits the Property Value slider to a range, values outside the range must be inputted numerically
    :type use_soft_limits: bool
    :param array_length: Array Length
    :type array_length: int
    :param default_int: Default Value
    :type default_int: typing.List[int]
    :param min_int: Min
    :type min_int: int
    :param max_int: Max
    :type max_int: int
    :param soft_min_int: Soft Min
    :type soft_min_int: int
    :param soft_max_int: Soft Max
    :type soft_max_int: int
    :param step_int: Step
    :type step_int: int
    :param default_bool: Default Value
    :type default_bool: typing.List[bool]
    :param default_float: Default Value
    :type default_float: typing.List[float]
    :param min_float: Min
    :type min_float: float
    :param max_float: Max
    :type max_float: float
    :param soft_min_float: Soft Min
    :type soft_min_float: float
    :param soft_max_float: Soft Max
    :type soft_max_float: float
    :param precision: Precision
    :type precision: int
    :param step_float: Step
    :type step_float: float
    :param subtype: Subtype * NONE Plain Data -- Data values without special behavior. * COLOR Linear Color -- Color in the linear space. * COLOR_GAMMA Gamma-Corrected Color -- Color in the gamma corrected space. * EULER Euler Angles -- Euler rotation angles in radians. * QUATERNION Quaternion Rotation -- Quaternion rotation (affects NLA blending).
    :type subtype: typing.Union[int, str]
    :param default_string: Default Value
    :type default_string: str
    :param eval_string: Value, Python value for unsupported custom property types
    :type eval_string: str
    '''

    pass


def properties_edit_value(data_path: str = "",
                          property_name: str = "",
                          eval_string: str = ""):
    ''' Edit the value of a custom property :File: startup/bl_operators/wm.py\:1973 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/wm.py#L1973> __

    :param data_path: Property Edit, Property data_path edit
    :type data_path: str
    :param property_name: Property Name, Property name edit
    :type property_name: str
    :param eval_string: Value, Value for custom property types that can only be edited as a Python expression
    :type eval_string: str
    '''

    pass


def properties_remove(data_path: str = "", property_name: str = ""):
    ''' Internal use (edit a property data_path) :File: startup/bl_operators/wm.py\:2074 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/wm.py#L2074> __

    :param data_path: Property Edit, Property data_path edit
    :type data_path: str
    :param property_name: Property Name, Property name edit
    :type property_name: str
    '''

    pass


def quit_blender():
    ''' Quit Blender

    '''

    pass


def radial_control(data_path_primary: str = "",
                   data_path_secondary: str = "",
                   use_secondary: str = "",
                   rotation_path: str = "",
                   color_path: str = "",
                   fill_color_path: str = "",
                   fill_color_override_path: str = "",
                   fill_color_override_test_path: str = "",
                   zoom_path: str = "",
                   image_id: str = "",
                   secondary_tex: bool = False,
                   release_confirm: bool = False):
    ''' Set some size property (e.g. brush size) with mouse wheel

    :param data_path_primary: Primary Data Path, Primary path of property to be set by the radial control
    :type data_path_primary: str
    :param data_path_secondary: Secondary Data Path, Secondary path of property to be set by the radial control
    :type data_path_secondary: str
    :param use_secondary: Use Secondary, Path of property to select between the primary and secondary data paths
    :type use_secondary: str
    :param rotation_path: Rotation Path, Path of property used to rotate the texture display
    :type rotation_path: str
    :param color_path: Color Path, Path of property used to set the color of the control
    :type color_path: str
    :param fill_color_path: Fill Color Path, Path of property used to set the fill color of the control
    :type fill_color_path: str
    :param fill_color_override_path: Fill Color Override Path
    :type fill_color_override_path: str
    :param fill_color_override_test_path: Fill Color Override Test
    :type fill_color_override_test_path: str
    :param zoom_path: Zoom Path, Path of property used to set the zoom level for the control
    :type zoom_path: str
    :param image_id: Image ID, Path of ID that is used to generate an image for the control
    :type image_id: str
    :param secondary_tex: Secondary Texture, Tweak brush secondary/mask texture
    :type secondary_tex: bool
    :param release_confirm: Confirm On Release, Finish operation on key release
    :type release_confirm: bool
    '''

    pass


def read_factory_settings(use_factory_startup_app_template_only: bool = False,
                          app_template: str = "Template",
                          use_empty: bool = False):
    ''' Load factory default startup file and preferences. To make changes permanent, use "Save Startup File" and "Save Preferences"

    :param use_factory_startup_app_template_only: Factory Startup App-Template Only
    :type use_factory_startup_app_template_only: bool
    :type app_template: str
    :param use_empty: Empty
    :type use_empty: bool
    '''

    pass


def read_factory_userpref(use_factory_startup_app_template_only: bool = False):
    ''' Load factory default preferences. To make changes to preferences permanent, use "Save Preferences"

    :param use_factory_startup_app_template_only: Factory Startup App-Template Only
    :type use_factory_startup_app_template_only: bool
    '''

    pass


def read_history():
    ''' Reloads history and bookmarks

    '''

    pass


def read_homefile(filepath: str = "",
                  load_ui: bool = True,
                  use_splash: bool = False,
                  use_factory_startup: bool = False,
                  use_factory_startup_app_template_only: bool = False,
                  app_template: str = "Template",
                  use_empty: bool = False):
    ''' Open the default file (doesn't save the current file)

    :param filepath: File Path, Path to an alternative start-up file
    :type filepath: str
    :param load_ui: Load UI, Load user interface setup from the .blend file
    :type load_ui: bool
    :param use_splash: Splash
    :type use_splash: bool
    :param use_factory_startup: Factory Startup
    :type use_factory_startup: bool
    :param use_factory_startup_app_template_only: Factory Startup App-Template Only
    :type use_factory_startup_app_template_only: bool
    :type app_template: str
    :param use_empty: Empty
    :type use_empty: bool
    '''

    pass


def read_userpref():
    ''' Load last saved preferences

    '''

    pass


def recover_auto_save(filepath: str = "",
                      hide_props_region: bool = True,
                      check_existing: bool = False,
                      filter_blender: bool = True,
                      filter_backup: bool = False,
                      filter_image: bool = False,
                      filter_movie: bool = False,
                      filter_python: bool = False,
                      filter_font: bool = False,
                      filter_sound: bool = False,
                      filter_text: bool = False,
                      filter_archive: bool = False,
                      filter_btx: bool = False,
                      filter_collada: bool = False,
                      filter_alembic: bool = False,
                      filter_usd: bool = False,
                      filter_obj: bool = False,
                      filter_volume: bool = False,
                      filter_folder: bool = False,
                      filter_blenlib: bool = False,
                      filemode: int = 8,
                      display_type: typing.Union[int, str] = 'LIST_VERTICAL',
                      sort_method: typing.Union[int, str] = '',
                      use_scripts: bool = True):
    ''' Open an automatically saved file to recover it

    :param filepath: File Path, Path to file
    :type filepath: str
    :param hide_props_region: Hide Operator Properties, Collapse the region displaying the operator settings
    :type hide_props_region: bool
    :param check_existing: Check Existing, Check and warn on overwriting existing files
    :type check_existing: bool
    :param filter_blender: Filter .blend files
    :type filter_blender: bool
    :param filter_backup: Filter .blend files
    :type filter_backup: bool
    :param filter_image: Filter image files
    :type filter_image: bool
    :param filter_movie: Filter movie files
    :type filter_movie: bool
    :param filter_python: Filter python files
    :type filter_python: bool
    :param filter_font: Filter font files
    :type filter_font: bool
    :param filter_sound: Filter sound files
    :type filter_sound: bool
    :param filter_text: Filter text files
    :type filter_text: bool
    :param filter_archive: Filter archive files
    :type filter_archive: bool
    :param filter_btx: Filter btx files
    :type filter_btx: bool
    :param filter_collada: Filter COLLADA files
    :type filter_collada: bool
    :param filter_alembic: Filter Alembic files
    :type filter_alembic: bool
    :param filter_usd: Filter USD files
    :type filter_usd: bool
    :param filter_obj: Filter OBJ files
    :type filter_obj: bool
    :param filter_volume: Filter OpenVDB volume files
    :type filter_volume: bool
    :param filter_folder: Filter folders
    :type filter_folder: bool
    :param filter_blenlib: Filter Blender IDs
    :type filter_blenlib: bool
    :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
    :type filemode: int
    :param display_type: Display Type * DEFAULT Default -- Automatically determine display type for files. * LIST_VERTICAL Short List -- Display files as short list. * LIST_HORIZONTAL Long List -- Display files as a detailed list. * THUMBNAIL Thumbnails -- Display files as thumbnails.
    :type display_type: typing.Union[int, str]
    :param sort_method: File sorting mode
    :type sort_method: typing.Union[int, str]
    :param use_scripts: Trusted Source, Allow .blend file to execute scripts automatically, default available from system preferences
    :type use_scripts: bool
    '''

    pass


def recover_last_session(use_scripts: bool = True):
    ''' Open the last closed file ("quit.blend")

    :param use_scripts: Trusted Source, Allow .blend file to execute scripts automatically, default available from system preferences
    :type use_scripts: bool
    '''

    pass


def redraw_timer(type: typing.Union[int, str] = 'DRAW',
                 iterations: int = 10,
                 time_limit: float = 0.0):
    ''' Simple redraw timer to test the speed of updating the interface

    :param type: Type * DRAW Draw Region -- Draw region. * DRAW_SWAP Draw Region & Swap -- Draw region and swap. * DRAW_WIN Draw Window -- Draw window. * DRAW_WIN_SWAP Draw Window & Swap -- Draw window and swap. * ANIM_STEP Animation Step -- Animation steps. * ANIM_PLAY Animation Play -- Animation playback. * UNDO Undo/Redo -- Undo and redo.
    :type type: typing.Union[int, str]
    :param iterations: Iterations, Number of times to redraw
    :type iterations: int
    :param time_limit: Time Limit, Seconds to run the test for (override iterations)
    :type time_limit: float
    '''

    pass


def revert_mainfile(use_scripts: bool = True):
    ''' Reload the saved file

    :param use_scripts: Trusted Source, Allow .blend file to execute scripts automatically, default available from system preferences
    :type use_scripts: bool
    '''

    pass


def save_as_mainfile(filepath: str = "",
                     hide_props_region: bool = True,
                     check_existing: bool = True,
                     filter_blender: bool = True,
                     filter_backup: bool = False,
                     filter_image: bool = False,
                     filter_movie: bool = False,
                     filter_python: bool = False,
                     filter_font: bool = False,
                     filter_sound: bool = False,
                     filter_text: bool = False,
                     filter_archive: bool = False,
                     filter_btx: bool = False,
                     filter_collada: bool = False,
                     filter_alembic: bool = False,
                     filter_usd: bool = False,
                     filter_obj: bool = False,
                     filter_volume: bool = False,
                     filter_folder: bool = True,
                     filter_blenlib: bool = False,
                     filemode: int = 8,
                     display_type: typing.Union[int, str] = 'DEFAULT',
                     sort_method: typing.Union[int, str] = '',
                     compress: bool = False,
                     relative_remap: bool = True,
                     copy: bool = False):
    ''' Save the current file in the desired location

    :param filepath: File Path, Path to file
    :type filepath: str
    :param hide_props_region: Hide Operator Properties, Collapse the region displaying the operator settings
    :type hide_props_region: bool
    :param check_existing: Check Existing, Check and warn on overwriting existing files
    :type check_existing: bool
    :param filter_blender: Filter .blend files
    :type filter_blender: bool
    :param filter_backup: Filter .blend files
    :type filter_backup: bool
    :param filter_image: Filter image files
    :type filter_image: bool
    :param filter_movie: Filter movie files
    :type filter_movie: bool
    :param filter_python: Filter python files
    :type filter_python: bool
    :param filter_font: Filter font files
    :type filter_font: bool
    :param filter_sound: Filter sound files
    :type filter_sound: bool
    :param filter_text: Filter text files
    :type filter_text: bool
    :param filter_archive: Filter archive files
    :type filter_archive: bool
    :param filter_btx: Filter btx files
    :type filter_btx: bool
    :param filter_collada: Filter COLLADA files
    :type filter_collada: bool
    :param filter_alembic: Filter Alembic files
    :type filter_alembic: bool
    :param filter_usd: Filter USD files
    :type filter_usd: bool
    :param filter_obj: Filter OBJ files
    :type filter_obj: bool
    :param filter_volume: Filter OpenVDB volume files
    :type filter_volume: bool
    :param filter_folder: Filter folders
    :type filter_folder: bool
    :param filter_blenlib: Filter Blender IDs
    :type filter_blenlib: bool
    :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
    :type filemode: int
    :param display_type: Display Type * DEFAULT Default -- Automatically determine display type for files. * LIST_VERTICAL Short List -- Display files as short list. * LIST_HORIZONTAL Long List -- Display files as a detailed list. * THUMBNAIL Thumbnails -- Display files as thumbnails.
    :type display_type: typing.Union[int, str]
    :param sort_method: File sorting mode
    :type sort_method: typing.Union[int, str]
    :param compress: Compress, Write compressed .blend file
    :type compress: bool
    :param relative_remap: Remap Relative, Remap relative paths when saving to a different directory
    :type relative_remap: bool
    :param copy: Save Copy, Save a copy of the actual working state but does not make saved file active
    :type copy: bool
    '''

    pass


def save_homefile():
    ''' Make the current file the default .blend file

    '''

    pass


def save_mainfile(filepath: str = "",
                  hide_props_region: bool = True,
                  check_existing: bool = True,
                  filter_blender: bool = True,
                  filter_backup: bool = False,
                  filter_image: bool = False,
                  filter_movie: bool = False,
                  filter_python: bool = False,
                  filter_font: bool = False,
                  filter_sound: bool = False,
                  filter_text: bool = False,
                  filter_archive: bool = False,
                  filter_btx: bool = False,
                  filter_collada: bool = False,
                  filter_alembic: bool = False,
                  filter_usd: bool = False,
                  filter_obj: bool = False,
                  filter_volume: bool = False,
                  filter_folder: bool = True,
                  filter_blenlib: bool = False,
                  filemode: int = 8,
                  display_type: typing.Union[int, str] = 'DEFAULT',
                  sort_method: typing.Union[int, str] = '',
                  compress: bool = False,
                  relative_remap: bool = False,
                  exit: bool = False):
    ''' Save the current Blender file

    :param filepath: File Path, Path to file
    :type filepath: str
    :param hide_props_region: Hide Operator Properties, Collapse the region displaying the operator settings
    :type hide_props_region: bool
    :param check_existing: Check Existing, Check and warn on overwriting existing files
    :type check_existing: bool
    :param filter_blender: Filter .blend files
    :type filter_blender: bool
    :param filter_backup: Filter .blend files
    :type filter_backup: bool
    :param filter_image: Filter image files
    :type filter_image: bool
    :param filter_movie: Filter movie files
    :type filter_movie: bool
    :param filter_python: Filter python files
    :type filter_python: bool
    :param filter_font: Filter font files
    :type filter_font: bool
    :param filter_sound: Filter sound files
    :type filter_sound: bool
    :param filter_text: Filter text files
    :type filter_text: bool
    :param filter_archive: Filter archive files
    :type filter_archive: bool
    :param filter_btx: Filter btx files
    :type filter_btx: bool
    :param filter_collada: Filter COLLADA files
    :type filter_collada: bool
    :param filter_alembic: Filter Alembic files
    :type filter_alembic: bool
    :param filter_usd: Filter USD files
    :type filter_usd: bool
    :param filter_obj: Filter OBJ files
    :type filter_obj: bool
    :param filter_volume: Filter OpenVDB volume files
    :type filter_volume: bool
    :param filter_folder: Filter folders
    :type filter_folder: bool
    :param filter_blenlib: Filter Blender IDs
    :type filter_blenlib: bool
    :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
    :type filemode: int
    :param display_type: Display Type * DEFAULT Default -- Automatically determine display type for files. * LIST_VERTICAL Short List -- Display files as short list. * LIST_HORIZONTAL Long List -- Display files as a detailed list. * THUMBNAIL Thumbnails -- Display files as thumbnails.
    :type display_type: typing.Union[int, str]
    :param sort_method: File sorting mode
    :type sort_method: typing.Union[int, str]
    :param compress: Compress, Write compressed .blend file
    :type compress: bool
    :param relative_remap: Remap Relative, Remap relative paths when saving to a different directory
    :type relative_remap: bool
    :param exit: Exit, Exit Blender after saving
    :type exit: bool
    '''

    pass


def save_userpref():
    ''' Make the current preferences default

    '''

    pass


def search_menu():
    ''' Pop-up a search over all menus in the current context

    '''

    pass


def search_operator():
    ''' Pop-up a search over all available operators in current context

    '''

    pass


def set_stereo_3d(display_mode: typing.Union[int, str] = 'ANAGLYPH',
                  anaglyph_type: typing.Union[int, str] = 'RED_CYAN',
                  interlace_type: typing.Union[int, str] = 'ROW_INTERLEAVED',
                  use_interlace_swap: bool = False,
                  use_sidebyside_crosseyed: bool = False):
    ''' Toggle 3D stereo support for current window (or change the display mode)

    :param display_mode: Display Mode
    :type display_mode: typing.Union[int, str]
    :param anaglyph_type: Anaglyph Type
    :type anaglyph_type: typing.Union[int, str]
    :param interlace_type: Interlace Type
    :type interlace_type: typing.Union[int, str]
    :param use_interlace_swap: Swap Left/Right, Swap left and right stereo channels
    :type use_interlace_swap: bool
    :param use_sidebyside_crosseyed: Cross-Eyed, Right eye should see left image and vice versa
    :type use_sidebyside_crosseyed: bool
    '''

    pass


def splash():
    ''' Open the splash screen with release info

    '''

    pass


def splash_about():
    ''' Open a window with information about UPBGE

    '''

    pass


def stl_import(
        filepath: str = "",
        directory: str = "",
        files: typing.
        Union[typing.Dict[str, 'bpy.types.OperatorFileListElement'], typing.
              List['bpy.types.OperatorFileListElement'],
              'bpy_prop_collection'] = None,
        check_existing: bool = False,
        filter_blender: bool = False,
        filter_backup: bool = False,
        filter_image: bool = False,
        filter_movie: bool = False,
        filter_python: bool = False,
        filter_font: bool = False,
        filter_sound: bool = False,
        filter_text: bool = False,
        filter_archive: bool = False,
        filter_btx: bool = False,
        filter_collada: bool = False,
        filter_alembic: bool = False,
        filter_usd: bool = False,
        filter_obj: bool = False,
        filter_volume: bool = False,
        filter_folder: bool = True,
        filter_blenlib: bool = False,
        filemode: int = 8,
        display_type: typing.Union[int, str] = 'DEFAULT',
        sort_method: typing.Union[int, str] = '',
        global_scale: float = 1.0,
        use_scene_unit: bool = False,
        use_facet_normal: bool = False,
        forward_axis: typing.Union[int, str] = 'Y',
        up_axis: typing.Union[int, str] = 'Z',
        use_mesh_validate: bool = False,
        filter_glob: str = "*.stl"):
    ''' Import an STL file as an object

    :param filepath: File Path, Path to file
    :type filepath: str
    :param directory: Directory, Directory of the file
    :type directory: str
    :param files: Files
    :type files: typing.Union[typing.Dict[str, 'bpy.types.OperatorFileListElement'], typing.List['bpy.types.OperatorFileListElement'], 'bpy_prop_collection']
    :param check_existing: Check Existing, Check and warn on overwriting existing files
    :type check_existing: bool
    :param filter_blender: Filter .blend files
    :type filter_blender: bool
    :param filter_backup: Filter .blend files
    :type filter_backup: bool
    :param filter_image: Filter image files
    :type filter_image: bool
    :param filter_movie: Filter movie files
    :type filter_movie: bool
    :param filter_python: Filter python files
    :type filter_python: bool
    :param filter_font: Filter font files
    :type filter_font: bool
    :param filter_sound: Filter sound files
    :type filter_sound: bool
    :param filter_text: Filter text files
    :type filter_text: bool
    :param filter_archive: Filter archive files
    :type filter_archive: bool
    :param filter_btx: Filter btx files
    :type filter_btx: bool
    :param filter_collada: Filter COLLADA files
    :type filter_collada: bool
    :param filter_alembic: Filter Alembic files
    :type filter_alembic: bool
    :param filter_usd: Filter USD files
    :type filter_usd: bool
    :param filter_obj: Filter OBJ files
    :type filter_obj: bool
    :param filter_volume: Filter OpenVDB volume files
    :type filter_volume: bool
    :param filter_folder: Filter folders
    :type filter_folder: bool
    :param filter_blenlib: Filter Blender IDs
    :type filter_blenlib: bool
    :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
    :type filemode: int
    :param display_type: Display Type * DEFAULT Default -- Automatically determine display type for files. * LIST_VERTICAL Short List -- Display files as short list. * LIST_HORIZONTAL Long List -- Display files as a detailed list. * THUMBNAIL Thumbnails -- Display files as thumbnails.
    :type display_type: typing.Union[int, str]
    :param sort_method: File sorting mode
    :type sort_method: typing.Union[int, str]
    :param global_scale: Scale
    :type global_scale: float
    :param use_scene_unit: Scene Unit, Apply current scene's unit (as defined by unit scale) to imported data
    :type use_scene_unit: bool
    :param use_facet_normal: Facet Normals, Use (import) facet normals (note that this will still give flat shading)
    :type use_facet_normal: bool
    :param forward_axis: Forward Axis * X X -- Positive X axis. * Y Y -- Positive Y axis. * Z Z -- Positive Z axis. * NEGATIVE_X -X -- Negative X axis. * NEGATIVE_Y -Y -- Negative Y axis. * NEGATIVE_Z -Z -- Negative Z axis.
    :type forward_axis: typing.Union[int, str]
    :param up_axis: Up Axis * X X -- Positive X axis. * Y Y -- Positive Y axis. * Z Z -- Positive Z axis. * NEGATIVE_X -X -- Negative X axis. * NEGATIVE_Y -Y -- Negative Y axis. * NEGATIVE_Z -Z -- Negative Z axis.
    :type up_axis: typing.Union[int, str]
    :param use_mesh_validate: Validate Mesh, Validate and correct imported mesh (slow)
    :type use_mesh_validate: bool
    :param filter_glob: Extension Filter
    :type filter_glob: str
    '''

    pass


def sysinfo(filepath: str = ""):
    ''' Generate system information, saved into a text file :File: startup/bl_operators/wm.py\:2103 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/wm.py#L2103> __

    :param filepath: filepath
    :type filepath: str
    '''

    pass


def tool_set_by_id(name: str = "",
                   cycle: bool = False,
                   as_fallback: bool = False,
                   space_type: typing.Union[int, str] = 'EMPTY'):
    ''' Set the tool by name (for keymaps) :File: startup/bl_operators/wm.py\:2254 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/wm.py#L2254> __

    :param name: Identifier, Identifier of the tool
    :type name: str
    :param cycle: Cycle, Cycle through tools in this group
    :type cycle: bool
    :param as_fallback: Set Fallback, Set the fallback tool instead of the primary tool
    :type as_fallback: bool
    :param space_type: Type
    :type space_type: typing.Union[int, str]
    '''

    pass


def tool_set_by_index(index: int = 0,
                      cycle: bool = False,
                      expand: bool = True,
                      as_fallback: bool = False,
                      space_type: typing.Union[int, str] = 'EMPTY'):
    ''' Set the tool by index (for keymaps) :File: startup/bl_operators/wm.py\:2306 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/wm.py#L2306> __

    :param index: Index in Toolbar
    :type index: int
    :param cycle: Cycle, Cycle through tools in this group
    :type cycle: bool
    :param expand: expand, Include tool subgroups
    :type expand: bool
    :param as_fallback: Set Fallback, Set the fallback tool instead of the primary
    :type as_fallback: bool
    :param space_type: Type
    :type space_type: typing.Union[int, str]
    '''

    pass


def toolbar():
    ''' Undocumented, consider contributing <https://developer.blender.org/> __. :File: startup/bl_operators/wm.py\:2361 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/wm.py#L2361> __

    '''

    pass


def toolbar_fallback_pie():
    ''' Undocumented, consider contributing <https://developer.blender.org/> __. :File: startup/bl_operators/wm.py\:2385 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/wm.py#L2385> __

    '''

    pass


def toolbar_prompt():
    ''' Leader key like functionality for accessing tools :File: startup/bl_operators/wm.py\:2485 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/wm.py#L2485> __

    '''

    pass


def url_open(url: str = ""):
    ''' Open a website in the web browser :File: startup/bl_operators/wm.py\:1021 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/wm.py#L1021> __

    :param url: URL, URL to open
    :type url: str
    '''

    pass


def url_open_preset(type: typing.Union[int, str] = '', id: str = ""):
    ''' Open a preset website in the web browser :File: startup/bl_operators/wm.py\:1096 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/wm.py#L1096> __

    :param type: Site
    :type type: typing.Union[int, str]
    :param id: Identifier, Optional identifier
    :type id: str
    '''

    pass


def window_close():
    ''' Close the current window

    '''

    pass


def window_fullscreen_toggle():
    ''' Toggle the current window full-screen

    '''

    pass


def window_new():
    ''' Create a new window

    '''

    pass


def window_new_main():
    ''' Create a new main window with its own workspace and scene selection

    '''

    pass
