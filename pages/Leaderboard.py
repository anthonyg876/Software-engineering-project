import streamlit as st
import db

if "user" not in st.experimental_get_query_params():
    st.experimental_set_query_params(user="no")

if "balloons" not in st.session_state:
    st.session_state["balloons"] = 0
    st.balloons()

st.title("Leaderboard")

ids = db.distinct_business_ids()

number_names = st.slider("Number of Businesses", min_value=1, max_value=len(ids))

businesses = db.displayLeaderboard(number_names)

for i, business in enumerate(businesses):

    if i == 0:
        st.markdown(f"""<h1 class="leaderboard">{i+1}. {business[0]} --- ${format(business[1], ",.2f")}</h1>""", unsafe_allow_html=True)

    elif i == 1:
        st.markdown(f"""<h2 class="leaderboard">{i+1}. {business[0]} --- ${format(business[1], ",.2f")}</h2>""", unsafe_allow_html=True)

    elif i == 2:
        st.markdown(f"""<h3 class="leaderboard">{i+1}. {business[0]} --- ${format(business[1], ",.2f")}</h3>""", unsafe_allow_html=True)

    elif i == 3:
        st.markdown(f"""<h4 class="leaderboard">{i+1}. {business[0]} --- ${format(business[1], ",.2f")}</h4>""", unsafe_allow_html=True)

    elif i == 4:
        st.markdown(f"""<h5 class="leaderboard">{i+1}. {business[0]} --- ${format(business[1], ",.2f")}</h5>""", unsafe_allow_html=True)

    else:
        st.markdown(f"""<h6 class="leaderboard">{i+1}. {business[0]} --- ${format(business[1], ",.2f")}</h6>""", unsafe_allow_html=True)

with open("footer.html") as f:
    foot = f.read()

with open("styles.css") as f:
    styling = f.read()

st.markdown(foot, unsafe_allow_html=True)
st.markdown(f"""<style>{styling}</style>""", unsafe_allow_html=True)