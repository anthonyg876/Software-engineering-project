import streamlit as st
import db

if "user" not in st.experimental_get_query_params():
    st.experimental_set_query_params(user="no")

def logout():
    st.experimental_set_query_params(user="no")

def delete_account():
    
    email = st.experimental_get_query_params()["email"][0]
    user_type = st.experimental_get_query_params()["user"][0]

    if user_type == "both" or user_type == "seller":
        bID = db.returnBusinessID(email)
        print(db.deleteBusiness(bID))

    print(db.deleteParticipant(email))

    logout()


def display_seller_buyer_data():

    profCol1,profCol2,profCol3 = st.columns(spec=[1,2,2])

    email = st.experimental_get_query_params()["email"][0]

    business = db.returnBusinessInfo(email)
    user_info = db.return_participant_info(email)

    business_name = business[1]
    address = business[3]
    county = business[4]
    phone_number = business[5]

    first_name = user_info[1]
    last_name = user_info[2]
    income = user_info[3]


    with profCol1:
        st.markdown(f"""
        <div class ="leftblock">
            <img class="pic" src = "https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-chat/ava3.webp" alt = "profile" width="100" height="100">
        </div>
        <div>
            <h3 class="profName">  {first_name} {last_name} </h3>
        </div>
        
        """, unsafe_allow_html=True)
        st.markdown(f"""""", unsafe_allow_html=True)



    with profCol2:

        st.markdown(f"""<div class="emptyDiv"></div>""", unsafe_allow_html=True)
    # Profile data
    
        st.markdown(f"""<h3 class="profile-info"> Business: </h3>""", unsafe_allow_html=True)
        st.markdown(f"""<h3 class="profile-info">Address: </h3>""", unsafe_allow_html=True)
        st.markdown(f"""<h3 class="profile-info">County:  </h3>""", unsafe_allow_html=True)
        st.markdown(f"""<h3 class="profile-info">Phone Number: </h3>""", unsafe_allow_html=True)
        st.markdown(f"""<h3 class="profile-info">Income: </h3>""", unsafe_allow_html=True)
        st.markdown(f"""<div class="emptyDiv"></div>""", unsafe_allow_html=True)
        st.markdown(f"""<div class="emptyDiv"></div>""", unsafe_allow_html=True)

    with profCol3:
        st.markdown(f"""<h3 class="profile-info"> {business_name}</h3>""", unsafe_allow_html=True)
        st.markdown(f"""<h3 class="profile-info"> {address} </h3>""", unsafe_allow_html=True)
        st.markdown(f"""<h3 class="profile-info">{county} </h3>""", unsafe_allow_html=True)
        st.markdown(f"""<h3 class="profile-info">{phone_number}</h3>""", unsafe_allow_html=True)
        st.markdown(f"""<h3 class="profile-info">${income}</h3>""", unsafe_allow_html=True)
        st.markdown(f"""<div class="emptyDiv"></div>""", unsafe_allow_html=True)
        st.markdown(f"""<div class="emptyDiv"></div>""", unsafe_allow_html=True)




def display_seller_data():
    profCol1,profCol2,profCol3 = st.columns(spec=[1,2,2])

    email = st.experimental_get_query_params()["email"][0]

    business = db.returnBusinessInfo(email)
    user_info = db.return_participant_info(email)

    business_name = business[1]
    address = business[3]
    county = business[4]
    phone_number = business[5]

    first_name = user_info[1]
    last_name = user_info[2]
    income = user_info[3]

    
    with profCol1:
        st.markdown(f"""
        <div class ="leftblock">
            <img class="pic" src = "https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-chat/ava3.webp" alt = "profile" width="100" height="100">
        </div>
        <div>
            <h3 class="profName">  {first_name} {last_name} </h3>
        </div>
        
        """, unsafe_allow_html=True)
        st.markdown(f"""""", unsafe_allow_html=True)


