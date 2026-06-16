import streamlit as st

file = st.file_uploader("drop your resume in pdf format",type = ["pdf"])

if file:
    st.write("File Uploaded successfully")