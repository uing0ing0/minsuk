import os


import sys

# Get the current script directory
current_script_directory = os.path.dirname(os.path.abspath(__file__))

# Get the parent directory
parent_directory = os.path.dirname(current_script_directory)

# Add the parent directory to the system path
sys.path.append(parent_directory)



from pages import render
from utils.page import PageModel
from utils.init import init_once
import streamlit as st


if __name__ == '__main__':
    # Init
    settings = init_once()

    with st.sidebar:
        st.markdown(
            """
            <style>
            [data-testid="stSidebar"] {
                background-color: #ed1b1a;  /* Change this to your desired color */

            }
            </style>
            """,
            unsafe_allow_html=True
        )


    # Configure metadata
    name = os.path.basename(__file__)[:-3]

    # Configure home page
    model = PageModel(
        settings=settings,
        input=name,
        function=name,
        output_type='pydantic',
    )

    # Draw
    render(model)
