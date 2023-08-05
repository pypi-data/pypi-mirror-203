import sys
import typing
import mathutils
import bpy.types


def align(axis: typing.Union[int, str] = 'ALIGN_AUTO'):
    ''' Align selected UV vertices to an axis

    :param axis: Axis, Axis to align UV locations on * ALIGN_S Straighten -- Align UVs along the line defined by the endpoints. * ALIGN_T Straighten X -- Align UVs along the line defined by the endpoints along the X axis. * ALIGN_U Straighten Y -- Align UVs along the line defined by the endpoints along the Y axis. * ALIGN_AUTO Align Auto -- Automatically choose the axis on which there is most alignment already. * ALIGN_X Align X -- Align UVs on X axis. * ALIGN_Y Align Y -- Align UVs on Y axis.
    :type axis: typing.Union[int, str]
    '''

    pass


def align_rotation(method: typing.Union[int, str] = 'AUTO',
                   axis: typing.Union[int, str] = 'X'):
    ''' Align the UV island's rotation :File: startup/bl_operators/uvcalc_transform.py\:275 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/uvcalc_transform.py#L275> __

    :param method: Method, Method to calculate rotation angle * AUTO Auto -- Align from all edges. * EDGE Edge -- Only selected edges. * GEOMETRY Geometry -- Align to Geometry axis.
    :type method: typing.Union[int, str]
    :param axis: Axis, Axis to align to * X X -- X axis. * Y Y -- Y axis. * Z Z -- Z axis.
    :type axis: typing.Union[int, str]
    '''

    pass


def average_islands_scale(scale_uv: bool = False, shear: bool = False):
    ''' Average the size of separate UV islands, based on their area in 3D space

    :param scale_uv: Non-Uniform, Scale U and V independently
    :type scale_uv: bool
    :param shear: Shear, Reduce shear within islands
    :type shear: bool
    '''

    pass


def copy():
    ''' Copy selected UV vertices

    '''

    pass


def cube_project(cube_size: float = 1.0,
                 correct_aspect: bool = True,
                 clip_to_bounds: bool = False,
                 scale_to_bounds: bool = False):
    ''' Project the UV vertices of the mesh over the six faces of a cube

    :param cube_size: Cube Size, Size of the cube to project on
    :type cube_size: float
    :param correct_aspect: Correct Aspect, Map UVs taking image aspect ratio into account
    :type correct_aspect: bool
    :param clip_to_bounds: Clip to Bounds, Clip UV coordinates to bounds after unwrapping
    :type clip_to_bounds: bool
    :param scale_to_bounds: Scale to Bounds, Scale UV coordinates to bounds after unwrapping
    :type scale_to_bounds: bool
    '''

    pass


def cursor_set(location: 'mathutils.Vector' = (0.0, 0.0)):
    ''' Set 2D cursor location

    :param location: Location, Cursor location in normalized (0.0 to 1.0) coordinates
    :type location: 'mathutils.Vector'
    '''

    pass


def cylinder_project(direction: typing.Union[int, str] = 'VIEW_ON_EQUATOR',
                     align: typing.Union[int, str] = 'POLAR_ZX',
                     pole: typing.Union[int, str] = 'PINCH',
                     seam: bool = False,
                     radius: float = 1.0,
                     correct_aspect: bool = True,
                     clip_to_bounds: bool = False,
                     scale_to_bounds: bool = False):
    ''' Project the UV vertices of the mesh over the curved wall of a cylinder

    :param direction: Direction, Direction of the sphere or cylinder * VIEW_ON_EQUATOR View on Equator -- 3D view is on the equator. * VIEW_ON_POLES View on Poles -- 3D view is on the poles. * ALIGN_TO_OBJECT Align to Object -- Align according to object transform.
    :type direction: typing.Union[int, str]
    :param align: Align, How to determine rotation around the pole * POLAR_ZX Polar ZX -- Polar 0 is X. * POLAR_ZY Polar ZY -- Polar 0 is Y.
    :type align: typing.Union[int, str]
    :param pole: Pole, How to handle faces at the poles * PINCH Pinch -- UVs are pinched at the poles. * FAN Fan -- UVs are fanned at the poles.
    :type pole: typing.Union[int, str]
    :param seam: Preserve Seams, Separate projections by islands isolated by seams
    :type seam: bool
    :param radius: Radius, Radius of the sphere or cylinder
    :type radius: float
    :param correct_aspect: Correct Aspect, Map UVs taking image aspect ratio into account
    :type correct_aspect: bool
    :param clip_to_bounds: Clip to Bounds, Clip UV coordinates to bounds after unwrapping
    :type clip_to_bounds: bool
    :param scale_to_bounds: Scale to Bounds, Scale UV coordinates to bounds after unwrapping
    :type scale_to_bounds: bool
    '''

    pass


