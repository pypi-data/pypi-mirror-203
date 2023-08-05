import sys
import typing
import mathutils
import bpy.types


def add_simple_uvs():
    ''' Add cube map UVs on mesh

    '''

    pass


def add_texture_paint_slot(type: typing.Union[int, str] = 'BASE_COLOR',
                           slot_type: typing.Union[int, str] = 'IMAGE',
                           name: str = "Untitled",
                           color: typing.List[float] = (0.0, 0.0, 0.0, 1.0),
                           width: int = 1024,
                           height: int = 1024,
                           alpha: bool = True,
                           generated_type: typing.Union[int, str] = 'BLANK',
                           float: bool = False,
                           domain: typing.Union[int, str] = 'POINT',
                           data_type: typing.Union[int, str] = 'COLOR'):
    ''' Add a paint slot

    :param type: Material Layer Type, Material layer type of new paint slot
    :type type: typing.Union[int, str]
    :param slot_type: Slot Type, Type of new paint slot
    :type slot_type: typing.Union[int, str]
    :param name: Name, Name for new paint slot source
    :type name: str
    :param color: Color, Default fill color
    :type color: typing.List[float]
    :param width: Width, Image width
    :type width: int
    :param height: Height, Image height
    :type height: int
    :param alpha: Alpha, Create an image with an alpha channel
    :type alpha: bool
    :param generated_type: Generated Type, Fill the image with a grid for UV map testing
    :type generated_type: typing.Union[int, str]
    :param float: 32-bit Float, Create image with 32-bit floating-point bit depth
    :type float: bool
    :param domain: Domain, Type of element that attribute is stored on
    :type domain: typing.Union[int, str]
    :param data_type: Data Type, Type of data stored in attribute
    :type data_type: typing.Union[int, str]
    '''

    pass


def brush_colors_flip():
    ''' Swap primary and secondary brush colors

    '''

    pass


def brush_select(sculpt_tool: typing.Union[int, str] = 'DRAW',
                 vertex_tool: typing.Union[int, str] = 'DRAW',
                 weight_tool: typing.Union[int, str] = 'DRAW',
                 image_tool: typing.Union[int, str] = 'DRAW',
                 gpencil_tool: typing.Union[int, str] = 'DRAW',
                 gpencil_vertex_tool: typing.Union[int, str] = 'DRAW',
                 gpencil_sculpt_tool: typing.Union[int, str] = 'SMOOTH',
                 gpencil_weight_tool: typing.Union[int, str] = 'WEIGHT',
                 curves_sculpt_tool: typing.Union[int, str] = 'COMB',
                 toggle: bool = False,
                 create_missing: bool = False):
    ''' Select a paint mode's brush by tool type

    :param sculpt_tool: sculpt_tool
    :type sculpt_tool: typing.Union[int, str]
    :param vertex_tool: vertex_tool
    :type vertex_tool: typing.Union[int, str]
    :param weight_tool: weight_tool
    :type weight_tool: typing.Union[int, str]
    :param image_tool: image_tool
    :type image_tool: typing.Union[int, str]
    :param gpencil_tool: gpencil_tool
    :type gpencil_tool: typing.Union[int, str]
    :param gpencil_vertex_tool: gpencil_vertex_tool
    :type gpencil_vertex_tool: typing.Union[int, str]
    :param gpencil_sculpt_tool: gpencil_sculpt_tool
    :type gpencil_sculpt_tool: typing.Union[int, str]
    :param gpencil_weight_tool: gpencil_weight_tool
    :type gpencil_weight_tool: typing.Union[int, str]
    :param curves_sculpt_tool: curves_sculpt_tool
    :type curves_sculpt_tool: typing.Union[int, str]
    :param toggle: Toggle, Toggle between two brushes rather than cycling
    :type toggle: bool
    :param create_missing: Create Missing, If the requested brush type does not exist, create a new brush
    :type create_missing: bool
    '''

    pass


