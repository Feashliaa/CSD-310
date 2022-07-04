from platform import python_branch
import mysql.connector
from mysql.connector import errorcode

mydb = {
    "host": '127.0.0.1',
    "user": 'root',
    "password": '---------', # I used a password that I shouldn't be posting on github, so I wont be putting it in the code
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
    
    ## Inner join on the team_id column
    sql = " SELECT player.player_id, player.first_name, player.last_name, team.team_name FROM player INNER JOIN team ON player.team_id = team.team_id"

    cursor.execute(sql)

    my_result = cursor.fetchall()
    
    # Print the results
    for row in my_result:
        print("Player ID: ", row[0])
        print("First Name: ", row[1])
        print("Last Name: ", row[2])
        print("Team Name: ", row[3])
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