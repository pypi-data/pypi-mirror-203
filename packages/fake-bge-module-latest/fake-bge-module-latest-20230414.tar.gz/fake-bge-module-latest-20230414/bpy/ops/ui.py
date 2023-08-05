import sys
import typing
import mathutils


def assign_default_button():
    ''' Set this property's current value as the new default

    '''

    pass


def button_execute(skip_depressed: bool = False):
    ''' Presses active button

    :param skip_depressed: Skip Depressed
    :type skip_depressed: bool
    '''

    pass


def button_string_clear():
    ''' Unsets the text of the active button

    '''

    pass


def copy_as_driver_button():
    ''' Create a new driver with this property as input, and copy it to the clipboard. Use Paste Driver to add it to the target property, or Paste Driver Variables to extend an existing driver

    '''

    pass


def copy_data_path_button(full_path: bool = False):
    ''' Copy the RNA data path for this property to the clipboard

    :param full_path: full_path, Copy full data path
    :type full_path: bool
    '''

    pass


def copy_python_command_button():
    ''' Copy the Python command matching this button

    '''

    pass


def copy_to_selected_button(all: bool = True):
    ''' Copy the property's value from the active item to the same property of all selected items if the same property exists

    :param all: All, Copy to selected all elements of the array
    :type all: bool
    '''

    pass


def drop_color(color: 'mathutils.Color' = (0.0, 0.0, 0.0),
               gamma: bool = False):
    ''' Drop colors to buttons

    :param color: Color, Source color
    :type color: 'mathutils.Color'
    :param gamma: Gamma Corrected, The source color is gamma corrected
    :type gamma: bool
    '''

    pass


def drop_material(session_uuid: int = 0):
    ''' Drag material to Material slots in Properties

    :param session_uuid: Session UUID, Session UUID of the data-block to use by the operator
    :type session_uuid: int
    '''

    pass


def drop_name(string: str = ""):
    ''' Drop name to button

    :param string: String, The string value to drop into the button
    :type string: str
    '''

    pass


def editsource():
    ''' Edit UI source code of the active button

    '''

    pass


def edittranslation_init():
    ''' Edit i18n in current language for the active button

    '''

    pass


def eyedropper_color():
    ''' Sample a color from the Blender window to store in a property

    '''

    pass


def eyedropper_colorramp():
    ''' Sample a color band

    '''

    pass


def eyedropper_colorramp_point():
    ''' Point-sample a color band

    '''

    pass


def eyedropper_depth():
    ''' Sample depth from the 3D view

    '''

    pass


def eyedropper_driver(mapping_type: typing.Union[int, str] = 'SINGLE_MANY'):
    ''' Pick a property to use as a driver target

    :param mapping_type: Mapping Type, Method used to match target and driven properties * SINGLE_MANY All from Target -- Drive all components of this property using the target picked. * DIRECT Single from Target -- Drive this component of this property using the target picked. * MATCH Match Indices -- Create drivers for each pair of corresponding elements. * NONE_ALL Manually Create Later -- Create drivers for all properties without assigning any targets yet. * NONE_SINGLE Manually Create Later (Single) -- Create driver for this property only and without assigning any targets yet.
    :type mapping_type: typing.Union[int, str]
    '''

    pass


def eyedropper_gpencil_color(mode: typing.Union[int, str] = 'MATERIAL'):
    ''' Sample a color from the Blender Window and create Grease Pencil material

    :param mode: Mode
    :type mode: typing.Union[int, str]
    '''

    pass


def eyedropper_id():
    ''' Sample a data-block from the 3D View to store in a property

    '''

    pass


def jump_to_target_button():
    ''' Switch to the target object or bone

    '''

    pass


def list_start_filter():
    ''' Start entering filter text for the list in focus

    '''

    pass


def override_idtemplate_clear():
    ''' Delete the selected local override and relink its usages to the linked data-block if possible, else reset it and mark it as non editable

    '''

    pass


def override_idtemplate_make():
    ''' Create a local override of the selected linked data-block, and its hierarchy of dependencies

    '''

    pass


def override_idtemplate_reset():
    ''' Reset the selected local override to its linked reference values

    '''

    pass


def override_remove_button(all: bool = True):
    ''' Remove an override operation

    :param all: All, Reset to default values all elements of the array
    :type all: bool
    '''

    pass


def override_type_set_button(all: bool = True,
                             type: typing.Union[int, str] = 'REPLACE'):
    ''' Create an override operation, or set the type of an existing one

    :param all: All, Reset to default values all elements of the array
    :type all: bool
    :param type: Type, Type of override operation * NOOP NoOp -- 'No-Operation', place holder preventing automatic override to ever affect the property. * REPLACE Replace -- Completely replace value from linked data by local one. * DIFFERENCE Difference -- Store difference to linked data value. * FACTOR Factor -- Store factor to linked data value (useful e.g. for scale).
    :type type: typing.Union[int, str]
    '''

    pass


def reloadtranslation():
    ''' Force a full reload of UI translation

    '''

    pass


def reset_default_button(all: bool = True):
    ''' Reset this property's value to its default value

    :param all: All, Reset to default values all elements of the array
    :type all: bool
    '''

    pass


def unset_property_button():
    ''' Clear the property and use default or generated value in operators

    '''

    pass


def view_drop():
    ''' Drag and drop onto a data-set or item within the data-set

    '''

    pass


def view_item_rename():
    ''' Rename the active item in the data-set view

    '''

    pass
