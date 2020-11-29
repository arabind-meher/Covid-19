# import packages
import streamlit as st

# import local packages
from api import Covid19API
import world
import india

# pages in website
pages = {
    'World': world,
    'India': india
}

# Main
if __name__ == '__main__':
    # navigation bar
    st.sidebar.title('Navigation')
    # pages in website
    choice = st.sidebar.radio('Go to:', list(pages.keys()))
    page = pages[choice]
    page.app()

    st.sidebar.write('\n\n')

    # worldwide status
    world_status = Covid19API.world()
    st.sidebar.write('## Worldwide')
    st.sidebar.json(world_status)