# Profile data
    with profCol2:

        st.markdown(f"""<div class="emptyDiv"></div>""", unsafe_allow_html=True)
    
        st.markdown(f"""<h3 class="profile-info"> Business: </h3>""", unsafe_allow_html=True)
        st.markdown(f"""<h3 class="profile-info">Address: </h3>""", unsafe_allow_html=True)
        st.markdown(f"""<h3 class="profile-info">County:  </h3>""", unsafe_allow_html=True)
        st.markdown(f"""<h3 class="profile-info">Phone Number: </h3>""", unsafe_allow_html=True)
        st.markdown(f"""<div class="emptyDiv"></div>""", unsafe_allow_html=True)
        st.markdown(f"""<div class="emptyDiv"></div>""", unsafe_allow_html=True)

    with profCol3:
        st.markdown(f"""<h3 class="profile-info"> {business_name}</h3>""", unsafe_allow_html=True)
        st.markdown(f"""<h3 class="profile-info"> {address} </h3>""", unsafe_allow_html=True)
        st.markdown(f"""<h3 class="profile-info">{county} </h3>""", unsafe_allow_html=True)
        st.markdown(f"""<h3 class="profile-info">{phone_number}</h3>""", unsafe_allow_html=True)
        st.markdown(f"""<div class="emptyDiv"></div>""", unsafe_allow_html=True)
        st.markdown(f"""<div class="emptyDiv"></div>""", unsafe_allow_html=True)

def display_buyer_data():

    profCol1,profCol2,profCol3 = st.columns(spec=[1,2,2])

    email = st.experimental_get_query_params()["email"][0]
    user_info = db.return_participant_info(email)

    first_name = user_info[1]
    last_name = user_info[2]
    income = user_info[3]

    

    with profCol1:
        st.markdown(f"""
        <div class ="leftblock">
            <img class="pic" src = "https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-chat/ava3.webp" alt = "profile" width="100" height="100">
        </div>
        <div>
            <h3 class="profName">  {first_name} {last_name} </h3>
        </div>
        
        """, unsafe_allow_html=True)
        st.markdown(f"""""", unsafe_allow_html=True)



    with profCol2:

        st.markdown(f"""<div class="emptyDiv"></div>""", unsafe_allow_html=True)
    # Profile data
    
        st.markdown(f"""<h3 class="profile-info">Income: </h3>""", unsafe_allow_html=True)
        st.markdown(f"""<div class="emptyDiv"></div>""", unsafe_allow_html=True)
        st.markdown(f"""<div class="emptyDiv"></div>""", unsafe_allow_html=True)

    with profCol3:
        
        st.markdown(f"""<h3 class="profile-info">${income}</h3>""", unsafe_allow_html=True)
        st.markdown(f"""<div class="emptyDiv"></div>""", unsafe_allow_html=True)
        st.markdown(f"""<div class="emptyDiv"></div>""", unsafe_allow_html=True)

def edit_profile_info():

    updated_info = {}

    if st.experimental_get_query_params()["user"][0] == "seller":
        editing_choices = st.multiselect("Choose what you'd like to change", 
                    options=["Business Name", "Address", "County", "Phone Number","First Name", "Last Name"])

    elif st.experimental_get_query_params()["user"][0] == "buyer":
        editing_choices = st.multiselect("Choose what you'd like to change", 
                    options=["First Name", "Last Name", "Income"])
    else:
        editing_choices = st.multiselect("Choose what you'd like to change", 
                    options=["Business Name", "Address", "County", "Phone Number", 
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

    email = st.experimental_get_query_params()["email"][0]
    bID = db.returnBusinessID(email)

    if "" in updated_info.values():
        return "Fill out every input box"

    if len(updated_info.keys()) == 0:
        return "No update criteria selected."

    for k, v in updated_info.items():

        if k == "Business Name":
            db.updateBusinessName(bID, v)
    
        elif k == "Address":
            db.updateBusinessAddress(bID, v)
        
        elif k == "County":
            db.updateBusinessCounty(bID, v)
        
        elif k == "Phone Number":

            try:
                v = int(v)
                db.updateBusinessPhoneNumber(bID, v)
            except:
                return "Phone number needs to be just numerical digits (no hyphens or other characters)"

        elif k == "First Name":
            db.updateParticipantsFirstName(email, v)
        
        elif k == "Last Name":
            db.updateParticipantsLastName(email, v)

        elif k == "Income":
            db.updateParticipantsIncome(email, v)

    return "Edits Saved"

def display_profile_buttons(updated_info):

    col1, col2, col3, _ = st.columns(4)

    with col1:
        if st.button("Save Edits"):
            st.write(save_edits(updated_info))

    with col2:
        if st.button("Logout", on_click=logout):
            pass

    with col3:
        if st.button("Delete Account", on_click=delete_account):
            pass


if st.experimental_get_query_params()["user"][0] == "no":
    st.title("Login to see this page")

else:

    st.markdown(f"""<div class="pages-div">
    <h3 class="page-headings right-head">Profile</h3>
    <img class= "logo-img" src = "https://cdn-icons-png.flaticon.com/512/3237/3237472.png" alt = "profile" width="100" height="100">
</div>""", unsafe_allow_html=True)


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