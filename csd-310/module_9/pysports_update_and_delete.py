import mysql.connector
from mysql.connector import errorcode

mydb = {
    "host": '127.0.0.1',
    "user": 'root',
    "password": '----------', # hidden password for github
    "database": 'pysports',
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**mydb)

    print("\n Database user {} connected to MySQL on host {} with database {}".format(
        mydb['user'], mydb['host'], mydb['database']))

    input("\n Press any key to continue...")
    print("\n")

    cursor = db.cursor()

    # Insert a new player into team_id = 1 - team gandalf
    cursor.execute(
        "INSERT INTO player (first_name, last_name, team_id) VALUES ('Smeagol', 'Shire Folk', 1)")

    # Inner joining on the team_id column
    sql = " SELECT player.player_id, player.first_name, player.last_name, team.team_name FROM player INNER JOIN team ON player.team_id = team.team_id"

    cursor.execute(sql)

    player_result = cursor.fetchall()

    print("-- Displaying Players After Insert --")
    for row in player_result:
        print("Player ID: ", row[0])
        print("First Name: ", row[1])
        print("Last Name: ", row[2])
        print("Team Name: ", row[3])

    # update the smeeagol team to sauron, and change his name to gollum
    sql = "UPDATE player SET team_id = 2, first_name = 'Gollum', last_name = 'Ring Stealer' WHERE first_name = 'Smeagol'"
    cursor.execute(sql)

    # Inner joining on the team_id column
    sql = " SELECT player.player_id, player.first_name, player.last_name, team.team_name FROM player INNER JOIN team ON player.team_id = team.team_id"
    cursor.execute(sql)
    updated_results = cursor.fetchall()

    print("-- Displaying Players After Update --")

    for row in updated_results:
        print("Player ID: ", row[0])
        print("First Name: ", row[1])
        print("Last Name: ", row[2])
        print("Team Name: ", row[3])
        
    # Delete the new player record from the database with the name of "Gollum"
    sql = "DELETE FROM player WHERE first_name = 'Gollum'"
    cursor.execute(sql)
    
    # Inner joining on the team_id column
    sql = " SELECT player.player_id, player.first_name, player.last_name, team.team_name FROM player INNER JOIN team ON player.team_id = team.team_id"
    cursor.execute(sql)
    deleted_results = cursor.fetchall()
    
    print("-- Displaying Players After Delete --")
    
    for row in deleted_results:
        print("Player ID: ", row[0])
        print("First Name: ", row[1])
        print("Last Name: ", row[2])
        print("Team Name: ", row[3])


except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("\n Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("\n Database does not exist")
    else:
        print(err)

finally:
    db.close()
