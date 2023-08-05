import sys
import typing
import bpy.types


def addon_disable(module: str = ""):
    ''' Disable an add-on :File: startup/bl_operators/userpref.py\:480 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/userpref.py#L480> __

    :param module: Module, Module name of the add-on to disable
    :type module: str
    '''

    pass


def addon_enable(module: str = ""):
    ''' Enable an add-on :File: startup/bl_operators/userpref.py\:434 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/userpref.py#L434> __

    :param module: Module, Module name of the add-on to enable
    :type module: str
    '''

    pass


def addon_expand(module: str = ""):
    ''' Display information and preferences for this add-on :File: startup/bl_operators/userpref.py\:816 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/userpref.py#L816> __

    :param module: Module, Module name of the add-on to expand
    :type module: str
    '''

    pass


def addon_install(overwrite: bool = True,
                  target: typing.Union[str, int] = '',
                  filepath: str = "",
                  filter_folder: bool = True,
                  filter_python: bool = True,
                  filter_glob: str = "*.py;*.zip"):
    ''' Install an add-on :File: startup/bl_operators/userpref.py\:622 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/userpref.py#L622> __

    :param overwrite: Overwrite, Remove existing add-ons with the same ID
    :type overwrite: bool
    :param target: Target Path
    :type target: typing.Union[str, int]
    :param filepath: filepath
    :type filepath: str
    :param filter_folder: Filter folders
    :type filter_folder: bool
    :param filter_python: Filter python
    :type filter_python: bool
    :param filter_glob: filter_glob
    :type filter_glob: str
    '''

    pass


def addon_refresh():
    ''' Scan add-on directories for new modules :File: startup/bl_operators/userpref.py\:570 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/userpref.py#L570> __

    '''

    pass


def addon_remove(module: str = ""):
    ''' Delete the add-on from the file system :File: startup/bl_operators/userpref.py\:771 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/userpref.py#L771> __

    :param module: Module, Module name of the add-on to remove
    :type module: str
    '''

    pass


def addon_show(module: str = ""):
    ''' Show add-on preferences :File: startup/bl_operators/userpref.py\:840 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/userpref.py#L840> __

    :param module: Module, Module name of the add-on to expand
    :type module: str
    '''

    pass


def app_template_install(overwrite: bool = True,
                         filepath: str = "",
                         filter_folder: bool = True,
                         filter_glob: str = "*.zip"):
    ''' Install an application template :File: startup/bl_operators/userpref.py\:886 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/userpref.py#L886> __

    :param overwrite: Overwrite, Remove existing template with the same ID
    :type overwrite: bool
    :param filepath: filepath
    :type filepath: str
    :param filter_folder: Filter folders
    :type filter_folder: bool
    :param filter_glob: filter_glob
    :type filter_glob: str
    '''

    pass


def asset_library_add(directory: str = "",
                      hide_props_region: bool = True,
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
                      filemode: int = 9,
                      display_type: typing.Union[str, int] = 'DEFAULT',
                      sort_method: typing.Union[str, int] = ''):
    ''' Add a directory to be used by the Asset Browser as source of assets

    :param directory: Directory, Directory of the file
    :type directory: str
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
    :type display_type: typing.Union[str, int]
    :param sort_method: File sorting mode
    :type sort_method: typing.Union[str, int]
    '''

    pass


def asset_library_remove(index: int = 0):
    ''' Remove a path to a .blend file, so the Asset Browser will not attempt to show it anymore

    :param index: Index
    :type index: int
    '''

    pass


def associate_blend():
    ''' Use this installation for .blend files and to display thumbnails

    '''

    pass


def autoexec_path_add():
    ''' Add path to exclude from auto-execution

    '''

    pass


def autoexec_path_remove(index: int = 0):
    ''' Remove path to exclude from auto-execution

    :param index: Index
    :type index: int
    '''

    pass


def copy_prev():
    ''' Copy settings from previous version :File: startup/bl_operators/userpref.py\:141 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/userpref.py#L141> __

    '''

    pass


def keyconfig_activate(filepath: str = ""):
    ''' Undocumented, consider contributing <https://developer.blender.org/> __. :File: startup/bl_operators/userpref.py\:63 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/userpref.py#L63> __

    :param filepath: filepath
    :type filepath: str
    '''

    pass


def keyconfig_export(all: bool = False,
                     filepath: str = "",
                     filter_folder: bool = True,
                     filter_text: bool = True,
                     filter_python: bool = True):
    ''' Export key configuration to a python script :File: startup/bl_operators/userpref.py\:276 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/userpref.py#L276> __

    :param all: All Keymaps, Write all keymaps (not just user modified)
    :type all: bool
    :param filepath: filepath
    :type filepath: str
    :param filter_folder: Filter folders
    :type filter_folder: bool
    :param filter_text: Filter text
    :type filter_text: bool
    :param filter_python: Filter python
    :type filter_python: bool
    '''

    pass


