import sys
import typing
import mathutils
import bpy.types


def add(radius: float = 1.0,
        type: typing.Union[str, int] = 'EMPTY',
        enter_editmode: bool = False,
        align: typing.Union[str, int] = 'WORLD',
        location: 'mathutils.Vector' = (0.0, 0.0, 0.0),
        rotation: 'mathutils.Euler' = (0.0, 0.0, 0.0),
        scale: 'mathutils.Vector' = (0.0, 0.0, 0.0)):
    ''' Add an object to the scene

    :param radius: Radius
    :type radius: float
    :param type: Type
    :type type: typing.Union[str, int]
    :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
    :type enter_editmode: bool
    :param align: Align, The alignment of the new object * WORLD World -- Align the new object to the world. * VIEW View -- Align the new object to the view. * CURSOR 3D Cursor -- Use the 3D cursor orientation for the new object.
    :type align: typing.Union[str, int]
    :param location: Location, Location for the newly added object
    :type location: 'mathutils.Vector'
    :param rotation: Rotation, Rotation for the newly added object
    :type rotation: 'mathutils.Euler'
    :param scale: Scale, Scale for the newly added object
    :type scale: 'mathutils.Vector'
    '''

    pass


def add_named(linked: bool = False,
              name: str = "",
              session_uuid: int = 0,
              matrix: 'mathutils.Matrix' = ((0.0, 0.0, 0.0, 0.0), (0.0, 0.0,
                                                                   0.0, 0.0),
                                            (0.0, 0.0, 0.0, 0.0), (0.0, 0.0,
                                                                   0.0, 0.0)),
              drop_x: int = 0,
              drop_y: int = 0):
    ''' Add named object

    :param linked: Linked, Duplicate object but not object data, linking to the original data
    :type linked: bool
    :param name: Name, Name of the data-block to use by the operator
    :type name: str
    :param session_uuid: Session UUID, Session UUID of the data-block to use by the operator
    :type session_uuid: int
    :param matrix: Matrix
    :type matrix: 'mathutils.Matrix'
    :param drop_x: Drop X, X-coordinate (screen space) to place the new object under
    :type drop_x: int
    :param drop_y: Drop Y, Y-coordinate (screen space) to place the new object under
    :type drop_y: int
    '''

    pass


def align(bb_quality: bool = True,
          align_mode: typing.Union[str, int] = 'OPT_2',
          relative_to: typing.Union[str, int] = 'OPT_4',
          align_axis: typing.Union[typing.Set[str], typing.Set[int]] = {}):
    ''' Align objects :File: startup/bl_operators/object_align.py\:391 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/object_align.py#L391> __

    :param bb_quality: High Quality, Enables high quality but slow calculation of the bounding box for perfect results on complex shape meshes with rotation/scale
    :type bb_quality: bool
    :param align_mode: Align Mode, Side of object to use for alignment
    :type align_mode: typing.Union[str, int]
    :param relative_to: Relative To, Reference location to align to * OPT_1 Scene Origin -- Use the scene origin as the position for the selected objects to align to. * OPT_2 3D Cursor -- Use the 3D cursor as the position for the selected objects to align to. * OPT_3 Selection -- Use the selected objects as the position for the selected objects to align to. * OPT_4 Active -- Use the active object as the position for the selected objects to align to.
    :type relative_to: typing.Union[str, int]
    :param align_axis: Align, Align to axis
    :type align_axis: typing.Union[typing.Set[str], typing.Set[int]]
    '''

    pass


def anim_transforms_to_deltas():
    ''' Convert object animation for normal transforms to delta transforms :File: startup/bl_operators/object.py\:773 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/object.py#L773> __

    '''

    pass


def armature_add(radius: float = 1.0,
                 enter_editmode: bool = False,
                 align: typing.Union[str, int] = 'WORLD',
                 location: 'mathutils.Vector' = (0.0, 0.0, 0.0),
                 rotation: 'mathutils.Euler' = (0.0, 0.0, 0.0),
                 scale: 'mathutils.Vector' = (0.0, 0.0, 0.0)):
    ''' Add an armature object to the scene

    :param radius: Radius
    :type radius: float
    :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
    :type enter_editmode: bool
    :param align: Align, The alignment of the new object * WORLD World -- Align the new object to the world. * VIEW View -- Align the new object to the view. * CURSOR 3D Cursor -- Use the 3D cursor orientation for the new object.
    :type align: typing.Union[str, int]
    :param location: Location, Location for the newly added object
    :type location: 'mathutils.Vector'
    :param rotation: Rotation, Rotation for the newly added object
    :type rotation: 'mathutils.Euler'
    :param scale: Scale, Scale for the newly added object
    :type scale: 'mathutils.Vector'
    '''

    pass


def assign_property_defaults(process_data: bool = True,
                             process_bones: bool = True):
    ''' Assign the current values of custom properties as their defaults, for use as part of the rest pose state in NLA track mixing :File: startup/bl_operators/object.py\:1153 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/object.py#L1153> __

    :param process_data: Process data properties
    :type process_data: bool
    :param process_bones: Process bone properties
    :type process_bones: bool
    '''

    pass


def bake(type: typing.Union[str, int] = 'COMBINED',
         pass_filter: typing.Union[typing.Set[str], typing.Set[int]] = {},
         filepath: str = "",
         width: int = 512,
         height: int = 512,
         margin: int = 16,
         margin_type: typing.Union[str, int] = 'EXTEND',
         use_selected_to_active: bool = False,
         max_ray_distance: float = 0.0,
         cage_extrusion: float = 0.0,
         cage_object: str = "",
         normal_space: typing.Union[str, int] = 'TANGENT',
         normal_r: typing.Union[str, int] = 'POS_X',
         normal_g: typing.Union[str, int] = 'POS_Y',
         normal_b: typing.Union[str, int] = 'POS_Z',
         target: typing.Union[str, int] = 'IMAGE_TEXTURES',
         save_mode: typing.Union[str, int] = 'INTERNAL',
         use_clear: bool = False,
         use_cage: bool = False,
         use_split_materials: bool = False,
         use_automatic_name: bool = False,
         uv_layer: str = ""):
    ''' Bake image textures of selected objects

    :param type: Type, Type of pass to bake, some of them may not be supported by the current render engine
    :type type: typing.Union[str, int]
    :param pass_filter: Pass Filter, Filter to combined, diffuse, glossy, transmission and subsurface passes
    :type pass_filter: typing.Union[typing.Set[str], typing.Set[int]]
    :param filepath: File Path, Image filepath to use when saving externally
    :type filepath: str
    :param width: Width, Horizontal dimension of the baking map (external only)
    :type width: int
    :param height: Height, Vertical dimension of the baking map (external only)
    :type height: int
    :param margin: Margin, Extends the baked result as a post process filter
    :type margin: int
    :param margin_type: Margin Type, Which algorithm to use to generate the margin
    :type margin_type: typing.Union[str, int]
    :param use_selected_to_active: Selected to Active, Bake shading on the surface of selected objects to the active object
    :type use_selected_to_active: bool
    :param max_ray_distance: Max Ray Distance, The maximum ray distance for matching points between the active and selected objects. If zero, there is no limit
    :type max_ray_distance: float
    :param cage_extrusion: Cage Extrusion, Inflate the active object by the specified distance for baking. This helps matching to points nearer to the outside of the selected object meshes
    :type cage_extrusion: float
    :param cage_object: Cage Object, Object to use as cage, instead of calculating the cage from the active object with cage extrusion
    :type cage_object: str
    :param normal_space: Normal Space, Choose normal space for baking
    :type normal_space: typing.Union[str, int]
    :param normal_r: R, Axis to bake in red channel
    :type normal_r: typing.Union[str, int]
    :param normal_g: G, Axis to bake in green channel
    :type normal_g: typing.Union[str, int]
    :param normal_b: B, Axis to bake in blue channel
    :type normal_b: typing.Union[str, int]
    :param target: Target, Where to output the baked map
    :type target: typing.Union[str, int]
    :param save_mode: Save Mode, Where to save baked image textures
    :type save_mode: typing.Union[str, int]
    :param use_clear: Clear, Clear images before baking (only for internal saving)
    :type use_clear: bool
    :param use_cage: Cage, Cast rays to active object from a cage
    :type use_cage: bool
    :param use_split_materials: Split Materials, Split baked maps per material, using material name in output file (external only)
    :type use_split_materials: bool
    :param use_automatic_name: Automatic Name, Automatically name the output file with the pass type
    :type use_automatic_name: bool
    :param uv_layer: UV Layer, UV layer to override active
    :type uv_layer: str
    '''

    pass


def bake_image():
    ''' Bake image textures of selected objects

    '''

    pass


def camera_add(enter_editmode: bool = False,
               align: typing.Union[str, int] = 'WORLD',
               location: 'mathutils.Vector' = (0.0, 0.0, 0.0),
               rotation: 'mathutils.Euler' = (0.0, 0.0, 0.0),
               scale: 'mathutils.Vector' = (0.0, 0.0, 0.0)):
    ''' Add a camera object to the scene

    :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
    :type enter_editmode: bool
    :param align: Align, The alignment of the new object * WORLD World -- Align the new object to the world. * VIEW View -- Align the new object to the view. * CURSOR 3D Cursor -- Use the 3D cursor orientation for the new object.
    :type align: typing.Union[str, int]
    :param location: Location, Location for the newly added object
    :type location: 'mathutils.Vector'
    :param rotation: Rotation, Rotation for the newly added object
    :type rotation: 'mathutils.Euler'
    :param scale: Scale, Scale for the newly added object
    :type scale: 'mathutils.Vector'
    '''

    pass


def clear_override_library():
    ''' Delete the selected local overrides and relink their usages to the linked data-blocks if possible, else reset them and mark them as non editable

    '''

    pass


def collection_add():
    ''' Add an object to a new collection

    '''

    pass


def collection_external_asset_drop(
        session_uuid: int = 0,
        align: typing.Union[str, int] = 'WORLD',
        location: 'mathutils.Vector' = (0.0, 0.0, 0.0),
        rotation: 'mathutils.Euler' = (0.0, 0.0, 0.0),
        scale: 'mathutils.Vector' = (0.0, 0.0, 0.0),
        use_instance: bool = True,
        drop_x: int = 0,
        drop_y: int = 0,
        collection: typing.Union[str, int] = ''):
    ''' Add the dragged collection to the scene

    :param session_uuid: Session UUID, Session UUID of the data-block to use by the operator
    :type session_uuid: int
    :param align: Align, The alignment of the new object * WORLD World -- Align the new object to the world. * VIEW View -- Align the new object to the view. * CURSOR 3D Cursor -- Use the 3D cursor orientation for the new object.
    :type align: typing.Union[str, int]
    :param location: Location, Location for the newly added object
    :type location: 'mathutils.Vector'
    :param rotation: Rotation, Rotation for the newly added object
    :type rotation: 'mathutils.Euler'
    :param scale: Scale, Scale for the newly added object
    :type scale: 'mathutils.Vector'
    :param use_instance: Instance, Add the dropped collection as collection instance
    :type use_instance: bool
    :param drop_x: Drop X, X-coordinate (screen space) to place the new object under
    :type drop_x: int
    :param drop_y: Drop Y, Y-coordinate (screen space) to place the new object under
    :type drop_y: int
    :param collection: Collection
    :type collection: typing.Union[str, int]
    '''

    pass