def face_select_all(action: typing.Union[int, str] = 'TOGGLE'):
    ''' Change selection for all faces

    :param action: Action, Selection action to execute * TOGGLE Toggle -- Toggle selection for all elements. * SELECT Select -- Select all elements. * DESELECT Deselect -- Deselect all elements. * INVERT Invert -- Invert selection of all elements.
    :type action: typing.Union[int, str]
    '''

    pass


def face_select_hide(unselected: bool = False):
    ''' Hide selected faces

    :param unselected: Unselected, Hide unselected rather than selected objects
    :type unselected: bool
    '''

    pass


def face_select_less(face_step: bool = True):
    ''' Deselect Faces connected to existing selection

    :param face_step: Face Step, Also deselect faces that only touch on a corner
    :type face_step: bool
    '''

    pass


def face_select_linked():
    ''' Select linked faces

    '''

    pass


def face_select_linked_pick(deselect: bool = False):
    ''' Select linked faces under the cursor

    :param deselect: Deselect, Deselect rather than select items
    :type deselect: bool
    '''

    pass


def face_select_more(face_step: bool = True):
    ''' Select Faces connected to existing selection

    :param face_step: Face Step, Also select faces that only touch on a corner
    :type face_step: bool
    '''

    pass


def face_vert_reveal(select: bool = True):
    ''' Reveal hidden faces and vertices

    :param select: Select, Specifies whether the newly revealed geometry should be selected
    :type select: bool
    '''

    pass


def grab_clone(delta: 'mathutils.Vector' = (0.0, 0.0)):
    ''' Move the clone source image

    :param delta: Delta, Delta offset of clone image in 0.0 to 1.0 coordinates
    :type delta: 'mathutils.Vector'
    '''

    pass


