import sys
import typing


def action_set(action: typing.Union[str, int] = ''):
    ''' Change the active action used

    :param action: Action
    :type action: typing.Union[str, int]
    '''

    pass


def animdata_operation(type: typing.Union[str, int] = 'CLEAR_ANIMDATA'):
    ''' Undocumented, consider contributing <https://developer.blender.org/> __.

    :param type: Animation Operation * CLEAR_ANIMDATA Clear Animation Data -- Remove this animation data container. * SET_ACT Set Action. * CLEAR_ACT Unlink Action. * REFRESH_DRIVERS Refresh Drivers. * CLEAR_DRIVERS Clear Drivers.
    :type type: typing.Union[str, int]
    '''

    pass


def collection_color_tag_set(color: typing.Union[str, int] = 'NONE'):
    ''' Set a color tag for the selected collections

    :param color: Color Tag
    :type color: typing.Union[str, int]
    '''

    pass


def collection_disable():
    ''' Disable viewport display in the view layers

    '''

    pass


def collection_disable_render():
    ''' Do not render this collection

    '''

    pass


def collection_drop():
    ''' Drag to move to collection in Outliner

    '''

    pass


def collection_duplicate():
    ''' Recursively duplicate the collection, all its children, objects and object data

    '''

    pass


def collection_duplicate_linked():
    ''' Recursively duplicate the collection, all its children and objects, with linked object data

    '''

    pass


def collection_enable():
    ''' Enable viewport display in the view layers

    '''

    pass


def collection_enable_render():
    ''' Render the collection

    '''

    pass


def collection_exclude_clear():
    ''' Include collection in the active view layer

    '''

    pass


def collection_exclude_set():
    ''' Exclude collection from the active view layer

    '''

    pass


def collection_hide():
    ''' Hide the collection in this view layer

    '''

    pass


def collection_hide_inside():
    ''' Hide all the objects and collections inside the collection

    '''

    pass


def collection_hierarchy_delete():
    ''' Delete selected collection hierarchies

    '''

    pass


def collection_holdout_clear():
    ''' Clear masking of collection in the active view layer

    '''

    pass


def collection_holdout_set():
    ''' Mask collection in the active view layer

    '''

    pass


def collection_indirect_only_clear():
    ''' Clear collection contributing only indirectly in the view layer

    '''

    pass


def collection_indirect_only_set():
    ''' Set collection to only contribute indirectly (through shadows and reflections) in the view layer

    '''

    pass


def collection_instance():
    ''' Instance selected collections to active scene

    '''

    pass


def collection_isolate(extend: bool = False):
    ''' Hide all but this collection and its parents

    :param extend: Extend, Extend current visible collections
    :type extend: bool
    '''

    pass


def collection_link():
    ''' Link selected collections to active scene

    '''

    pass


def collection_new(nested: bool = True):
    ''' Add a new collection inside selected collection

    :param nested: Nested, Add as child of selected collection
    :type nested: bool
    '''

    pass


def collection_objects_deselect():
    ''' Deselect objects in collection

    '''

    pass


def collection_objects_select():
    ''' Select objects in collection

    '''

    pass


def collection_show():
    ''' Show the collection in this view layer

    '''

    pass


def collection_show_inside():
    ''' Show all the objects and collections inside the collection

    '''

    pass


def constraint_operation(type: typing.Union[str, int] = 'ENABLE'):
    ''' Undocumented, consider contributing <https://developer.blender.org/> __.

    :param type: Constraint Operation
    :type type: typing.Union[str, int]
    '''

    pass


def data_operation(type: typing.Union[str, int] = 'DEFAULT'):
    ''' Undocumented, consider contributing <https://developer.blender.org/> __.

    :param type: Data Operation
    :type type: typing.Union[str, int]
    '''

    pass


def datastack_drop():
    ''' Copy or reorder modifiers, constraints, and effects

    '''

    pass


def delete(hierarchy: bool = False):
    ''' Delete selected objects and collections

    :param hierarchy: Hierarchy, Delete child objects and collections
    :type hierarchy: bool
    '''

    pass


def drivers_add_selected():
    ''' Add drivers to selected items

    '''

    pass


def drivers_delete_selected():
    ''' Delete drivers assigned to selected items

    '''

    pass


def expanded_toggle():
    ''' Expand/Collapse all items

    '''

    pass


def hide():
    ''' Hide selected objects and collections

    '''

    pass


def highlight_update():
    ''' Update the item highlight based on the current mouse position

    '''

    pass


def id_copy():
    ''' Selected data-blocks are copied to the clipboard

    '''

    pass


def id_delete():
    ''' Delete the ID under cursor

    '''

    pass


