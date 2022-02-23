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

# Function to  perform an INNER JOIN on player and team tables and display the results.
def show_players(cursor, title):
    # inner join query 
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")

    # Fetch results from the cursor object 
    players = cursor.fetchall()

    # Set the format for the titles.
    print("{}\n".format(title))
    
    # Display results using a loop. 
    for player in players:
        print("Player ID: {}\nFirst Name: {}\nLast Name: {}\nTeam Name: {}\n".format(player[0], player[1], player[2], player[3]))

try:
	# Connect to the pysports database.
    db = mysql.connector.connect(**config) 

    # Get the cursor object.
    cursor = db.cursor()

    # Inserting new player into Team Gandalf. 
    add_player = ("INSERT INTO player(first_name, last_name, team_id)"
                 "VALUES(%s, %s, %s)")
    player_data = ("Smeagol", "Shire Folk", 1)
    cursor.execute(add_player, player_data)

    # Commit the insert to the database. 
    db.commit()

    # Show all records in the player table after inserting new playerl 
    show_players(cursor, "DISPLAYING PLAYERS AFTER INSERT:")

    # Update the newly inserted record to Team Sauron.
    update_player = ("UPDATE player SET team_id = 2, first_name = 'Gollum', last_name = 'Ring-Stealer' WHERE first_name = 'Smeagol'")

    # Execute the update query
    cursor.execute(update_player)

    # Show all records in the player table using show_players function.
    show_players(cursor, "DISPLAYING PLAYERS AFTER UPDATE:")

    # Removing the update record with a delete query. 
    delete_player = ("DELETE FROM player WHERE first_name = 'Gollum'")
    cursor.execute(delete_player)

    # show all records in the player table 
    show_players(cursor, "DISPLAYING PLAYERS AFTER DELETE:")

# Error handling.
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Invalid user name or password. Access denied.")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database not found.")

    else:
        print(err)
finally:
    db.close()