def hide_show(action: typing.Union[int, str] = 'HIDE',
              area: typing.Union[int, str] = 'INSIDE',
              xmin: int = 0,
              xmax: int = 0,
              ymin: int = 0,
              ymax: int = 0,
              wait_for_input: bool = True):
    ''' Hide/show some vertices

    :param action: Action, Whether to hide or show vertices * HIDE Hide -- Hide vertices. * SHOW Show -- Show vertices.
    :type action: typing.Union[int, str]
    :param area: Area, Which vertices to hide or show * OUTSIDE Outside -- Hide or show vertices outside the selection. * INSIDE Inside -- Hide or show vertices inside the selection. * ALL All -- Hide or show all vertices. * MASKED Masked -- Hide or show vertices that are masked (minimum mask value of 0.5).
    :type area: typing.Union[int, str]
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


def image_from_view(filepath: str = ""):
    ''' Make an image from biggest 3D view for reprojection

    :param filepath: File Path, Name of the file
    :type filepath: str
    '''

    pass


def image_paint(stroke: typing.Union[
        typing.Dict[str, 'bpy.types.OperatorStrokeElement'], typing.
        List['bpy.types.OperatorStrokeElement'], 'bpy_prop_collection'] = None,
                mode: typing.Union[int, str] = 'NORMAL'):
    ''' Paint a stroke into the image

    :param stroke: Stroke
    :type stroke: typing.Union[typing.Dict[str, 'bpy.types.OperatorStrokeElement'], typing.List['bpy.types.OperatorStrokeElement'], 'bpy_prop_collection']
    :param mode: Stroke Mode, Action taken when a paint stroke is made * NORMAL Regular -- Apply brush normally. * INVERT Invert -- Invert action of brush for duration of stroke. * SMOOTH Smooth -- Switch brush to smooth mode for duration of stroke.
    :type mode: typing.Union[int, str]
    '''

    pass


def mask_box_gesture(xmin: int = 0,
                     xmax: int = 0,
                     ymin: int = 0,
                     ymax: int = 0,
                     wait_for_input: bool = True,
                     use_front_faces_only: bool = False,
                     use_limit_to_segment: bool = False,
                     mode: typing.Union[int, str] = 'VALUE',
                     value: float = 1.0):
    ''' Add mask within the box as you move the brush

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
    :param use_front_faces_only: Front Faces Only, Affect only faces facing towards the view
    :type use_front_faces_only: bool
    :param use_limit_to_segment: Limit to Segment, Apply the gesture action only to the area that is contained within the segment without extending its effect to the entire line
    :type use_limit_to_segment: bool
    :param mode: Mode * VALUE Value -- Set mask to the level specified by the 'value' property. * VALUE_INVERSE Value Inverted -- Set mask to the level specified by the inverted 'value' property. * INVERT Invert -- Invert the mask.
    :type mode: typing.Union[int, str]
    :param value: Value, Mask level to use when mode is 'Value'; zero means no masking and one is fully masked
    :type value: float
    '''

    pass


def mask_flood_fill(mode: typing.Union[int, str] = 'VALUE',
                    value: float = 0.0):
    ''' Fill the whole mask with a given value, or invert its values

    :param mode: Mode * VALUE Value -- Set mask to the level specified by the 'value' property. * VALUE_INVERSE Value Inverted -- Set mask to the level specified by the inverted 'value' property. * INVERT Invert -- Invert the mask.
    :type mode: typing.Union[int, str]
    :param value: Value, Mask level to use when mode is 'Value'; zero means no masking and one is fully masked
    :type value: float
    '''

    pass


def mask_lasso_gesture(path: typing.Union[
        typing.Dict[str, 'bpy.types.OperatorMousePath'], typing.
        List['bpy.types.OperatorMousePath'], 'bpy_prop_collection'] = None,
                       use_front_faces_only: bool = False,
                       use_limit_to_segment: bool = False,
                       mode: typing.Union[int, str] = 'VALUE',
                       value: float = 1.0):
    ''' Add mask within the lasso as you move the brush

    :param path: Path
    :type path: typing.Union[typing.Dict[str, 'bpy.types.OperatorMousePath'], typing.List['bpy.types.OperatorMousePath'], 'bpy_prop_collection']
    :param use_front_faces_only: Front Faces Only, Affect only faces facing towards the view
    :type use_front_faces_only: bool
    :param use_limit_to_segment: Limit to Segment, Apply the gesture action only to the area that is contained within the segment without extending its effect to the entire line
    :type use_limit_to_segment: bool
    :param mode: Mode * VALUE Value -- Set mask to the level specified by the 'value' property. * VALUE_INVERSE Value Inverted -- Set mask to the level specified by the inverted 'value' property. * INVERT Invert -- Invert the mask.
    :type mode: typing.Union[int, str]
    :param value: Value, Mask level to use when mode is 'Value'; zero means no masking and one is fully masked
    :type value: float
    '''

    pass


def mask_line_gesture(xstart: int = 0,
                      xend: int = 0,
                      ystart: int = 0,
                      yend: int = 0,
                      flip: bool = False,
                      cursor: int = 5,
                      use_front_faces_only: bool = False,
                      use_limit_to_segment: bool = False,
                      mode: typing.Union[int, str] = 'VALUE',
                      value: float = 1.0):
    ''' Add mask to the right of a line as you move the brush

    :param xstart: X Start
    :type xstart: int
    :param xend: X End
    :type xend: int
    :param ystart: Y Start
    :type ystart: int
    :param yend: Y End
    :type yend: int
    :param flip: Flip
    :type flip: bool
    :param cursor: Cursor, Mouse cursor style to use during the modal operator
    :type cursor: int
    :param use_front_faces_only: Front Faces Only, Affect only faces facing towards the view
    :type use_front_faces_only: bool
    :param use_limit_to_segment: Limit to Segment, Apply the gesture action only to the area that is contained within the segment without extending its effect to the entire line
    :type use_limit_to_segment: bool
    :param mode: Mode * VALUE Value -- Set mask to the level specified by the 'value' property. * VALUE_INVERSE Value Inverted -- Set mask to the level specified by the inverted 'value' property. * INVERT Invert -- Invert the mask.
    :type mode: typing.Union[int, str]
    :param value: Value, Mask level to use when mode is 'Value'; zero means no masking and one is fully masked
    :type value: float
    '''

    pass


def project_image(image: typing.Union[int, str] = ''):
    ''' Project an edited render from the active camera back onto the object

    :param image: Image
    :type image: typing.Union[int, str]
    '''

    pass


def sample_color(location: typing.List[int] = (0, 0),
                 merged: bool = False,
                 palette: bool = False):
    ''' Use the mouse to sample a color in the image

    :param location: Location
    :type location: typing.List[int]
    :param merged: Sample Merged, Sample the output display color
    :type merged: bool
    :param palette: Add to Palette
    :type palette: bool
    '''

    pass


def texture_paint_toggle():
    ''' Toggle texture paint mode in 3D view

    '''

    pass


def vert_select_all(action: typing.Union[int, str] = 'TOGGLE'):
    ''' Change selection for all vertices

    :param action: Action, Selection action to execute * TOGGLE Toggle -- Toggle selection for all elements. * SELECT Select -- Select all elements. * DESELECT Deselect -- Deselect all elements. * INVERT Invert -- Invert selection of all elements.
    :type action: typing.Union[int, str]
    '''

    pass


def vert_select_hide(unselected: bool = False):
    ''' Hide selected vertices

    :param unselected: Unselected, Hide unselected rather than selected vertices
    :type unselected: bool
    '''

    pass


def vert_select_less(face_step: bool = True):
    ''' Deselect Vertices connected to existing selection

    :param face_step: Face Step, Also deselect faces that only touch on a corner
    :type face_step: bool
    '''

    pass


def vert_select_linked():
    ''' Select linked vertices

    '''

    pass


def vert_select_linked_pick(select: bool = True):
    ''' Select linked vertices under the cursor

    :param select: Select, Whether to select or deselect linked vertices under the cursor
    :type select: bool
    '''

    pass


def vert_select_more(face_step: bool = True):
    ''' Select Vertices connected to existing selection

    :param face_step: Face Step, Also select faces that only touch on a corner
    :type face_step: bool
    '''

    pass


def vert_select_ungrouped(extend: bool = False):
    ''' Select vertices without a group

    :param extend: Extend, Extend the selection
    :type extend: bool
    '''

    pass


def vertex_color_brightness_contrast(brightness: float = 0.0,
                                     contrast: float = 0.0):
    ''' Adjust vertex color brightness/contrast

    :param brightness: Brightness
    :type brightness: float
    :param contrast: Contrast
    :type contrast: float
    '''

    pass


def vertex_color_dirt(blur_strength: float = 1.0,
                      blur_iterations: int = 1,
                      clean_angle: float = 3.14159,
                      dirt_angle: float = 0.0,
                      dirt_only: bool = False,
                      normalize: bool = True):
    ''' Generate a dirt map gradient based on cavity :File: startup/bl_operators/vertexpaint_dirt.py\:179 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/vertexpaint_dirt.py#L179> __

    :param blur_strength: Blur Strength, Blur strength per iteration
    :type blur_strength: float
    :param blur_iterations: Blur Iterations, Number of times to blur the colors (higher blurs more)
    :type blur_iterations: int
    :param clean_angle: Highlight Angle, Less than 90 limits the angle used in the tonal range
    :type clean_angle: float
    :param dirt_angle: Dirt Angle, Less than 90 limits the angle used in the tonal range
    :type dirt_angle: float
    :param dirt_only: Dirt Only, Don't calculate cleans for convex areas
    :type dirt_only: bool
    :param normalize: Normalize, Normalize the colors, increasing the contrast
    :type normalize: bool
    '''

    pass


def vertex_color_from_weight():
    ''' Convert active weight into gray scale vertex colors

    '''

    pass


def vertex_color_hsv(h: float = 0.5, s: float = 1.0, v: float = 1.0):
    ''' Adjust vertex color HSV values

    :param h: Hue
    :type h: float
    :param s: Saturation
    :type s: float
    :param v: Value
    :type v: float
    '''

    pass


def vertex_color_invert():
    ''' Invert RGB values

    '''

    pass


def vertex_color_levels(offset: float = 0.0, gain: float = 1.0):
    ''' Adjust levels of vertex colors

    :param offset: Offset, Value to add to colors
    :type offset: float
    :param gain: Gain, Value to multiply colors by
    :type gain: float
    '''

    pass


def vertex_color_set():
    ''' Fill the active vertex color layer with the current paint color

    '''

    pass


def vertex_color_smooth():
    ''' Smooth colors across vertices

    '''

    pass


def vertex_paint(stroke: typing.Union[
        typing.Dict[str, 'bpy.types.OperatorStrokeElement'], typing.
        List['bpy.types.OperatorStrokeElement'], 'bpy_prop_collection'] = None,
                 mode: typing.Union[int, str] = 'NORMAL'):
    ''' Paint a stroke in the active color attribute layer

    :param stroke: Stroke
    :type stroke: typing.Union[typing.Dict[str, 'bpy.types.OperatorStrokeElement'], typing.List['bpy.types.OperatorStrokeElement'], 'bpy_prop_collection']
    :param mode: Stroke Mode, Action taken when a paint stroke is made * NORMAL Regular -- Apply brush normally. * INVERT Invert -- Invert action of brush for duration of stroke. * SMOOTH Smooth -- Switch brush to smooth mode for duration of stroke.
    :type mode: typing.Union[int, str]
    '''

    pass


def vertex_paint_toggle():
    ''' Toggle the vertex paint mode in 3D view

    '''

    pass


def weight_from_bones(type: typing.Union[int, str] = 'AUTOMATIC'):
    ''' Set the weights of the groups matching the attached armature's selected bones, using the distance between the vertices and the bones

    :param type: Type, Method to use for assigning weights * AUTOMATIC Automatic -- Automatic weights from bones. * ENVELOPES From Envelopes -- Weights from envelopes with user defined radius.
    :type type: typing.Union[int, str]
    '''

    pass


def weight_gradient(type: typing.Union[int, str] = 'LINEAR',
                    xstart: int = 0,
                    xend: int = 0,
                    ystart: int = 0,
                    yend: int = 0,
                    flip: bool = False,
                    cursor: int = 5):
    ''' Draw a line to apply a weight gradient to selected vertices

    :param type: Type
    :type type: typing.Union[int, str]
    :param xstart: X Start
    :type xstart: int
    :param xend: X End
    :type xend: int
    :param ystart: Y Start
    :type ystart: int
    :param yend: Y End
    :type yend: int
    :param flip: Flip
    :type flip: bool
    :param cursor: Cursor, Mouse cursor style to use during the modal operator
    :type cursor: int
    '''

    pass


def weight_paint(stroke: typing.Union[
        typing.Dict[str, 'bpy.types.OperatorStrokeElement'], typing.
        List['bpy.types.OperatorStrokeElement'], 'bpy_prop_collection'] = None,
                 mode: typing.Union[int, str] = 'NORMAL'):
    ''' Paint a stroke in the current vertex group's weights

    :param stroke: Stroke
    :type stroke: typing.Union[typing.Dict[str, 'bpy.types.OperatorStrokeElement'], typing.List['bpy.types.OperatorStrokeElement'], 'bpy_prop_collection']
    :param mode: Stroke Mode, Action taken when a paint stroke is made * NORMAL Regular -- Apply brush normally. * INVERT Invert -- Invert action of brush for duration of stroke. * SMOOTH Smooth -- Switch brush to smooth mode for duration of stroke.
    :type mode: typing.Union[int, str]
    '''

    pass


def weight_paint_toggle():
    ''' Toggle weight paint mode in 3D view

    '''

    pass


def weight_sample():
    ''' Use the mouse to sample a weight in the 3D view

    '''

    pass


def weight_sample_group(group: typing.Union[int, str] = ''):
    ''' Select one of the vertex groups available under current mouse position

    :param group: Group, Vertex group to set as active
    :type group: typing.Union[int, str]
    '''

    pass


def weight_set():
    ''' Fill the active vertex group with the current paint weight

    '''

    pass
