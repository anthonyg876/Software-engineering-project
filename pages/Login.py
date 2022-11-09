import streamlit as st


def seller_account_form():

    business_name = st.text_input("Business name", placeholder="Name here")
    address = st.text_input("Business address", placeholder="Address, City, State")
    county = st.text_input("County", placeholder="County here")
    phone_number = st.text_input("Phone number", placeholder="Enter number with no hyphens or separators")
    business_id = st.text_input("Enter your unique store id", placeholder="Number here")

def buyer_account_form():

    first_name = st.text_input("First Name", placeholder="Name here")
    last_name = st.text_input("Last Name", placeholder="Name here")
    income = st.number_input("Income", min_value=0, step=1000)
    buyer_email = st.text_input("Email", placeholder="Type email here")


account_tab, login_tab = st.tabs(["Create Account", "Login"])

with account_tab:

    st.markdown("""<div class="emptyDiv"></div>""", unsafe_allow_html=True)

    combined_account = st.checkbox("Check box if you are BOTH a seller and buyer")

    if combined_account:
        
        seller_account_form()
        st.markdown("""<div class="emptyDiv"></div>""", unsafe_allow_html=True)
        buyer_account_form()



    else:

        user = st.radio(label="User Type", options=("Seller", "Buyer"))

        st.markdown("""<div class="emptyDiv"></div>""", unsafe_allow_html=True)

        if user == "Seller":
            seller_account_form()

        if user == "Buyer":
            buyer_account_form()
            
    password = st.text_input("Password", placeholder="Type a good password here", type="password")

    st.markdown("""<div class="emptyDiv"></div>""", unsafe_allow_html=True)

    create_account_cols = st.columns(2)

    with create_account_cols[0]:
        st.write("When all input has been filled, click Create Account.")

    with create_account_cols[1]:
        if st.button("Create Account"):
            st.write("Account Created")

            

with login_tab:

    st.markdown("""<div class="emptyDiv"></div>""", unsafe_allow_html=True)

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        st.write("You are now logged in")



if "login_bool" not in st.session_state:
    st.session_state["login_bool"] = False

if "username" not in st.session_state:
        st.session_state["username"] = "Default"

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
    css_style = f.read()

st.markdown(f"""
    <style>{css_style}</style>""", unsafe_allow_html=True
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