def id_operation(type: typing.Union[str, int] = 'UNLINK'):
    ''' General data-block management operations

    :param type: ID Data Operation * UNLINK Unlink. * LOCAL Make Local. * SINGLE Make Single User. * DELETE Delete. * REMAP Remap Users -- Make all users of selected data-blocks to use instead current (clicked) one. * COPY Copy. * PASTE Paste. * ADD_FAKE Add Fake User -- Ensure data-block gets saved even if it isn't in use (e.g. for motion and material libraries). * CLEAR_FAKE Clear Fake User. * RENAME Rename. * SELECT_LINKED Select Linked.
    :type type: typing.Union[str, int]
    '''

    pass


def id_paste():
    ''' Data-blocks from the clipboard are pasted

    '''

    pass


def id_remap(id_type: typing.Union[str, int] = 'OBJECT',
             old_id: typing.Union[str, int] = '',
             new_id: typing.Union[str, int] = ''):
    ''' Undocumented, consider contributing <https://developer.blender.org/> __.

    :param id_type: ID Type
    :type id_type: typing.Union[str, int]
    :param old_id: Old ID, Old ID to replace
    :type old_id: typing.Union[str, int]
    :param new_id: New ID, New ID to remap all selected IDs' users to
    :type new_id: typing.Union[str, int]
    '''

    pass


def item_activate(extend: bool = False,
                  extend_range: bool = False,
                  deselect_all: bool = False):
    ''' Handle mouse clicks to select and activate items

    :param extend: Extend, Extend selection for activation
    :type extend: bool
    :param extend_range: Extend Range, Select a range from active element
    :type extend_range: bool
    :param deselect_all: Deselect On Nothing, Deselect all when nothing under the cursor
    :type deselect_all: bool
    '''

    pass


def item_drag_drop():
    ''' Drag and drop element to another place

    '''

    pass


def item_openclose(all: bool = False):
    ''' Toggle whether item under cursor is enabled or closed

    :param all: All, Close or open all items
    :type all: bool
    '''

    pass


def item_rename(use_active: bool = False):
    ''' Rename the active element

    :param use_active: Use Active, Rename the active item, rather than the one the mouse is over
    :type use_active: bool
    '''

    pass


def keyingset_add_selected():
    ''' Add selected items (blue-gray rows) to active Keying Set

    '''

    pass


def keyingset_remove_selected():
    ''' Remove selected items (blue-gray rows) from active Keying Set

    '''

    pass


def lib_operation(type: typing.Union[str, int] = 'DELETE'):
    ''' Undocumented, consider contributing <https://developer.blender.org/> __.

    :param type: Library Operation * DELETE Delete -- Delete this library and all its items. Warning: No undo. * RELOCATE Relocate -- Select a new path for this library, and reload all its data. * RELOAD Reload -- Reload all data from this library.
    :type type: typing.Union[str, int]
    '''

    pass


def lib_relocate():
    ''' Relocate the library under cursor

    '''

    pass


def liboverride_operation(
        type: typing.Union[str, int] = 'OVERRIDE_LIBRARY_CREATE_HIERARCHY',
        selection_set: typing.Union[str, int] = 'SELECTED'):
    ''' Create, reset or clear library override hierarchies

    :param type: Library Override Operation * OVERRIDE_LIBRARY_CREATE_HIERARCHY Make -- Create a local override of the selected linked data-blocks, and their hierarchy of dependencies. * OVERRIDE_LIBRARY_RESET Reset -- Reset the selected local overrides to their linked references values. * OVERRIDE_LIBRARY_CLEAR_SINGLE Clear -- Delete the selected local overrides and relink their usages to the linked data-blocks if possible, else reset them and mark them as non editable.
    :type type: typing.Union[str, int]
    :param selection_set: Selection Set, Over which part of the tree items to apply the operation * SELECTED Selected -- Apply the operation over selected data-blocks only. * CONTENT Content -- Apply the operation over content of the selected items only (the data-blocks in their sub-tree). * SELECTED_AND_CONTENT Selected & Content -- Apply the operation over selected data-blocks and all their dependencies.
    :type selection_set: typing.Union[str, int]
    '''

    pass


def liboverride_troubleshoot_operation(
        type: typing.Union[str, int] = 'OVERRIDE_LIBRARY_RESYNC_HIERARCHY',
        selection_set: typing.Union[str, int] = 'SELECTED'):
    ''' Advanced operations over library override to help fix broken hierarchies

    :param type: Library Override Troubleshoot Operation * OVERRIDE_LIBRARY_RESYNC_HIERARCHY Resync -- Rebuild the selected local overrides from their linked references, as well as their hierarchies of dependencies. * OVERRIDE_LIBRARY_RESYNC_HIERARCHY_ENFORCE Resync Enforce -- Rebuild the selected local overrides from their linked references, as well as their hierarchies of dependencies, enforcing these hierarchies to match the linked data (i.e. ignoring existing overrides on data-blocks pointer properties). * OVERRIDE_LIBRARY_DELETE_HIERARCHY Delete -- Delete the selected local overrides (including their hierarchies of override dependencies) and relink their usages to the linked data-blocks.
    :type type: typing.Union[str, int]
    :param selection_set: Selection Set, Over which part of the tree items to apply the operation * SELECTED Selected -- Apply the operation over selected data-blocks only. * CONTENT Content -- Apply the operation over content of the selected items only (the data-blocks in their sub-tree). * SELECTED_AND_CONTENT Selected & Content -- Apply the operation over selected data-blocks and all their dependencies.
    :type selection_set: typing.Union[str, int]
    '''

    pass