def collection_instance_add(name: str = "Collection",
                            collection: typing.Union[str, int] = '',
                            align: typing.Union[str, int] = 'WORLD',
                            location: 'mathutils.Vector' = (0.0, 0.0, 0.0),
                            rotation: 'mathutils.Euler' = (0.0, 0.0, 0.0),
                            scale: 'mathutils.Vector' = (0.0, 0.0, 0.0),
                            session_uuid: int = 0,
                            drop_x: int = 0,
                            drop_y: int = 0):
    ''' Add a collection instance

    :param name: Name, Collection name to add
    :type name: str
    :param collection: Collection
    :type collection: typing.Union[str, int]
    :param align: Align, The alignment of the new object * WORLD World -- Align the new object to the world. * VIEW View -- Align the new object to the view. * CURSOR 3D Cursor -- Use the 3D cursor orientation for the new object.
    :type align: typing.Union[str, int]
    :param location: Location, Location for the newly added object
    :type location: 'mathutils.Vector'
    :param rotation: Rotation, Rotation for the newly added object
    :type rotation: 'mathutils.Euler'
    :param scale: Scale, Scale for the newly added object
    :type scale: 'mathutils.Vector'
    :param session_uuid: Session UUID, Session UUID of the data-block to use by the operator
    :type session_uuid: int
    :param drop_x: Drop X, X-coordinate (screen space) to place the new object under
    :type drop_x: int
    :param drop_y: Drop Y, Y-coordinate (screen space) to place the new object under
    :type drop_y: int
    '''

    pass


def collection_link(collection: typing.Union[str, int] = ''):
    ''' Add an object to an existing collection

    :param collection: Collection
    :type collection: typing.Union[str, int]
    '''

    pass


def collection_objects_select():
    ''' Select all objects in collection

    '''

    pass


def collection_remove():
    ''' Remove the active object from this collection

    '''

    pass


def collection_unlink():
    ''' Unlink the collection from all objects

    '''

    pass


def constraint_add(type: typing.Union[str, int] = ''):
    ''' Add a constraint to the active object

    :param type: Type
    :type type: typing.Union[str, int]
    '''

    pass


def constraint_add_with_targets(type: typing.Union[str, int] = ''):
    ''' Add a constraint to the active object, with target (where applicable) set to the selected objects/bones

    :param type: Type
    :type type: typing.Union[str, int]
    '''

    pass


def constraints_clear():
    ''' Clear all the constraints for the active object only

    '''

    pass


def constraints_copy():
    ''' Copy constraints to other selected objects

    '''

    pass


def convert(target: typing.Union[str, int] = 'MESH',
            keep_original: bool = False,
            merge_customdata: bool = True,
            angle: float = 1.22173,
            thickness: int = 5,
            seams: bool = False,
            faces: bool = True,
            offset: float = 0.01):
    ''' Convert selected objects to another type

    :param target: Target, Type of object to convert to * CURVE Curve -- Curve from Mesh or Text objects. * MESH Mesh -- Mesh from Curve, Surface, Metaball, Text, or Point Cloud objects. * GPENCIL Grease Pencil -- Grease Pencil from Curve or Mesh objects. * POINTCLOUD Point Cloud -- Point Cloud from Mesh objects. * CURVES Curves -- Curves from evaluated curve data.
    :type target: typing.Union[str, int]
    :param keep_original: Keep Original, Keep original objects instead of replacing them
    :type keep_original: bool
    :param merge_customdata: Merge UVs, Merge UV coordinates that share a vertex to account for imprecision in some modifiers
    :type merge_customdata: bool
    :param angle: Threshold Angle, Threshold to determine ends of the strokes
    :type angle: float
    :param thickness: Thickness
    :type thickness: int
    :param seams: Only Seam Edges, Convert only seam edges
    :type seams: bool
    :param faces: Export Faces, Export faces as filled strokes
    :type faces: bool
    :param offset: Stroke Offset, Offset strokes from fill
    :type offset: float
    '''

    pass


def correctivesmooth_bind(modifier: str = ""):
    ''' Bind base pose in Corrective Smooth modifier

    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: str
    '''

    pass


def curves_empty_hair_add(align: typing.Union[str, int] = 'WORLD',
                          location: 'mathutils.Vector' = (0.0, 0.0, 0.0),
                          rotation: 'mathutils.Euler' = (0.0, 0.0, 0.0),
                          scale: 'mathutils.Vector' = (0.0, 0.0, 0.0)):
    ''' Add an empty curve object to the scene with the selected mesh as surface

    :param align: Align, The alignment of the new object * WORLD World -- Align the new object to the world. * VIEW View -- Align the new object to the view. * CURSOR 3D Cursor -- Use the 3D cursor orientation for the new object.
    :type align: typing.Union[str, int]
    :param location: Location, Location for the newly added object
    :type location: 'mathutils.Vector'
    :param rotation: Rotation, Rotation for the newly added object
    :type rotation: 'mathutils.Euler'
    :param scale: Scale, Scale for the newly added object
    :type scale: 'mathutils.Vector'
    '''

    pass


def curves_random_add(align: typing.Union[str, int] = 'WORLD',
                      location: 'mathutils.Vector' = (0.0, 0.0, 0.0),
                      rotation: 'mathutils.Euler' = (0.0, 0.0, 0.0),
                      scale: 'mathutils.Vector' = (0.0, 0.0, 0.0)):
    ''' Add a curves object with random curves to the scene

    :param align: Align, The alignment of the new object * WORLD World -- Align the new object to the world. * VIEW View -- Align the new object to the view. * CURSOR 3D Cursor -- Use the 3D cursor orientation for the new object.
    :type align: typing.Union[str, int]
    :param location: Location, Location for the newly added object
    :type location: 'mathutils.Vector'
    :param rotation: Rotation, Rotation for the newly added object
    :type rotation: 'mathutils.Euler'
    :param scale: Scale, Scale for the newly added object
    :type scale: 'mathutils.Vector'
    '''

    pass


def data_instance_add(name: str = "",
                      session_uuid: int = 0,
                      type: typing.Union[str, int] = 'ACTION',
                      align: typing.Union[str, int] = 'WORLD',
                      location: 'mathutils.Vector' = (0.0, 0.0, 0.0),
                      rotation: 'mathutils.Euler' = (0.0, 0.0, 0.0),
                      scale: 'mathutils.Vector' = (0.0, 0.0, 0.0),
                      drop_x: int = 0,
                      drop_y: int = 0):
    ''' Add an object data instance

    :param name: Name, Name of the data-block to use by the operator
    :type name: str
    :param session_uuid: Session UUID, Session UUID of the data-block to use by the operator
    :type session_uuid: int
    :param type: Type
    :type type: typing.Union[str, int]
    :param align: Align, The alignment of the new object * WORLD World -- Align the new object to the world. * VIEW View -- Align the new object to the view. * CURSOR 3D Cursor -- Use the 3D cursor orientation for the new object.
    :type align: typing.Union[str, int]
    :param location: Location, Location for the newly added object
    :type location: 'mathutils.Vector'
    :param rotation: Rotation, Rotation for the newly added object
    :type rotation: 'mathutils.Euler'
    :param scale: Scale, Scale for the newly added object
    :type scale: 'mathutils.Vector'
    :param drop_x: Drop X, X-coordinate (screen space) to place the new object under
    :type drop_x: int
    :param drop_y: Drop Y, Y-coordinate (screen space) to place the new object under
    :type drop_y: int
    '''

    pass


def data_transfer(use_reverse_transfer: bool = False,
                  use_freeze: bool = False,
                  data_type: typing.Union[str, int] = '',
                  use_create: bool = True,
                  vert_mapping: typing.Union[str, int] = 'NEAREST',
                  edge_mapping: typing.Union[str, int] = 'NEAREST',
                  loop_mapping: typing.Union[str, int] = 'NEAREST_POLYNOR',
                  poly_mapping: typing.Union[str, int] = 'NEAREST',
                  use_auto_transform: bool = False,
                  use_object_transform: bool = True,
                  use_max_distance: bool = False,
                  max_distance: float = 1.0,
                  ray_radius: float = 0.0,
                  islands_precision: float = 0.1,
                  layers_select_src: typing.Union[str, int] = 'ACTIVE',
                  layers_select_dst: typing.Union[str, int] = 'ACTIVE',
                  mix_mode: typing.Union[str, int] = 'REPLACE',
                  mix_factor: float = 1.0):
    ''' Transfer data layer(s) (weights, edge sharp, etc.) from active to selected meshes

    :param use_reverse_transfer: Reverse Transfer, Transfer from selected objects to active one
    :type use_reverse_transfer: bool
    :param use_freeze: Freeze Operator, Prevent changes to settings to re-run the operator, handy to change several things at once with heavy geometry
    :type use_freeze: bool
    :param data_type: Data Type, Which data to transfer * VGROUP_WEIGHTS Vertex Group(s) -- Transfer active or all vertex groups. * BEVEL_WEIGHT_VERT Bevel Weight -- Transfer bevel weights. * COLOR_VERTEX Colors -- Color Attributes. * SHARP_EDGE Sharp -- Transfer sharp mark. * SEAM UV Seam -- Transfer UV seam mark. * CREASE Subdivision Crease -- Transfer crease values. * BEVEL_WEIGHT_EDGE Bevel Weight -- Transfer bevel weights. * FREESTYLE_EDGE Freestyle Mark -- Transfer Freestyle edge mark. * CUSTOM_NORMAL Custom Normals -- Transfer custom normals. * COLOR_CORNER Colors -- Color Attributes. * UV UVs -- Transfer UV layers. * SMOOTH Smooth -- Transfer flat/smooth mark. * FREESTYLE_FACE Freestyle Mark -- Transfer Freestyle face mark.
    :type data_type: typing.Union[str, int]
    :param use_create: Create Data, Add data layers on destination meshes if needed
    :type use_create: bool
    :param vert_mapping: Vertex Mapping, Method used to map source vertices to destination ones
    :type vert_mapping: typing.Union[str, int]
    :param edge_mapping: Edge Mapping, Method used to map source edges to destination ones
    :type edge_mapping: typing.Union[str, int]
    :param loop_mapping: Face Corner Mapping, Method used to map source faces' corners to destination ones
    :type loop_mapping: typing.Union[str, int]
    :param poly_mapping: Face Mapping, Method used to map source faces to destination ones
    :type poly_mapping: typing.Union[str, int]
    :param use_auto_transform: Results will never be as good as manual matching of objects
    :type use_auto_transform: bool
    :param use_object_transform: Object Transform, Evaluate source and destination meshes in global space
    :type use_object_transform: bool
    :param use_max_distance: Only Neighbor Geometry, Source elements must be closer than given distance from destination one
    :type use_max_distance: bool
    :param max_distance: Max Distance, Maximum allowed distance between source and destination element, for non-topology mappings
    :type max_distance: float
    :param ray_radius: Ray Radius, 'Width' of rays (especially useful when raycasting against vertices or edges)
    :type ray_radius: float
    :param islands_precision: Islands Precision, Factor controlling precision of islands handling (the higher, the better the results)
    :type islands_precision: float
    :param layers_select_src: Source Layers Selection, Which layers to transfer, in case of multi-layers types
    :type layers_select_src: typing.Union[str, int]
    :param layers_select_dst: Destination Layers Matching, How to match source and destination layers
    :type layers_select_dst: typing.Union[str, int]
    :param mix_mode: Mix Mode, How to affect destination elements with source values
    :type mix_mode: typing.Union[str, int]
    :param mix_factor: Mix Factor, Factor to use when applying data to destination (exact behavior depends on mix mode)
    :type mix_factor: float
    '''

    pass


