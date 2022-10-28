from gc import callbacks
import streamlit as st

st.title("This is the Site Profile Page")

col1, col2, col3, = st.columns([1, 1, 2], gap="small")

name = "Matthew"

with col1:
    st.write("Name: ", name)

with col2:
    editbtn = st.button("Edit")

if editbtn:
    st.radio(label="Change field", options=["Name", "Email", "Phone number"])


with open("styles.css") as f:
    styling = f.read()

st.markdown(f"""<style>{styling}</style>""", unsafe_allow_html=True)