def follow_active_quads(mode: typing.Union[int, str] = 'LENGTH_AVERAGE'):
    ''' Follow UVs from active quads along continuous face loops :File: startup/bl_operators/uvcalc_follow_active.py\:257 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/uvcalc_follow_active.py#L257> __

    :param mode: Edge Length Mode, Method to space UV edge loops * EVEN Even -- Space all UVs evenly. * LENGTH Length -- Average space UVs edge length of each loop. * LENGTH_AVERAGE Length Average -- Average space UVs edge length of each loop.
    :type mode: typing.Union[int, str]
    '''

    pass


def hide(unselected: bool = False):
    ''' Hide (un)selected UV vertices

    :param unselected: Unselected, Hide unselected rather than selected
    :type unselected: bool
    '''

    pass


def lightmap_pack(PREF_CONTEXT: typing.Union[int, str] = 'SEL_FACES',
                  PREF_PACK_IN_ONE: bool = True,
                  PREF_NEW_UVLAYER: bool = False,
                  PREF_APPLY_IMAGE: bool = False,
                  PREF_IMG_PX_SIZE: int = 512,
                  PREF_BOX_DIV: int = 12,
                  PREF_MARGIN_DIV: float = 0.1):
    ''' Pack each face's UVs into the UV bounds :File: startup/bl_operators/uvcalc_lightmap.py\:661 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/uvcalc_lightmap.py#L661> __

    :param PREF_CONTEXT: Selection * SEL_FACES Selected Faces -- Space all UVs evenly. * ALL_FACES All Faces -- Average space UVs edge length of each loop.
    :type PREF_CONTEXT: typing.Union[int, str]
    :param PREF_PACK_IN_ONE: Share Texture Space, Objects share texture space, map all objects into a single UV map
    :type PREF_PACK_IN_ONE: bool
    :param PREF_NEW_UVLAYER: New UV Map, Create a new UV map for every mesh packed
    :type PREF_NEW_UVLAYER: bool
    :param PREF_APPLY_IMAGE: New Image, Assign new images for every mesh (only one if Share Texture Space is enabled)
    :type PREF_APPLY_IMAGE: bool
    :param PREF_IMG_PX_SIZE: Image Size, Width and height for the new image
    :type PREF_IMG_PX_SIZE: int
    :param PREF_BOX_DIV: Pack Quality, Quality of the packing. Higher values will be slower but waste less space
    :type PREF_BOX_DIV: int
    :param PREF_MARGIN_DIV: Margin, Size of the margin as a division of the UV
    :type PREF_MARGIN_DIV: float
    '''

    pass


def mark_seam(clear: bool = False):
    ''' Mark selected UV edges as seams

    :param clear: Clear Seams, Clear instead of marking seams
    :type clear: bool
    '''

    pass


def minimize_stretch(fill_holes: bool = True,
                     blend: float = 0.0,
                     iterations: int = 0):
    ''' Reduce UV stretching by relaxing angles

    :param fill_holes: Fill Holes, Virtually fill holes in mesh before unwrapping, to better avoid overlaps and preserve symmetry
    :type fill_holes: bool
    :param blend: Blend, Blend factor between stretch minimized and original
    :type blend: float
    :param iterations: Iterations, Number of iterations to run, 0 is unlimited when run interactively
    :type iterations: int
    '''

    pass


