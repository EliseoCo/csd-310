import mysql.connector
from mysql.connector import errorcode

""" database config object """
config = {
    "user": "pytest_user",
    "password": "LetMeIn!",
    "host": "127.0.0.1",
    "database": "pytest",
    "raise_on_warnings": True
}

# Try/catch for potential connection errors.

try:

    db = mysql.connector.connect(**config) # connect to pytest database 
    
    # Display output.
    print("Database user {} connected to MySQL with database {} on host {}".format(config["user"], config["database"], config["host"]))

except mysql.connector.Error as err:
    """ on error code """

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Invalid username or password. Access to database denied.")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database not found.")

    else:
        print(err)

finally:
    db.close()
