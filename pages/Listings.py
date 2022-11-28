import streamlit as st
import db

def categoryImg(category):

    if category == "Toiletries":
        st.image("img/hygienic.png",use_column_width="always")

    elif category == "Medicine":
        st.image("img/medicine.png",use_column_width="always")

    elif category == "Food":
        st.image("img/shopping-bag.png",use_column_width="always")

    elif category == "Clothing":
        st.image("img/shirts.png",use_column_width="always")

    else:
        st.image("img/jelly-beans.png",use_column_width="always")



def add_item():

    email = st.experimental_get_query_params()["email"][0]
    bID = db.returnBusinessID(email)

    item_name = st.text_input("Item Name")
    category = st.selectbox("Item Category", options=["Food", "Clothing", "Medicine", "Toiletries", "Misc"])
    post_price = st.number_input("Post Price", min_value=0.0, max_value=50000.0, step=.01)
    original_price = st.number_input("Original Price", min_value=0.0, max_value=50000.0, step=.01)
    quantity = st.number_input("Quantity", min_value = 1, max_value = 50000, step=1)

    if st.button("Save Item"):

        if item_name == "":
            st.write("Item name is blank")

        else:

            item_added = db.addItem(item_name, category, post_price, original_price, quantity, bID)

            if item_added == "Inserted item into database.":
                st.write("You saved an item.")
            else:
                st.write("Unable to save item")


def update_item(updated_item_info):

    successful = True

    email = st.experimental_get_query_params()["email"][0]
    bID = db.returnBusinessID(email)

    item_name = updated_item_info["Item Name"]

    if item_name == "":
        st.write("Item name is blank")
        return

    if db.find_item(item_name, bID) == "Item not found":
        st.write("Item not found")
        return

    if len(updated_item_info.keys()) == 1:
        st.write("No update criteria selected")
        st.write(updated_item_info.items())
        return

    for k, v in updated_item_info.items():

        if k == "Category":
            if db.updateItemsCategory(v, item_name, bID) != "Updated item":
                successful = False
    
        elif k == "Post Price":
            if db.updateItemsPostPrice(v, item_name, bID) != "Updated item":
                successful = False
        
        elif k == "Original Price":
            if db.updateItemsOriginalPrice(v, item_name, bID) != "Updated item":
                successful = False
        
        elif k == "Quantity":
            if db.updateItemsQuantity(v, item_name, bID) != "Updated item":
                successful = False

    if successful:
        st.write("Item Updated")
    else:
        st.write("Could not update item")


def delete_item(item_name):

    email = st.experimental_get_query_params()["email"][0]
    bID = db.returnBusinessID(email)

    st.write(db.deleteItems(item_name, bID))


def filter_interface():

    user_type = st.experimental_get_query_params()["user"][0] 

    if user_type == "both" or user_type == "buyer":
        options = ["Category", "County", "Business name"]
    else:
        options = ["Category"]

    filterOptions = st.multiselect("Select the filter category",
                            options=options)

    for i in range(len(filterOptions)):

        if filterOptions[i] == "Category":
            filter_col = st.multiselect(f"Filter {filterOptions[i]}", key=i, options=["Food", "Clothing", "Toiletries", "Medicine", "Misc"])
            
        else:
            filter_col = st.multiselect(f"Filter {filterOptions[i]}", key=i, options=["sample", "sample2", "Sample3"])

        st.write("you wrote", filter_col)

    price = st.slider("Listings price", value = (0,100), step = 1)
    st.write(price) #debuging

    st.markdown("""<div class="emptyItemDiv"></div>""", unsafe_allow_html=True)

def listing_heading(business_name, item_name):

    st.markdown(f"""<p class= "itemHead">{business_name}</p>
                                    <p class = "titleHead">{item_name}</p>""",
                                    unsafe_allow_html=True)

def listing_info(price, quantity, county, address, phone):
    st.markdown(f"""
        <p class = "itemInfo">Price -- ${format(price, ".2f")}</p>
        <p class = "itemInfo">Quantity -- {quantity} </p>
        <p class = "itemInfo">County -- {county}</p>
        <p class = "itemInfo">Address -- {address}</p>
        <p class = "itemInfo">Phone # -- {phone}</p>""",unsafe_allow_html=True)

    st.markdown("""<div class="emptyItemDiv"></div>""", unsafe_allow_html=True)

def get_update_info():

    updated_item_info = {}

    updated_item_info["Item Name"] = st.text_input("Enter in the name of the item you want to change")

    item_update_options = st.multiselect("Choose what you'd like to change", 
                        options=["Category", "Post Price", "Original Price", "Quantity"])

    for i in range(len(item_update_options)):

        if item_update_options[i] == "Post Price" or item_update_options[i] == "Original Price":
            changed_item_value = st.number_input(f"Change {item_update_options[i]}", 
                        min_value = 0.0, max_value = 50000.0, step=.01, key=i)

        elif item_update_options[i] == "Quantity":
                changed_item_value = st.number_input(f"Change {item_update_options[i]}", 
                        min_value = 0, max_value = 50000, step=1, key=i)

        elif item_update_options[i] == "Category":
            changed_item_value= st.selectbox("Item Category", options=["Food", "Clothing", "Medicine", "Toiletries", "Misc"])

        else:
            changed_item_value = st.text_input(f"Change {item_update_options[i]}", key=i)
                
        updated_item_info[item_update_options[i]] = changed_item_value

    return updated_item_info
    
if st.experimental_get_query_params()["user"][0] == "no":
    st.title("Login to see this page")

else:

    filter_interface()

    if st.button("Show listings"):

        st.markdown("""<div class="emptyItemDiv"></div>""", unsafe_allow_html=True)

        col1, col2, col3 = st.columns(3)

        items = db.return_all_items()

        for i in range(len(items)):

            item_name = items[i][0]
            category = items[i][1]
            price = items[i][2]
            quantity = items[i][4]
            bID = items[i][5]

            business_info = db.returnBusinessInfoById(bID)

            business_name = business_info[1]
            address = business_info[3]
            county = business_info[4]
            phone = business_info[5]

            if i % 3 == 0:

                with col1:

                    listing_heading(business_name, item_name)
                    categoryImg(category)
                    listing_info(price, quantity, county, address, phone)

            elif i % 3 == 1:

                with col2:
                    
                    listing_heading(business_name, item_name)
                    categoryImg(category)
                    listing_info(price, quantity, county, address, phone)

            else:
                
                with col3:
                    
                    listing_heading(business_name, item_name)
                    categoryImg(category)
                    listing_info(price, quantity, county, address, phone)
                    
    
    user_type = st.experimental_get_query_params()["user"][0]

    if user_type == "seller" or  user_type == "both":
        
        st.title("Edit your items")
        item_choices = st.radio(" ", options=["Add Item", "Update Item", "Delete Item"])

        if item_choices == "Add Item":
            add_item()
            
        elif item_choices == "Update Item":

            updated_item_info = get_update_info()

            if st.button("Update item"):
                update_item(updated_item_info)

        else:

            item_name = st.text_input("Enter item name that you want deleted.")

            if st.button("Delete Item"):
                delete_item(item_name)


with open("footer.html") as f:
    foot = f.read()

with open("styles.css") as f:
    styling = f.read()

st.markdown(foot, unsafe_allow_html=True)
st.markdown(f"""<style>{styling}</style>""", unsafe_allow_html=True)