def datalayout_transfer(modifier: str = "",
                        data_type: typing.Union[str, int] = '',
                        use_delete: bool = False,
                        layers_select_src: typing.Union[str, int] = 'ACTIVE',
                        layers_select_dst: typing.Union[str, int] = 'ACTIVE'):
    ''' Transfer layout of data layer(s) from active to selected meshes

    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: str
    :param data_type: Data Type, Which data to transfer * VGROUP_WEIGHTS Vertex Group(s) -- Transfer active or all vertex groups. * BEVEL_WEIGHT_VERT Bevel Weight -- Transfer bevel weights. * COLOR_VERTEX Colors -- Color Attributes. * SHARP_EDGE Sharp -- Transfer sharp mark. * SEAM UV Seam -- Transfer UV seam mark. * CREASE Subdivision Crease -- Transfer crease values. * BEVEL_WEIGHT_EDGE Bevel Weight -- Transfer bevel weights. * FREESTYLE_EDGE Freestyle Mark -- Transfer Freestyle edge mark. * CUSTOM_NORMAL Custom Normals -- Transfer custom normals. * COLOR_CORNER Colors -- Color Attributes. * UV UVs -- Transfer UV layers. * SMOOTH Smooth -- Transfer flat/smooth mark. * FREESTYLE_FACE Freestyle Mark -- Transfer Freestyle face mark.
    :type data_type: typing.Union[str, int]
    :param use_delete: Exact Match, Also delete some data layers from destination if necessary, so that it matches exactly source
    :type use_delete: bool
    :param layers_select_src: Source Layers Selection, Which layers to transfer, in case of multi-layers types
    :type layers_select_src: typing.Union[str, int]
    :param layers_select_dst: Destination Layers Matching, How to match source and destination layers
    :type layers_select_dst: typing.Union[str, int]
    '''

    pass


def delete(use_global: bool = False, confirm: bool = True):
    ''' Delete selected objects

    :param use_global: Delete Globally, Remove object from all scenes
    :type use_global: bool
    :param confirm: Confirm, Prompt for confirmation
    :type confirm: bool
    '''

    pass


def drop_geometry_nodes(session_uuid: int = 0):
    ''' Undocumented, consider contributing <https://developer.blender.org/> __.

    :param session_uuid: Session UUID, Session UUID of the geometry node group being dropped
    :type session_uuid: int
    '''

    pass


def drop_named_image(filepath: str = "",
                     relative_path: bool = True,
                     name: str = "",
                     session_uuid: int = 0,
                     align: typing.Union[str, int] = 'WORLD',
                     location: 'mathutils.Vector' = (0.0, 0.0, 0.0),
                     rotation: 'mathutils.Euler' = (0.0, 0.0, 0.0),
                     scale: 'mathutils.Vector' = (0.0, 0.0, 0.0)):
    ''' Add an empty image type to scene with data

    :param filepath: Filepath, Path to image file
    :type filepath: str
    :param relative_path: Relative Path, Select the file relative to the blend file
    :type relative_path: bool
    :param name: Name, Name of the data-block to use by the operator
    :type name: str
    :param session_uuid: Session UUID, Session UUID of the data-block to use by the operator
    :type session_uuid: int
    :param align: Align, The alignment of the new object * WORLD World -- Align the new object to the world. * VIEW View -- Align the new object to the view. * CURSOR 3D Cursor -- Use the 3D cursor orientation for the new object.
    :type align: typing.Union[str, int]
    :param location: Location, Location for the newly added object
    :type location: 'mathutils.Vector'
    :param rotation: Rotation, Rotation for the newly added object
    :type rotation: 'mathutils.Euler'
    :param scale: Scale, Scale for the newly added object
    :type scale: 'mathutils.Vector'
    '''

    pass


def drop_named_material(name: str = "", session_uuid: int = 0):
    ''' Undocumented, consider contributing <https://developer.blender.org/> __.

    :param name: Name, Name of the data-block to use by the operator
    :type name: str
    :param session_uuid: Session UUID, Session UUID of the data-block to use by the operator
    :type session_uuid: int
    '''

    pass


def duplicate(linked: bool = False,
              mode: typing.Union[str, int] = 'TRANSLATION'):
    ''' Duplicate selected objects

    :param linked: Linked, Duplicate object but not object data, linking to the original data
    :type linked: bool
    :param mode: Mode
    :type mode: typing.Union[str, int]
    '''

    pass


def duplicate_move(OBJECT_OT_duplicate=None, TRANSFORM_OT_translate=None):
    ''' Duplicate the selected objects and move them

    :param OBJECT_OT_duplicate: Duplicate Objects, Duplicate selected objects
    :param TRANSFORM_OT_translate: Move, Move selected items
    '''

    pass


def duplicate_move_linked(OBJECT_OT_duplicate=None,
                          TRANSFORM_OT_translate=None):
    ''' Duplicate the selected objects, but not their object data, and move them

    :param OBJECT_OT_duplicate: Duplicate Objects, Duplicate selected objects
    :param TRANSFORM_OT_translate: Move, Move selected items
    '''

    pass


def duplicates_make_real(use_base_parent: bool = False,
                         use_hierarchy: bool = False):
    ''' Make instanced objects attached to this object real

    :param use_base_parent: Parent, Parent newly created objects to the original instancer
    :type use_base_parent: bool
    :param use_hierarchy: Keep Hierarchy, Maintain parent child relationships
    :type use_hierarchy: bool
    '''

    pass


def editmode_toggle():
    ''' Toggle object's edit mode

    '''

    pass


def effector_add(type: typing.Union[str, int] = 'FORCE',
                 radius: float = 1.0,
                 enter_editmode: bool = False,
                 align: typing.Union[str, int] = 'WORLD',
                 location: 'mathutils.Vector' = (0.0, 0.0, 0.0),
                 rotation: 'mathutils.Euler' = (0.0, 0.0, 0.0),
                 scale: 'mathutils.Vector' = (0.0, 0.0, 0.0)):
    ''' Add an empty object with a physics effector to the scene

    :param type: Type
    :type type: typing.Union[str, int]
    :param radius: Radius
    :type radius: float
    :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
    :type enter_editmode: bool
    :param align: Align, The alignment of the new object * WORLD World -- Align the new object to the world. * VIEW View -- Align the new object to the view. * CURSOR 3D Cursor -- Use the 3D cursor orientation for the new object.
    :type align: typing.Union[str, int]
    :param location: Location, Location for the newly added object
    :type location: 'mathutils.Vector'
    :param rotation: Rotation, Rotation for the newly added object
    :type rotation: 'mathutils.Euler'
    :param scale: Scale, Scale for the newly added object
    :type scale: 'mathutils.Vector'
    '''

    pass


def empty_add(type: typing.Union[str, int] = 'PLAIN_AXES',
              radius: float = 1.0,
              align: typing.Union[str, int] = 'WORLD',
              location: 'mathutils.Vector' = (0.0, 0.0, 0.0),
              rotation: 'mathutils.Euler' = (0.0, 0.0, 0.0),
              scale: 'mathutils.Vector' = (0.0, 0.0, 0.0)):
    ''' Add an empty object to the scene

    :param type: Type
    :type type: typing.Union[str, int]
    :param radius: Radius
    :type radius: float
    :param align: Align, The alignment of the new object * WORLD World -- Align the new object to the world. * VIEW View -- Align the new object to the view. * CURSOR 3D Cursor -- Use the 3D cursor orientation for the new object.
    :type align: typing.Union[str, int]
    :param location: Location, Location for the newly added object
    :type location: 'mathutils.Vector'
    :param rotation: Rotation, Rotation for the newly added object
    :type rotation: 'mathutils.Euler'
    :param scale: Scale, Scale for the newly added object
    :type scale: 'mathutils.Vector'
    '''

    pass


def explode_refresh(modifier: str = ""):
    ''' Refresh data in the Explode modifier

    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: str
    '''

    pass


def face_map_add():
    ''' Add a new face map to the active object

    '''

    pass


def face_map_assign():
    ''' Assign faces to a face map

    '''

    pass


def face_map_deselect():
    ''' Deselect faces belonging to a face map

    '''

    pass


def face_map_move(direction: typing.Union[str, int] = 'UP'):
    ''' Move the active face map up/down in the list

    :param direction: Direction, Direction to move, up or down
    :type direction: typing.Union[str, int]
    '''

    pass


def face_map_remove():
    ''' Remove a face map from the active object

    '''

    pass


def face_map_remove_from():
    ''' Remove faces from a face map

    '''

    pass


def face_map_select():
    ''' Select faces belonging to a face map

    '''

    pass


def forcefield_toggle():
    ''' Toggle object's force field

    '''

    pass


def game_physics_copy():
    ''' Copy game physics properties to other selected objects

    '''

    pass


def game_property_clear():
    ''' Remove all game properties from all selected objects

    '''

    pass


def game_property_copy(operation: typing.Union[str, int] = 'COPY',
                       property: typing.Union[str, int] = ''):
    ''' Copy/merge/replace a game property from active object to all selected objects

    :param operation: Operation
    :type operation: typing.Union[str, int]
    :param property: Property, Properties to copy
    :type property: typing.Union[str, int]
    '''

    pass


def game_property_move(index: int = 0,
                       direction: typing.Union[str, int] = 'UP'):
    ''' Move game property

    :param index: Index, Property index to move
    :type index: int
    :param direction: Direction, Direction for moving the property
    :type direction: typing.Union[str, int]
    '''

    pass


def game_property_new(type: typing.Union[str, int] = 'FLOAT', name: str = ""):
    ''' Create a new property available to the game engine

    :param type: Type, Type of game property to add
    :type type: typing.Union[str, int]
    :param name: Name, Name of the game property to add
    :type name: str
    '''

    pass


def game_property_remove(index: int = 0):
    ''' Remove game property

    :param index: Index, Property index to remove
    :type index: int
    '''

    pass


def geometry_node_tree_copy_assign():
    ''' Copy the active geometry node group and assign it to the active modifier

    '''

    pass


def geometry_nodes_input_attribute_toggle(prop_path: str = "",
                                          modifier_name: str = ""):
    ''' Switch between an attribute and a single value to define the data for every element

    :param prop_path: Prop Path
    :type prop_path: str
    :param modifier_name: Modifier Name
    :type modifier_name: str
    '''

    pass


def geometry_nodes_move_to_nodes():
    ''' Move inputs and outputs from in the modifier to a new node group :File: startup/bl_operators/geometry_nodes.py\:110 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/geometry_nodes.py#L110> __

    '''

    pass


def gpencil_add(radius: float = 1.0,
                align: typing.Union[str, int] = 'WORLD',
                location: 'mathutils.Vector' = (0.0, 0.0, 0.0),
                rotation: 'mathutils.Euler' = (0.0, 0.0, 0.0),
                scale: 'mathutils.Vector' = (0.0, 0.0, 0.0),
                type: typing.Union[str, int] = 'EMPTY',
                use_in_front: bool = True,
                stroke_depth_offset: float = 0.05,
                use_lights: bool = False,
                stroke_depth_order: typing.Union[str, int] = '3D'):
    ''' Add a Grease Pencil object to the scene

    :param radius: Radius
    :type radius: float
    :param align: Align, The alignment of the new object * WORLD World -- Align the new object to the world. * VIEW View -- Align the new object to the view. * CURSOR 3D Cursor -- Use the 3D cursor orientation for the new object.
    :type align: typing.Union[str, int]
    :param location: Location, Location for the newly added object
    :type location: 'mathutils.Vector'
    :param rotation: Rotation, Rotation for the newly added object
    :type rotation: 'mathutils.Euler'
    :param scale: Scale, Scale for the newly added object
    :type scale: 'mathutils.Vector'
    :param type: Type
    :type type: typing.Union[str, int]
    :param use_in_front: Show In Front, Show line art grease pencil in front of everything
    :type use_in_front: bool
    :param stroke_depth_offset: Stroke Offset, Stroke offset for the line art modifier
    :type stroke_depth_offset: float
    :param use_lights: Use Lights, Use lights for this grease pencil object
    :type use_lights: bool
    :param stroke_depth_order: Stroke Depth Order, Defines how the strokes are ordered in 3D space (for objects not displayed 'In Front') * 2D 2D Layers -- Display strokes using grease pencil layers to define order. * 3D 3D Location -- Display strokes using real 3D position in 3D space.
    :type stroke_depth_order: typing.Union[str, int]
    '''

    pass


