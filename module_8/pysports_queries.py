import mysql.connector
from mysql.connector import errorcode

""" database config object """
config = {
    "user": "pysports_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

# Try/catch block to handle possible errors.
try:
    db = mysql.connector.connect(**config) # connect to the pysports database 

    cursor = db.cursor()

    # Team table query. 
    cursor.execute("SELECT team_id, team_name, mascot FROM team")
 
    teams = cursor.fetchall()

    print("DISPLAYING TEAM RECORDS:")
    
    # Loop to display team records. 
    for team in teams: 
        print("Team ID: {}\nTeam Name: {}\nMascot: {}\n".format(team[0], team[1], team[2]))

    # Player table query.
    cursor.execute("SELECT player_id, first_name, last_name, team_id FROM player")
 
    players = cursor.fetchall()

    print ("\nDISPLAYING PLAYER RECORDS:")

    # Loop to display player records. 
    for player in players:
        print("Player ID: {}\nFirst Name: {}\nLast Name: {}\nTeam ID: {}\n".format(player[0], player[1], player[2], player[3]))

# Error handling.
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Invalid username or password. Access is denied.")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Cannot find database.")

    else:
        print(err)

finally:
    db.close()
    
