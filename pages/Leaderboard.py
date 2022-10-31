import streamlit as st

st.title("Leaderboard")

names = ["McDonalds", "Walmart", "Target", "Publix", "Marshalls", "Kohls", "Winn-Dixie", "Kroger"]

number_names = st.slider("Number of Businesses", min_value=1, max_value=len(names))

for i in range(number_names):
    st.write(names[i])


with open("footer.html") as f:
    foot = f.read()

with open("styles.css") as f:
    styling = f.read()

st.markdown(foot, unsafe_allow_html=True)
st.markdown(f"""<style>{styling}</style>""", unsafe_allow_html=True)