def keyconfig_import(filepath: str = "keymap.py",
                     filter_folder: bool = True,
                     filter_text: bool = True,
                     filter_python: bool = True,
                     keep_original: bool = True):
    ''' Import key configuration from a python script :File: startup/bl_operators/userpref.py\:205 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/userpref.py#L205> __

    :param filepath: filepath
    :type filepath: str
    :param filter_folder: Filter folders
    :type filter_folder: bool
    :param filter_text: Filter text
    :type filter_text: bool
    :param filter_python: Filter python
    :type filter_python: bool
    :param keep_original: Keep Original, Keep original file after copying to configuration folder
    :type keep_original: bool
    '''

    pass


def keyconfig_remove():
    ''' Remove key config :File: startup/bl_operators/userpref.py\:414 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/userpref.py#L414> __

    '''

    pass


def keyconfig_test():
    ''' Test key configuration for conflicts :File: startup/bl_operators/userpref.py\:163 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/userpref.py#L163> __

    '''

    pass


def keyitem_add():
    ''' Add key map item :File: startup/bl_operators/userpref.py\:362 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/userpref.py#L362> __

    '''

    pass


def keyitem_remove(item_id: int = 0):
    ''' Remove key map item :File: startup/bl_operators/userpref.py\:394 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/userpref.py#L394> __

    :param item_id: Item Identifier, Identifier of the item to remove
    :type item_id: int
    '''

    pass


def keyitem_restore(item_id: int = 0):
    ''' Restore key map item :File: startup/bl_operators/userpref.py\:347 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/userpref.py#L347> __

    :param item_id: Item Identifier, Identifier of the item to restore
    :type item_id: int
    '''

    pass


def keymap_restore(all: bool = False):
    ''' Restore key map(s) :File: startup/bl_operators/userpref.py\:318 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/userpref.py#L318> __

    :param all: All Keymaps, Restore all keymaps to default
    :type all: bool
    '''

    pass


def reset_default_theme():
    ''' Reset to the default theme colors

    '''

    pass


def script_directory_add(directory: str = "", filter_folder: bool = True):
    ''' Undocumented, consider contributing <https://developer.blender.org/> __. :File: startup/bl_operators/userpref.py\:1163 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/userpref.py#L1163> __

    :param directory: directory
    :type directory: str
    :param filter_folder: Filter Folders
    :type filter_folder: bool
    '''

    pass


def script_directory_remove(index: int = 0):
    ''' Undocumented, consider contributing <https://developer.blender.org/> __. :File: startup/bl_operators/userpref.py\:1193 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/userpref.py#L1193> __

    :param index: Index, Index of the script directory to remove
    :type index: int
    '''

    pass


def studiolight_copy_settings(index: int = 0):
    ''' Copy Studio Light settings to the Studio Light editor :File: startup/bl_operators/userpref.py\:1118 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/userpref.py#L1118> __

    :param index: index
    :type index: int
    '''

    pass


def studiolight_install(
        files: typing.
        Union[typing.Dict[str, 'bpy.types.OperatorFileListElement'], typing.
              List['bpy.types.OperatorFileListElement'],
              'bpy_prop_collection'] = None,
        directory: str = "",
        filter_folder: bool = True,
        filter_glob: str = "*.png;*.jpg;*.hdr;*.exr",
        type: typing.Union[str, int] = 'MATCAP'):
    ''' Install a user defined light :File: startup/bl_operators/userpref.py\:995 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/userpref.py#L995> __

    :param files: File Path
    :type files: typing.Union[typing.Dict[str, 'bpy.types.OperatorFileListElement'], typing.List['bpy.types.OperatorFileListElement'], 'bpy_prop_collection']
    :param directory: directory
    :type directory: str
    :param filter_folder: Filter Folders
    :type filter_folder: bool
    :param filter_glob: filter_glob
    :type filter_glob: str
    :param type: Type * MATCAP MatCap -- Install custom MatCaps. * WORLD World -- Install custom HDRIs. * STUDIO Studio -- Install custom Studio Lights.
    :type type: typing.Union[str, int]
    '''

    pass


def studiolight_new(filename: str = "StudioLight"):
    ''' Save custom studio light from the studio light editor settings :File: startup/bl_operators/userpref.py\:1041 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/userpref.py#L1041> __

    :param filename: Name
    :type filename: str
    '''

    pass


def studiolight_show():
    ''' Show light preferences :File: startup/bl_operators/userpref.py\:1144 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/userpref.py#L1144> __

    '''

    pass


def studiolight_uninstall(index: int = 0):
    ''' Delete Studio Light :File: startup/bl_operators/userpref.py\:1095 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/userpref.py#L1095> __

    :param index: index
    :type index: int
    '''

    pass


def theme_install(overwrite: bool = True,
                  filepath: str = "",
                  filter_folder: bool = True,
                  filter_glob: str = "*.xml"):
    ''' Load and apply a Blender XML theme file :File: startup/bl_operators/userpref.py\:522 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/userpref.py#L522> __

    :param overwrite: Overwrite, Remove existing theme file if exists
    :type overwrite: bool
    :param filepath: filepath
    :type filepath: str
    :param filter_folder: Filter folders
    :type filter_folder: bool
    :param filter_glob: filter_glob
    :type filter_glob: str
    '''

    pass
