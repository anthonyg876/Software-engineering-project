import streamlit as st
import db
import validPasswordChecker as vp

if "user" not in st.experimental_get_query_params():
    st.experimental_set_query_params(user="no")


def check_form_for_blanks(form_list):

    for form in form_list:
        for text_value in form:
            if text_value == "":
                return True
    return False

def check_form_requirements(participant_values, seller_values, user_type):

    successful_account = True

    form_values = None

    if user_type == "both" or user_type == "seller":
        form_values = [seller_values.values(), participant_values.values()]

    else:
        form_values = [participant_values.values()]

    if check_form_for_blanks(form_values):
        st.write("Fill out every input box")
        return False

    if user_type == "both" or user_type == "buyer":

        if participant_values["income"] > 30000:
            st.write("Income must be $30,000 or less.")
            successful_account = False

    if user_type == "both" or user_type == "seller":

        try:
            seller_values["phone_number"] = int(seller_values["phone_number"])
        except:
            st.write("Phone number needs to be just numerical digits (no hyphens or other characters)")
            successful_account = False

        try:
            seller_values["business_id"] = int(seller_values["business_id"]) 
        except:
            st.write("Need a numerical value for business id")
            return False

        if not db.checkBusinessId(seller_values["business_id"]):
            st.write("Business id must be unique and between 1 and 100.")
            successful_account = False

    if not db.verifyEmail(participant_values["email"]):
        st.write("Need a unique email.")
        successful_account = False

    if not vp.validPasswordCheck(participant_values["password"]):
        st.write("Password requirements not met.")
        successful_account = False

    return successful_account


def login(email, login):

    user = db.verifyLogin(email, password)

    if user is None:
        st.write("Your email and/or password are incorrect")

    else:

        user_email = user[0][0]

        user_type = db.returnUserType(user_email)

        if user_type == "Both":
            st.experimental_set_query_params(user="both", email=user_email)

        elif user_type == "Seller":
            st.experimental_set_query_params(user="seller", email=user_email)

        elif user_type == "Buyer":
            st.experimental_set_query_params(user="buyer", email=user_email)

        st.write("You are logged in")

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
    participant_values["password"]  = st.text_input("Password (Between 13 and 25 characters with 1 capital letter, 1 lowercase letter, 1 number, 1 special character)", placeholder="Type a good password here", type="password")

    return participant_values


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

            if combined_account:

                if check_form_requirements(participant_values, seller_values, "both"):

                    if db.addParticipants(
                        participant_values["email"],
                        participant_values["first_name"],
                        participant_values["last_name"],
                        participant_values["income"],
                        participant_values["password"]
                        ) != "Added user into database":
                            st.write("User was not added")

                    elif db.addBusiness(
                        participant_values["email"], 
                        seller_values["business_id"], 
                        seller_values["business_name"], 
                        participant_values["password"], 
                        seller_values["address"], 
                        seller_values["county"], 
                        seller_values["phone_number"]
                        ) == "Unsuccessful":
                            st.write("User was not added")
                                    
                    else:
                        st.write("User account was added")
                                

            elif user == "Seller":

                if check_form_requirements(participant_values, seller_values, "seller"):

                    if db.addParticipants(
                        participant_values["email"],
                        participant_values["first_name"],
                        participant_values["last_name"],
                        participant_values["income"],
                        participant_values["password"]
                    ) != "Added user into database":
                        st.write("User was not added")

                    elif db.addBusiness(
                        participant_values["email"], 
                        seller_values["business_id"], 
                        seller_values["business_name"], 
                        participant_values["password"], 
                        seller_values["address"], 
                        seller_values["county"], 
                        seller_values["phone_number"]
                    ) == "Unsuccessful":
                        st.write("User was not added")
                                
                    else:
                        st.write("User account was added")

            else:

                if check_form_requirements(participant_values, None, "buyer"):

                    if db.addParticipants(
                        participant_values["email"],
                        participant_values["first_name"],
                        participant_values["last_name"],
                        participant_values["income"],
                        participant_values["password"]
                    ) != "Added user into database":
                        st.write("User was not added")

                    else:
                        st.write("User account was added")
      

with login_tab:

    if st.experimental_get_query_params()["user"][0] == "no":

        st.markdown("""<div class="emptyDiv"></div>""", unsafe_allow_html=True)

        email = st.text_input("Email")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            login(email, password)

    else:
        st.title("You're logged in")


with open("styles.css") as f:
    css_style = f.read()

st.markdown(f"""
    <style>{css_style}</style>""", unsafe_allow_html=True
)

with open("footer.html") as f:
    foot = f.read()

st.markdown(foot, unsafe_allow_html=True)