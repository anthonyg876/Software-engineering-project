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
def addUser(email: str, firstName: str, lastName: str, income: int, password: str) -> None:
    connection = oracledb.connect(dsn = dsn)
    cur = connection.cursor()
    cur.execute("insert into participants values (:email, :firstName, :lastName, :income, :password)", [email, firstName, lastName, income, password])
    connection.commit()
    connection.close()
    
def deleteUser(email: str) -> None:
    connection = oracledb.connect(dsn = dsn)
    cur = connection.cursor()
    cur.execute("delete from participants where email = :email", [email])
    connection.commit()
    connection.close()
    
def update_items():
    connection = oracledb.connect(dsn = dsn)

    with connection.cursor() as cursor:
        cursor.execute("insert into table participants")
    st.write("Updated")

if __name__ == "__main__":
    addUser("ag@gamil.com", "Anthony", "Gravier", 85000, "boof")
    deleteUser("ag@gamil.com")
    

