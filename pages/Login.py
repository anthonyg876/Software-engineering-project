import streamlit as st
import db

if "user" not in st.experimental_get_query_params():
    st.experimental_set_query_params(user="no")

def login():
    st.experimental_set_query_params(user="both")

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

                        if successful_account:

                            if db.addUser(
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

                            if db.addUser(
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

                    blank = check_form_for_blanks([participant_values.values()])
                
                    if blank:
                        st.write("Fill out every input box")
                        successful_account = False
                    
                    else:

                        if participant_values["income"] > 30000:
                            st.write("Income must be $30,000 or less.")
                            successful_account = False

                        else:
                            if db.addUser(
                                participant_values["email"],
                                participant_values["first_name"],
                                participant_values["last_name"],
                                participant_values["income"],
                                participant_values["password"]
                            ) != "Added user into database":
                                st.write("User was not added")

                            else:
                                st.write("User account was added")


            print("Participants")
            print()

            for row in db.return_all_participants():
                print(row)

            print("Businesses")
            print()

            for row in db.return_all_businesses():
                print(row)

            print()
            print()
            print()
            print("Owned")
            
            for row in db.return_all_owned():
                print(row)         

with login_tab:

    if st.experimental_get_query_params()["user"][0] == "no":

        st.markdown("""<div class="emptyDiv"></div>""", unsafe_allow_html=True)

        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login", on_click=login):
            st.write("You are now logged in")

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