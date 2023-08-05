import sys
import typing
import bl_operators.node
import bpy.types


def add_collection(name: str = "", session_uuid: int = 0):
    ''' Add a collection info node to the current node editor

    :param name: Name, Name of the data-block to use by the operator
    :type name: str
    :param session_uuid: Session UUID, Session UUID of the data-block to use by the operator
    :type session_uuid: int
    '''

    pass


def add_file(filepath: str = "",
             hide_props_region: bool = True,
             check_existing: bool = False,
             filter_blender: bool = False,
             filter_backup: bool = False,
             filter_image: bool = True,
             filter_movie: bool = True,
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
             relative_path: bool = True,
             show_multiview: bool = False,
             use_multiview: bool = False,
             display_type: typing.Union[str, int] = 'DEFAULT',
             sort_method: typing.Union[str, int] = '',
             name: str = "",
             session_uuid: int = 0):
    ''' Add a file node to the current node editor

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
    :param relative_path: Relative Path, Select the file relative to the blend file
    :type relative_path: bool
    :param show_multiview: Enable Multi-View
    :type show_multiview: bool
    :param use_multiview: Use Multi-View
    :type use_multiview: bool
    :param display_type: Display Type * DEFAULT Default -- Automatically determine display type for files. * LIST_VERTICAL Short List -- Display files as short list. * LIST_HORIZONTAL Long List -- Display files as a detailed list. * THUMBNAIL Thumbnails -- Display files as thumbnails.
    :type display_type: typing.Union[str, int]
    :param sort_method: File sorting mode
    :type sort_method: typing.Union[str, int]
    :param name: Name, Name of the data-block to use by the operator
    :type name: str
    :param session_uuid: Session UUID, Session UUID of the data-block to use by the operator
    :type session_uuid: int
    '''

    pass


def add_group(name: str = "", session_uuid: int = 0):
    ''' Add an existing node group to the current node editor

    :param name: Name, Name of the data-block to use by the operator
    :type name: str
    :param session_uuid: Session UUID, Session UUID of the data-block to use by the operator
    :type session_uuid: int
    '''

    pass


def add_group_asset():
    ''' Add a node group asset to the active node tree

    '''

    pass


def add_mask(name: str = "", session_uuid: int = 0):
    ''' Add a mask node to the current node editor

    :param name: Name, Name of the data-block to use by the operator
    :type name: str
    :param session_uuid: Session UUID, Session UUID of the data-block to use by the operator
    :type session_uuid: int
    '''

    pass


def add_node(type: str = "",
             use_transform: bool = False,
             settings: typing.
             Union[typing.Dict[str, 'bl_operators.node.NodeSetting'], typing.
                   List['bl_operators.node.NodeSetting'],
                   'bpy_prop_collection'] = None):
    ''' Add a node to the active tree :File: startup/bl_operators/node.py\:115 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/node.py#L115> __

    :param type: Node Type, Node type
    :type type: str
    :param use_transform: Use Transform, Start transform operator after inserting the node
    :type use_transform: bool
    :param settings: Settings, Settings to be applied on the newly created node
    :type settings: typing.Union[typing.Dict[str, 'bl_operators.node.NodeSetting'], typing.List['bl_operators.node.NodeSetting'], 'bpy_prop_collection']
    '''

    pass


def add_object(name: str = "", session_uuid: int = 0):
    ''' Add an object info node to the current node editor

    :param name: Name, Name of the data-block to use by the operator
    :type name: str
    :param session_uuid: Session UUID, Session UUID of the data-block to use by the operator
    :type session_uuid: int
    '''

    pass


def add_reroute(path: typing.Union[
        typing.Dict[str, 'bpy.types.OperatorMousePath'], typing.
        List['bpy.types.OperatorMousePath'], 'bpy_prop_collection'] = None,
                cursor: int = 8):
    ''' Add a reroute node

    :param path: Path
    :type path: typing.Union[typing.Dict[str, 'bpy.types.OperatorMousePath'], typing.List['bpy.types.OperatorMousePath'], 'bpy_prop_collection']
    :param cursor: Cursor
    :type cursor: int
    '''

    pass


def add_search(use_transform: bool = True):
    ''' Search for nodes and add one to the active tree

    :param use_transform: Use Transform, Start moving the node after adding it
    :type use_transform: bool
    '''

    pass


