import oracledb
import hashlib

# Variables needed for the login.
username = "hlee3"
userpwd = "dzPHnwNnvWrLjXL7S0oZNmYv"
host = "oracle.cise.ufl.edu"
port = 1521
service_name = "orcl"

dsn = f'{username}/{userpwd}@{host}:{port}/{service_name}'    
salt = "5gz"

def hashPassword(password: str) -> str:
    password = password + salt
    hashed = hashlib.md5(password.encode())
    # print("Hashed Password is: " + hashed)
    return hashed


'''
Adds user to the database.
'''
def addParticipants(email: str, firstName: str, lastName: str, income: int, password: str) -> str:

    hashed = hashPassword(password)

    # Attempt connection to Oracle database.
    try:
        connection = oracledb.connect(dsn = dsn)
        print("Connected to database")

    except:
        print("Was not able to connect to the database.")
    cur = connection.cursor()
    try:
        cur.execute("insert into participants values (:email, :firstName, :lastName, :income, :password)", [email, firstName, lastName, income, hashed.hexdigest()])
        connection.commit()
        output = "Added user into database"
    except:
        output = "Unsuccessful"    
    connection.close()
    return output
'''
Adds business to db
'''
def addBusiness(email: str, id: int, name: str, password: str, address: str, county: str, phoneNumber: int) -> str:

    password = hashPassword(password)
    # Attempt connection to Oracle database.
    try:
        connection = oracledb.connect(dsn = dsn)
        print("Connected to database")
    except:
        print("Was not able to connect to database")
    cur = connection.cursor()
    # Insert into database a business model.
    try:
        cur.execute("insert into Business values(:id, :name, :password, :address, :county, :phone_number)", [id, name, password.hexdigest(), address, county, phoneNumber])
        connection.commit()
        output = "Added business to database"
    except:
        output = "Unsuccessful"
        print("Unsuccesful business insertion")
    try:
        cur.execute("insert into ownsbusiness values(:email, :bid)", [email, id])
        connection.commit()
        output = "inserted ownsbusiness relationship Email"
    except:
        output = "Unsuccessful"
        print("Unsuccesful owns business inseert")
    connection.close()

    return output

    
def deleteParticipant(email: str) -> None:
    try:
        connection = oracledb.connect(dsn = dsn)
        print("Connected to database")
    except:
        print("Was not able to connect to database")
    cur = connection.cursor()
    try:
        cur.execute("delete from ownsbusiness where email = :email", [email])
        connection.commit()
        output = "Deleted ownsbusiness from database."
    except:
        output = "Unable to deleted ownsbusiness from database"
    try:
        cur.execute("delete from participants where email = :email", [email])
        connection.commit()
        output = "Deleted user from database."
    except:
        output = "Unable to deleted user from database"
    connection.close()
    return output

def deleteOwnsBusiness(email: str) -> None:
    try:
        connection = oracledb.connect(dsn = dsn)
        print("Connected to database")
    except:
        print("Was not able to connect to database")
    cur = connection.cursor()
    try:
        cur.execute("delete from ownsbusiness where email = :email", [email])
        connection.commit()
        output = "Deleted ownsbusiness from database."
    except:
        output = "Unable to deleted ownsbusiness from database"
    connection.close()
    return output

def deleteBusiness(id: int) -> str:
    try:
        connection = oracledb.connect(dsn = dsn)
        print("Connected to database")
    except:
        print("Was not able to connect to database")
    cur = connection.cursor()
    try:
        cur.execute("delete from items where bid = :bid", [id])
        connection.commit()
        output = "Deleted item from database."
    except:
        output = "Unable to deleted ownsbusiness from database"
    try:
        cur.execute("delete from ownsbusiness where bid = :bid", [id])
        connection.commit()
        output = "Deleted ownsbusiness from database."
    except:
        output = "Unable to deleted ownsbusiness from database"
    try:
        cur.execute("delete from business where id = :id", [id])
        connection.commit()
        output = "Deleted user from database."
    except:
        output = "Unable to delete business from database"
    connection.close()
    return output

