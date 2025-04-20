import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

st.set_page_config(layout='wide')

df = pd.read_csv('India.csv')
df.drop(columns=['Male','Female','Literate'], inplace= True)


list_of_state = list(df['State'].unique())
list_of_state.insert(0, 'Overall India')


st.sidebar.title('Data Visualization of India')

selected_state = st.sidebar.selectbox('Select a State', list_of_state)
primary = st.sidebar.selectbox('Select Primary', sorted(df.columns[5:]))
secondary = st.sidebar.selectbox('Select Secondary Primary', sorted(df.columns[5:]))


plot = st.sidebar.button('Plot Graph')

if plot:
    
    st.text('Size Represent Primary Parameter')
    st.text("Color Represent Secondary Parameter")
    
    if selected_state == 'Overall India':
        fig = px.scatter_map(df, 
                    lat="Latitude", 
                    lon="Longitude",
                    size=primary,
                    color=secondary,
                    zoom=4,
                    size_max=35,
                    height=700,
                    width=1200,
                    color_continuous_scale="Plasma",
                    hover_name='District'
                    )

        st.plotly_chart(fig, use_container_width=True)


    else:
        state_df = df[df['State'] == selected_state]
        
        fig = px.scatter_map(state_df, 
                    lat="Latitude", 
                    lon="Longitude",
                    size=primary,
                    color=secondary,
                    zoom=6,
                    size_max=35,
                    height=700,
                    width=1200,
                    color_continuous_scale="Plasma",
                    hover_name='District'
                    )

        st.plotly_chart(fig, use_container_width=True)