def attach():
    ''' Attach active node to a frame

    '''

    pass


def backimage_fit():
    ''' Fit the background image to the view

    '''

    pass


def backimage_move():
    ''' Move node backdrop

    '''

    pass


def backimage_sample():
    ''' Use mouse to sample background image

    '''

    pass


def backimage_zoom(factor: float = 1.2):
    ''' Zoom in/out the background image

    :param factor: Factor
    :type factor: float
    '''

    pass


def clear_viewer_border():
    ''' Clear the boundaries for viewer operations

    '''

    pass


def clipboard_copy():
    ''' Copies selected nodes to the clipboard

    '''

    pass


def clipboard_paste(offset: typing.List[float] = (0.0, 0.0)):
    ''' Pastes nodes from the clipboard to the active node tree

    :param offset: Location, The 2D view location for the center of the new nodes, or unchanged if not set
    :type offset: typing.List[float]
    '''

    pass


def collapse_hide_unused_toggle():
    ''' Toggle collapsed nodes and hide unused sockets :File: startup/bl_operators/node.py\:165 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/node.py#L165> __

    '''

    pass


def cryptomatte_layer_add():
    ''' Add a new input layer to a Cryptomatte node

    '''

    pass


def cryptomatte_layer_remove():
    ''' Remove layer from a Cryptomatte node

    '''

    pass


def deactivate_viewer():
    ''' Deactivate selected viewer node in geometry nodes

    '''

    pass


def delete():
    ''' Remove selected nodes

    '''

    pass


def delete_reconnect():
    ''' Remove nodes and reconnect nodes as if deletion was muted

    '''

    pass


def detach():
    ''' Detach selected nodes from parents

    '''

    pass


def detach_translate_attach(NODE_OT_detach=None,
                            TRANSFORM_OT_translate=None,
                            NODE_OT_attach=None):
    ''' Detach nodes, move and attach to frame

    :param NODE_OT_detach: Detach Nodes, Detach selected nodes from parents
    :param TRANSFORM_OT_translate: Move, Move selected items
    :param NODE_OT_attach: Attach Nodes, Attach active node to a frame
    '''

    pass


def duplicate(keep_inputs: bool = False, linked: bool = True):
    ''' Duplicate selected nodes

    :param keep_inputs: Keep Inputs, Keep the input links to duplicated nodes
    :type keep_inputs: bool
    :param linked: Linked, Duplicate node but not node trees, linking to the original data
    :type linked: bool
    '''

    pass


def duplicate_move(NODE_OT_duplicate=None, NODE_OT_translate_attach=None):
    ''' Duplicate selected nodes and move them

    :param NODE_OT_duplicate: Duplicate Nodes, Duplicate selected nodes
    :param NODE_OT_translate_attach: Move and Attach, Move nodes and attach to frame
    '''

    pass


def duplicate_move_keep_inputs(NODE_OT_duplicate=None,
                               NODE_OT_translate_attach=None):
    ''' Duplicate selected nodes keeping input links and move them

    :param NODE_OT_duplicate: Duplicate Nodes, Duplicate selected nodes
    :param NODE_OT_translate_attach: Move and Attach, Move nodes and attach to frame
    '''

    pass


def duplicate_move_linked(NODE_OT_duplicate=None,
                          NODE_OT_translate_attach=None):
    ''' Duplicate selected nodes, but not their node trees, and move them

    :param NODE_OT_duplicate: Duplicate Nodes, Duplicate selected nodes
    :param NODE_OT_translate_attach: Move and Attach, Move nodes and attach to frame
    '''

    pass


def find_node():
    ''' Search for a node by name and focus and select it

    '''

    pass


def group_edit(exit: bool = False):
    ''' Edit node group

    :param exit: Exit
    :type exit: bool
    '''

    pass


def group_insert():
    ''' Insert selected nodes into a node group

    '''

    pass


def group_make():
    ''' Make group from selected nodes

    '''

    pass


def group_separate(type: typing.Union[str, int] = 'COPY'):
    ''' Separate selected nodes from the node group

    :param type: Type * COPY Copy -- Copy to parent node tree, keep group intact. * MOVE Move -- Move to parent node tree, remove from group.
    :type type: typing.Union[str, int]
    '''

    pass


def group_ungroup():
    ''' Ungroup selected nodes

    '''

    pass