def material_drop():
    ''' Drag material to object in Outliner

    '''

    pass


def modifier_operation(type: typing.Union[str, int] = 'TOGVIS'):
    ''' Undocumented, consider contributing <https://developer.blender.org/> __.

    :param type: Modifier Operation
    :type type: typing.Union[str, int]
    '''

    pass


def object_operation(type: typing.Union[str, int] = 'SELECT'):
    ''' Undocumented, consider contributing <https://developer.blender.org/> __.

    :param type: Object Operation * SELECT Select. * DESELECT Deselect. * SELECT_HIERARCHY Select Hierarchy. * REMAP Remap Users -- Make all users of selected data-blocks to use instead a new chosen one. * RENAME Rename.
    :type type: typing.Union[str, int]
    '''

    pass


def operation():
    ''' Context menu for item operations

    '''

    pass


def orphans_purge(num_deleted: int = 0,
                  do_local_ids: bool = True,
                  do_linked_ids: bool = True,
                  do_recursive: bool = False):
    ''' Clear all orphaned data-blocks without any users from the file

    :type num_deleted: int
    :param do_local_ids: Local Data-blocks, Include unused local data-blocks into deletion
    :type do_local_ids: bool
    :param do_linked_ids: Linked Data-blocks, Include unused linked data-blocks into deletion
    :type do_linked_ids: bool
    :param do_recursive: Recursive Delete, Recursively check for indirectly unused data-blocks, ensuring that no orphaned data-blocks remain after execution
    :type do_recursive: bool
    '''

    pass


def parent_clear():
    ''' Drag to clear parent in Outliner

    '''

    pass


def parent_drop():
    ''' Drag to parent in Outliner

    '''

    pass


def scene_drop():
    ''' Drag object to scene in Outliner

    '''

    pass


def scene_operation(type: typing.Union[str, int] = 'DELETE'):
    ''' Context menu for scene operations

    :param type: Scene Operation
    :type type: typing.Union[str, int]
    '''

    pass


def scroll_page(up: bool = False):
    ''' Scroll page up or down

    :param up: Up, Scroll up one page
    :type up: bool
    '''

    pass


def select_all(action: typing.Union[str, int] = 'TOGGLE'):
    ''' Toggle the Outliner selection of items

    :param action: Action, Selection action to execute * TOGGLE Toggle -- Toggle selection for all elements. * SELECT Select -- Select all elements. * DESELECT Deselect -- Deselect all elements. * INVERT Invert -- Invert selection of all elements.
    :type action: typing.Union[str, int]
    '''

    pass


def select_box(tweak: bool = False,
               xmin: int = 0,
               xmax: int = 0,
               ymin: int = 0,
               ymax: int = 0,
               wait_for_input: bool = True,
               mode: typing.Union[str, int] = 'SET'):
    ''' Use box selection to select tree elements

    :param tweak: Tweak, Tweak gesture from empty space for box selection
    :type tweak: bool
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
    :param mode: Mode * SET Set -- Set a new selection. * ADD Extend -- Extend existing selection. * SUB Subtract -- Subtract existing selection.
    :type mode: typing.Union[str, int]
    '''

    pass


def select_walk(direction: typing.Union[str, int] = 'UP',
                extend: bool = False,
                toggle_all: bool = False):
    ''' Use walk navigation to select tree elements

    :param direction: Walk Direction, Select/Deselect element in this direction
    :type direction: typing.Union[str, int]
    :param extend: Extend, Extend selection on walk
    :type extend: bool
    :param toggle_all: Toggle All, Toggle open/close hierarchy
    :type toggle_all: bool
    '''

    pass


def show_active():
    ''' Open up the tree and adjust the view so that the active object is shown centered

    '''

    pass


def show_hierarchy():
    ''' Open all object entries and close all others

    '''

    pass


def show_one_level(open: bool = True):
    ''' Expand/collapse all entries by one level

    :param open: Open, Expand all entries one level deep
    :type open: bool
    '''

    pass


def unhide_all():
    ''' Unhide all objects and collections

    '''

    pass