'''
Add item to database
'''
def addItem(name: str, category: str, postPrice: float, originalPrice: float, quantity: int, bId: int)-> str:
     # Attempt connection to Oracle database.
    try:
        connection = oracledb.connect(dsn = dsn)
        print("Connected to database")
    except:
        print("Was not able to connect to database")
    cur = connection.cursor()
    # Insert item into a business model.
    try:
        cur.execute("insert into items values(:name, :category, :postPrice, :originalPrice, :quantity, :bId)", [name, category, postPrice, originalPrice, quantity, bId])
        connection.commit()
        output = "Inserted item into database."
    except:
        output = "Unable to add item into database"
    connection.close()
    return output
'''
Verifies user credentials and returns user info.
'''
def verifyLogin(email: str, password: str):

    password = hashPassword(password)

    # Attempt connection to Oracle db.
    try: 
        connection = oracledb.connect(dsn=dsn)
        print("Connected to database")
    except:
        print("Was not able to connect to database")
    cur = connection.cursor()
    # Check if the user even exists
    cur.execute("select * from participants where email = :email", [email])
    number = cur.fetchall() 
    if (len(number) != 1):
        print("User with email does not exist")
        return None
    
    cur.execute("select * from participants where email = :email and password = :password", [email, password.hexdigest()])
    user = cur.fetchall()
    if (len(user) != 1):
        print("Password does not match, try again")
        return None
    print("Successfully verified user")
    return user

def returnUserType(email: str):
    # Attempt connection to Oracle db.
    try: 
        connection = oracledb.connect(dsn=dsn)
        print("Connected to database")
    except:
        print("Was not able to connect to database")
    cur = connection.cursor()
    # Check the user's income
    cur.execute("select income from participants where email = :email", [email])
    income = cur.fetchall() 
    #print("PRINTING INCOME:")
    #print(income)
    if (income[0][0] == -1):
        #print("User with email does not exist")
        return "Seller"
    # Check if the user even exists
    cur.execute("select * from ownsbusiness where email = :email", [email])
    number = cur.fetchall()
    if (len(number) != 1):
        print("User is not associated with any business")
        return "Buyer" 
    return "Both"

def returnBusinessInfo(email: str):
    # Attempt connection to Oracle db.
    try: 
        connection = oracledb.connect(dsn=dsn)
        print("Connected to database")
    except:
        print("Was not able to connect to database")
    cur = connection.cursor()
    # Check the user's income
    cur.execute("select bid from ownsbusiness where email = :email", [email])
    bid = cur.fetchall()[0][0] 
    cur.execute("select * from business where id = :id", [bid])
    businessInfo = cur.fetchall()
    if (len(businessInfo) != 1):
        print("User is not associated with any business")
        return None 
    return businessInfo[0]


def returnBusinessInfoById(bid: int):

    # Attempt connection to Oracle db.
    try: 
        connection = oracledb.connect(dsn=dsn)
        print("Connected to database")
    except:
        print("Was not able to connect to database")

    cur = connection.cursor()

    cur.execute("select * from business where id = :id", [bid])
    businessInfo = cur.fetchall()

    if (len(businessInfo) != 1):
        print("User is not associated with any business")
        return None 
    return businessInfo[0]

def returnBusinessID(email: str):
    # Attempt connection to Oracle db.
    try: 
        connection = oracledb.connect(dsn=dsn)
        print("Connected to database")
    except:
        print("Was not able to connect to database")
    cur = connection.cursor()
    # Check if the user even exists
    cur.execute("select * from ownsbusiness where email = :email", [email])
    number = cur.fetchall() 
    if (len(number) != 1):
        print("Business does not exist")
        return None
    
    cur.execute("select bid from ownsbusiness where email = :email", [email])
    bid = cur.fetchall()
    if (len(bid) != 1):
        print("Business does not exist")
        return None
    print("Successfully verified Business")
    return bid[0][0]