def hide_socket_toggle():
    ''' Toggle unused node socket display

    '''

    pass


def hide_toggle():
    ''' Toggle hiding of selected nodes

    '''

    pass


def insert_offset():
    ''' Automatically offset nodes on insertion

    '''

    pass


def join():
    ''' Attach selected nodes to a new common frame

    '''

    pass


def link(detach: bool = False,
         drag_start: typing.List[float] = (0.0, 0.0),
         inside_padding: float = 2.0,
         outside_padding: float = 0.0,
         speed_ramp: float = 1.0,
         max_speed: float = 26.0,
         delay: float = 0.5,
         zoom_influence: float = 0.5):
    ''' Use the mouse to create a link between two nodes

    :param detach: Detach, Detach and redirect existing links
    :type detach: bool
    :param drag_start: Drag Start, The position of the mouse cursor at the start of the operation
    :type drag_start: typing.List[float]
    :param inside_padding: Inside Padding, Inside distance in UI units from the edge of the region within which to start panning
    :type inside_padding: float
    :param outside_padding: Outside Padding, Outside distance in UI units from the edge of the region at which to stop panning
    :type outside_padding: float
    :param speed_ramp: Speed Ramp, Width of the zone in UI units where speed increases with distance from the edge
    :type speed_ramp: float
    :param max_speed: Max Speed, Maximum speed in UI units per second
    :type max_speed: float
    :param delay: Delay, Delay in seconds before maximum speed is reached
    :type delay: float
    :param zoom_influence: Zoom Influence, Influence of the zoom factor on scroll speed
    :type zoom_influence: float
    '''

    pass


def link_make(replace: bool = False):
    ''' Makes a link between selected output in input sockets

    :param replace: Replace, Replace socket connections with the new links
    :type replace: bool
    '''

    pass


def link_viewer():
    ''' Link to viewer node

    '''

    pass


def links_cut(path: typing.Union[
        typing.Dict[str, 'bpy.types.OperatorMousePath'], typing.
        List['bpy.types.OperatorMousePath'], 'bpy_prop_collection'] = None,
              cursor: int = 12):
    ''' Use the mouse to cut (remove) some links

    :param path: Path
    :type path: typing.Union[typing.Dict[str, 'bpy.types.OperatorMousePath'], typing.List['bpy.types.OperatorMousePath'], 'bpy_prop_collection']
    :param cursor: Cursor
    :type cursor: int
    '''

    pass


def links_detach():
    ''' Remove all links to selected nodes, and try to connect neighbor nodes together

    '''

    pass


def links_mute(path: typing.Union[
        typing.Dict[str, 'bpy.types.OperatorMousePath'], typing.
        List['bpy.types.OperatorMousePath'], 'bpy_prop_collection'] = None,
               cursor: int = 35):
    ''' Use the mouse to mute links

    :param path: Path
    :type path: typing.Union[typing.Dict[str, 'bpy.types.OperatorMousePath'], typing.List['bpy.types.OperatorMousePath'], 'bpy_prop_collection']
    :param cursor: Cursor
    :type cursor: int
    '''

    pass


def move_detach_links(NODE_OT_links_detach=None,
                      TRANSFORM_OT_translate=None,
                      NODE_OT_insert_offset=None):
    ''' Move a node to detach links

    :param NODE_OT_links_detach: Detach Links, Remove all links to selected nodes, and try to connect neighbor nodes together
    :param TRANSFORM_OT_translate: Move, Move selected items
    :param NODE_OT_insert_offset: Insert Offset, Automatically offset nodes on insertion
    '''

    pass


def move_detach_links_release(NODE_OT_links_detach=None,
                              NODE_OT_translate_attach=None):
    ''' Move a node to detach links

    :param NODE_OT_links_detach: Detach Links, Remove all links to selected nodes, and try to connect neighbor nodes together
    :param NODE_OT_translate_attach: Move and Attach, Move nodes and attach to frame
    '''

    pass


def mute_toggle():
    ''' Toggle muting of selected nodes

    '''

    pass


def new_geometry_node_group_assign():
    ''' Create a new geometry node group and assign it to the active modifier :File: startup/bl_operators/geometry_nodes.py\:229 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/geometry_nodes.py#L229> __

    '''

    pass


def new_geometry_nodes_modifier():
    ''' Create a new modifier with a new geometry node group :File: startup/bl_operators/geometry_nodes.py\:207 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/geometry_nodes.py#L207> __

    '''

    pass


