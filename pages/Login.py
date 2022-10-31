import streamlit as st

account_tab, login_tab = st.tabs(["Create Account", "Login"])

with account_tab:
    st.markdown("""<div class="emptyDiv"></div>""", unsafe_allow_html=True)
    st.write("Create An Account")

with login_tab:
    st.markdown("""<div class="emptyDiv"></div>""", unsafe_allow_html=True)
    st.write("Login")

st.markdown("""<div class="emptyDiv"></div>""", unsafe_allow_html=True)

user = st.radio(label="User Type", options=("Seller", "Buyer"))

if user == "Seller":
    st.write("Seller has been selected")

if user == "Buyer":
    st.write("Buyer has been selected")

if "login_bool" not in st.session_state:
    st.session_state["login_bool"] = False

if "username" not in st.session_state:
        st.session_state["username"] = "Default"

username = st.text_input("Username")
password = st.text_input("Password")

# if st.button("Submit"):

#     st.write(username)
#     st.write(password)

#     if password == "Password1":
    
#         st.write("You're Logged in")

#         st.session_state["username"] = username
#         st.session_state["login_bool"] = True

#     else:
#         st.write("Try again")



with open("styles.css") as f:
    heading_style = f.read()


with open("parth.html") as p:
    parth_html = p.read()

col1, col2, col3 = st.columns(3)


with col1:
    add_btn = st.button("Add")

with col2:

    if st.button("Update"):
      st.write("Update")

with col3:
    st.button("Delete")


st.markdown(f"""{parth_html}""", unsafe_allow_html=True)

st.markdown(f"""
    <style>{heading_style}</style>""", unsafe_allow_html=True
)


if "login_bool" not in st.session_state:
    st.session_state["login_bool"] = False

if "username" not in st.session_state:
    st.session_state["username"] = "Default"

if st.session_state["login_bool"]:
    st.write("Logged in as ", st.session_state["username"])
else:
     st.write("Get Logged in first")

with open("footer.html") as f:
    foot = f.read()

st.markdown(foot, unsafe_allow_html=True)