def gpencil_modifier_add(type: typing.Union[str, int] = 'GP_THICK'):
    ''' Add a procedural operation/effect to the active grease pencil object

    :param type: Type
    :type type: typing.Union[str, int]
    '''

    pass


def gpencil_modifier_apply(apply_as: typing.Union[str, int] = 'DATA',
                           modifier: str = "",
                           report: bool = False):
    ''' Apply modifier and remove from the stack

    :param apply_as: Apply As, How to apply the modifier to the geometry * DATA Object Data -- Apply modifier to the object's data. * SHAPE New Shape -- Apply deform-only modifier to a new shape on this object.
    :type apply_as: typing.Union[str, int]
    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: str
    :param report: Report, Create a notification after the operation
    :type report: bool
    '''

    pass


def gpencil_modifier_copy(modifier: str = ""):
    ''' Duplicate modifier at the same position in the stack

    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: str
    '''

    pass


def gpencil_modifier_copy_to_selected(modifier: str = ""):
    ''' Copy the modifier from the active object to all selected objects

    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: str
    '''

    pass


def gpencil_modifier_move_down(modifier: str = ""):
    ''' Move modifier down in the stack

    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: str
    '''

    pass


def gpencil_modifier_move_to_index(modifier: str = "", index: int = 0):
    ''' Change the modifier's position in the list so it evaluates after the set number of others

    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: str
    :param index: Index, The index to move the modifier to
    :type index: int
    '''

    pass


def gpencil_modifier_move_up(modifier: str = ""):
    ''' Move modifier up in the stack

    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: str
    '''

    pass


def gpencil_modifier_remove(modifier: str = "", report: bool = False):
    ''' Remove a modifier from the active grease pencil object

    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: str
    :param report: Report, Create a notification after the operation
    :type report: bool
    '''

    pass


def hide_collection(collection_index: int = -1,
                    toggle: bool = False,
                    extend: bool = False):
    ''' Show only objects in collection (Shift to extend)

    :param collection_index: Collection Index, Index of the collection to change visibility
    :type collection_index: int
    :param toggle: Toggle, Toggle visibility
    :type toggle: bool
    :param extend: Extend, Extend visibility
    :type extend: bool
    '''

    pass


def hide_render_clear_all():
    ''' Reveal all render objects by setting the hide render flag :File: startup/bl_operators/object.py\:680 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/object.py#L680> __

    '''

    pass


def hide_view_clear(select: bool = True):
    ''' Reveal temporarily hidden objects

    :param select: Select
    :type select: bool
    '''

    pass


def hide_view_set(unselected: bool = False):
    ''' Temporarily hide objects from the viewport

    :param unselected: Unselected, Hide unselected rather than selected objects
    :type unselected: bool
    '''

    pass


def hook_add_newob():
    ''' Hook selected vertices to a newly created object

    '''

    pass


def hook_add_selob(use_bone: bool = False):
    ''' Hook selected vertices to the first selected object

    :param use_bone: Active Bone, Assign the hook to the hook object's active bone
    :type use_bone: bool
    '''

    pass


def hook_assign(modifier: typing.Union[str, int] = ''):
    ''' Assign the selected vertices to a hook

    :param modifier: Modifier, Modifier number to assign to
    :type modifier: typing.Union[str, int]
    '''

    pass


def hook_recenter(modifier: typing.Union[str, int] = ''):
    ''' Set hook center to cursor position

    :param modifier: Modifier, Modifier number to assign to
    :type modifier: typing.Union[str, int]
    '''

    pass


def hook_remove(modifier: typing.Union[str, int] = ''):
    ''' Remove a hook from the active object

    :param modifier: Modifier, Modifier number to remove
    :type modifier: typing.Union[str, int]
    '''

    pass


def hook_reset(modifier: typing.Union[str, int] = ''):
    ''' Recalculate and clear offset transformation

    :param modifier: Modifier, Modifier number to assign to
    :type modifier: typing.Union[str, int]
    '''

    pass


def hook_select(modifier: typing.Union[str, int] = ''):
    ''' Select affected vertices on mesh

    :param modifier: Modifier, Modifier number to remove
    :type modifier: typing.Union[str, int]
    '''

    pass


def instance_offset_from_cursor():
    ''' Set offset used for collection instances based on cursor position :File: startup/bl_operators/object.py\:858 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/object.py#L858> __

    '''

    pass


def instance_offset_from_object():
    ''' Set offset used for collection instances based on the active object position :File: startup/bl_operators/object.py\:1046 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/object.py#L1046> __

    '''

    pass


def instance_offset_to_cursor():
    ''' Set cursor position to the offset used for collection instances :File: startup/bl_operators/object.py\:1029 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/object.py#L1029> __

    '''

    pass


def isolate_type_render():
    ''' Hide unselected render objects of same type as active by setting the hide render flag :File: startup/bl_operators/object.py\:660 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/object.py#L660> __

    '''

    pass


def join():
    ''' Join selected objects into active object

    '''

    pass


def join_shapes():
    ''' Copy the current resulting shape of another selected object to this one

    '''

    pass


def join_uvs():
    ''' Transfer UV Maps from active to selected objects (needs matching geometry) :File: startup/bl_operators/object.py\:567 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/object.py#L567> __

    '''

    pass


def laplaciandeform_bind(modifier: str = ""):
    ''' Bind mesh to system in laplacian deform modifier

    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: str
    '''

    pass


def light_add(type: typing.Union[str, int] = 'POINT',
              radius: float = 1.0,
              align: typing.Union[str, int] = 'WORLD',
              location: 'mathutils.Vector' = (0.0, 0.0, 0.0),
              rotation: 'mathutils.Euler' = (0.0, 0.0, 0.0),
              scale: 'mathutils.Vector' = (0.0, 0.0, 0.0)):
    ''' Add a light object to the scene

    :param type: Type
    :type type: typing.Union[str, int]
    :param radius: Radius
    :type radius: float
    :param align: Align, The alignment of the new object * WORLD World -- Align the new object to the world. * VIEW View -- Align the new object to the view. * CURSOR 3D Cursor -- Use the 3D cursor orientation for the new object.
    :type align: typing.Union[str, int]
    :param location: Location, Location for the newly added object
    :type location: 'mathutils.Vector'
    :param rotation: Rotation, Rotation for the newly added object
    :type rotation: 'mathutils.Euler'
    :param scale: Scale, Scale for the newly added object
    :type scale: 'mathutils.Vector'
    '''

    pass


def lightprobe_add(type: typing.Union[str, int] = 'CUBEMAP',
                   radius: float = 1.0,
                   enter_editmode: bool = False,
                   align: typing.Union[str, int] = 'WORLD',
                   location: 'mathutils.Vector' = (0.0, 0.0, 0.0),
                   rotation: 'mathutils.Euler' = (0.0, 0.0, 0.0),
                   scale: 'mathutils.Vector' = (0.0, 0.0, 0.0)):
    ''' Add a light probe object

    :param type: Type * CUBEMAP Reflection Cubemap -- Reflection probe with spherical or cubic attenuation. * PLANAR Reflection Plane -- Planar reflection probe. * GRID Irradiance Volume -- Irradiance probe to capture diffuse indirect lighting.
    :type type: typing.Union[str, int]
    :param radius: Radius
    :type radius: float
    :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
    :type enter_editmode: bool
    :param align: Align, The alignment of the new object * WORLD World -- Align the new object to the world. * VIEW View -- Align the new object to the view. * CURSOR 3D Cursor -- Use the 3D cursor orientation for the new object.
    :type align: typing.Union[str, int]
    :param location: Location, Location for the newly added object
    :type location: 'mathutils.Vector'
    :param rotation: Rotation, Rotation for the newly added object
    :type rotation: 'mathutils.Euler'
    :param scale: Scale, Scale for the newly added object
    :type scale: 'mathutils.Vector'
    '''

    pass


def lineart_bake_strokes():
    ''' Bake Line Art for current GPencil object

    '''

    pass


def lineart_bake_strokes_all():
    ''' Bake all Grease Pencil objects that have a line art modifier

    '''

    pass


def lineart_clear():
    ''' Clear all strokes in current GPencil object

    '''

    pass


def lineart_clear_all():
    ''' Clear all strokes in all Grease Pencil objects that have a line art modifier

    '''

    pass


def link_to_collection(collection_index: int = -1,
                       is_new: bool = False,
                       new_collection_name: str = ""):
    ''' Link objects to a collection

    :param collection_index: Collection Index, Index of the collection to move to
    :type collection_index: int
    :param is_new: New, Move objects to a new collection
    :type is_new: bool
    :param new_collection_name: Name, Name of the newly added collection
    :type new_collection_name: str
    '''

    pass


def load_background_image(filepath: str = "",
                          filter_image: bool = True,
                          filter_folder: bool = True,
                          view_align: bool = True):
    ''' Add a reference image into the background behind objects :File: startup/bl_operators/object.py\:1077 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/object.py#L1077> __

    :param filepath: filepath
    :type filepath: str
    :param filter_image: filter_image
    :type filter_image: bool
    :param filter_folder: filter_folder
    :type filter_folder: bool
    :param view_align: Align to View
    :type view_align: bool
    '''

    pass


def load_reference_image(filepath: str = "",
                         filter_image: bool = True,
                         filter_folder: bool = True,
                         view_align: bool = True):
    ''' Add a reference image into the scene between objects :File: startup/bl_operators/object.py\:1077 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/object.py#L1077> __

    :param filepath: filepath
    :type filepath: str
    :param filter_image: filter_image
    :type filter_image: bool
    :param filter_folder: filter_folder
    :type filter_folder: bool
    :param view_align: Align to View
    :type view_align: bool
    '''

    pass


def location_clear(clear_delta: bool = False):
    ''' Clear the object's location

    :param clear_delta: Clear Delta, Clear delta location in addition to clearing the normal location transform
    :type clear_delta: bool
    '''

    pass


def lod_add():
    ''' Add a level of detail to this object

    '''

    pass


def lod_by_name():
    ''' Add levels of detail to this object based on object names :File: startup/bl_operators/object.py\:1181 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/object.py#L1181> __

    '''

    pass


def lod_clear_all():
    ''' Remove all levels of detail from this object :File: startup/bl_operators/object.py\:1231 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/object.py#L1231> __

    '''

    pass


def lod_generate(count: int = 3, target: float = 0.1, package: bool = False):
    ''' Generate levels of detail using the decimate modifier :File: startup/bl_operators/object.py\:960 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/object.py#L960> __

    :param count: Count
    :type count: int
    :param target: Target Size
    :type target: float
    :param package: Package into Group
    :type package: bool
    '''

    pass


def lod_remove(index: int = 1):
    ''' Remove a level of detail from this object

    :param index: Index
    :type index: int
    '''

    pass


def logic_bricks_copy():
    ''' Copy logic bricks to other selected objects

    '''

    pass


def make_dupli_face():
    ''' Convert objects into instanced faces :File: startup/bl_operators/object.py\:648 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/object.py#L648> __

    '''

    pass


