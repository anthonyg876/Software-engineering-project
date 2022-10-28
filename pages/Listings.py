import streamlit as st

st.title("Listings")



with open("styles.css") as f:
    styling = f.read()

st.markdown(f"""<style>{styling}</style>""", unsafe_allow_html=True)