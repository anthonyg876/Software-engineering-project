import streamlit as st

st.title("Home Page")


with open("styles.css") as f:
    css_file = f.read()


st.markdown(f"""<style>{css_file}</style>""", unsafe_allow_html=True)