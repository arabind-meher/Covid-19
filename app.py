import streamlit as st

from api import Covid19API
import world
import india

pages = {
    'World': world,
    'India': india
}

if __name__ == '__main__':
    st.sidebar.title('Navigation')
    choice = st.sidebar.radio('Go to:', list(pages.keys()))
    page = pages[choice]
    page.app()

    st.sidebar.write('\n\n')

    world_status = Covid19API.world()
    st.sidebar.write('## Worldwide')
    st.sidebar.json(world_status)