def new_node_tree(type: typing.Union[str, int] = '', name: str = "NodeTree"):
    ''' Create a new node tree

    :param type: Tree Type
    :type type: typing.Union[str, int]
    :param name: Name
    :type name: str
    '''

    pass


def node_color_preset_add(name: str = "",
                          remove_name: bool = False,
                          remove_active: bool = False):
    ''' Add or remove a Node Color Preset :File: startup/bl_operators/presets.py\:73 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/presets.py#L73> __

    :param name: Name, Name of the preset, used to make the path name
    :type name: str
    :param remove_name: remove_name
    :type remove_name: bool
    :param remove_active: remove_active
    :type remove_active: bool
    '''

    pass


def node_copy_color():
    ''' Copy color to all selected nodes

    '''

    pass


def options_toggle():
    ''' Toggle option buttons display for selected nodes

    '''

    pass


def output_file_add_socket(file_path: str = "Image"):
    ''' Add a new input to a file output node

    :param file_path: File Path, Subpath of the output file
    :type file_path: str
    '''

    pass


def output_file_move_active_socket(direction: typing.Union[str, int] = 'DOWN'):
    ''' Move the active input of a file output node up or down the list

    :param direction: Direction
    :type direction: typing.Union[str, int]
    '''

    pass


def output_file_remove_active_socket():
    ''' Remove the active input from a file output node

    '''

    pass


def parent_set():
    ''' Attach selected nodes

    '''

    pass


def preview_toggle():
    ''' Toggle preview display for selected nodes

    '''

    pass


def read_viewlayers():
    ''' Read all render layers of all used scenes

    '''

    pass


def render_changed():
    ''' Render current scene, when input node's layer has been changed

    '''

    pass


def resize():
    ''' Resize a node

    '''

    pass


def select(extend: bool = False,
           deselect: bool = False,
           toggle: bool = False,
           deselect_all: bool = False,
           select_passthrough: bool = False,
           location: typing.List[int] = (0, 0),
           socket_select: bool = False,
           clear_viewer: bool = False):
    ''' Select the node under the cursor

    :param extend: Extend, Extend selection instead of deselecting everything first
    :type extend: bool
    :param deselect: Deselect, Remove from selection
    :type deselect: bool
    :param toggle: Toggle Selection, Toggle the selection
    :type toggle: bool
    :param deselect_all: Deselect On Nothing, Deselect all when nothing under the cursor
    :type deselect_all: bool
    :param select_passthrough: Only Select Unselected, Ignore the select action when the element is already selected
    :type select_passthrough: bool
    :param location: Location, Mouse location
    :type location: typing.List[int]
    :param socket_select: Socket Select
    :type socket_select: bool
    :param clear_viewer: Clear Viewer, Deactivate geometry nodes viewer when clicking in empty space
    :type clear_viewer: bool
    '''

    pass


def select_all(action: typing.Union[str, int] = 'TOGGLE'):
    ''' (De)select all nodes

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
    ''' Use box selection to select nodes

    :param tweak: Tweak, Only activate when mouse is not over a node (useful for tweak gesture)
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


def select_circle(x: int = 0,
                  y: int = 0,
                  radius: int = 25,
                  wait_for_input: bool = True,
                  mode: typing.Union[str, int] = 'SET'):
    ''' Use circle selection to select nodes

    :param x: X
    :type x: int
    :param y: Y
    :type y: int
    :param radius: Radius
    :type radius: int
    :param wait_for_input: Wait for Input
    :type wait_for_input: bool
    :param mode: Mode * SET Set -- Set a new selection. * ADD Extend -- Extend existing selection. * SUB Subtract -- Subtract existing selection.
    :type mode: typing.Union[str, int]
    '''

    pass


def select_grouped(extend: bool = False,
                   type: typing.Union[str, int] = 'TYPE'):
    ''' Select nodes with similar properties

    :param extend: Extend, Extend selection instead of deselecting everything first
    :type extend: bool
    :param type: Type
    :type type: typing.Union[str, int]
    '''

    pass


