import sys
import typing


def change_frame(frame: float = 0.0, snap: bool = False):
    ''' Interactively change the current frame number

    :param frame: Frame
    :type frame: float
    :param snap: Snap
    :type snap: bool
    '''

    pass


def channel_select_keys(extend: bool = False):
    ''' Select all keyframes of channel under mouse

    :param extend: Extend, Extend selection
    :type extend: bool
    '''

    pass


def channel_view_pick(include_handles: bool = True,
                      use_preview_range: bool = True):
    ''' Reset viewable area to show the channel under the cursor

    :param include_handles: Include Handles, Include handles of keyframes when calculating extents
    :type include_handles: bool
    :param use_preview_range: Use Preview Range, Ignore frames outside of the preview range
    :type use_preview_range: bool
    '''

    pass


def channels_clean_empty():
    ''' Delete all empty animation data containers from visible data-blocks

    '''

    pass


def channels_click(extend: bool = False, children_only: bool = False):
    ''' Handle mouse clicks over animation channels

    :param extend: Extend Select
    :type extend: bool
    :param children_only: Select Children Only
    :type children_only: bool
    '''

    pass


def channels_collapse(all: bool = True):
    ''' Collapse (close) all selected expandable animation channels

    :param all: All, Collapse all channels (not just selected ones)
    :type all: bool
    '''

    pass


def channels_delete():
    ''' Delete all selected animation channels

    '''

    pass


def channels_editable_toggle(mode: typing.Union[str, int] = 'TOGGLE',
                             type: typing.Union[str, int] = 'PROTECT'):
    ''' Toggle editability of selected channels

    :param mode: Mode
    :type mode: typing.Union[str, int]
    :param type: Type
    :type type: typing.Union[str, int]
    '''

    pass


def channels_expand(all: bool = True):
    ''' Expand (open) all selected expandable animation channels

    :param all: All, Expand all channels (not just selected ones)
    :type all: bool
    '''

    pass


def channels_fcurves_enable():
    ''' Clear 'disabled' tag from all F-Curves to get broken F-Curves working again

    '''

    pass


def channels_group(name: str = "New Group"):
    ''' Add selected F-Curves to a new group

    :param name: Name, Name of newly created group
    :type name: str
    '''

    pass


def channels_move(direction: typing.Union[str, int] = 'DOWN'):
    ''' Rearrange selected animation channels

    :param direction: Direction
    :type direction: typing.Union[str, int]
    '''

    pass


def channels_rename():
    ''' Rename animation channel under mouse

    '''

    pass


def channels_select_all(action: typing.Union[str, int] = 'TOGGLE'):
    ''' Toggle selection of all animation channels

    :param action: Action, Selection action to execute * TOGGLE Toggle -- Toggle selection for all elements. * SELECT Select -- Select all elements. * DESELECT Deselect -- Deselect all elements. * INVERT Invert -- Invert selection of all elements.
    :type action: typing.Union[str, int]
    '''

    pass


def channels_select_box(xmin: int = 0,
                        xmax: int = 0,
                        ymin: int = 0,
                        ymax: int = 0,
                        wait_for_input: bool = True,
                        deselect: bool = False,
                        extend: bool = True):
    ''' Select all animation channels within the specified region

    :param xmin: X Min
    :type xmin: int
    :param xmax: X Max
    :type xmax: int
    :param ymin: Y Min
    :type ymin: int
    :param ymax: Y Max
    :type ymax: int
    :param wait_for_input: Wait for Input
    :type wait_for_input: bool
    :param deselect: Deselect, Deselect rather than select items
    :type deselect: bool
    :param extend: Extend, Extend selection instead of deselecting everything first
    :type extend: bool
    '''

    pass


def channels_select_filter():
    ''' Start entering text which filters the set of channels shown to only include those with matching names

    '''

    pass


def channels_setting_disable(mode: typing.Union[str, int] = 'DISABLE',
                             type: typing.Union[str, int] = 'PROTECT'):
    ''' Disable specified setting on all selected animation channels

    :param mode: Mode
    :type mode: typing.Union[str, int]
    :param type: Type
    :type type: typing.Union[str, int]
    '''

    pass


def channels_setting_enable(mode: typing.Union[str, int] = 'ENABLE',
                            type: typing.Union[str, int] = 'PROTECT'):
    ''' Enable specified setting on all selected animation channels

    :param mode: Mode
    :type mode: typing.Union[str, int]
    :param type: Type
    :type type: typing.Union[str, int]
    '''

    pass


def channels_setting_toggle(mode: typing.Union[str, int] = 'TOGGLE',
                            type: typing.Union[str, int] = 'PROTECT'):
    ''' Toggle specified setting on all selected animation channels

    :param mode: Mode
    :type mode: typing.Union[str, int]
    :param type: Type
    :type type: typing.Union[str, int]
    '''

    pass


def channels_ungroup():
    ''' Remove selected F-Curves from their current groups

    '''

    pass


def channels_view_selected(include_handles: bool = True,
                           use_preview_range: bool = True):
    ''' Reset viewable area to show the selected channels

    :param include_handles: Include Handles, Include handles of keyframes when calculating extents
    :type include_handles: bool
    :param use_preview_range: Use Preview Range, Ignore frames outside of the preview range
    :type use_preview_range: bool
    '''

    pass


