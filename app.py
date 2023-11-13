import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np

st.set_page_config(layout='wide')

df = pd.read_csv('india_main.csv')
st.sidebar.title("Select Parameter")

l = df['State'].unique().tolist()
l.sort()
l.insert(0, 'India')

select_region = st.sidebar.selectbox('Choose Region Here', l)
primary = st.sidebar.selectbox('Choose Primary Parameter', df.columns[9:])
secondary = st.sidebar.selectbox('Choose Secondary Parameter', df.columns[9:])
plot = st.sidebar.button('Plot Map')

if plot:
    st.write('--> Size represents primary parameter')
    st.write('--> Color represents secondary parameter')
    if select_region == 'India':
        fig = px.scatter_mapbox(df, lat='Latitude', lon='Longitude', zoom=4,
                                size=primary, color=secondary, size_max=35, hover_name='District',
                                mapbox_style='carto-positron', width=1200, height=700, color_continuous_scale='Rainbow')
        st.plotly_chart(fig, use_container_width=True)
    else:
        state_df = df[df['State'] == select_region]
        fig = px.scatter_mapbox(state_df, lat='Latitude', lon='Longitude', zoom=4,
                                size=primary, color=secondary, size_max=35, hover_name='District',
                                mapbox_style='carto-positron', width=1200, height=700, color_continuous_scale='Rainbow')
        st.plotly_chart(fig, use_container_width=True)
