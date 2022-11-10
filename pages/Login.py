import streamlit as st
import db

def seller_account_form():

    seller_values = {}

    seller_values["business_name"] = st.text_input("Business name", placeholder="Name here")
    seller_values["address"] = st.text_input("Business address", placeholder="Address, City, State")
    seller_values["county"] = st.text_input("County", placeholder="County here")
    seller_values["phone_number"] = st.text_input("Phone number", placeholder="Enter number with no hyphens or separators")
    seller_values["business_id"] = st.text_input("Enter your unique store id", placeholder="Number here")

    return seller_values

def participant_form():

    participant_values = {}

    participant_values["first_name"] = st.text_input("First Name", placeholder="Name here")
    participant_values["last_name"]  = st.text_input("Last Name", placeholder="Name here")
    participant_values["email"]  = st.text_input("Email", placeholder="Type email here")
    participant_values["password"]  = st.text_input("Password", placeholder="Type a good password here", type="password")

    return participant_values


def check_form_for_blanks(form_list):

    for form in form_list:
        for text_value in form:
            if text_value == "":
                return True

    return False


account_tab, login_tab = st.tabs(["Create Account", "Login"])

with account_tab:

    st.markdown("""<div class="emptyDiv"></div>""", unsafe_allow_html=True)

    combined_account = st.checkbox("Check box if you are BOTH a seller and buyer")

    if combined_account:
        
        seller_values = seller_account_form()
        st.markdown("""<div class="emptyDiv"></div>""", unsafe_allow_html=True)
        participant_values = participant_form()

        participant_values["income"] = st.number_input("Annual income to the nearest US dollar", min_value=0, step=1000)

    else:

        user = st.radio(label="User Type", options=("Seller", "Buyer"))

        st.markdown("""<div class="emptyDiv"></div>""", unsafe_allow_html=True)

        if user == "Seller":

            seller_values = seller_account_form()
            st.markdown("""<div class="emptyDiv"></div>""", unsafe_allow_html=True)
            participant_values = participant_form()

            participant_values["income"] = "-1"

        if user == "Buyer":

            participant_values = participant_form()
            participant_values["income"] = st.number_input("Annual income to the nearest US dollar", min_value=0, step=1000)

    st.markdown("""<div class="emptyDiv"></div>""", unsafe_allow_html=True)

    create_account_cols = st.columns(2)

    with create_account_cols[0]:
        st.write("When all input has been filled, click Create Account.")

    with create_account_cols[1]:

        if st.button("Create Account"):

            successful_account = True

            if combined_account:

                blank = check_form_for_blanks([seller_values.values(), participant_values.values()])
                
                if blank:
                    st.write("Fill out every input box")
                    successful_account = False

                else:

                    try:
                        seller_values["phone_number"] = int(seller_values["phone_number"])
                    except:
                        st.write("Phone number needs to be just numerical digits (no hyphens or other characters)")
                        successful_account = False

                    try:
                        seller_values["business_id"] = int(seller_values["business_id"]) 
                    except:
                        st.write("Need a numerical value for business id")
                        successful_account = False

                    if participant_values["income"] > 30000:
                        st.write("Income must be $30,000 or less.")
                        successful_account = False

            else:

                if user == "Seller":

                    blank = check_form_for_blanks([seller_values.values()])
                
                    if blank:
                        st.write("Fill out every input box")
                        successful_account = False

                    else:

                        try:
                            seller_values["phone_number"] = int(seller_values["phone_number"])
                        except:
                            st.write("Phone number needs to be just numerical digits (no hyphens or other characters)")
                            successful_account = False

                        try:
                            seller_values["business_id"] = int(seller_values["business_id"]) 
                        except:
                            st.write("Need a numerical value for business id") 
                            successful_account = False

                        if successful_account:
                            #db.addBusiness()
                            pass

                else:

                    blank = check_form_for_blanks([participant_values.values()])
                
                    if blank:
                        st.write("Fill out every input box")
                        successful_account = False
                    
                    else:

                        if participant_values["income"] > 30000:
                            st.write("Income must be $30,000 or less.")
                            successful_account = False

            if successful_account:

                if db.addUser(
                            participant_values["email"],
                            participant_values["first_name"],
                            participant_values["last_name"],
                            participant_values["income"],
                            participant_values["password"]
                        ) != "Added user into database":
                            st.write("User was not added")
                else:
                    st.write("All sucessful!")

            

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