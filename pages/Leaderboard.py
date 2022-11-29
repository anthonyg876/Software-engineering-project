import streamlit as st
import db

if "user" not in st.experimental_get_query_params():
    st.experimental_set_query_params(user="no")

st.title("Leaderboard")

names = db.distinct_business_names()

number_names = st.slider("Number of Businesses", min_value=1, max_value=len(names))

# businesses = db.leaderboard_function()
# for b in businesses:
   # st.write(f'{b[0]} ${format(price, ".2f")})

for i in range(number_names):
    st.write(names[i])

with open("footer.html") as f:
    foot = f.read()

with open("styles.css") as f:
    styling = f.read()

st.markdown(foot, unsafe_allow_html=True)
st.markdown(f"""<style>{styling}</style>""", unsafe_allow_html=True)