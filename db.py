import oracledb
import hashlib

# Variables needed for the login.
username = "hlee3"
userpwd = "dzPHnwNnvWrLjXL7S0oZNmYv"
host = "oracle.cise.ufl.edu"
port = 1521
service_name = "orcl"

dsn = f'{username}/{userpwd}@{host}:{port}/{service_name}'    
salt = "HAPM4"

# Helper functions for project
def hashCode(code: str):
    code = code + salt
    hashed = hashlib.md5(code.encode())
    # print("Hashed Password is: " + hashed)
    return hashed

'''
    Verifies emails of users for testing, returns a boolean. True if participant with given email exists.
'''
def verifyEmail(email: str) -> bool:
    # Attempt connection to Oracle database.
    try:
        connection = oracledb.connect(dsn = dsn)
        print("Connected to database")
    except:
        print("Was not able to connect to the database.")
        return False
    
    email = hashCode(email).hexdigest()
    cur = connection.cursor()
    
    try:
        cur.execute("select * from participants where email = :email", [email])
        count = cur.fetchall()
        if (len(count) == 0):
            print("Unique email.")
            return True
        return False
    except:
        print("Could not execute query to find a user with given email.")
        return False
    
def checkBusinessId(id: int) ->bool:

    if id < 0 or id > 100:
        return False

    # Attempt connection to Oracle database.
    try:
        connection = oracledb.connect(dsn = dsn)
        print("Connected to database")
    except:
        print("Was not able to connect to the database.")
        return False
    cur = connection.cursor()
    
    try:
        cur.execute("select * from Business where id = :id", [id])
        count = cur.fetchall()
        if (len(count) == 0):
            print("Unique Id.")
            return True
        return False
    except:
        print("Could not execute query to check Business id")
        return False
'''
Adds user to the database.
'''
def addParticipants(email: str, firstName: str, lastName: str, income: int, password: str) -> str:

    hashedEmail = hashCode(email).hexdigest()
    hashedPassword = hashCode(password).hexdigest()

    # Attempt connection to Oracle database.
    try:
        connection = oracledb.connect(dsn = dsn)
        print("Connected to database")

    except:
        print("Was not able to connect to the database.")
    cur = connection.cursor()
    try:
        cur.execute("insert into participants values (:email, :firstName, :lastName, :income, :password)", [hashedEmail, firstName, lastName, income, hashedPassword])
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

    email = hashCode(email).hexdigest()
    password = hashCode(password).hexdigest()

    # Attempt connection to Oracle database.
    try:
        connection = oracledb.connect(dsn = dsn)
        print("Connected to database")
    except:
        print("Was not able to connect to database")
    cur = connection.cursor()
    # Insert into database a business model.
    try:
        cur.execute("insert into Business values(:id, :name, :password, :address, :county, :phone_number)", [id, name, password, address, county, phoneNumber])
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
        output = "Unable to delete ownsbusiness from database"
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

    email = hashCode(email).hexdigest()
    password = hashCode(password).hexdigest()

    # Attempt connection to Oracle db.
    try: 
        connection = oracledb.connect(dsn=dsn)
        print("Connected to database")
    except:
        print("Was not able to connect to database")
        print(oracledb.connect(dsn=dsn))
    cur = connection.cursor()
    # Check if the user even exists
    cur.execute("select * from participants where email = :email", [email])
    number = cur.fetchall() 
    if (len(number) != 1):
        print("User with email does not exist")
        return None
    
    cur.execute("select * from participants where email = :email and password = :password", [email, password])
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
    if (income[0][0] == -1):
        #print("User with email does not exist")
        return "Seller"
    # Check if the user is associated with a business
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
    except:
        print("Could not update participants information.")
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
    except:
        print("Could not update participants.")
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
    except:
        print("Could not update participants.")

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
    except:
        print("Could not update participants.")
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
    except:
        print("Could not update participants.")
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
    except:
        print("Could not update participants.")
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
    except:
        print("Could not update participants.")
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
    except:
        print("Could not update participants.")
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
    except:
        print("Could not update participants.")
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
        print("Connected to database distinct counties")
    except:
        print("Was not able to connect to database")
        print(oracledb.connect(dsn = dsn))

    cur = connection.cursor()

    cur.execute("SELECT DISTINCT(b.county) from Business b join items i on i.bID = b.id ORDER BY Lower(b.county) ASC")

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

    cur.execute("SELECT DISTINCT(b.name) from Business b join items i on i.bID = b.id ORDER BY Lower(b.name) ASC")

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
        cur.execute("SELECT DISTINCT(b.county) from Business b join items i on i.bID = b.id")
        all_counties = cur.fetchall()
        counties = [county[0] for county in all_counties]

    if len(business_names) == 0:
        cur.execute("SELECT DISTINCT(b.name) from Business b join items i on i.bID = b.id")
        all_businesses = cur.fetchall()
        business_names = [business[0] for business in all_businesses]

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
    for row in filter_items([], [], [], 0, 1000, "", "Price", 'ASC'):
        print(row)
    
