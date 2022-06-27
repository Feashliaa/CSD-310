import mysql.connector
from mysql.connector import errorcode

config = {
    'user': 'pysorts user',
    'password': 'pysorts D4rkGwen2#',
    'host': '127.0.0.1',
    'database': 'pysorts',
    'raise_on_warnings': True
}

try:
    cnx = mysql.connector.connect(**config)

    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

    input("\n Press Enter to continue...")

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print(' The supplied user name or password is wrong.')
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print(' Database does not exist.')
        else:
            print(err)
        
    finally:
        db.close()