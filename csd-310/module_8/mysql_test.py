import mysql.connector
from mysql.connector import errorcode

mydb = {
    "host": '127.0.0.1',
    "user": 'root',
    "password": 'D4rkGwen2#',
    "database": 'pysports',
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**mydb)
    
    print("\n Database user {} connected to MySQL on host {} with database {}".format(mydb['user'], mydb['host'], mydb['database']))
    
    input("\n Press any key to continue...")
    
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("\n Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("\n Database does not exist")
    else:
        print(err)

finally:
    db.close();