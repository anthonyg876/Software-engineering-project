import streamlit as st

st.title("Home Page")


with open("styles.css") as f:
    css_file = f.read()

with open("footer.html") as p:
    footer_html = p.read()

st.markdown(f"""{footer_html}""", unsafe_allow_html=True)

st.markdown(f"""<style>{css_file}</style>""", unsafe_allow_html=True)