def return_participant_info(email: str):

    # Attempt connection to Oracle db.
    try: 
        connection = oracledb.connect(dsn=dsn)
        print("Connected to database")
    except:
        print("Was not able to connect to database")

    cur = connection.cursor()

    cur.execute("select * from participants where email = :email", [email])
    user = cur.fetchall()

    if (len(user) != 1):
        print("User is not associated with any account")
        return None 

    return user[0]

def return_all_items():

    try:
        connection = oracledb.connect(dsn = dsn)

    except:
        return "Was not able to connect to the database"

    cur = connection.cursor()

    cur.execute("SELECT * FROM Items ORDER BY postPrice ASC")

    all_items = cur.fetchall()
    connection.close()

    return all_items

def return_all_participants():

    try:
        connection = oracledb.connect(dsn = dsn)

    except:
        return "Was not able to connect to the database"

    cur = connection.cursor()

    cur.execute("SELECT * FROM participants ORDER BY email")

    all_participants = cur.fetchall()
    connection.close()

    return all_participants

def return_all_businesses():

    try:
        connection = oracledb.connect(dsn = dsn)

    except:
        return "Was not able to connect to the database"

    cur = connection.cursor()

    cur.execute("SELECT * FROM Business ORDER BY id")

    all_businesses = cur.fetchall()
    connection.close()

    return all_businesses

def return_all_owned():

    try:
        connection = oracledb.connect(dsn = dsn)

    except:
        return "Was not able to connect to the database"

    cur = connection.cursor()

    cur.execute("SELECT * FROM ownsBusiness")

    all_owned = cur.fetchall()
    connection.close()

    return all_owned

def updateParticipantsFirstName(email: str, firstName: str) -> str:
    # Attempt connection to Oracle database.
    try:
        connection = oracledb.connect(dsn = dsn)
        print("Connected to database")
    except:
        print("Was not able to connect to database")
    cur = connection.cursor()
    try:
        cur.execute("update participants set firstName = :firstName where email = :email", [firstName, email])
        connection.commit()
        output = "Updated participants"
    except:
        output = "Unsuccessful"
    connection.close()

def updateParticipantsLastName(email: str, lastName: str) -> str:
    # Attempt connection to Oracle database.
    try:
        connection = oracledb.connect(dsn = dsn)
        print("Connected to database")
    except:
        print("Was not able to connect to database")
    cur = connection.cursor()
    try:
        cur.execute("update participants set lastName = :lastName where email = :email", [lastName, email])
        connection.commit()
        output = "Updated participants"
    except:
        output = "Unsuccessful"
    connection.close()

def updateParticipantsIncome(email: str, income: int) -> str:
    # Attempt connection to Oracle database.
    try:
        connection = oracledb.connect(dsn = dsn)
        print("Connected to database")
    except:
        print("Was not able to connect to database")
    cur = connection.cursor()
    try:
        cur.execute("update participants set income = :income where email = :email", [income, email])
        connection.commit()
        output = "Updated participants"
    except:
        output = "Unsuccessful"
    connection.close()

def updateParticipantsPassword(email: str, password: str) -> str:
    # Attempt connection to Oracle database.
    try:
        connection = oracledb.connect(dsn = dsn)
        print("Connected to database")
    except:
        print("Was not able to connect to database")
    cur = connection.cursor()
    try:
        cur.execute("update participants set password = :password where email = :email", [password, email])
        connection.commit()
        output = "Updated participants"
    except:
        output = "Unsuccessful"
    connection.close()

def updateBusinessName(id: int, name: str) -> str:
    # Attempt connection to Oracle database.
    try:
        connection = oracledb.connect(dsn = dsn)
        print("Connected to database")
    except:
        print("Was not able to connect to database")
    cur = connection.cursor()
    try:
        cur.execute("update business set name = :name where id = :id", [name, id])
        connection.commit()
        output = "Updated business"
    except:
        output = "Unsuccessful"
    connection.close()

