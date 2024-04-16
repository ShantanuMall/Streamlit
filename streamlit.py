import streamlit as st
import pandas as pd


options1 = ['Vikram Farm Block 26A']
options2 = ['22-June-2023']
options3 = ['75m']
options4 = ['None','Orthomosaic', 'BNDVI', 'GNDVI', 'LCI', 'MCARI', 'NDRE', 'NDVI', 'SIPI2', 'TGI', 'VARI']
options5 = ['None','Surface Model']

col1, col2, col3, col4, col5 = st.columns(5) 

with col1:
    selected_option1 = st.selectbox("Select Name", options1)

with col2:
    selected_option2 = st.selectbox("Select Date", options2)

with col3:
    selected_option3 = st.selectbox("Select Resolution", options3)

with col4:
    selected_option4 = st.selectbox("Select VIs", options4)
        
with col5:
    selected_option5 = st.selectbox("Select DSM", options5)

if st.button("Apply"):
    if selected_option4 == 'Orthomosaic': 
        st.image("/Users/punit/Downloads/ORTHOMOSAIC.jpg")
    if selected_option4 == 'BNDVI': 
        st.image("/Users/punit/Downloads/BNDVI.jpg")
    if selected_option4 == 'GNDVI': 
        st.image("/Users/punit/Downloads/GNDVI.jpg")
    if selected_option4 == 'LCI': 
        st.image("/Users/punit/Downloads/LCI.jpg")
    if selected_option4 == 'MCARI': 
        st.image("/Users/punit/Downloads/MCARI.jpg")
    if selected_option4 == 'NDRE': 
        st.image("/Users/punit/Downloads/NDRE.jpg")
    if selected_option4 == 'NDVI': 
        st.image("/Users/punit/Downloads/NDVI.jpg")
    if selected_option4 == 'SIPI2': 
        st.image("/Users/punit/Downloads/SIPI2.jpg")
    if selected_option4 == 'TGI': 
        st.image("/Users/punit/Downloads/TGI.jpg")
    if selected_option4 == 'VARI': 
        st.image("/Users/punit/Downloads/VARI.jpg")
    if selected_option5 == 'Surface Model': 
        st.image("/Users/punit/Downloads/Surface.jpg")

   
