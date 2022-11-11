import oracledb

# Variables needed for the login.
username = "agravier"
userpwd = "OlQYCYdeeIRYwRWfnhMePgKi"
host = "oracle.cise.ufl.edu"
port = 1521
service_name = "orcl"

dsn = f'{username}/{userpwd}@{host}:{port}/{service_name}'    

'''
Adds user to the database.
'''
def addUser(email: str, firstName: str, lastName: str, income: int, password: str) -> str:
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
    try:
        cur.execute("insert into ownsbusiness values(:email, :bid)", [email, id])
        connection.commit()
        output = "inserted ownsbusiness relationship Email"
    except:
        output = "Unsuccessful"
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
        cur.execute("delete from participants where email = :email", [email])
        connection.commit()
        output = "Deleted user from database."
    except:
        output = "Unable to deleted user from database"
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

# @TODO Needs to be completed.
def update_items():
    connection = oracledb.connect(dsn = dsn)

    with connection.cursor() as cursor:
        cursor.execute("insert into table participants")

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

    cur.execute("SELECT * FROM participants")

    all_participants = cur.fetchall()
    connection.close()

    return all_participants

def return_all_businesses():

    try:
        connection = oracledb.connect(dsn = dsn)

    except:
        return "Was not able to connect to the database"

    cur = connection.cursor()

    cur.execute("SELECT * FROM Business")

    all_businesses = cur.fetchall()
    connection.close()

    return all_businesses

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

  
# def addBusiness(email: str, id: int, name: str, password: str, address: str, county: str, phoneNumber: int)
# def addItem(name: str, category: str, postPrice: float, originalPrice: float, quantity: int, bId: int)-

if __name__ == "__main__":
    #addUser("ag@gamil.com", "Anthony", "Gravier", 85000, "boof")
    #deleteParticipant("realNewEmail@RealNew.com")  
    #deleteParticipant("ag@gamil.com")   
    #addUser("ag@gamil.com", "Anthony", "Gravier", 85000, "boof")
    #updateParticipants("ag@gamil.com", "newFirstName", "newLastName",911911,"newPassword")
    #updateEmail("ag@gamil.com", "newFirstName", "newLastName",911911,"newPassword","realNewEmail@RealNew.com")
    #deleteParticipant("realNewEmail@RealNew.com")
    #addBusiness("mk@gmail.com", 5, "Business", "pass1", "address1", "33612", 123456789)
    #updateBusiness(1, "NEwBusiness", "NEwpass1", "Newaddress1", "33615", 00000000)
    #print(deleteBusiness(5))
    #print(updateParticipantsFirstName("mk@gmail.com","RealNewNEWMatthew"))
    #print(updateParticipantsLastName("mk@gmail.com","REalNewKerekes"))
    #print(updateParticipantsIncome("mk@gmail.com",1000000))
    #print(updateParticipantsPassword("mk@gmail.com","NewPass"))
    # addUser("ag@gamil.com", "Anthony", "Gravier", 85000, "boof")\
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
    #addUser("han2@han.com", "han","lee",5555,"pass")
    #addBusiness("han2@han.com", 78, "hanNewBusiness", "HanNewPass", "myNewYard", "myCNewounty", 333444)


    # Testing out selecting items


    for row in return_all_participants():
        print(row)