def updateBusinessPassword(id: int, password: str) -> str:
    # Attempt connection to Oracle database.
    try:
        connection = oracledb.connect(dsn = dsn)
        print("Connected to database")
    except:
        print("Was not able to connect to database")
    cur = connection.cursor()
    try:
        cur.execute("update business set password = :password where id = :id", [password, id])
        connection.commit()
        output = "Updated business"
    except:
        output = "Unsuccessful"
    connection.close()

def updateBusinessAddress(id: int, address: str) -> str:
    # Attempt connection to Oracle database.
    try:
        connection = oracledb.connect(dsn = dsn)
        print("Connected to database")
    except:
        print("Was not able to connect to database")
    cur = connection.cursor()
    try:
        cur.execute("update business set address = :address where id = :id", [address, id])
        connection.commit()
        output = "Updated business"
    except:
        output = "Unsuccessful"
    connection.close()

def updateBusinessCounty(id: int, county: str) -> str:
    # Attempt connection to Oracle database.
    try:
        connection = oracledb.connect(dsn = dsn)
        print("Connected to database")
    except:
        print("Was not able to connect to database")
    cur = connection.cursor()
    try:
        cur.execute("update business set county = :county where id = :id", [county, id])
        connection.commit()
        output = "Updated business"
    except:
        output = "Unsuccessful"
    connection.close()

def updateBusinessPhoneNumber(id: int, phone_Number: str) -> str:
    # Attempt connection to Oracle database.
    try:
        connection = oracledb.connect(dsn = dsn)
        print("Connected to database")
    except:
        print("Was not able to connect to database")
    cur = connection.cursor()
    try:
        cur.execute("update business set phone_Number = :phone_Number where id = :id", [phone_Number, id])
        connection.commit()
        output = "Updated business"
    except:
        output = "Unsuccessful"
    connection.close()

def deleteItems(name: str, bid: int) -> str:

    try:
        connection = oracledb.connect(dsn = dsn)
        print("Connected to database")
    except:
        print("Was not able to connect to database")

    cur = connection.cursor()

    cur.execute("select * from items where name = :name and bid = :bid", [name, bid])
    items = cur.fetchall() 

    if (len(items) == 0):
        return "Item not found"

    try:
        cur.execute("delete from items where name = :name and bid = :bid", [name, bid])
        connection.commit()
        output = "Deleted item from database."
    except:
        output = "Unable to delete items from database"

    connection.close()
    return output

def updateItemsCategory(category: str, name: str, bid: int) -> str:
    # Attempt connection to Oracle database.
    try:
        connection = oracledb.connect(dsn = dsn)
        print("Connected to database")
    except:
        print("Was not able to connect to database")

    cur = connection.cursor()

    try:
        cur.execute("update items set category = :category where name = :name and bid = :bid", [category,name ,bid ])
        connection.commit()
        output = "Updated item"
    except:
        output = "Unsuccessful"

    connection.close()

    return output

def updateItemsPostPrice(postprice: float, name: str, bid: int) -> str:
    # Attempt connection to Oracle database.
    try:
        connection = oracledb.connect(dsn = dsn)
        print("Connected to database")
    except:
        print("Was not able to connect to database")

    cur = connection.cursor()

    try:
        cur.execute("update items set postprice = :postprice where name = :name and bid = :bid", [postprice,name ,bid ])
        connection.commit()
        output = "Updated item"
    except:
        output = "Unsuccessful"
    connection.close()

    return output


def updateItemsOriginalPrice(originalprice: float, name: str, bid: int) -> str:
    # Attempt connection to Oracle database.
    try:
        connection = oracledb.connect(dsn = dsn)
        print("Connected to database")
    except:
        print("Was not able to connect to database")

    cur = connection.cursor()

    try:
        cur.execute("update items set originalprice = :originalprice where name = :name and bid = :bid", [originalprice,name ,bid ])
        connection.commit()
        output = "Updated item"
    except:
        output = "Unsuccessful"

    connection.close()

    return output