def pack_islands(udim_source: typing.Union[int, str] = 'CLOSEST_UDIM',
                 rotate: bool = True,
                 margin_method: typing.Union[int, str] = 'SCALED',
                 margin: float = 0.001,
                 shape_method: typing.Union[int, str] = 'CONCAVE'):
    ''' Transform all islands so that they fill up the UV/UDIM space as much as possible

    :param udim_source: Pack to * CLOSEST_UDIM Closest UDIM -- Pack islands to closest UDIM. * ACTIVE_UDIM Active UDIM -- Pack islands to active UDIM image tile or UDIM grid tile where 2D cursor is located. * ORIGINAL_AABB Original bounding box -- Pack to starting bounding box of islands.
    :type udim_source: typing.Union[int, str]
    :param rotate: Rotate, Rotate islands for best fit
    :type rotate: bool
    :param margin_method: Margin Method * SCALED Scaled -- Use scale of existing UVs to multiply margin. * ADD Add -- Just add the margin, ignoring any UV scale. * FRACTION Fraction -- Specify a precise fraction of final UV output.
    :type margin_method: typing.Union[int, str]
    :param margin: Margin, Space between islands
    :type margin: float
    :param shape_method: Shape Method * CONCAVE Exact shape (Concave) -- Uses exact geometry. * CONVEX Boundary shape (Convex) -- Uses convex hull. * AABB Bounding box -- Uses bounding boxes.
    :type shape_method: typing.Union[int, str]
    '''

    pass


def paste():
    ''' Paste selected UV vertices

    '''

    pass


def pin(clear: bool = False):
    ''' Set/clear selected UV vertices as anchored between multiple unwrap operations

    :param clear: Clear, Clear pinning for the selection instead of setting it
    :type clear: bool
    '''

    pass


def project_from_view(orthographic: bool = False,
                      camera_bounds: bool = True,
                      correct_aspect: bool = True,
                      clip_to_bounds: bool = False,
                      scale_to_bounds: bool = False):
    ''' Project the UV vertices of the mesh as seen in current 3D view

    :param orthographic: Orthographic, Use orthographic projection
    :type orthographic: bool
    :param camera_bounds: Camera Bounds, Map UVs to the camera region taking resolution and aspect into account
    :type camera_bounds: bool
    :param correct_aspect: Correct Aspect, Map UVs taking image aspect ratio into account
    :type correct_aspect: bool
    :param clip_to_bounds: Clip to Bounds, Clip UV coordinates to bounds after unwrapping
    :type clip_to_bounds: bool
    :param scale_to_bounds: Scale to Bounds, Scale UV coordinates to bounds after unwrapping
    :type scale_to_bounds: bool
    '''

    pass


def randomize_uv_transform(random_seed: int = 0,
                           use_loc: bool = True,
                           loc: 'mathutils.Vector' = (0.0, 0.0),
                           use_rot: bool = True,
                           rot: float = 0.0,
                           use_scale: bool = True,
                           scale_even: bool = False,
                           scale: typing.List[float] = (1.0, 1.0)):
    ''' Randomize the UV island's location, rotation, and scale :File: startup/bl_operators/uvcalc_transform.py\:449 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/uvcalc_transform.py#L449> __

    :param random_seed: Random Seed, Seed value for the random generator
    :type random_seed: int
    :param use_loc: Randomize Location, Randomize the location values
    :type use_loc: bool
    :param loc: Location, Maximum distance the objects can spread over each axis
    :type loc: 'mathutils.Vector'
    :param use_rot: Randomize Rotation, Randomize the rotation value
    :type use_rot: bool
    :param rot: Rotation, Maximum rotation
    :type rot: float
    :param use_scale: Randomize Scale, Randomize the scale values
    :type use_scale: bool
    :param scale_even: Scale Even, Use the same scale value for both axes
    :type scale_even: bool
    :param scale: Scale, Maximum scale randomization over each axis
    :type scale: typing.List[float]
    '''

    pass


