import streamlit as st

st.title("Listings")

col1, col2, col3 = st.columns(3)

for i in range(18):

    if i % 3 == 0:
        with col1:
            st.image("Software-engineering-project/img/logo.png", use_column_width="always")
            st.write("Original price: $50")
            st.write("New Price: $10")

    elif i % 3 == 1:
        with col2:
            st.image("Software-engineering-project/img/logo.png", use_column_width="always")
            st.write("Original price: $50")
            st.write("New Price: $10")

    else:
        with col3:
            st.image("Software-engineering-project/img/logo.png", use_column_width="always")
            st.write("Original price: $50")
            st.write("New Price: $10")


with open("footer.html") as f:
    foot = f.read()

with open("styles.css") as f:
    styling = f.read()

st.markdown(foot, unsafe_allow_html=True)
st.markdown(f"""<style>{styling}</style>""", unsafe_allow_html=True)