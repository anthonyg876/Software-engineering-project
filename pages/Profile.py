import streamlit as st

if "user" not in st.experimental_get_query_params():
    st.experimental_set_query_params(user="no")

def logout():
    st.experimental_set_query_params(user="no")

def delete_account():
    logout()

def display_seller_buyer_data():

    business_name = "Target"
    address = "89 First Street, Gainesville, Florida"
    county = "Citrus"
    phone_number = "727-777-7777"

    first_name = "Brian"
    last_name = "Patterson"
    income = 10000

    st.markdown(f"""<div class="emptyDiv"></div>""", unsafe_allow_html=True)

    # Profile data
    st.markdown(f"""<h3 class="profile-info">Name: {business_name}</h3>""", unsafe_allow_html=True)
    st.markdown(f"""<h3 class="profile-info">Address: {address}</h3>""", unsafe_allow_html=True)
    st.markdown(f"""<h3 class="profile-info">County: {county}</h3>""", unsafe_allow_html=True)
    st.markdown(f"""<h3 class="profile-info">Phone Number: {phone_number}</h3>""", unsafe_allow_html=True)

    st.markdown(f"""<h3 class="profile-info">First Name {first_name}</h3>""", unsafe_allow_html=True)
    st.markdown(f"""<h3 class="profile-info">Last Name: {last_name}</h3>""", unsafe_allow_html=True)
    st.markdown(f"""<h3 class="profile-info">Income: ${income}</h3>""", unsafe_allow_html=True)


    st.markdown(f"""<div class="emptyDiv"></div>""", unsafe_allow_html=True)
    st.markdown(f"""<div class="emptyDiv"></div>""", unsafe_allow_html=True)

def display_seller_data():

    business_name = "Target"
    address = "89 First Street, Gainesville, Florida"
    county = "Citrus"
    phone_number = "727-777-7777"

    st.markdown(f"""<div class="emptyDiv"></div>""", unsafe_allow_html=True)

    # Profile data
    st.markdown(f"""<h3 class="profile-info">Name: {business_name}</h3>""", unsafe_allow_html=True)
    st.markdown(f"""<h3 class="profile-info">Address: {address}</h3>""", unsafe_allow_html=True)
    st.markdown(f"""<h3 class="profile-info">County: {county}</h3>""", unsafe_allow_html=True)
    st.markdown(f"""<h3 class="profile-info">Phone Number: {phone_number}</h3>""", unsafe_allow_html=True)

    st.markdown(f"""<div class="emptyDiv"></div>""", unsafe_allow_html=True)
    st.markdown(f"""<div class="emptyDiv"></div>""", unsafe_allow_html=True)


def display_buyer_data():

    first_name = "Brian"
    last_name = "Patterson"
    income = 10000

    st.markdown(f"""<div class="emptyDiv"></div>""", unsafe_allow_html=True)

    # Profile data
    st.markdown(f"""<h3 class="profile-info">First Name {first_name}</h3>""", unsafe_allow_html=True)
    st.markdown(f"""<h3 class="profile-info">Last Name: {last_name}</h3>""", unsafe_allow_html=True)
    st.markdown(f"""<h3 class="profile-info">Income: ${income}</h3>""", unsafe_allow_html=True)


    st.markdown(f"""<div class="emptyDiv"></div>""", unsafe_allow_html=True)
    st.markdown(f"""<div class="emptyDiv"></div>""", unsafe_allow_html=True)

def edit_profile_info():

    updated_info = {}

    if st.experimental_get_query_params()["user"][0] == "seller":
        editing_choices = st.multiselect("Choose what you'd like to change", 
                    options=["Business Name", "Address", "County", "Phone Number"])

    elif st.experimental_get_query_params()["user"][0] == "buyer":
        editing_choices = st.multiselect("Choose what you'd like to change", 
                    options=["First Name", "Last Name", "Income"])
    else:
        editing_choices = st.multiselect("Choose what you'd like to change", 
                    options=[" Business Name", "Address", "County", "Phone Number", 
                    "First Name", "Last Name", "Income"])

    for i in range(len(editing_choices)):

        if editing_choices[i] == "Income":
            changed_profile_value = st.number_input(f"Change {editing_choices[i]}", 
                                min_value = 0, max_value = 30000, step=1000, key=i)
        else:
            changed_profile_value = st.text_input(f"Change {editing_choices[i]}", key=i)
            updated_info[editing_choices[i]] = changed_profile_value

    return updated_info

def save_edits(updated_info):

    for k, v in updated_info.items():

        if v == "":
            return "Fill out every input box"

        if k == "Business Name":
            #db.updateBusinessName(, v)
            pass
        elif k == "Address":
            #db.updateBusinessAddress(, v)
            pass
        elif k == "County":
            #db.updateBusinessCounty(, v)
            pass
        elif k == "Phone Number":

            try:
                v = int(v)
                #db.updateBusinessPhoneNumber(, v)
            except:
                return "Phone number needs to be just numerical digits (no hyphens or other characters)"

        elif k == "First Name":
            #db.updateParticipantsFirstName(, v)
            pass
        elif k == "Last Name":
            #db.updateParticipantsLastName(, v)
            pass
        elif k == "Income":
            #db.updateParticipantsIncome(, v)
            pass

    return "Edits Saved"

def display_profile_buttons(updated_info):

    col1, col2, col3, _ = st.columns(4)

    with col1:
        if st.button("Save Edits"):
            st.write(save_edits(updated_info))

    with col2:
        if st.button("Logout", on_click=logout):
            st.write("Logged out")

    with col3:
        if st.button("Delete Account", on_click=delete_account):
            st.write("Account deleted")


if st.experimental_get_query_params()["user"][0] == "no":
    st.title("Login to see this page")

else:

    st.title("Profile")

    if st.experimental_get_query_params()["user"][0] == "both":
        display_seller_buyer_data()
    elif st.experimental_get_query_params()["user"][0] == "seller":
        display_seller_data()
    else:
        display_buyer_data()

    st.markdown(f"""<h3>Edit your info</h3>""", unsafe_allow_html=True)

    updated_info = edit_profile_info()

    display_profile_buttons(updated_info)


with open("styles.css") as f:
    styling = f.read()

with open("footer.html") as f:
    foot = f.read()

st.markdown(foot, unsafe_allow_html=True)
st.markdown(f"""<style>{styling}</style>""", unsafe_allow_html=True)