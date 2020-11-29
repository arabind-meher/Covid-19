# import packages
import streamlit as st

# import local packages
from api import Covid19API


# web app
def app():
    # title
    st.title('Covid-19 (Corona Virus)')
    st.write('\n\n')

    # country status
    st.write('### India')
    country_current_status, country_status_table = Covid19API.india_summary()
    st.json(country_current_status)

    """ Graphs """
    # total cases
    st.write('#### Cases')
    st.line_chart(country_status_table['New Cases'])
    st.write('\n')

    # total deaths
    st.write('#### Deaths')
    st.line_chart(country_status_table['New Deaths'])
    st.write('\n')

    # total recovered
    st.write('#### Recovered')
    st.line_chart(country_status_table['New Recovered'])
    st.write('\n')

    # active cases
    st.write('#### Active Cases')
    st.line_chart(country_status_table['Active Cases'])
    st.write('\n')
    """ ***** """
