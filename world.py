# import packages
import streamlit as st

# import local packages
from api import Covid19API


# web app
def app():
    # title
    st.title('Covid-19 (Corona Virus)')
    st.write('\n\n')

    # worldwide status
    st.write('### Worldwide status')
    world, countries = Covid19API.world_summary()
    st.json(world)
    st.write('\n\n')

    # country wise status (table)
    st.write('### Country wise status')
    st.table(countries)
