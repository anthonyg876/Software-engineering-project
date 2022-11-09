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
def addBusiness(id: int, name: str, password: str, address: str, county: str, phoneNumber: int) -> str:
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
    connection.close()
    
def deleteUser(email: str) -> None:
    connection = oracledb.connect(dsn = dsn)
    cur = connection.cursor()
    cur.execute("delete from participants where email = :email", [email])
    connection.commit()
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

if __name__ == "__main__":
    addUser("ag@gamil.com", "Anthony", "Gravier", 85000, "boof")
    deleteUser("ag@gamil.com")
    


    # addUser("ag@gamil.com", "Anthony", "Gravier", 85000, "boof")\

    #print(addBusiness(2, "Walmart", "password1", "100 Gainesville Road", "Sarasota County", 7271111111))
    #print(addItem("t-shirt", "clothing", 1.00, 10.00, 10, 2))

    # Testing out selecting items

    for row in return_all_items():
        print(row)