def make_links_data(type: typing.Union[str, int] = 'OBDATA'):
    ''' Transfer data from active object to selected objects

    :param type: Type * OBDATA Link Object Data -- Replace assigned Object Data. * MATERIAL Link Materials -- Replace assigned Materials. * ANIMATION Link Animation Data -- Replace assigned Animation Data. * GROUPS Link Collections -- Replace assigned Collections. * DUPLICOLLECTION Link Instance Collection -- Replace assigned Collection Instance. * FONTS Link Fonts to Text -- Replace Text object Fonts. * MODIFIERS Copy Modifiers -- Replace Modifiers. * EFFECTS Copy Grease Pencil Effects -- Replace Grease Pencil Effects.
    :type type: typing.Union[str, int]
    '''

    pass


def make_links_scene(scene: typing.Union[str, int] = ''):
    ''' Link selection to another scene

    :param scene: Scene
    :type scene: typing.Union[str, int]
    '''

    pass


def make_local(type: typing.Union[str, int] = 'SELECT_OBJECT'):
    ''' Make library linked data-blocks local to this file

    :param type: Type
    :type type: typing.Union[str, int]
    '''

    pass


def make_override_library(collection: int = 0):
    ''' Create a local override of the selected linked objects, and their hierarchy of dependencies

    :param collection: Override Collection, Session UUID of the directly linked collection containing the selected object, to make an override from
    :type collection: int
    '''

    pass


def make_single_user(type: typing.Union[str, int] = 'SELECTED_OBJECTS',
                     object: bool = False,
                     obdata: bool = False,
                     material: bool = False,
                     animation: bool = False,
                     obdata_animation: bool = False):
    ''' Make linked data local to each object

    :param type: Type
    :type type: typing.Union[str, int]
    :param object: Object, Make single user objects
    :type object: bool
    :param obdata: Object Data, Make single user object data
    :type obdata: bool
    :param material: Materials, Make materials local to each data-block
    :type material: bool
    :param animation: Object Animation, Make object animation data local to each object
    :type animation: bool
    :param obdata_animation: Object Data Animation, Make object data (mesh, curve etc.) animation data local to each object
    :type obdata_animation: bool
    '''

    pass


def material_slot_add():
    ''' Add a new material slot

    '''

    pass


def material_slot_assign():
    ''' Assign active material slot to selection

    '''

    pass


def material_slot_copy():
    ''' Copy material to selected objects

    '''

    pass


def material_slot_deselect():
    ''' Deselect by active material slot

    '''

    pass


def material_slot_move(direction: typing.Union[str, int] = 'UP'):
    ''' Move the active material up/down in the list

    :param direction: Direction, Direction to move the active material towards
    :type direction: typing.Union[str, int]
    '''

    pass


def material_slot_remove():
    ''' Remove the selected material slot

    '''

    pass


def material_slot_remove_unused():
    ''' Remove unused material slots

    '''

    pass


def material_slot_select():
    ''' Select by active material slot

    '''

    pass


def meshdeform_bind(modifier: str = ""):
    ''' Bind mesh to cage in mesh deform modifier

    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: str
    '''

    pass


def metaball_add(type: typing.Union[str, int] = 'BALL',
                 radius: float = 2.0,
                 enter_editmode: bool = False,
                 align: typing.Union[str, int] = 'WORLD',
                 location: 'mathutils.Vector' = (0.0, 0.0, 0.0),
                 rotation: 'mathutils.Euler' = (0.0, 0.0, 0.0),
                 scale: 'mathutils.Vector' = (0.0, 0.0, 0.0)):
    ''' Add an metaball object to the scene

    :param type: Primitive
    :type type: typing.Union[str, int]
    :param radius: Radius
    :type radius: float
    :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
    :type enter_editmode: bool
    :param align: Align, The alignment of the new object * WORLD World -- Align the new object to the world. * VIEW View -- Align the new object to the view. * CURSOR 3D Cursor -- Use the 3D cursor orientation for the new object.
    :type align: typing.Union[str, int]
    :param location: Location, Location for the newly added object
    :type location: 'mathutils.Vector'
    :param rotation: Rotation, Rotation for the newly added object
    :type rotation: 'mathutils.Euler'
    :param scale: Scale, Scale for the newly added object
    :type scale: 'mathutils.Vector'
    '''

    pass


def mode_set(mode: typing.Union[str, int] = 'OBJECT', toggle: bool = False):
    ''' Sets the object interaction mode

    :param mode: Mode
    :type mode: typing.Union[str, int]
    :param toggle: Toggle
    :type toggle: bool
    '''

    pass


def mode_set_with_submode(
        mode: typing.Union[str, int] = 'OBJECT',
        toggle: bool = False,
        mesh_select_mode: typing.Union[typing.Set[str], typing.Set[int]] = {}):
    ''' Sets the object interaction mode

    :param mode: Mode
    :type mode: typing.Union[str, int]
    :param toggle: Toggle
    :type toggle: bool
    :param mesh_select_mode: Mesh Mode
    :type mesh_select_mode: typing.Union[typing.Set[str], typing.Set[int]]
    '''

    pass


def modifier_add(type: typing.Union[str, int] = 'SUBSURF'):
    ''' Add a procedural operation/effect to the active object

    :param type: Type
    :type type: typing.Union[str, int]
    '''

    pass


def modifier_apply(modifier: str = "",
                   report: bool = False,
                   merge_customdata: bool = True,
                   single_user: bool = False):
    ''' Apply modifier and remove from the stack

    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: str
    :param report: Report, Create a notification after the operation
    :type report: bool
    :param merge_customdata: Merge UVs, For mesh objects, merge UV coordinates that share a vertex to account for imprecision in some modifiers
    :type merge_customdata: bool
    :param single_user: Make Data Single User, Make the object's data single user if needed
    :type single_user: bool
    '''

    pass


def modifier_apply_as_shapekey(keep_modifier: bool = False,
                               modifier: str = "",
                               report: bool = False):
    ''' Apply modifier as a new shape key and remove from the stack

    :param keep_modifier: Keep Modifier, Do not remove the modifier from stack
    :type keep_modifier: bool
    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: str
    :param report: Report, Create a notification after the operation
    :type report: bool
    '''

    pass


def modifier_convert(modifier: str = ""):
    ''' Convert particles to a mesh object

    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: str
    '''

    pass


def modifier_copy(modifier: str = ""):
    ''' Duplicate modifier at the same position in the stack

    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: str
    '''

    pass


def modifier_copy_to_selected(modifier: str = ""):
    ''' Copy the modifier from the active object to all selected objects

    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: str
    '''

    pass


def modifier_move_down(modifier: str = ""):
    ''' Move modifier down in the stack

    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: str
    '''

    pass


def modifier_move_to_index(modifier: str = "", index: int = 0):
    ''' Change the modifier's index in the stack so it evaluates after the set number of others

    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: str
    :param index: Index, The index to move the modifier to
    :type index: int
    '''

    pass


def modifier_move_up(modifier: str = ""):
    ''' Move modifier up in the stack

    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: str
    '''

    pass


def modifier_remove(modifier: str = "", report: bool = False):
    ''' Remove a modifier from the active object

    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: str
    :param report: Report, Create a notification after the operation
    :type report: bool
    '''

    pass


def modifier_set_active(modifier: str = ""):
    ''' Activate the modifier to use as the context

    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: str
    '''

    pass


def move_to_collection(collection_index: int = -1,
                       is_new: bool = False,
                       new_collection_name: str = ""):
    ''' Move objects to a collection

    :param collection_index: Collection Index, Index of the collection to move to
    :type collection_index: int
    :param is_new: New, Move objects to a new collection
    :type is_new: bool
    :param new_collection_name: Name, Name of the newly added collection
    :type new_collection_name: str
    '''

    pass


def multires_base_apply(modifier: str = ""):
    ''' Modify the base mesh to conform to the displaced mesh

    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: str
    '''

    pass


def multires_external_pack():
    ''' Pack displacements from an external file

    '''

    pass


def multires_external_save(filepath: str = "",
                           hide_props_region: bool = True,
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
                           filter_btx: bool = True,
                           filter_collada: bool = False,
                           filter_alembic: bool = False,
                           filter_usd: bool = False,
                           filter_obj: bool = False,
                           filter_volume: bool = False,
                           filter_folder: bool = True,
                           filter_blenlib: bool = False,
                           filemode: int = 9,
                           relative_path: bool = True,
                           display_type: typing.Union[str, int] = 'DEFAULT',
                           sort_method: typing.Union[str, int] = '',
                           modifier: str = ""):
    ''' Save displacements to an external file

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
    :param display_type: Display Type * DEFAULT Default -- Automatically determine display type for files. * LIST_VERTICAL Short List -- Display files as short list. * LIST_HORIZONTAL Long List -- Display files as a detailed list. * THUMBNAIL Thumbnails -- Display files as thumbnails.
    :type display_type: typing.Union[str, int]
    :param sort_method: File sorting mode
    :type sort_method: typing.Union[str, int]
    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: str
    '''

    pass


def multires_higher_levels_delete(modifier: str = ""):
    ''' Deletes the higher resolution mesh, potential loss of detail

    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: str
    '''

    pass


def multires_rebuild_subdiv(modifier: str = ""):
    ''' Rebuilds all possible subdivisions levels to generate a lower resolution base mesh

    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: str
    '''

    pass


def multires_reshape(modifier: str = ""):
    ''' Copy vertex coordinates from other object

    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: str
    '''

    pass


def multires_subdivide(modifier: str = "",
                       mode: typing.Union[str, int] = 'CATMULL_CLARK'):
    ''' Add a new level of subdivision

    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: str
    :param mode: Subdivision Mode, How the mesh is going to be subdivided to create a new level * CATMULL_CLARK Catmull-Clark -- Create a new level using Catmull-Clark subdivisions. * SIMPLE Simple -- Create a new level using simple subdivisions. * LINEAR Linear -- Create a new level using linear interpolation of the sculpted displacement.
    :type mode: typing.Union[str, int]
    '''

    pass


def multires_unsubdivide(modifier: str = ""):
    ''' Rebuild a lower subdivision level of the current base mesh

    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: str
    '''

    pass


def ocean_bake(modifier: str = "", free: bool = False):
    ''' Bake an image sequence of ocean data

    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: str
    :param free: Free, Free the bake, rather than generating it
    :type free: bool
    '''

    pass


def origin_clear():
    ''' Clear the object's origin

    '''

    pass


def origin_set(type: typing.Union[str, int] = 'GEOMETRY_ORIGIN',
               center: typing.Union[str, int] = 'MEDIAN'):
    ''' Set the object's origin, by either moving the data, or set to center of data, or use 3D cursor

    :param type: Type * GEOMETRY_ORIGIN Geometry to Origin -- Move object geometry to object origin. * ORIGIN_GEOMETRY Origin to Geometry -- Calculate the center of geometry based on the current pivot point (median, otherwise bounding box). * ORIGIN_CURSOR Origin to 3D Cursor -- Move object origin to position of the 3D cursor. * ORIGIN_CENTER_OF_MASS Origin to Center of Mass (Surface) -- Calculate the center of mass from the surface area. * ORIGIN_CENTER_OF_VOLUME Origin to Center of Mass (Volume) -- Calculate the center of mass from the volume (must be manifold geometry with consistent normals).
    :type type: typing.Union[str, int]
    :param center: Center
    :type center: typing.Union[str, int]
    '''

    pass


def parent_clear(type: typing.Union[str, int] = 'CLEAR'):
    ''' Clear the object's parenting

    :param type: Type * CLEAR Clear Parent -- Completely clear the parenting relationship, including involved modifiers if any. * CLEAR_KEEP_TRANSFORM Clear and Keep Transformation -- As 'Clear Parent', but keep the current visual transformations of the object. * CLEAR_INVERSE Clear Parent Inverse -- Reset the transform corrections applied to the parenting relationship, does not remove parenting itself.
    :type type: typing.Union[str, int]
    '''

    pass


