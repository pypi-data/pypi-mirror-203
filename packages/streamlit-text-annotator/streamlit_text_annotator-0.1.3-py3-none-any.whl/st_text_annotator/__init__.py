import os
import random

import streamlit.components.v1 as components

parent_dir = os.path.dirname(os.path.abspath(__file__))
build_dir = os.path.join(parent_dir, "frontend/build")
_component_func = components.declare_component("StTextAnnotator", path=build_dir)

def StTextAnnotator(text, annotations):
    """Create a new instance of "StTextAnnotator".

    Parameters
    ----------
    text : str
        The text to be annotated

    annotations : list
        If the text has already been annotated, the annotations can be passed to the component in the form of a list of dictionaries with the following structure:
        [
            [
                {
                    label: "label",
                    start: 0,
                    end: 10
                },
                {
                    label: "label",
                    start: 0,
                    end: 10
                }
            ],
            [
                {
                    label: "label",
                    start: 0,
                    end: 10
                }
            ]
        ]
        
    Returns
    -------
    dict or None
        The annotations made by the user in the form of a dictionary with the following structure: 
        {
            label: "label",
            start: 0,
            end: 10
        }

    """
    
    # Call through to our private component function. Arguments we pass here
    # will be sent to the frontend, where they'll be available in an "args"
    # dictionary.
    #
    # "default" is a special argument that specifies the initial return
    # value of the component before the user has interacted with it.
    component_value = _component_func(text=text, annotations=annotations)

    # We could modify the value returned from the component if we wanted.
    # There's no need to do this in our simple example - but it's an option.
    return component_value

