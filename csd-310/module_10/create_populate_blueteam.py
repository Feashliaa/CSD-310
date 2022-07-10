from platform import python_branch
import mysql.connector
from mysql.connector import errorcode

mydb = {
    "host": '127.0.0.1',
    "user": 'root',
    "password": 'password',  # replace with your own password
    # make sure to have an existing database of this name to store
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

    # Drop all tables if they exist - ONLY USE THIS FOR TESTING,
    # you need to drop the tables every time you run the script.
    # Once you have the tables, you can comment this out.
    cursor.execute("DROP TABLE IF EXISTS COMPANY;")
    cursor.execute("DROP TABLE IF EXISTS EMPLOYEE;")
    cursor.execute("DROP TABLE IF EXISTS PRODUCTS;")
    cursor.execute("DROP TABLE IF EXISTS DISTRIBUTOR_ORDERS;")
    cursor.execute("DROP TABLE IF EXISTS DISTRIBUTOR;")
    cursor.execute("DROP TABLE IF EXISTS SUPPLIES;")
    cursor.execute("DROP TABLE IF EXISTS SUPPLY_ORDERS;")
    cursor.execute("DROP TABLE IF EXISTS SUPPLIER;")

    # Creating all tables
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

    # Inserting data INTO the Company table
    sql = "INSERT INTO COMPANY (COMPANY_NAME) VALUES (%s)"
    val = ('Bacchus Winery')
    cursor.execute(sql, (val,))

    # Inserting data INTO the Employee table
    sql = "INSERT INTO EMPLOYEE (EMPLOYEE_ID, FIRST_NAME, LAST_NAME, JOB_TITLE, HOURS_WORKED) VALUES (%s, %s, %s, %s, %s)"
    val = [
        (1001, "Stan", "Bacchus", "Owner", 40),
        (1002, "Davis", "Bacchus", "Owner", 40),
        (1003, "Janet", "Collins", "Finances/Payroll", 40),
        (1004,	"Roz",	"Murphy", "Marketing", 40),
        (1005,	"Bob",	"Ulrich", "Assistant to Roz", 40),
        (1006,	"Henry", "Doyle", "Manages Production", 40),
        (1007,	"Maria", "Costanza", "Manages Distribution", 40)
    ]
    print("test 1")
    cursor.executemany(sql, val,)

    # Inserting data INTO the Products table
    sql = "INSERT INTO PRODUCTS (PRODUCT_ID, PRODUCT_NAME, AMOUNT_IN_INVENTORY, AMOUNT_SOLD, PRICE) VALUES (%s, %s, %s, %s, %s)"
    val = [
        (70001, "Merlot", 499, 1000, 99.99),
        (70002, "Cabernet", 499, 1000, 59.99),
        (70003, "Chablis", 499, 1000, 67.99),
        (70004, "Chardonnay", 499, 1000, 55.99)
    ]
    print("test 2")
    cursor.executemany(sql, val,)

    # Inserting data INTO the DISTRIBUTOR_ORDERS table
    sql = '''INSERT INTO DISTRIBUTOR_ORDERS (DISTRIBUTOR_ORDER_NUMBER, DISTRIBUTOR_ID, 
    PRODUCT_ID, AMOUNT_BOUGHT, TOTAL_PRICE, TRACKING_NUMBER, ORDER_DATE, SHIP_DATE) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'''
    val = [
        (200101, 2001, 70001, 20, 1980, "2004001", "2022-01-01", "2022-01-03"),
        (200102, 2001, 70002, 20, 1180, "2004002", "2022-01-01", "2022-01-03"),
        (200103, 2001, 70003, 20, 1340, "2004003", "2022-01-01", "2022-01-03"),
        (200104, 2001, 70004, 20, 1100, "2004004", "2022-01-01", "2022-01-03")
    ]
    print("test 3")
    cursor.executemany(sql, val,)

    # Inserting data INTO the Distributor table
    sql = "INSERT INTO DISTRIBUTOR (DISTRIBUTOR_ID, DISTRIBUTOR_NAME) VALUES (%s, %s)"
    val = [
        (2001, "ABC Wines"),
        (2002, "Wine & Dine"),
        (2003, "Day Drinking"),
        (2004, "Live, Laugh, Wine")
    ]
    print("test 4")
    cursor.executemany(sql, val,)

    # Inserting data INTO the Supplies table
    sql = "INSERT INTO SUPPLIES (SUPPLY_ID, SUPPLY_NAME, AMOUNT_ON_HAND) VALUES (%s, %s, %s)"
    val = [
        (90001, "Bottles", 21),
        (90002, "Corks", 29),
        (90003, "Labels", 90),
        (90004, "Boxes", 86),
        (90005, "Vats", 101),
        (90006, "Tubing", 49)
    ]
    print("test 5")
    cursor.executemany(sql, val,)

    # Inserting data INTO the Supply_Orders table
    sql = '''INSERT INTO SUPPLY_ORDERS (SUPPLY_ORDER_NUMBER, SUPPLIER_ID, SUPPLY_ID, AMOUNT_ORDERED, TOTAL_COST, 
    SUPPLY_ORDER_DATE, SUPPLY_SHIP_DATE, EXPECTED_DELIVERY_DATE, ACTUAL_DELIVERY_DATE) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)'''
    val = [
        (300101, 3001, 90001, 23, 2500, "2022-02-01",
         "2022-02-03", "2022-02-05", "2022-02-05"),
        (300102, 3001, 90002, 23, 2500, "2022-02-01",
         "2022-02-03", "2022-02-05", "2022-02-05"),

        (300103, 3002, 90003, 29, 2500, "2022-02-02",
         "2022-02-04", "2022-02-06", "2022-02-06"),
        (300104, 3002, 90004, 29, 2500, "2022-02-01",
         "2022-02-03", "2022-02-05", "2022-02-05"),

        (300105, 3003, 90005, 90, 2500, "2022-02-03",
         "2022-02-05", "2022-02-07", "2022-02-09"),
        (300106, 3003, 90006, 90, 2500, "2022-02-01",
         "2022-02-03", "2022-02-05", "2022-02-05")
    ]
    print("test 6")
    cursor.executemany(sql, val,)

    # Inserting data INTO the Supplier table
    sql = "INSERT INTO SUPPLIER (SUPPLIER_ID, SUPPLIER_NAME) VALUES (%s, %s)"
    val = [
        (3001, "B&C"),
        (3002, "L&B"),
        (3003, "V&T")
    ]
    print("test 7")
    cursor.executemany(sql, val,)

    # Showing the tables
    cursor.execute("SHOW TABLES;")

    # Executing the query
    result = cursor.fetchall()

    for x in result:
        print(x)
        print("\n")

    # execute your query
    cursor.execute("SELECT * FROM COMPANY;")
    # fetch all the matching rows
    result = cursor.fetchall()
    # loop through the rows
    print("------------------------------")
    print("COMPANY")
    print("------------------------------")
    for row in result:
        print(row)
        print("\n")

    # execute your query
    cursor.execute("SELECT * FROM DISTRIBUTOR;")
    # fetch all the matching rows
    result = cursor.fetchall()
    # loop through the rows
    print("----------------------------")
    print("DISTRIBUTOR")
    print("----------------------------")
    for row in result:
        print(row)
        print("\n")

    # execute your query
    cursor.execute("SELECT * FROM DISTRIBUTOR_ORDERS;")
    # fetch all the matching rows
    result = cursor.fetchall()
    # loop through the rows
    print("-------------------------------------------------------------------------------------------------------")
    print("DISTRIBUTOR_ORDERS")
    print("-------------------------------------------------------------------------------------------------------")
    for row in result:
        print(row)
        print("\n")

    # execute your query
    cursor.execute("SELECT * FROM EMPLOYEE;")
    # fetch all the matching rows
    result = cursor.fetchall()
    # loop through the rows
    print("----------------------------------------")
    print("EMPLOYEE")
    print("----------------------------------------")
    for row in result:
        print(row)
        print("\n")

    # execute your query
    cursor.execute("SELECT * FROM PRODUCTS;")
    # fetch all the matching rows
    result = cursor.fetchall()
    # loop through the rows
    print("------------------------------")
    print("PRODUCTS")
    print("------------------------------")
    for row in result:
        print(row)
        print("\n")

    # execute your query
    cursor.execute("SELECT * FROM SUPPLIES;")
    # fetch all the matching rows
    result = cursor.fetchall()
    # loop through the rows
    print("-----------------------------")
    print("SUPPLIES")
    print("-----------------------------")
    for row in result:
        print(row)
        print("\n")

    # execute your query
    cursor.execute("SELECT * FROM SUPPLY_ORDERS;")
    # fetch all the matching rows
    result = cursor.fetchall()
    # loop through the rows
    print("----------------------------------------------------------------------------------------------------------------------------------------------------")
    print("SUPPLY_ORDERS")
    print("----------------------------------------------------------------------------------------------------------------------------------------------------")
    for row in result:
        print(row)
        print("\n")

    # execute your query
    cursor.execute("SELECT * FROM SUPPLIER;")
    # fetch all the matching rows
    result = cursor.fetchall()
    # loop through the rows
    print("-------------------")
    print("SUPPLIERS")
    print("-------------------")
    for row in result:
        print(row)
        print("\n")


except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("\n Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("\n Database does not exist")
    else:
        print(err)

finally:
    # committing the changes, and closing the connection
    db.commit()
    db.close()
    print("\n Database connection closed")
