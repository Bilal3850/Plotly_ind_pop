import streamlit as st
import pandas as pd
import matplotlib as plt
import plotly.express as px

st.set_page_config(page_title='India_Pop_Visual', page_icon='📈', layout="wide")

ind_pop = pd.read_csv('Summerize_Ind_pop.csv')
list_of_states = list(ind_pop['State'].unique())
list_of_states.insert(0, 'Overall India')


st.sidebar.title('Indian population Visualise')
select_state = st.sidebar.selectbox('Select State', list_of_states)
Primary = st.sidebar.selectbox('Select Primary Parameter', sorted(ind_pop.columns[6:]))
secondary = st.sidebar.selectbox('Select Secondary Parameter', sorted(ind_pop.columns[6:]))

plot = st.sidebar.button('Plot Graph')

if plot:
    st.text('Size represent primary parameter')
    st.text('Color represents secondary parameter')
    if select_state == "Overall India":
    # plot over all india
        fig = px.scatter_map(ind_pop, lat="Latitude", lon="Longitude", size=Primary, color=secondary,zoom=3.5,
                  map_style="carto-positron", width=1200, height=600, hover_name='District')
        st.plotly_chart(fig, use_container_width=True, theme=None)

    else:
        # plot for state
        state_df = ind_pop[ind_pop['State'] == select_state]
        fig = px.scatter_map(state_df, lat="Latitude", lon="Longitude", size=Primary, color=secondary,zoom=6,
                  map_style="carto-positron", width=1200, height=600, hover_name='District', text='District')
        st.plotly_chart(fig, use_container_width=True, theme=None)
    