def parent_inverse_apply():
    ''' Apply the object's parent inverse to its data

    '''

    pass


def parent_no_inverse_set(keep_transform: bool = False):
    ''' Set the object's parenting without setting the inverse parent correction

    :param keep_transform: Keep Transform, Preserve the world transform throughout parenting
    :type keep_transform: bool
    '''

    pass


def parent_set(type: typing.Union[str, int] = 'OBJECT',
               xmirror: bool = False,
               keep_transform: bool = False):
    ''' Set the object's parenting

    :param type: Type
    :type type: typing.Union[str, int]
    :param xmirror: X Mirror, Apply weights symmetrically along X axis, for Envelope/Automatic vertex groups creation
    :type xmirror: bool
    :param keep_transform: Keep Transform, Apply transformation before parenting
    :type keep_transform: bool
    '''

    pass


def particle_system_add():
    ''' Add a particle system

    '''

    pass


def particle_system_remove():
    ''' Remove the selected particle system

    '''

    pass


def paths_calculate(display_type: typing.Union[str, int] = 'RANGE',
                    range: typing.Union[str, int] = 'SCENE'):
    ''' Generate motion paths for the selected objects

    :param display_type: Display type
    :type display_type: typing.Union[str, int]
    :param range: Computation Range
    :type range: typing.Union[str, int]
    '''

    pass


def paths_clear(only_selected: bool = False):
    ''' Undocumented, consider contributing <https://developer.blender.org/> __.

    :param only_selected: Only Selected, Only clear motion paths of selected objects
    :type only_selected: bool
    '''

    pass


def paths_update():
    ''' Recalculate motion paths for selected objects

    '''

    pass


def paths_update_visible():
    ''' Recalculate all visible motion paths for objects and poses

    '''

    pass


def pointcloud_add(align: typing.Union[str, int] = 'WORLD',
                   location: 'mathutils.Vector' = (0.0, 0.0, 0.0),
                   rotation: 'mathutils.Euler' = (0.0, 0.0, 0.0),
                   scale: 'mathutils.Vector' = (0.0, 0.0, 0.0)):
    ''' Add a point cloud object to the scene

    :param align: Align, The alignment of the new object * WORLD World -- Align the new object to the world. * VIEW View -- Align the new object to the view. * CURSOR 3D Cursor -- Use the 3D cursor orientation for the new object.
    :type align: typing.Union[str, int]
    :param location: Location, Location for the newly added object
    :type location: 'mathutils.Vector'
    :param rotation: Rotation, Rotation for the newly added object
    :type rotation: 'mathutils.Euler'
    :param scale: Scale, Scale for the newly added object
    :type scale: 'mathutils.Vector'
    '''

    pass


def posemode_toggle():
    ''' Enable or disable posing/selecting bones

    '''

    pass


def quadriflow_remesh(use_mesh_symmetry: bool = True,
                      use_preserve_sharp: bool = False,
                      use_preserve_boundary: bool = False,
                      preserve_paint_mask: bool = False,
                      smooth_normals: bool = False,
                      mode: typing.Union[str, int] = 'FACES',
                      target_ratio: float = 1.0,
                      target_edge_length: float = 0.1,
                      target_faces: int = 4000,
                      mesh_area: float = -1.0,
                      seed: int = 0):
    ''' Create a new quad based mesh using the surface data of the current mesh. All data layers will be lost

    :param use_mesh_symmetry: Use Mesh Symmetry, Generates a symmetrical mesh using the mesh symmetry configuration
    :type use_mesh_symmetry: bool
    :param use_preserve_sharp: Preserve Sharp, Try to preserve sharp features on the mesh
    :type use_preserve_sharp: bool
    :param use_preserve_boundary: Preserve Mesh Boundary, Try to preserve mesh boundary on the mesh
    :type use_preserve_boundary: bool
    :param preserve_paint_mask: Preserve Paint Mask, Reproject the paint mask onto the new mesh
    :type preserve_paint_mask: bool
    :param smooth_normals: Smooth Normals, Set the output mesh normals to smooth
    :type smooth_normals: bool
    :param mode: Mode, How to specify the amount of detail for the new mesh * RATIO Ratio -- Specify target number of faces relative to the current mesh. * EDGE Edge Length -- Input target edge length in the new mesh. * FACES Faces -- Input target number of faces in the new mesh.
    :type mode: typing.Union[str, int]
    :param target_ratio: Ratio, Relative number of faces compared to the current mesh
    :type target_ratio: float
    :param target_edge_length: Edge Length, Target edge length in the new mesh
    :type target_edge_length: float
    :param target_faces: Number of Faces, Approximate number of faces (quads) in the new mesh
    :type target_faces: int
    :param mesh_area: Old Object Face Area, This property is only used to cache the object area for later calculations
    :type mesh_area: float
    :param seed: Seed, Random seed to use with the solver. Different seeds will cause the remesher to come up with different quad layouts on the mesh
    :type seed: int
    '''

    pass


def quick_explode(style: typing.Union[str, int] = 'EXPLODE',
                  amount: int = 100,
                  frame_duration: int = 50,
                  frame_start: int = 1,
                  frame_end: int = 10,
                  velocity: float = 1.0,
                  fade: bool = True):
    ''' Make selected objects explode :File: startup/bl_operators/object_quick_effects.py\:255 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/object_quick_effects.py#L255> __

    :param style: Explode Style
    :type style: typing.Union[str, int]
    :param amount: Number of Pieces
    :type amount: int
    :param frame_duration: Duration
    :type frame_duration: int
    :param frame_start: Start Frame
    :type frame_start: int
    :param frame_end: End Frame
    :type frame_end: int
    :param velocity: Outwards Velocity
    :type velocity: float
    :param fade: Fade, Fade the pieces over time
    :type fade: bool
    '''

    pass


def quick_fur(density: typing.Union[str, int] = 'MEDIUM',
              length: float = 0.1,
              radius: float = 0.001,
              view_percentage: float = 1.0,
              apply_hair_guides: bool = True,
              use_noise: bool = True,
              use_frizz: bool = True):
    ''' Add a fur setup to the selected objects :File: startup/bl_operators/object_quick_effects.py\:86 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/object_quick_effects.py#L86> __

    :param density: Density
    :type density: typing.Union[str, int]
    :param length: Length
    :type length: float
    :param radius: Hair Radius
    :type radius: float
    :param view_percentage: View Percentage
    :type view_percentage: float
    :param apply_hair_guides: Apply Hair Guides
    :type apply_hair_guides: bool
    :param use_noise: Noise
    :type use_noise: bool
    :param use_frizz: Frizz
    :type use_frizz: bool
    '''

    pass


def quick_liquid(show_flows: bool = False):
    ''' Make selected objects liquid :File: startup/bl_operators/object_quick_effects.py\:536 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/object_quick_effects.py#L536> __

    :param show_flows: Render Liquid Objects, Keep the liquid objects visible during rendering
    :type show_flows: bool
    '''

    pass


def quick_smoke(style: typing.Union[str, int] = 'SMOKE',
                show_flows: bool = False):
    ''' Use selected objects as smoke emitters :File: startup/bl_operators/object_quick_effects.py\:431 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/object_quick_effects.py#L431> __

    :param style: Smoke Style
    :type style: typing.Union[str, int]
    :param show_flows: Render Smoke Objects, Keep the smoke objects visible during rendering
    :type show_flows: bool
    '''

    pass


def randomize_transform(random_seed: int = 0,
                        use_delta: bool = False,
                        use_loc: bool = True,
                        loc: 'mathutils.Vector' = (0.0, 0.0, 0.0),
                        use_rot: bool = True,
                        rot: 'mathutils.Euler' = (0.0, 0.0, 0.0),
                        use_scale: bool = True,
                        scale_even: bool = False,
                        scale: typing.List[float] = (1.0, 1.0, 1.0)):
    ''' Randomize objects location, rotation, and scale :File: startup/bl_operators/object_randomize_transform.py\:157 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/object_randomize_transform.py#L157> __

    :param random_seed: Random Seed, Seed value for the random generator
    :type random_seed: int
    :param use_delta: Transform Delta, Randomize delta transform values instead of regular transform
    :type use_delta: bool
    :param use_loc: Randomize Location, Randomize the location values
    :type use_loc: bool
    :param loc: Location, Maximum distance the objects can spread over each axis
    :type loc: 'mathutils.Vector'
    :param use_rot: Randomize Rotation, Randomize the rotation values
    :type use_rot: bool
    :param rot: Rotation, Maximum rotation over each axis
    :type rot: 'mathutils.Euler'
    :param use_scale: Randomize Scale, Randomize the scale values
    :type use_scale: bool
    :param scale_even: Scale Even, Use the same scale value for all axis
    :type scale_even: bool
    :param scale: Scale, Maximum scale randomization over each axis
    :type scale: typing.List[float]
    '''

    pass


def reset_override_library():
    ''' Reset the selected local overrides to their linked references values

    '''

    pass


def rotation_clear(clear_delta: bool = False):
    ''' Clear the object's rotation

    :param clear_delta: Clear Delta, Clear delta rotation in addition to clearing the normal rotation transform
    :type clear_delta: bool
    '''

    pass


def scale_clear(clear_delta: bool = False):
    ''' Clear the object's scale

    :param clear_delta: Clear Delta, Clear delta scale in addition to clearing the normal scale transform
    :type clear_delta: bool
    '''

    pass


def select_all(action: typing.Union[str, int] = 'TOGGLE'):
    ''' Change selection of all visible objects in scene

    :param action: Action, Selection action to execute * TOGGLE Toggle -- Toggle selection for all elements. * SELECT Select -- Select all elements. * DESELECT Deselect -- Deselect all elements. * INVERT Invert -- Invert selection of all elements.
    :type action: typing.Union[str, int]
    '''

    pass


def select_by_type(extend: bool = False,
                   type: typing.Union[str, int] = 'MESH'):
    ''' Select all visible objects that are of a type

    :param extend: Extend, Extend selection instead of deselecting everything first
    :type extend: bool
    :param type: Type
    :type type: typing.Union[str, int]
    '''

    pass


def select_camera(extend: bool = False):
    ''' Select the active camera :File: startup/bl_operators/object.py\:116 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/object.py#L116> __

    :param extend: Extend, Extend the selection
    :type extend: bool
    '''

    pass


def select_grouped(extend: bool = False,
                   type: typing.Union[str, int] = 'CHILDREN_RECURSIVE'):
    ''' Select all visible objects grouped by various properties

    :param extend: Extend, Extend selection instead of deselecting everything first
    :type extend: bool
    :param type: Type * CHILDREN_RECURSIVE Children. * CHILDREN Immediate Children. * PARENT Parent. * SIBLINGS Siblings -- Shared parent. * TYPE Type -- Shared object type. * COLLECTION Collection -- Shared collection. * HOOK Hook. * PASS Pass -- Render pass index. * COLOR Color -- Object color. * PROPERTIES Properties -- Game Properties. * KEYINGSET Keying Set -- Objects included in active Keying Set. * LIGHT_TYPE Light Type -- Matching light types.
    :type type: typing.Union[str, int]
    '''

    pass


def select_hierarchy(direction: typing.Union[str, int] = 'PARENT',
                     extend: bool = False):
    ''' Select object relative to the active object's position in the hierarchy :File: startup/bl_operators/object.py\:166 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/object.py#L166> __

    :param direction: Direction, Direction to select in the hierarchy
    :type direction: typing.Union[str, int]
    :param extend: Extend, Extend the existing selection
    :type extend: bool
    '''

    pass


def select_less():
    ''' Deselect objects at the boundaries of parent/child relationships

    '''

    pass