def remove_doubles(threshold: float = 0.02, use_unselected: bool = False):
    ''' Selected UV vertices that are within a radius of each other are welded together

    :param threshold: Merge Distance, Maximum distance between welded vertices
    :type threshold: float
    :param use_unselected: Unselected, Merge selected to other unselected vertices
    :type use_unselected: bool
    '''

    pass


def reset():
    ''' Reset UV projection

    '''

    pass


def reveal(select: bool = True):
    ''' Reveal all hidden UV vertices

    :param select: Select
    :type select: bool
    '''

    pass


def rip(mirror: bool = False,
        release_confirm: bool = False,
        use_accurate: bool = False,
        location: 'mathutils.Vector' = (0.0, 0.0)):
    ''' Rip selected vertices or a selected region

    :param mirror: Mirror Editing
    :type mirror: bool
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :type release_confirm: bool
    :param use_accurate: Accurate, Use accurate transformation
    :type use_accurate: bool
    :param location: Location, Mouse location in normalized coordinates, 0.0 to 1.0 is within the image bounds
    :type location: 'mathutils.Vector'
    '''

    pass


def rip_move(UV_OT_rip=None, TRANSFORM_OT_translate=None):
    ''' Unstitch UVs and move the result

    :param UV_OT_rip: UV Rip, Rip selected vertices or a selected region
    :param TRANSFORM_OT_translate: Move, Move selected items
    '''

    pass


def seams_from_islands(mark_seams: bool = True, mark_sharp: bool = False):
    ''' Set mesh seams according to island setup in the UV editor

    :param mark_seams: Mark Seams, Mark boundary edges as seams
    :type mark_seams: bool
    :param mark_sharp: Mark Sharp, Mark boundary edges as sharp
    :type mark_sharp: bool
    '''

    pass


def select(extend: bool = False,
           deselect: bool = False,
           toggle: bool = False,
           deselect_all: bool = False,
           select_passthrough: bool = False,
           location: 'mathutils.Vector' = (0.0, 0.0)):
    ''' Select UV vertices

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
    :param location: Location, Mouse location in normalized coordinates, 0.0 to 1.0 is within the image bounds
    :type location: 'mathutils.Vector'
    '''

    pass


def select_all(action: typing.Union[int, str] = 'TOGGLE'):
    ''' Change selection of all UV vertices

    :param action: Action, Selection action to execute * TOGGLE Toggle -- Toggle selection for all elements. * SELECT Select -- Select all elements. * DESELECT Deselect -- Deselect all elements. * INVERT Invert -- Invert selection of all elements.
    :type action: typing.Union[int, str]
    '''

    pass


def select_box(pinned: bool = False,
               xmin: int = 0,
               xmax: int = 0,
               ymin: int = 0,
               ymax: int = 0,
               wait_for_input: bool = True,
               mode: typing.Union[int, str] = 'SET'):
    ''' Select UV vertices using box selection

    :param pinned: Pinned, Border select pinned UVs only
    :type pinned: bool
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
    :type mode: typing.Union[int, str]
    '''

    pass


def select_circle(x: int = 0,
                  y: int = 0,
                  radius: int = 25,
                  wait_for_input: bool = True,
                  mode: typing.Union[int, str] = 'SET'):
    ''' Select UV vertices using circle selection

    :param x: X
    :type x: int
    :param y: Y
    :type y: int
    :param radius: Radius
    :type radius: int
    :param wait_for_input: Wait for Input
    :type wait_for_input: bool
    :param mode: Mode * SET Set -- Set a new selection. * ADD Extend -- Extend existing selection. * SUB Subtract -- Subtract existing selection.
    :type mode: typing.Union[int, str]
    '''

    pass


