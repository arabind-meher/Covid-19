import streamlit as st

from api import Covid19API


def app():
    st.title('Covid-19 (Corona Virus)')
    st.write('\n\n')

    st.write('### Worldwide status')
    world, countries = Covid19API.world_summary()
    st.json(world)

    st.write('\n\n')
    st.write('### Country wise status')
    st.table(countries)
