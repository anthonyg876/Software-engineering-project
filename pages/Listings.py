import streamlit as st

if "user" not in st.experimental_get_query_params():
    st.experimental_set_query_params(user="no")


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
        filter_col = st.text_input(f"Filter {filterOptions[i]}", key=i)
        st.write("you wrote", filter_col)

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

with open("footer.html") as f:
    foot = f.read()

with open("styles.css") as f:
    styling = f.read()

st.markdown(foot, unsafe_allow_html=True)
st.markdown(f"""<style>{styling}</style>""", unsafe_allow_html=True)