def clear_useless_actions(only_unused: bool = True):
    ''' Mark actions with no F-Curves for deletion after save and reload of file preserving "action libraries" :File: startup/bl_operators/anim.py\:322 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/anim.py#L322> __

    :param only_unused: Only Unused, Only unused (Fake User only) actions get considered
    :type only_unused: bool
    '''

    pass


def copy_driver_button():
    ''' Copy the driver for the highlighted button

    '''

    pass


def driver_button_add():
    ''' Add driver for the property under the cursor

    '''

    pass


def driver_button_edit():
    ''' Edit the drivers for the connected property represented by the highlighted button

    '''

    pass


def driver_button_remove(all: bool = True):
    ''' Remove the driver(s) for the connected property(s) represented by the highlighted button

    :param all: All, Delete drivers for all elements of the array
    :type all: bool
    '''

    pass


def end_frame_set():
    ''' Set the current frame as the preview or scene end frame

    '''

    pass


def keyframe_clear_button(all: bool = True):
    ''' Clear all keyframes on the currently active property

    :param all: All, Clear keyframes from all elements of the array
    :type all: bool
    '''

    pass


def keyframe_clear_v3d():
    ''' Remove all keyframe animation for selected objects

    '''

    pass


def keyframe_delete(type: typing.Union[str, int] = 'DEFAULT'):
    ''' Delete keyframes on the current frame for all properties in the specified Keying Set

    :param type: Keying Set, The Keying Set to use
    :type type: typing.Union[str, int]
    '''

    pass


def keyframe_delete_button(all: bool = True):
    ''' Delete current keyframe of current UI-active property

    :param all: All, Delete keyframes from all elements of the array
    :type all: bool
    '''

    pass


def keyframe_delete_by_name(type: str = ""):
    ''' Alternate access to 'Delete Keyframe' for keymaps to use

    :param type: Keying Set, The Keying Set to use
    :type type: str
    '''

    pass


def keyframe_delete_v3d():
    ''' Remove keyframes on current frame for selected objects and bones

    '''

    pass


def keyframe_insert(type: typing.Union[str, int] = 'DEFAULT'):
    ''' Insert keyframes on the current frame for all properties in the specified Keying Set

    :param type: Keying Set, The Keying Set to use
    :type type: typing.Union[str, int]
    '''

    pass


def keyframe_insert_button(all: bool = True):
    ''' Insert a keyframe for current UI-active property

    :param all: All, Insert a keyframe for all element of the array
    :type all: bool
    '''

    pass


def keyframe_insert_by_name(type: str = ""):
    ''' Alternate access to 'Insert Keyframe' for keymaps to use

    :param type: Keying Set, The Keying Set to use
    :type type: str
    '''

    pass


def keyframe_insert_menu(type: typing.Union[str, int] = 'DEFAULT',
                         always_prompt: bool = False):
    ''' Insert Keyframes for specified Keying Set, with menu of available Keying Sets if undefined

    :param type: Keying Set, The Keying Set to use
    :type type: typing.Union[str, int]
    :param always_prompt: Always Show Menu
    :type always_prompt: bool
    '''

    pass


def keying_set_active_set(type: typing.Union[str, int] = 'DEFAULT'):
    ''' Set a new active keying set

    :param type: Keying Set, The Keying Set to use
    :type type: typing.Union[str, int]
    '''

    pass


def keying_set_add():
    ''' Add a new (empty) keying set to the active Scene

    '''

    pass


def keying_set_export(filepath: str = "",
                      filter_folder: bool = True,
                      filter_text: bool = True,
                      filter_python: bool = True):
    ''' Export Keying Set to a python script :File: startup/bl_operators/anim.py\:46 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/anim.py#L46> __

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


def keying_set_path_add():
    ''' Add empty path to active keying set

    '''

    pass


def keying_set_path_remove():
    ''' Remove active Path from active keying set

    '''

    pass


def keying_set_remove():
    ''' Remove the active keying set

    '''

    pass


def keyingset_button_add(all: bool = True):
    ''' Add current UI-active property to current keying set

    :param all: All, Add all elements of the array to a Keying Set
    :type all: bool
    '''

    pass


def keyingset_button_remove():
    ''' Remove current UI-active property from current keying set

    '''

    pass


def paste_driver_button():
    ''' Paste the driver in the clipboard to the highlighted button

    '''

    pass


def previewrange_clear():
    ''' Clear preview range

    '''

    pass


def previewrange_set(xmin: int = 0,
                     xmax: int = 0,
                     ymin: int = 0,
                     ymax: int = 0,
                     wait_for_input: bool = True):
    ''' Interactively define frame range used for playback

    :param xmin: X Min
    :type xmin: int
    :param xmax: X Max
    :type xmax: int
    :param ymin: Y Min
    :type ymin: int
    :param ymax: Y Max
    :type ymax: int
    :param wait_for_input: Wait for Input
    :type wait_for_input: bool
    '''

    pass


def start_frame_set():
    ''' Set the current frame as the preview or scene start frame

    '''

    pass


def update_animated_transform_constraints(use_convert_to_radians: bool = True):
    ''' Update f-curves/drivers affecting Transform constraints (use it with files from 2.70 and earlier) :File: startup/bl_operators/anim.py\:358 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/anim.py#L358> __

    :param use_convert_to_radians: Use this only once
    :type use_convert_to_radians: bool
    '''

    pass