def select_linked(extend: bool = False,
                  type: typing.Union[str, int] = 'OBDATA'):
    ''' Select all visible objects that are linked

    :param extend: Extend, Extend selection instead of deselecting everything first
    :type extend: bool
    :param type: Type
    :type type: typing.Union[str, int]
    '''

    pass


def select_mirror(extend: bool = False):
    ''' Select the mirror objects of the selected object e.g. "L.sword" and "R.sword"

    :param extend: Extend, Extend selection instead of deselecting everything first
    :type extend: bool
    '''

    pass


def select_more():
    ''' Select connected parent/child objects

    '''

    pass


def select_pattern(pattern: str = "*",
                   case_sensitive: bool = False,
                   extend: bool = True):
    ''' Select objects matching a naming pattern :File: startup/bl_operators/object.py\:39 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/object.py#L39> __

    :param pattern: Pattern, Name filter using '*', '?' and '[abc]' unix style wildcards
    :type pattern: str
    :param case_sensitive: Case Sensitive, Do a case sensitive compare
    :type case_sensitive: bool
    :param extend: Extend, Extend the existing selection
    :type extend: bool
    '''

    pass


def select_random(ratio: float = 0.5,
                  seed: int = 0,
                  action: typing.Union[str, int] = 'SELECT'):
    ''' Select or deselect random visible objects

    :param ratio: Ratio, Portion of items to select randomly
    :type ratio: float
    :param seed: Random Seed, Seed for the random number generator
    :type seed: int
    :param action: Action, Selection action to execute * SELECT Select -- Select all elements. * DESELECT Deselect -- Deselect all elements.
    :type action: typing.Union[str, int]
    '''

    pass


def select_same_collection(collection: str = ""):
    ''' Select object in the same collection

    :param collection: Collection, Name of the collection to select
    :type collection: str
    '''

    pass


def shade_flat():
    ''' Render and display faces uniform, using Face Normals

    '''

    pass


def shade_smooth(use_auto_smooth: bool = False,
                 auto_smooth_angle: float = 0.523599):
    ''' Render and display faces smooth, using interpolated Vertex Normals

    :param use_auto_smooth: Auto Smooth, Enable automatic smooth based on smooth/sharp faces/edges and angle between faces
    :type use_auto_smooth: bool
    :param auto_smooth_angle: Angle, Maximum angle between face normals that will be considered as smooth (unused if custom split normals data are available)
    :type auto_smooth_angle: float
    '''

    pass


def shaderfx_add(type: typing.Union[str, int] = 'FX_BLUR'):
    ''' Add a visual effect to the active object

    :param type: Type
    :type type: typing.Union[str, int]
    '''

    pass


def shaderfx_copy(shaderfx: str = ""):
    ''' Duplicate effect at the same position in the stack

    :param shaderfx: Shader, Name of the shaderfx to edit
    :type shaderfx: str
    '''

    pass


def shaderfx_move_down(shaderfx: str = ""):
    ''' Move effect down in the stack

    :param shaderfx: Shader, Name of the shaderfx to edit
    :type shaderfx: str
    '''

    pass


def shaderfx_move_to_index(shaderfx: str = "", index: int = 0):
    ''' Change the effect's position in the list so it evaluates after the set number of others

    :param shaderfx: Shader, Name of the shaderfx to edit
    :type shaderfx: str
    :param index: Index, The index to move the effect to
    :type index: int
    '''

    pass


def shaderfx_move_up(shaderfx: str = ""):
    ''' Move effect up in the stack

    :param shaderfx: Shader, Name of the shaderfx to edit
    :type shaderfx: str
    '''

    pass


def shaderfx_remove(shaderfx: str = "", report: bool = False):
    ''' Remove a effect from the active grease pencil object

    :param shaderfx: Shader, Name of the shaderfx to edit
    :type shaderfx: str
    :param report: Report, Create a notification after the operation
    :type report: bool
    '''

    pass


def shape_key_add(from_mix: bool = True):
    ''' Add shape key to the object

    :param from_mix: From Mix, Create the new shape key from the existing mix of keys
    :type from_mix: bool
    '''

    pass


def shape_key_clear():
    ''' Clear weights for all shape keys

    '''

    pass


def shape_key_mirror(use_topology: bool = False):
    ''' Mirror the current shape key along the local X axis

    :param use_topology: Topology Mirror, Use topology based mirroring (for when both sides of mesh have matching, unique topology)
    :type use_topology: bool
    '''

    pass


def shape_key_move(type: typing.Union[str, int] = 'TOP'):
    ''' Move the active shape key up/down in the list

    :param type: Type * TOP Top -- Top of the list. * UP Up. * DOWN Down. * BOTTOM Bottom -- Bottom of the list.
    :type type: typing.Union[str, int]
    '''

    pass


def shape_key_remove(all: bool = False, apply_mix: bool = False):
    ''' Remove shape key from the object

    :param all: All, Remove all shape keys
    :type all: bool
    :param apply_mix: Apply Mix, Apply current mix of shape keys to the geometry before removing them
    :type apply_mix: bool
    '''

    pass


def shape_key_retime():
    ''' Resets the timing for absolute shape keys

    '''

    pass


def shape_key_transfer(mode: typing.Union[str, int] = 'OFFSET',
                       use_clamp: bool = False):
    ''' Copy the active shape key of another selected object to this one :File: startup/bl_operators/object.py\:464 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/object.py#L464> __

    :param mode: Transformation Mode, Relative shape positions to the new shape method * OFFSET Offset -- Apply the relative positional offset. * RELATIVE_FACE Relative Face -- Calculate relative position (using faces). * RELATIVE_EDGE Relative Edge -- Calculate relative position (using edges).
    :type mode: typing.Union[str, int]
    :param use_clamp: Clamp Offset, Clamp the transformation to the distance each vertex moves in the original shape
    :type use_clamp: bool
    '''

    pass


def skin_armature_create(modifier: str = ""):
    ''' Create an armature that parallels the skin layout

    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: str
    '''

    pass


def skin_loose_mark_clear(action: typing.Union[str, int] = 'MARK'):
    ''' Mark/clear selected vertices as loose

    :param action: Action * MARK Mark -- Mark selected vertices as loose. * CLEAR Clear -- Set selected vertices as not loose.
    :type action: typing.Union[str, int]
    '''

    pass


def skin_radii_equalize():
    ''' Make skin radii of selected vertices equal on each axis

    '''

    pass


def skin_root_mark():
    ''' Mark selected vertices as roots

    '''

    pass


def speaker_add(enter_editmode: bool = False,
                align: typing.Union[str, int] = 'WORLD',
                location: 'mathutils.Vector' = (0.0, 0.0, 0.0),
                rotation: 'mathutils.Euler' = (0.0, 0.0, 0.0),
                scale: 'mathutils.Vector' = (0.0, 0.0, 0.0)):
    ''' Add a speaker object to the scene

    :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
    :type enter_editmode: bool
    :param align: Align, The alignment of the new object * WORLD World -- Align the new object to the world. * VIEW View -- Align the new object to the view. * CURSOR 3D Cursor -- Use the 3D cursor orientation for the new object.
    :type align: typing.Union[str, int]
    :param location: Location, Location for the newly added object
    :type location: 'mathutils.Vector'
    :param rotation: Rotation, Rotation for the newly added object
    :type rotation: 'mathutils.Euler'
    :param scale: Scale, Scale for the newly added object
    :type scale: 'mathutils.Vector'
    '''

    pass


def subdivision_set(level: int = 1, relative: bool = False):
    ''' Sets a Subdivision Surface level (1 to 5) :File: startup/bl_operators/object.py\:234 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/object.py#L234> __

    :param level: Level
    :type level: int
    :param relative: Relative, Apply the subdivision surface level as an offset relative to the current level
    :type relative: bool
    '''

    pass


def surfacedeform_bind(modifier: str = ""):
    ''' Bind mesh to target in surface deform modifier

    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: str
    '''

    pass


def text_add(radius: float = 1.0,
             enter_editmode: bool = False,
             align: typing.Union[str, int] = 'WORLD',
             location: 'mathutils.Vector' = (0.0, 0.0, 0.0),
             rotation: 'mathutils.Euler' = (0.0, 0.0, 0.0),
             scale: 'mathutils.Vector' = (0.0, 0.0, 0.0)):
    ''' Add a text object to the scene

    :param radius: Radius
    :type radius: float
    :param enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
    :type enter_editmode: bool
    :param align: Align, The alignment of the new object * WORLD World -- Align the new object to the world. * VIEW View -- Align the new object to the view. * CURSOR 3D Cursor -- Use the 3D cursor orientation for the new object.
    :type align: typing.Union[str, int]
    :param location: Location, Location for the newly added object
    :type location: 'mathutils.Vector'
    :param rotation: Rotation, Rotation for the newly added object
    :type rotation: 'mathutils.Euler'
    :param scale: Scale, Scale for the newly added object
    :type scale: 'mathutils.Vector'
    '''

    pass


def track_clear(type: typing.Union[str, int] = 'CLEAR'):
    ''' Clear tracking constraint or flag from object

    :param type: Type
    :type type: typing.Union[str, int]
    '''

    pass


def track_set(type: typing.Union[str, int] = 'DAMPTRACK'):
    ''' Make the object track another object, using various methods/constraints

    :param type: Type
    :type type: typing.Union[str, int]
    '''

    pass


def transfer_mode(use_flash_on_transfer: bool = True):
    ''' Switches the active object and assigns the same mode to a new one under the mouse cursor, leaving the active mode in the current one

    :param use_flash_on_transfer: Flash On Transfer, Flash the target object when transferring the mode
    :type use_flash_on_transfer: bool
    '''

    pass


def transform_apply(location: bool = True,
                    rotation: bool = True,
                    scale: bool = True,
                    properties: bool = True,
                    isolate_users: bool = False):
    ''' Apply the object's transformation to its data

    :param location: Location
    :type location: bool
    :param rotation: Rotation
    :type rotation: bool
    :param scale: Scale
    :type scale: bool
    :param properties: Apply Properties, Modify properties such as curve vertex radius, font size and bone envelope
    :type properties: bool
    :param isolate_users: Isolate Multi User Data, Create new object-data users if needed
    :type isolate_users: bool
    '''

    pass


def transform_axis_target():
    ''' Interactively point cameras and lights to a location (Ctrl translates)

    '''

    pass


def transform_to_mouse(name: str = "",
                       session_uuid: int = 0,
                       matrix: 'mathutils.Matrix' = ((0.0, 0.0, 0.0, 0.0),
                                                     (0.0, 0.0, 0.0,
                                                      0.0), (0.0, 0.0, 0.0,
                                                             0.0), (0.0, 0.0,
                                                                    0.0, 0.0)),
                       drop_x: int = 0,
                       drop_y: int = 0):
    ''' Snap selected item(s) to the mouse location

    :param name: Name, Object name to place (uses the active object when this and 'session_uuid' are unset)
    :type name: str
    :param session_uuid: Session UUID, Session UUID of the object to place (uses the active object when this and 'name' are unset)
    :type session_uuid: int
    :param matrix: Matrix
    :type matrix: 'mathutils.Matrix'
    :param drop_x: Drop X, X-coordinate (screen space) to place the new object under
    :type drop_x: int
    :param drop_y: Drop Y, Y-coordinate (screen space) to place the new object under
    :type drop_y: int
    '''

    pass


def transforms_to_deltas(mode: typing.Union[str, int] = 'ALL',
                         reset_values: bool = True):
    ''' Convert normal object transforms to delta transforms, any existing delta transforms will be included as well :File: startup/bl_operators/object.py\:715 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/object.py#L715> __

    :param mode: Mode, Which transforms to transfer * ALL All Transforms -- Transfer location, rotation, and scale transforms. * LOC Location -- Transfer location transforms only. * ROT Rotation -- Transfer rotation transforms only. * SCALE Scale -- Transfer scale transforms only.
    :type mode: typing.Union[str, int]
    :param reset_values: Reset Values, Clear transform values after transferring to deltas
    :type reset_values: bool
    '''

    pass