def select_edge_ring(extend: bool = False,
                     location: 'mathutils.Vector' = (0.0, 0.0)):
    ''' Select an edge ring of connected UV vertices

    :param extend: Extend, Extend selection rather than clearing the existing selection
    :type extend: bool
    :param location: Location, Mouse location in normalized coordinates, 0.0 to 1.0 is within the image bounds
    :type location: 'mathutils.Vector'
    '''

    pass


def select_lasso(path: typing.Union[
        typing.Dict[str, 'bpy.types.OperatorMousePath'], typing.
        List['bpy.types.OperatorMousePath'], 'bpy_prop_collection'] = None,
                 mode: typing.Union[int, str] = 'SET'):
    ''' Select UVs using lasso selection

    :param path: Path
    :type path: typing.Union[typing.Dict[str, 'bpy.types.OperatorMousePath'], typing.List['bpy.types.OperatorMousePath'], 'bpy_prop_collection']
    :param mode: Mode * SET Set -- Set a new selection. * ADD Extend -- Extend existing selection. * SUB Subtract -- Subtract existing selection.
    :type mode: typing.Union[int, str]
    '''

    pass


def select_less():
    ''' Deselect UV vertices at the boundary of each selection region

    '''

    pass


def select_linked():
    ''' Select all UV vertices linked to the active UV map

    '''

    pass


def select_linked_pick(extend: bool = False,
                       deselect: bool = False,
                       location: 'mathutils.Vector' = (0.0, 0.0)):
    ''' Select all UV vertices linked under the mouse

    :param extend: Extend, Extend selection rather than clearing the existing selection
    :type extend: bool
    :param deselect: Deselect, Deselect linked UV vertices rather than selecting them
    :type deselect: bool
    :param location: Location, Mouse location in normalized coordinates, 0.0 to 1.0 is within the image bounds
    :type location: 'mathutils.Vector'
    '''

    pass


def select_loop(extend: bool = False,
                location: 'mathutils.Vector' = (0.0, 0.0)):
    ''' Select a loop of connected UV vertices

    :param extend: Extend, Extend selection rather than clearing the existing selection
    :type extend: bool
    :param location: Location, Mouse location in normalized coordinates, 0.0 to 1.0 is within the image bounds
    :type location: 'mathutils.Vector'
    '''

    pass


def select_mode(type: typing.Union[int, str] = 'VERTEX'):
    ''' Change UV selection mode

    :param type: Type
    :type type: typing.Union[int, str]
    '''

    pass


def select_more():
    ''' Select more UV vertices connected to initial selection

    '''

    pass


def select_overlap(extend: bool = False):
    ''' Select all UV faces which overlap each other

    :param extend: Extend, Extend selection rather than clearing the existing selection
    :type extend: bool
    '''

    pass


def select_pinned():
    ''' Select all pinned UV vertices

    '''

    pass


def select_similar(type: typing.Union[int, str] = 'PIN',
                   compare: typing.Union[int, str] = 'EQUAL',
                   threshold: float = 0.0):
    ''' Select similar UVs by property types

    :param type: Type
    :type type: typing.Union[int, str]
    :param compare: Compare
    :type compare: typing.Union[int, str]
    :param threshold: Threshold
    :type threshold: float
    '''

    pass


def select_split():
    ''' Select only entirely selected faces

    '''

    pass


def shortest_path_pick(use_face_step: bool = False,
                       use_topology_distance: bool = False,
                       use_fill: bool = False,
                       skip: int = 0,
                       nth: int = 1,
                       offset: int = 0,
                       object_index: int = -1,
                       index: int = -1):
    ''' Select shortest path between two selections

    :param use_face_step: Face Stepping, Traverse connected faces (includes diagonals and edge-rings)
    :type use_face_step: bool
    :param use_topology_distance: Topology Distance, Find the minimum number of steps, ignoring spatial distance
    :type use_topology_distance: bool
    :param use_fill: Fill Region, Select all paths between the source/destination elements
    :type use_fill: bool
    :param skip: Deselected, Number of deselected elements in the repetitive sequence
    :type skip: int
    :param nth: Selected, Number of selected elements in the repetitive sequence
    :type nth: int
    :param offset: Offset, Offset from the starting point
    :type offset: int
    :type object_index: int
    :type index: int
    '''

    pass


