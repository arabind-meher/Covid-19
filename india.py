import streamlit as st

from api import Covid19API


def app():
    st.title('Covid-19 (Corona Virus)')
    st.write('\n\n')

    st.write('### India')
    country_current_status, country_status_table = Covid19API.india_summary()
    st.json(country_current_status)

    st.write('#### Cases')
    st.line_chart(country_status_table['New Cases'])
    st.write('\n')

    st.write('#### Deaths')
    st.line_chart(country_status_table['New Deaths'])
    st.write('\n')

    st.write('#### Recovered')
    st.line_chart(country_status_table['New Recovered'])
    st.write('\n')

    st.write('#### Active Cases')
    st.line_chart(country_status_table['Active Cases'])
    st.write('\n')
