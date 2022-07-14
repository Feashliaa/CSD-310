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

    # Executing a SQL query to get the order number, expected delivery date, and the actual delivery date
    cursor.execute(
        "SELECT SUPPLY_ORDER_NUMBER, EXPECTED_DELIVERY_DATE, ACTUAL_DELIVERY_DATE FROM SUPPLY_ORDERS")

    # Storing the results of the query in a variable
    delivery_Dates = cursor.fetchall()

    print("-- Expected vs. Actual Delivery Date --")

    # Looping through the results of the query
    for row in delivery_Dates:
        print("Supply Order Number:           {}".format(row[0]))
        print("Expected Delivery Date:        {}".format(row[1]))
        print("Actual Delivery Date:          {}".format(row[2]))
        print("\n")

    # Select the distributor name, wine name, and the amount of wine sold
    cursor.execute('''SELECT DISTRIBUTOR.DISTRIBUTOR_NAME, PRODUCTS.PRODUCT_NAME, DISTRIBUTOR_ORDERS.AMOUNT_BOUGHT 
                   FROM PRODUCTS INNER JOIN DISTRIBUTOR_ORDERS ON PRODUCTS.PRODUCT_ID = DISTRIBUTOR_ORDERS.PRODUCT_ID INNER JOIN 
                   DISTRIBUTOR ON DISTRIBUTOR_ORDERS.DISTRIBUTOR_ID = DISTRIBUTOR.DISTRIBUTOR_ID''')

    # Storing the results of the query in a variable
    wine_sold = cursor.fetchall()

    print("-- Wines Sold --")

    # Looping through the results of the query
    for row in wine_sold:
        print("Distributor:          {}".format(row[0]))
        print("Wine:                 {}".format(row[1]))
        print("Amount Sold:          {}".format(row[2]))
        print("\n")

    # select the employee name and the numbers of hours worked per quarter
    cursor.execute('''SELECT EMPLOYEE.FIRST_NAME, EMPLOYEE.LAST_NAME, HOURS_WORKED.Q1, HOURS_WORKED.Q2, HOURS_WORKED.Q3, HOURS_WORKED.Q4
                   FROM EMPLOYEE INNER JOIN HOURS_WORKED ON EMPLOYEE.EMPLOYEE_ID = HOURS_WORKED.EMPLOYEE_ID''')

    # Storing the results of the query in a variable
    hours_worked = cursor.fetchall()

    print("-- Hours Worked --")

    # Looping through the results of the query
    for row in hours_worked:
        print("Employee:        {}".format(row[0]) + " " + row[1])
        print("Q1:              {}".format(row[2]) + " hours")
        print("Q2:              {}".format(row[3]) + " hours")
        print("Q3:              {}".format(row[4]) + " hours")
        print("Q4:              {}".format(row[5]) + " hours")
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
