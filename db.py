import oracledb

# Variables needed for the login.
username = "hlee3"
userpwd = "dzPHnwNnvWrLjXL7S0oZNmYv"
host = "oracle.cise.ufl.edu"
port = 1521
service_name = "orcl"

dsn = f'{username}/{userpwd}@{host}:{port}/{service_name}'    

'''
Adds user to the database.
'''
def addParticipants(email: str, firstName: str, lastName: str, income: int, password: str) -> str:
    # Attempt connection to Oracle database.
    try:
        connection = oracledb.connect(dsn = dsn)
        print("Connected to database")

    except:
        print("Was not able to connect to the database.")
    cur = connection.cursor()
    try:
        cur.execute("insert into participants values (:email, :firstName, :lastName, :income, :password)", [email, firstName, lastName, income, password])
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

def deleteBusiness(id: int) -> None:
    try:
        connection = oracledb.connect(dsn = dsn)
        print("Connected to database")
    except:
        print("Was not able to connect to database")
    cur = connection.cursor()
    try:
        cur.execute("delete from items where bid = :bid", [id])
        connection.commit()
        output = "Deleted items from database."
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
    
    cur.execute("select * from participants where email = :email and password = :password", [email, password])
    user = cur.fetchall()
    if (len(user) != 1):
        print("Password does not match, try again")
        return None
    print("Successfully verified user")
    return user

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
    return bid[0]

def return_all_items():

    try:
        connection = oracledb.connect(dsn = dsn)

    except:
        return "Was not able to connect to the database"

    cur = connection.cursor()

    cur.execute("SELECT * FROM Items")

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

def deleteItems(name: str, bid: int) -> None:
    try:
        connection = oracledb.connect(dsn = dsn)
        print("Connected to database")
    except:
        print("Was not able to connect to database")
    cur = connection.cursor()
    try:
        cur.execute("delete from items where name = :name and bid = :bid", [name, bid])
        connection.commit()
        output = "Deleted items from database."
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
        output = "Updated business"
    except:
        output = "Unsuccessful"
    connection.close()

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
        output = "Updated business"
    except:
        output = "Unsuccessful"
    connection.close()
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
        output = "Updated business"
    except:
        output = "Unsuccessful"
    connection.close()  
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
        output = "Updated business"
    except:
        output = "Unsuccessful"
    connection.close()  
    
# def addBusiness(email: str, id: int, name: str, password: str, address: str, county: str, phoneNumber: int)
# def addItem(name: str, category: str, postPrice: float, originalPrice: float, quantity: int, bId: int)-

if __name__ == "__main__":
    #addParticipants("ag@gamil.com", "Anthony", "Gravier", 85000, "boof")
    #Returning business id, based on email


    #deleteParticipant("realNewEmail@RealNew.com")  
    #deleteParticipant("ag@gamil.com")   
    #addParticipants("ag@gamil.com", "Anthony", "Gravier", 85000, "boof")
    #updateParticipants("ag@gamil.com", "newFirstName", "newLastName",911911,"newPassword")
    #updateEmail("ag@gamil.com", "newFirstName", "newLastName",911911,"newPassword","realNewEmail@RealNew.com")
    #deleteParticipant("realNewEmail@RealNew.com")
    #addBusiness("ag@gamil.com", 5, "Business", "pass1", "address1", "33612", 123456789)
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
    print("Participants")
    print()

    for row in return_all_participants():
        print(row)

