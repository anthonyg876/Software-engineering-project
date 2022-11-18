import streamlit as st

if "user" not in st.experimental_get_query_params():
    st.experimental_set_query_params(user="no")

with open("styles.css") as f:
    css_file = f.read()

with open("home.html") as p:
    home_html = p.read()



with open("footer.html") as p:
    footer_html = p.read()

st.markdown(f"""{home_html}""", unsafe_allow_html=True)

st.markdown(f"""{footer_html}""", unsafe_allow_html=True)

st.markdown(f"""<style>{css_file}</style>""", unsafe_allow_html=True)