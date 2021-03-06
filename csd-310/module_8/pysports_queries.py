import mysql.connector
from mysql.connector import errorcode

mydb = {
    "host": '127.0.0.1',
    "user": 'root',
    "password": '---------',
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

    cursor.execute("SELECT * FROM team")

    team_result = cursor.fetchall()

    print("-- Displaying Team Records --")
    
    for row in team_result:
        print("Team ID: ", row[0])
        print("Team Name: ", row[1])
        print("Mascot: ", row[2])
        print("\n")

    cursor = db.cursor()

    cursor.execute("SELECT * FROM player")

    player_result = cursor.fetchall()
    
    print("-- Displaying Player Records --")

    for row in player_result:
        print("Player ID: ", row[0])
        print("First Name: ", row[1])
        print("Last Name: ", row[2])
        print("Team ID: ", row[3])
        print("\n")


except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("\n Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("\n Database does not exist")
    else:
        print(err)

finally:
    db.close()