def shortest_path_select(use_face_step: bool = False,
                         use_topology_distance: bool = False,
                         use_fill: bool = False,
                         skip: int = 0,
                         nth: int = 1,
                         offset: int = 0):
    ''' Selected shortest path between two vertices/edges/faces

    :param use_face_step: Face Stepping, Traverse connected faces (includes diagonals and edge-rings)
    :type use_face_step: bool
    :param use_topology_distance: Topology Distance, Find the minimum number of steps, ignoring spatial distance
    :type use_topology_distance: bool
    :param use_fill: Fill Region, Select all paths between the source/destination elements
    :type use_fill: bool
    :param skip: Deselected, Number of deselected elements in the repetitive sequence
    :type skip: int
    :param nth: Selected, Number of selected elements in the repetitive sequence
    :type nth: int
    :param offset: Offset, Offset from the starting point
    :type offset: int
    '''

    pass


def smart_project(angle_limit: float = 1.15192,
                  margin_method: typing.Union[int, str] = 'SCALED',
                  island_margin: float = 0.0,
                  area_weight: float = 0.0,
                  correct_aspect: bool = True,
                  scale_to_bounds: bool = False):
    ''' Projection unwraps the selected faces of mesh objects

    :param angle_limit: Angle Limit, Lower for more projection groups, higher for less distortion
    :type angle_limit: float
    :param margin_method: Margin Method * SCALED Scaled -- Use scale of existing UVs to multiply margin. * ADD Add -- Just add the margin, ignoring any UV scale. * FRACTION Fraction -- Specify a precise fraction of final UV output.
    :type margin_method: typing.Union[int, str]
    :param island_margin: Island Margin, Margin to reduce bleed from adjacent islands
    :type island_margin: float
    :param area_weight: Area Weight, Weight projection's vector by faces with larger areas
    :type area_weight: float
    :param correct_aspect: Correct Aspect, Map UVs taking image aspect ratio into account
    :type correct_aspect: bool
    :param scale_to_bounds: Scale to Bounds, Scale UV coordinates to bounds after unwrapping
    :type scale_to_bounds: bool
    '''

    pass


def snap_cursor(target: typing.Union[int, str] = 'PIXELS'):
    ''' Snap cursor to target type

    :param target: Target, Target to snap the selected UVs to
    :type target: typing.Union[int, str]
    '''

    pass


def snap_selected(target: typing.Union[int, str] = 'PIXELS'):
    ''' Snap selected UV vertices to target type

    :param target: Target, Target to snap the selected UVs to
    :type target: typing.Union[int, str]
    '''

    pass


def sphere_project(direction: typing.Union[int, str] = 'VIEW_ON_EQUATOR',
                   align: typing.Union[int, str] = 'POLAR_ZX',
                   pole: typing.Union[int, str] = 'PINCH',
                   seam: bool = False,
                   correct_aspect: bool = True,
                   clip_to_bounds: bool = False,
                   scale_to_bounds: bool = False):
    ''' Project the UV vertices of the mesh over the curved surface of a sphere

    :param direction: Direction, Direction of the sphere or cylinder * VIEW_ON_EQUATOR View on Equator -- 3D view is on the equator. * VIEW_ON_POLES View on Poles -- 3D view is on the poles. * ALIGN_TO_OBJECT Align to Object -- Align according to object transform.
    :type direction: typing.Union[int, str]
    :param align: Align, How to determine rotation around the pole * POLAR_ZX Polar ZX -- Polar 0 is X. * POLAR_ZY Polar ZY -- Polar 0 is Y.
    :type align: typing.Union[int, str]
    :param pole: Pole, How to handle faces at the poles * PINCH Pinch -- UVs are pinched at the poles. * FAN Fan -- UVs are fanned at the poles.
    :type pole: typing.Union[int, str]
    :param seam: Preserve Seams, Separate projections by islands isolated by seams
    :type seam: bool
    :param correct_aspect: Correct Aspect, Map UVs taking image aspect ratio into account
    :type correct_aspect: bool
    :param clip_to_bounds: Clip to Bounds, Clip UV coordinates to bounds after unwrapping
    :type clip_to_bounds: bool
    :param scale_to_bounds: Scale to Bounds, Scale UV coordinates to bounds after unwrapping
    :type scale_to_bounds: bool
    '''

    pass