def select_lasso(
        tweak: bool = False,
        path: typing.Union[
            typing.Dict[str, 'bpy.types.OperatorMousePath'], typing.
            List['bpy.types.OperatorMousePath'], 'bpy_prop_collection'] = None,
        mode: typing.Union[str, int] = 'SET'):
    ''' Select nodes using lasso selection

    :param tweak: Tweak, Only activate when mouse is not over a node (useful for tweak gesture)
    :type tweak: bool
    :param path: Path
    :type path: typing.Union[typing.Dict[str, 'bpy.types.OperatorMousePath'], typing.List['bpy.types.OperatorMousePath'], 'bpy_prop_collection']
    :param mode: Mode * SET Set -- Set a new selection. * ADD Extend -- Extend existing selection. * SUB Subtract -- Subtract existing selection.
    :type mode: typing.Union[str, int]
    '''

    pass


def select_link_viewer(NODE_OT_select=None, NODE_OT_link_viewer=None):
    ''' Select node and link it to a viewer node

    :param NODE_OT_select: Select, Select the node under the cursor
    :param NODE_OT_link_viewer: Link to Viewer Node, Link to viewer node
    '''

    pass


def select_linked_from():
    ''' Select nodes linked from the selected ones

    '''

    pass


def select_linked_to():
    ''' Select nodes linked to the selected ones

    '''

    pass


def select_same_type_step(prev: bool = False):
    ''' Activate and view same node type, step by step

    :param prev: Previous
    :type prev: bool
    '''

    pass


def shader_script_update():
    ''' Update shader script node with new sockets and options from the script

    '''

    pass


def switch_view_update():
    ''' Update views of selected node

    '''

    pass


def translate_attach(TRANSFORM_OT_translate=None,
                     NODE_OT_attach=None,
                     NODE_OT_insert_offset=None):
    ''' Move nodes and attach to frame

    :param TRANSFORM_OT_translate: Move, Move selected items
    :param NODE_OT_attach: Attach Nodes, Attach active node to a frame
    :param NODE_OT_insert_offset: Insert Offset, Automatically offset nodes on insertion
    '''

    pass


def translate_attach_remove_on_cancel(TRANSFORM_OT_translate=None,
                                      NODE_OT_attach=None,
                                      NODE_OT_insert_offset=None):
    ''' Move nodes and attach to frame

    :param TRANSFORM_OT_translate: Move, Move selected items
    :param NODE_OT_attach: Attach Nodes, Attach active node to a frame
    :param NODE_OT_insert_offset: Insert Offset, Automatically offset nodes on insertion
    '''

    pass


def tree_path_parent():
    ''' Go to parent node tree :File: startup/bl_operators/node.py\:195 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/node.py#L195> __

    '''

    pass


def tree_socket_add(in_out: typing.Union[str, int] = 'IN'):
    ''' Add an input or output to the active node tree

    :param in_out: Socket Type
    :type in_out: typing.Union[str, int]
    '''

    pass


def tree_socket_change_subtype(
        socket_subtype: typing.Union[str, int] = 'DEFAULT'):
    ''' Change the subtype of a socket of the active node tree

    :param socket_subtype: Socket Subtype
    :type socket_subtype: typing.Union[str, int]
    '''

    pass


def tree_socket_change_type(in_out: typing.Union[str, int] = 'IN',
                            socket_type: typing.Union[str, int] = 'DEFAULT'):
    ''' Change the type of an input or output of the active node tree

    :param in_out: Socket Type
    :type in_out: typing.Union[str, int]
    :param socket_type: Socket Type
    :type socket_type: typing.Union[str, int]
    '''

    pass


def tree_socket_move(direction: typing.Union[str, int] = 'UP',
                     in_out: typing.Union[str, int] = 'IN'):
    ''' Move a socket up or down in the active node tree's interface

    :param direction: Direction
    :type direction: typing.Union[str, int]
    :param in_out: Socket Type
    :type in_out: typing.Union[str, int]
    '''

    pass


def tree_socket_remove(in_out: typing.Union[str, int] = 'IN'):
    ''' Remove an input or output from the active node tree

    :param in_out: Socket Type
    :type in_out: typing.Union[str, int]
    '''

    pass


def view_all():
    ''' Resize view so you can see all nodes

    '''

    pass


def view_selected():
    ''' Resize view so you can see selected nodes

    '''

    pass


def viewer_border(xmin: int = 0,
                  xmax: int = 0,
                  ymin: int = 0,
                  ymax: int = 0,
                  wait_for_input: bool = True):
    ''' Set the boundaries for viewer operations

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
