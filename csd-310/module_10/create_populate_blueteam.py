from platform import python_branch
import mysql.connector
from mysql.connector import errorcode

mydb = {
    "host": '127.0.0.1',
    "user": 'root',
    "password": 'password',  # replace with your own password
    # make sure to have an existing database of this name to store into
    "database": 'bacchus_winery',
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**mydb)

    print("\n Database user {} connected to MySQL on host {} with database {}".format(
        mydb['user'], mydb['host'], mydb['database']))

    input("\n Press any key to continue...")
    print("\n")

    # Creating a cursor object using the cursor method
    cursor = db.cursor()

    # Drop all tables if they exist

    cursor.execute("DROP TABLE IF EXISTS COMPANY;")
    cursor.execute("DROP TABLE IF EXISTS EMPLOYEE;")
    cursor.execute("DROP TABLE IF EXISTS PRODUCTS;")
    cursor.execute("DROP TABLE IF EXISTS DISTRIBUTOR_ORDERS;")
    cursor.execute("DROP TABLE IF EXISTS DISTRIBUTOR;")
    cursor.execute("DROP TABLE IF EXISTS SUPPLIES;")
    cursor.execute("DROP TABLE IF EXISTS SUPPLY_ORDERS;")
    cursor.execute("DROP TABLE IF EXISTS SUPPLIER;")

    # Executing the query
    cursor.execute("CREATE TABLE COMPANY (COMPANY_NAME CHAR(20))")

    cursor.execute(
        "CREATE TABLE EMPLOYEE (EMPLOYEE_ID int, FIRST_NAME CHAR(20), LAST_NAME CHAR(20),JOB_TITLE CHAR(20), HOURS_WORKED int)")

    cursor.execute(
        "CREATE TABLE PRODUCTS (PRODUCT_ID int, PRODUCT_NAME char(20), AMOUNT_IN_INVENTORY int, AMOUNT_SOLD int, PRICE float)")

    cursor.execute('''CREATE TABLE DISTRIBUTOR_ORDERS (DISTRIBUTOR_ORDER_NUMBER int, DISTRIBUTOR_ID int, 
        PRODUCT_ID int,AMOUNT_BOUGHT int, TOTAL_PRICE float, TRACKING_NUMBER CHAR(20), ORDER_DATE date, SHIP_DATE date)''')

    cursor.execute(
        "CREATE TABLE DISTRIBUTOR (DISTRIBUTOR_ID int, DISTRIBUTOR_NAME CHAR(20))")

    cursor.execute(
        "CREATE TABLE SUPPLIES (SUPPLY_ID int, SUPPLY_NAME char(20), AMOUNT_ON_HAND int)")

    cursor.execute('''CREATE TABLE SUPPLY_ORDERS (SUPPLY_ORDER_NUMBER int,  SUPPLIER_ID int, SUPPLY_ID int, AMOUNT_ORDERED int, 
        TOTAL_COST float, SUPPLY_ORDER_DATE date,  SUPPLY_SHIP_DATE date, EXPECTED_DELIVERY_DATE date, ACTUAL_DELIVERY_DATE date)''')

    cursor.execute(
        "CREATE TABLE SUPPLIER (SUPPLIER_ID int,  SUPPLIER_NAME CHAR(20))")

    # Dropping the table if it exists
    cursor.execute("SHOW TABLES;")

    # Executing the query
    result = cursor.fetchall()

    for x in result:
        print(x)


except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("\n Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("\n Database does not exist")
    else:
        print(err)

finally:
    db.close()
