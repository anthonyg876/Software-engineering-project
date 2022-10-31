import streamlit as st

st.title("This is the Site Profile Page")

st.markdown(f"""<div class="emptyDiv"></div>""", unsafe_allow_html=True)

name = "Matthew Johnson"
email = "email@gmail.com"
county = "Some County"
phone_number = "727-777-7777"
zip_code = "33333"
income = 20000


# Profile data
st.markdown(f"""<h3 class="profile-info">Name: {name}</h3>""", unsafe_allow_html=True)
st.markdown(f"""<h3 class="profile-info">Email: {email}</h3>""", unsafe_allow_html=True)
st.markdown(f"""<h3 class="profile-info">County: {county}</h3>""", unsafe_allow_html=True)
st.markdown(f"""<h3 class="profile-info">Phone Number: {phone_number}</h3>""", unsafe_allow_html=True)
st.markdown(f"""<h3 class="profile-info">Zip Code: {zip_code}</h3>""", unsafe_allow_html=True)
st.markdown(f"""<h3 class="profile-info">Income: ${income}</h3>""", unsafe_allow_html=True)


st.markdown(f"""<div class="emptyDiv"></div>""", unsafe_allow_html=True)
st.markdown(f"""<div class="emptyDiv"></div>""", unsafe_allow_html=True)

st.markdown(f"""<h3>Edit your info</h3>""", unsafe_allow_html=True)

editing_choices = st.multiselect("Choose what you'd like to change", 
                options=["name", "email", "county", "phone number", "zip code", "income"])

for i in range(len(editing_choices)):
    changed_profile_value = st.text_input(f"Change {editing_choices[i]}", key=i)
    st.write(changed_profile_value)


st.write(editing_choices)


with open("styles.css") as f:
    styling = f.read()

with open("footer.html") as f:
    foot = f.read()

st.markdown(foot, unsafe_allow_html=True)
st.markdown(f"""<style>{styling}</style>""", unsafe_allow_html=True)