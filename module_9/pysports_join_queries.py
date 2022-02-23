import mysql.connector
from mysql.connector import errorcode

# Database config object
config = {
    "user": "pysports_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

try: 
	# Connect to the pysports database
    db = mysql.connector.connect(**config) 
    cursor = db.cursor()

    # INNER JOIN to connect play and team table using team_id. 
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")

    # Fetch results from cursor object. 
    players = cursor.fetchall()

    print("DISPLAYING PLAYER RECORDS:\n")
    
    # Display the results using a loop.
    for player in players:
        print("Player ID: {}\nFirst Name: {}\nLast Name: {}\nTeam Name: {}\n".format(player[0], player[1], player[2], player[3]))

# Error handling.
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Invalid name or password. Access denied.")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database not found.")

    else:
        print(err)

finally:
    db.close()
