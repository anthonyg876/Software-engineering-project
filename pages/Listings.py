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

filterOptions = st.multiselect("Select the filter category",
                        options=["catagory", "county",
                        "Business name"])

for i in range(len(filterOptions)):
    changed_profile_value = st.text_input(f"Change {filterOptions[i]}", key=i)
    st.write("you wrote",changed_profile_value)

price = st.slider("Listings price", value = (0,100), step = 1)
st.write(price) #debuging

st.title("Listings")

listingbutton = st.button("Show listings")

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
            st.markdown("""<h1 class= "itemHead">CVS</h1>
                            <h2 class = "titleHead">Tooth paste</h2>""",
                            unsafe_allow_html=True)
            categoryImg(cat)
            st.markdown(f"""
                            <h3 class = "itemInfo">price ${price1}</h3>
                            <h3 class = "itemInfo"> Quantity {quatitiy} </h3>
                            <h3 class = "itemInfo">county : {county}</h3>
                            <h3 class = "itemInfo">address {address}</h3>
                            <h3 class = "itemInfo">phone # {phone}</h3>""",
                            unsafe_allow_html=True)
    elif i % 3 == 1:

        with col2:
            st.markdown("""<h1 class= "itemHead">CVS</h1>
                            <h2 class = "titleHead">Tooth paste</h2>""",
                            unsafe_allow_html=True)
            categoryImg(cat)
            st.markdown(f"""
                            <h3 class = "itemInfo">price ${price1}</h3>
                            <h3 class = "itemInfo"> Quantity {quatitiy} </h3>
                            <h3 class = "itemInfo">county : {county}</h3>
                            <h3 class = "itemInfo">address {address}</h3>
                            <h3 class = "itemInfo">phone # {phone}</h3>""",
                            unsafe_allow_html=True)
    else:
        
        with col3:
            st.markdown("""<h1 class= "itemHead">CVS</h1>
                            <h2 class = "titleHead">Tooth paste</h2>""",
                            unsafe_allow_html=True)
            categoryImg(cat)
            st.markdown(f"""
                            <h3 class = "itemInfo">price ${price1}</h3>
                            <h3 class = "itemInfo"> Quantity {quatitiy} </h3>
                            <h3 class = "itemInfo">county : {county}</h3>
                            <h3 class = "itemInfo">address {address}</h3>
                            <h3 class = "itemInfo">phone # {phone}</h3>""",
                            unsafe_allow_html=True)

with open("footer.html") as f:
    foot = f.read()

with open("styles.css") as f:
    styling = f.read()

st.markdown(foot, unsafe_allow_html=True)
st.markdown(f"""<style>{styling}</style>""", unsafe_allow_html=True)