def updateItemsQuantity(quantity: int, name: str, bid: int) -> str:
    # Attempt connection to Oracle database.
    try:
        connection = oracledb.connect(dsn = dsn)
        print("Connected to database")
    except:
        print("Was not able to connect to database")

    cur = connection.cursor()

    try:
        cur.execute("update items set quantity = :quantity where name = :name and bid = :bid", [quantity,name ,bid ])
        connection.commit()
        output = "Updated item"
    except:
        output = "Unsuccessful"

    connection.close()  

    return output


def find_item(name: str, bid: int) -> str:
    # Attempt connection to Oracle database.
    try:
        connection = oracledb.connect(dsn = dsn)
        print("Connected to database")
    except:
        print("Was not able to connect to database")

    cur = connection.cursor()

    cur.execute("select * from items where name = :name and bid = :bid", [name, bid])

    items = cur.fetchall() 

    if (len(items) == 0):
        return "Item not found"

    connection.close()  

    return "Successful"

def displayLeaderboard(topRows: int):
    try: 
        connection = oracledb.connect(dsn=dsn)
        print("Connected to database")
    except:
        print("Was not able to connect to database")
    cur = connection.cursor()
    cur.execute("select business.name, sum((originalprice - postprice)*quantity) as Donation from business inner join items on business.id = items.bid group by business.name order by Donation desc fetch first :topRows rows only", [topRows])
    itemInfo = cur.fetchall()
    return itemInfo


def distinct_counties():

    # Attempt connection to Oracle database.
    try:
        connection = oracledb.connect(dsn = dsn)
        print("Connected to database")
    except:
        print("Was not able to connect to database")

    cur = connection.cursor()

    cur.execute("select DISTINCT(county) from Business")

    counties = cur.fetchall()

    return counties

def distinct_business_names():

    # Attempt connection to Oracle database.
    try:
        connection = oracledb.connect(dsn = dsn)
        print("Connected to database")
    except:
        print("Was not able to connect to database")

    cur = connection.cursor()

    cur.execute("select DISTINCT(name) from Business")

    names = cur.fetchall()

    return names

def distinct_business_ids():

    # Attempt connection to Oracle database.
    try:
        connection = oracledb.connect(dsn = dsn)
        print("Connected to database")
    except:
        print("Was not able to connect to database")

    cur = connection.cursor()

    cur.execute("SELECT DISTINCT(bId) from items")

    ids = cur.fetchall()

    return ids

def max_price():

    # Attempt connection to Oracle database.
    try:
        connection = oracledb.connect(dsn = dsn)
        print("Connected to database")
    except:
        print("Was not able to connect to database")

    cur = connection.cursor()

    cur.execute("select MAX(postPrice) from Items")

    max_price = cur.fetchall()

    return max_price[0][0]