def stitch(
        use_limit: bool = False,
        snap_islands: bool = True,
        limit: float = 0.01,
        static_island: int = 0,
        active_object_index: int = 0,
        midpoint_snap: bool = False,
        clear_seams: bool = True,
        mode: typing.Union[int, str] = 'VERTEX',
        stored_mode: typing.Union[int, str] = 'VERTEX',
        selection: typing.Union[
            typing.Dict[str, 'bpy.types.SelectedUvElement'], typing.
            List['bpy.types.SelectedUvElement'], 'bpy_prop_collection'] = None,
        objects_selection_count: typing.List[int] = (0, 0, 0, 0, 0, 0)):
    ''' Stitch selected UV vertices by proximity

    :param use_limit: Use Limit, Stitch UVs within a specified limit distance
    :type use_limit: bool
    :param snap_islands: Snap Islands, Snap islands together (on edge stitch mode, rotates the islands too)
    :type snap_islands: bool
    :param limit: Limit, Limit distance in normalized coordinates
    :type limit: float
    :param static_island: Static Island, Island that stays in place when stitching islands
    :type static_island: int
    :param active_object_index: Active Object, Index of the active object
    :type active_object_index: int
    :param midpoint_snap: Snap at Midpoint, UVs are stitched at midpoint instead of at static island
    :type midpoint_snap: bool
    :param clear_seams: Clear Seams, Clear seams of stitched edges
    :type clear_seams: bool
    :param mode: Operation Mode, Use vertex or edge stitching
    :type mode: typing.Union[int, str]
    :param stored_mode: Stored Operation Mode, Use vertex or edge stitching
    :type stored_mode: typing.Union[int, str]
    :param selection: Selection
    :type selection: typing.Union[typing.Dict[str, 'bpy.types.SelectedUvElement'], typing.List['bpy.types.SelectedUvElement'], 'bpy_prop_collection']
    :param objects_selection_count: Objects Selection Count
    :type objects_selection_count: typing.List[int]
    '''

    pass


def unwrap(method: typing.Union[int, str] = 'ANGLE_BASED',
           fill_holes: bool = True,
           correct_aspect: bool = True,
           use_subsurf_data: bool = False,
           margin_method: typing.Union[int, str] = 'SCALED',
           margin: float = 0.001):
    ''' Unwrap the mesh of the object being edited

    :param method: Method, Unwrapping method (Angle Based usually gives better results than Conformal, while being somewhat slower)
    :type method: typing.Union[int, str]
    :param fill_holes: Fill Holes, Virtually fill holes in mesh before unwrapping, to better avoid overlaps and preserve symmetry
    :type fill_holes: bool
    :param correct_aspect: Correct Aspect, Map UVs taking image aspect ratio into account
    :type correct_aspect: bool
    :param use_subsurf_data: Use Subdivision Surface, Map UVs taking vertex position after Subdivision Surface modifier has been applied
    :type use_subsurf_data: bool
    :param margin_method: Margin Method * SCALED Scaled -- Use scale of existing UVs to multiply margin. * ADD Add -- Just add the margin, ignoring any UV scale. * FRACTION Fraction -- Specify a precise fraction of final UV output.
    :type margin_method: typing.Union[int, str]
    :param margin: Margin, Space between islands
    :type margin: float
    '''

    pass


def weld():
    ''' Weld selected UV vertices together

    '''

    pass
