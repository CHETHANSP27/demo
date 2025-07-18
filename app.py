import streamlit as st

st.title("Python Version Test App")
st.write("Hello! This app is running on Python:")
import sys
st.write(sys.version)
