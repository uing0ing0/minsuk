from pages import render
from utils.page import PageModel
from utils.init import init_once
import streamlit as st
import os


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