def unlink_data():
    ''' Undocumented, consider contributing <https://developer.blender.org/> __.

    '''

    pass


def vertex_group_add():
    ''' Add a new vertex group to the active object

    '''

    pass


def vertex_group_assign():
    ''' Assign the selected vertices to the active vertex group

    '''

    pass


def vertex_group_assign_new():
    ''' Assign the selected vertices to a new vertex group

    '''

    pass


def vertex_group_clean(group_select_mode: typing.Union[str, int] = '',
                       limit: float = 0.0,
                       keep_single: bool = False):
    ''' Remove vertex group assignments which are not required

    :param group_select_mode: Subset, Define which subset of groups shall be used
    :type group_select_mode: typing.Union[str, int]
    :param limit: Limit, Remove vertices which weight is below or equal to this limit
    :type limit: float
    :param keep_single: Keep Single, Keep verts assigned to at least one group when cleaning
    :type keep_single: bool
    '''

    pass


def vertex_group_copy():
    ''' Make a copy of the active vertex group

    '''

    pass


def vertex_group_copy_to_selected():
    ''' Replace vertex groups of selected objects by vertex groups of active object

    '''

    pass


def vertex_group_deselect():
    ''' Deselect all selected vertices assigned to the active vertex group

    '''

    pass


def vertex_group_invert(group_select_mode: typing.Union[str, int] = '',
                        auto_assign: bool = True,
                        auto_remove: bool = True):
    ''' Invert active vertex group's weights

    :param group_select_mode: Subset, Define which subset of groups shall be used
    :type group_select_mode: typing.Union[str, int]
    :param auto_assign: Add Weights, Add vertices from groups that have zero weight before inverting
    :type auto_assign: bool
    :param auto_remove: Remove Weights, Remove vertices from groups that have zero weight after inverting
    :type auto_remove: bool
    '''

    pass


def vertex_group_levels(group_select_mode: typing.Union[str, int] = '',
                        offset: float = 0.0,
                        gain: float = 1.0):
    ''' Add some offset and multiply with some gain the weights of the active vertex group

    :param group_select_mode: Subset, Define which subset of groups shall be used
    :type group_select_mode: typing.Union[str, int]
    :param offset: Offset, Value to add to weights
    :type offset: float
    :param gain: Gain, Value to multiply weights by
    :type gain: float
    '''

    pass


def vertex_group_limit_total(group_select_mode: typing.Union[str, int] = '',
                             limit: int = 4):
    ''' Limit deform weights associated with a vertex to a specified number by removing lowest weights

    :param group_select_mode: Subset, Define which subset of groups shall be used
    :type group_select_mode: typing.Union[str, int]
    :param limit: Limit, Maximum number of deform weights
    :type limit: int
    '''

    pass


def vertex_group_lock(action: typing.Union[str, int] = 'TOGGLE',
                      mask: typing.Union[str, int] = 'ALL'):
    ''' Change the lock state of all or some vertex groups of active object

    :param action: Action, Lock action to execute on vertex groups * TOGGLE Toggle -- Unlock all vertex groups if there is at least one locked group, lock all in other case. * LOCK Lock -- Lock all vertex groups. * UNLOCK Unlock -- Unlock all vertex groups. * INVERT Invert -- Invert the lock state of all vertex groups.
    :type action: typing.Union[str, int]
    :param mask: Mask, Apply the action based on vertex group selection * ALL All -- Apply action to all vertex groups. * SELECTED Selected -- Apply to selected vertex groups. * UNSELECTED Unselected -- Apply to unselected vertex groups. * INVERT_UNSELECTED Invert Unselected -- Apply the opposite of Lock/Unlock to unselected vertex groups.
    :type mask: typing.Union[str, int]
    '''

    pass


def vertex_group_mirror(mirror_weights: bool = True,
                        flip_group_names: bool = True,
                        all_groups: bool = False,
                        use_topology: bool = False):
    ''' Mirror vertex group, flip weights and/or names, editing only selected vertices, flipping when both sides are selected otherwise copy from unselected

    :param mirror_weights: Mirror Weights, Mirror weights
    :type mirror_weights: bool
    :param flip_group_names: Flip Group Names, Flip vertex group names
    :type flip_group_names: bool
    :param all_groups: All Groups, Mirror all vertex groups weights
    :type all_groups: bool
    :param use_topology: Topology Mirror, Use topology based mirroring (for when both sides of mesh have matching, unique topology)
    :type use_topology: bool
    '''

    pass


def vertex_group_move(direction: typing.Union[str, int] = 'UP'):
    ''' Move the active vertex group up/down in the list

    :param direction: Direction, Direction to move the active vertex group towards
    :type direction: typing.Union[str, int]
    '''

    pass


def vertex_group_normalize():
    ''' Normalize weights of the active vertex group, so that the highest ones are now 1.0

    '''

    pass


def vertex_group_normalize_all(group_select_mode: typing.Union[str, int] = '',
                               lock_active: bool = True):
    ''' Normalize all weights of all vertex groups, so that for each vertex, the sum of all weights is 1.0

    :param group_select_mode: Subset, Define which subset of groups shall be used
    :type group_select_mode: typing.Union[str, int]
    :param lock_active: Lock Active, Keep the values of the active group while normalizing others
    :type lock_active: bool
    '''

    pass


def vertex_group_quantize(group_select_mode: typing.Union[str, int] = '',
                          steps: int = 4):
    ''' Set weights to a fixed number of steps

    :param group_select_mode: Subset, Define which subset of groups shall be used
    :type group_select_mode: typing.Union[str, int]
    :param steps: Steps, Number of steps between 0 and 1
    :type steps: int
    '''

    pass


def vertex_group_remove(all: bool = False, all_unlocked: bool = False):
    ''' Delete the active or all vertex groups from the active object

    :param all: All, Remove all vertex groups
    :type all: bool
    :param all_unlocked: All Unlocked, Remove all unlocked vertex groups
    :type all_unlocked: bool
    '''

    pass


def vertex_group_remove_from(use_all_groups: bool = False,
                             use_all_verts: bool = False):
    ''' Remove the selected vertices from active or all vertex group(s)

    :param use_all_groups: All Groups, Remove from all groups
    :type use_all_groups: bool
    :param use_all_verts: All Vertices, Clear the active group
    :type use_all_verts: bool
    '''

    pass


def vertex_group_select():
    ''' Select all the vertices assigned to the active vertex group

    '''

    pass


def vertex_group_set_active(group: typing.Union[str, int] = ''):
    ''' Set the active vertex group

    :param group: Group, Vertex group to set as active
    :type group: typing.Union[str, int]
    '''

    pass


def vertex_group_smooth(group_select_mode: typing.Union[str, int] = '',
                        factor: float = 0.5,
                        repeat: int = 1,
                        expand: float = 0.0):
    ''' Smooth weights for selected vertices

    :param group_select_mode: Subset, Define which subset of groups shall be used
    :type group_select_mode: typing.Union[str, int]
    :param factor: Factor
    :type factor: float
    :param repeat: Iterations
    :type repeat: int
    :param expand: Expand/Contract, Expand/contract weights
    :type expand: float
    '''

    pass


def vertex_group_sort(sort_type: typing.Union[str, int] = 'NAME'):
    ''' Sort vertex groups

    :param sort_type: Sort Type, Sort type
    :type sort_type: typing.Union[str, int]
    '''

    pass


def vertex_parent_set():
    ''' Parent selected objects to the selected vertices

    '''

    pass


def vertex_weight_copy():
    ''' Copy weights from active to selected

    '''

    pass


def vertex_weight_delete(weight_group: int = -1):
    ''' Delete this weight from the vertex (disabled if vertex group is locked)

    :param weight_group: Weight Index, Index of source weight in active vertex group
    :type weight_group: int
    '''

    pass


def vertex_weight_normalize_active_vertex():
    ''' Normalize active vertex's weights

    '''

    pass


def vertex_weight_paste(weight_group: int = -1):
    ''' Copy this group's weight to other selected vertices (disabled if vertex group is locked)

    :param weight_group: Weight Index, Index of source weight in active vertex group
    :type weight_group: int
    '''

    pass


def vertex_weight_set_active(weight_group: int = -1):
    ''' Set as active vertex group

    :param weight_group: Weight Index, Index of source weight in active vertex group
    :type weight_group: int
    '''

    pass


def visual_transform_apply():
    ''' Apply the object's visual transformation to its data

    '''

    pass


def volume_add(align: typing.Union[str, int] = 'WORLD',
               location: 'mathutils.Vector' = (0.0, 0.0, 0.0),
               rotation: 'mathutils.Euler' = (0.0, 0.0, 0.0),
               scale: 'mathutils.Vector' = (0.0, 0.0, 0.0)):
    ''' Add a volume object to the scene

    :param align: Align, The alignment of the new object * WORLD World -- Align the new object to the world. * VIEW View -- Align the new object to the view. * CURSOR 3D Cursor -- Use the 3D cursor orientation for the new object.
    :type align: typing.Union[str, int]
    :param location: Location, Location for the newly added object
    :type location: 'mathutils.Vector'
    :param rotation: Rotation, Rotation for the newly added object
    :type rotation: 'mathutils.Euler'
    :param scale: Scale, Scale for the newly added object
    :type scale: 'mathutils.Vector'
    '''

    pass


def volume_import(
        filepath: str = "",
        directory: str = "",
        files: typing.
        Union[typing.Dict[str, 'bpy.types.OperatorFileListElement'], typing.
              List['bpy.types.OperatorFileListElement'],
              'bpy_prop_collection'] = None,
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
        filter_volume: bool = True,
        filter_folder: bool = True,
        filter_blenlib: bool = False,
        filemode: int = 9,
        relative_path: bool = True,
        display_type: typing.Union[str, int] = 'DEFAULT',
        sort_method: typing.Union[str, int] = '',
        use_sequence_detection: bool = True,
        align: typing.Union[str, int] = 'WORLD',
        location: 'mathutils.Vector' = (0.0, 0.0, 0.0),
        rotation: 'mathutils.Euler' = (0.0, 0.0, 0.0),
        scale: 'mathutils.Vector' = (0.0, 0.0, 0.0)):
    ''' Import OpenVDB volume file

    :param filepath: File Path, Path to file
    :type filepath: str
    :param directory: Directory, Directory of the file
    :type directory: str
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
    :type display_type: typing.Union[str, int]
    :param sort_method: File sorting mode
    :type sort_method: typing.Union[str, int]
    :param use_sequence_detection: Detect Sequences, Automatically detect animated sequences in selected volume files (based on file names)
    :type use_sequence_detection: bool
    :param align: Align, The alignment of the new object * WORLD World -- Align the new object to the world. * VIEW View -- Align the new object to the view. * CURSOR 3D Cursor -- Use the 3D cursor orientation for the new object.
    :type align: typing.Union[str, int]
    :param location: Location, Location for the newly added object
    :type location: 'mathutils.Vector'
    :param rotation: Rotation, Rotation for the newly added object
    :type rotation: 'mathutils.Euler'
    :param scale: Scale, Scale for the newly added object
    :type scale: 'mathutils.Vector'
    '''

    pass


def voxel_remesh():
    ''' Calculates a new manifold mesh based on the volume of the current mesh. All data layers will be lost

    '''

    pass


def voxel_size_edit():
    ''' Modify the mesh voxel size interactively used in the voxel remesher

    '''

    pass
