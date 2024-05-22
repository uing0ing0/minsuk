import os

import pages
from utils.page import PageModel
from utils.init import init_once

logo_path = "E:\eun\Frontend\logo.jpg.png"

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
    st.image(logo_path, width=80)

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
    pages.render(model)
