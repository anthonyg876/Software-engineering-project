import streamlit as st

def categoryImg(category):

    if category == "hygienics":
        st.image("img/hygienic.png",use_column_width="always")

    elif category == "medicine":
        st.image("img/medicine.png",use_column_width="always")

    elif category == "food":
        st.image("img/shopping-bag.png",use_column_width="always")

    elif category == "clothing":
        st.image("img/shirts.png",use_column_width="always")

    else:
        st.image("img/jelly-beans.png",use_column_width="always")


if st.experimental_get_query_params()["user"][0] == "no":
    st.title("Login to see this page")

else:

    filterOptions = st.multiselect("Select the filter category",
                            options=["category", "county",
                            "Business name"])

    for i in range(len(filterOptions)):

        if filterOptions[i] == "category":
            filter_col = st.multiselect(f"Filter {filterOptions[i]}", key=i, options=["Food", "Clothing", "Toiletries", "Medicine", "Misc"])
        
        else:
            filter_col = st.multiselect(f"Filter {filterOptions[i]}", key=i, options=["sample", "sample2", "Sample3"])

        st.write("you wrote", filter_col)

    price = st.slider("Listings price", value = (0,100), step = 1)
    st.write(price) #debuging

    st.markdown("""<div class="emptyItemDiv"></div>""", unsafe_allow_html=True)

    listing_button = st.button("Show listings")

    st.markdown("""<div class="emptyItemDiv"></div>""", unsafe_allow_html=True)

    price1 = 20
    quatitiy = 10
    county = "pinellas"
    address = "12 buckel my shoue,Tampa,FL"
    items = 0
    phone = 1111111
    cat = "food"

    col1, col2, col3 = st.columns(3)

    numItems = 19

    for i in range(numItems):

        if i % 3 == 0:

            with col1:
                st.markdown("""<p class= "itemHead">CVS</h1>
                                <p class = "titleHead">Tooth paste</h2>""",
                                unsafe_allow_html=True)
                categoryImg(cat)
                st.markdown(f"""
                                <p class = "itemInfo">price ${price1}</h3>
                                <p class = "itemInfo"> Quantity {quatitiy} </h3>
                                <p class = "itemInfo">county : {county}</h3>
                                <p class = "itemInfo">address {address}</h3>
                                <p class = "itemInfo">phone # {phone}</h3>""",
                                unsafe_allow_html=True)

                st.markdown("""<div class="emptyItemDiv"></div>""", unsafe_allow_html=True)

        elif i % 3 == 1:

            with col2:
                st.markdown("""<p class= "itemHead">CVS</h1>
                                <p class = "titleHead">Tooth paste</h2>""",
                                unsafe_allow_html=True)
                categoryImg(cat)
                st.markdown(f"""
                                <p class = "itemInfo">price ${price1}</h3>
                                <p class = "itemInfo"> Quantity {quatitiy} </h3>
                                <p class = "itemInfo">county : {county}</h3>
                                <p class = "itemInfo">address {address}</h3>
                                <p class = "itemInfo">phone # {phone}</h3>""",
                                unsafe_allow_html=True)

                st.markdown("""<div class="emptyItemDiv"></div>""", unsafe_allow_html=True)

        else:
            
            with col3:
                st.markdown("""<p class= "itemHead">CVS</h1>
                                <p class = "titleHead">Tooth paste</h2>""",
                                unsafe_allow_html=True)
                categoryImg(cat)
                st.markdown(f"""
                                <p class = "itemInfo">price ${price1}</h3>
                                <p class = "itemInfo"> Quantity {quatitiy} </h3>
                                <p class = "itemInfo">county : {county}</h3>
                                <p class = "itemInfo">address {address}</h3>
                                <p class = "itemInfo">phone # {phone}</h3>""",
                                unsafe_allow_html=True)

                st.markdown("""<div class="emptyItemDiv"></div>""", unsafe_allow_html=True)
    
    st.title("Edit your items")
    item_choices = st.radio(" ", options=["Add Item", "Update Item", "Delete Item"])

    if item_choices == "Add Item":

        item_name = st.text_input("Item Name")
        category= st.selectbox("Item Category", options=["Food", "Clothing", "Medicine", "Toiletries", "Misc"])
        post_price = st.number_input("Post Price", min_value=0.0, max_value=50000.0, step=.01)
        original_price = st.number_input("Original Price", min_value=0.0, max_value=50000.0, step=.01)

        if st.button("Save Item"):
            st.write("You saved an item. Collect $200.")

        
    elif item_choices == "Update Item":

        updated_item_info = {}

        item_update_options = st.multiselect("Choose what you'd like to change", 
                    options=["Item Name", "Category", "Post Price", "Original Price", "Quantity"])

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

        if st.button("Update item"):
            st.write("Item has been updated")

    else:
        item_name = st.text_input("Enter item name that you want deleted.")

        if st.button("Delete Item"):
            st.write(item_name, " was deleted")


with open("footer.html") as f:
    foot = f.read()

with open("styles.css") as f:
    styling = f.read()

st.markdown(foot, unsafe_allow_html=True)
st.markdown(f"""<style>{styling}</style>""", unsafe_allow_html=True)