def filter_items(categories, counties, business_names, 
                min_price, max_price, search_item_name, sort_type, sort_order):

    try:
        connection = oracledb.connect(dsn = dsn)
        print("Connected to database")
    except:
        print("Was not able to connect to database")

    cur = connection.cursor()

    if len(categories) == 0:
        categories = ["Food", "Clothing", "Medicine", "Toiletries", "Misc"]

    if len(counties) == 0:
        counties = [county[0] for county in distinct_counties()]

    if len(business_names) == 0:
        business_names = [business[0] for business in distinct_business_names()]

    bind_value_length = 0

    placeholders_category = [":" + str(i + 1) for i in range(len(categories))]
    bind_value_length += len(categories)

    placeholders_county = [":" + str(i + 1) for i in range(bind_value_length, bind_value_length + len(counties))]
    bind_value_length += len(counties)

    placeholders_business_names = [":" + str(i + 1) for i in range(bind_value_length, bind_value_length + len(business_names))]
    bind_value_length += len(business_names)

    placeholders_min_price = [":" + str(i + 1) for i in range(bind_value_length, bind_value_length+1)]
    bind_value_length += 1

    placeholders_max_price = [":" + str(i + 1) for i in range(bind_value_length, bind_value_length+1)]
    bind_value_length += 1

    placeholders_item_name = [":" + str(i + 1) for i in range(bind_value_length, bind_value_length+1)]
    bind_value_length += 1


    if sort_type == "Price" and sort_order == "ASC":

        query = "select i.* FROM items i join business b on i.bId = b.id " + \
            "where i.category in (%s) " % (",".join(placeholders_category)) + \
            "AND b.county in (%s) " % (",".join(placeholders_county)) + \
            "AND b.name in (%s) " % (",".join(placeholders_business_names)) + \
            "AND i.postPrice >= (%s) " % (",".join(placeholders_min_price)) + \
            "AND i.postPrice <= (%s) " % (",".join(placeholders_max_price)) + \
            "AND LOWER(i.name) LIKE (%s) " % (",".join(placeholders_item_name)) + \
            "ORDER BY i.postPrice ASC"

    elif sort_type == "Price" and sort_order == "DESC":

        query = "select i.* FROM items i join business b on i.bId = b.id " + \
            "where i.category in (%s) " % (",".join(placeholders_category)) + \
            "AND b.county in (%s) " % (",".join(placeholders_county)) + \
            "AND b.name in (%s) " % (",".join(placeholders_business_names)) + \
            "AND i.postPrice >= (%s) " % (",".join(placeholders_min_price)) + \
            "AND i.postPrice <= (%s) " % (",".join(placeholders_max_price)) + \
            "AND LOWER(i.name) LIKE (%s) " % (",".join(placeholders_item_name)) + \
            "ORDER BY i.postPrice DESC"

    elif sort_type == "Alphabetical" and sort_order == "ASC":

        query = "select i.* FROM items i join business b on i.bId = b.id " + \
            "where i.category in (%s) " % (",".join(placeholders_category)) + \
            "AND b.county in (%s) " % (",".join(placeholders_county)) + \
            "AND b.name in (%s) " % (",".join(placeholders_business_names)) + \
            "AND i.postPrice >= (%s) " % (",".join(placeholders_min_price)) + \
            "AND i.postPrice <= (%s) " % (",".join(placeholders_max_price)) + \
            "AND LOWER(i.name) LIKE (%s) " % (",".join(placeholders_item_name)) + \
            "ORDER BY LOWER(i.name) ASC"

    else:
        query = "select i.* FROM items i join business b on i.bId = b.id " + \
            "where i.category in (%s) " % (",".join(placeholders_category)) + \
            "AND b.county in (%s) " % (",".join(placeholders_county)) + \
            "AND b.name in (%s) " % (",".join(placeholders_business_names)) + \
            "AND i.postPrice >= (%s) " % (",".join(placeholders_min_price)) + \
            "AND i.postPrice <= (%s) " % (",".join(placeholders_max_price)) + \
            "AND LOWER(i.name) LIKE (%s) " % (",".join(placeholders_item_name)) + \
            "ORDER BY LOWER(i.name) DESC"


    bind_values = []

    for cat in categories:
        bind_values.append(cat)

    for county in counties:
        bind_values.append(county)

    for b_name in business_names:
        bind_values.append(b_name)

    bind_values.append(min_price)
    bind_values.append(max_price)

    bind_values.append(f"%{search_item_name}%")

    cur.execute(query, bind_values)

    items = cur.fetchall()

    connection.close()

    return items

if __name__ == "__main__":
    #addParticipants("ag@gamil.com", "Anthony", "Gravier", 85000, "boof")
    #addParticipants("buyer@gmail.com", "buyer", "buyer", 22222, "pass1")
    #addParticipants("seller@gmail.com", "seller", "seller", -1, "pass1")
    #Returning business id, based on email
    #deleteParticipant("realNewEmail@RealNew.com")  
    #deleteParticipant("ag@gamil.com")   
    #addParticipants("ag@gamil.com", "Anthony", "Gravier", 85000, "boof")
    #updateParticipants("ag@gamil.com", "newFirstName", "newLastName",911911,"newPassword")
    #updateEmail("ag@gamil.com", "newFirstName", "newLastName",911911,"newPassword","realNewEmail@RealNew.com")
    #deleteParticipant("realNewEmail@RealNew.com")
    #addBusiness("seller@gmail.com", 99, "sellerMart", "pass1", "address2", "33612", 123456789)
    #updateBusiness(1, "NEwBusiness", "NEwpass1", "Newaddress1", "33615", 00000000)
    #print(deleteBusiness(5))
    #print(updateParticipantsFirstName("mk@gmail.com","RealNewNEWMatthew"))
    #print(updateParticipantsLastName("mk@gmail.com","REalNewKerekes"))
    #print(updateParticipantsIncome("mk@gmail.com",1000000))
    #print(updateParticipantsPassword("mk@gmail.com","NewPass"))
    # addParticipants("ag@gamil.com", "Anthony", "Gravier", 85000, "boof")\
    #print(updateBusinessName(5, "REalNewBusiness"))
    #print(addBusiness(2, "Walmart", "password1", "100 Gainesville Road", "Sarasota County", 7271111111))
    #print(addItem("t-shirt", "clothing", 1.00, 10.00, 10, 2))
    #updateBusinessAddress(2, "newaddress")
    #updateBusinessName(2, "Walmart2")
    #updateBusinessPassword(2, "newPass")
    #updateBusinessCounty(2, "NewCounty")
    #updateBusinessPhoneNumber(2, 9999999)
    #updateParticipantsFirstName("hantetst@gmail.com","newFirst")
    #updateParticipantsLastName("hantetst@gmail.com","newLast")
    #updateParticipantsIncome("hantetst@gmail.com",5555)
    #updateParticipantsPassword("hantetst@gmail.com","newPAss")
    #addParticipants("han2@han.com", "han","lee",5555,"pass")
    #addBusiness("han2@han.com", 78, "hanNewBusiness", "HanNewPass", "myNewYard", "myCNewounty", 333444)
    #deleteBusiness(5)
    #addItem("tampon", "misc", 33, 50, 10, 5)
    #addItem("cigar", "misc", 10, 20, 10, 5)
    #deleteItems("tampon", 5) 
    #print(deleteBusiness(5))
    # Testing out selecting items
    #updateItemsCategory("NewNew", "tampon", 5)
    #updateItemsPostPrice(999, "tampon", 5)
    #updateItemsOriginalPrice(9999, "tampon", 5)
    #updateItemsQuantity(999, "tampon", 5)
    #print("TEST PRINTING: ")
    #print(verifyLogin("ag@gamil.com","boof"))
    #print("TEST PRINTING for returnBusinessID: ")
    #print(returnBusinessID("ag@gamil.com"))
    #print("TEST PRINTING, BUYER or SELLER: ")
    #print(returnUserType("ag@gamil.com"))
    #print(returnUserType("buyer@gmail.com"))
    #print(returnUserType("seller@gmail.com"))
    # print("TEST PRINTING, returnBusinessInfo: ")
    # print(returnBusinessInfo("ag@gamil.com"))
    # print("Participants")
    # addParticipants("ag1941@gmail.com", "Anthony", "Bologni", 25, "cbd123")

    # categories = ["Food", "Clothing", "Medicine"]
    # counties = []

    # for row in return_all_items("DESC", "DESC"):
    #     print(row)
    for row in filter_items(["Food", "Misc"], [], [], 0, 100, "", "Price", 'DESC'):
        print(row)
