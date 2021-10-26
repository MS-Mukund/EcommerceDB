from os import uname
import subprocess as sp
import pymysql
import pymysql.cursors
import datetime

import bisect

UserName = ""
dbName = "BUYNOW"

# price range
PriceUpperBounds = [500, 1000, 2000, 3000, 5000, 10000, 20000, 50000, 100000, 200000, 500000, 1000000]
PriceFilter = (MIN, MAX) = (0, 1e9)

# Category List
CategoryList = []
CategoryFilter = []

def UpdateUserDetails():
    """
    if username of customer is not present in the database, then asks user to create a new account
    else, updates the columns requested by the user.
    """
    try:
        # Take username as input
        # if username already exists, update the columns specified by user
        # else, ask for all the columns and insert the data into the database

        row = {}
        # columns = []
        UserName = input("Username: ")

        # Check if the username already exists
        cur.execute("SELECT EXISTS(SELECT * FROM Users WHERE Username = %s);" % (UserName))

        check = cur.fetchone()[0]

        if( check > 0 ):
            print("Type the columns (comma-separated) you want to update: ")
            print("List of columns:")
            print("1. Phone_number")
            print("2. First_name")
            print("3. middle_name")
            print("4. Last_name")
            print("5. Email")
            print("6. Password")
            print("7. Premium_subscription")
            print("8. Address_Line1")
            print("9. Address_Line2")
            print("10. Pincode")
            print()

            # Get the columns to be updated
            columns = input("Enter the columns, comma-separated: ").split(",")
            for column in columns:
                if(column.lower() == "Premium_subscription".lower()):
                    row[column] = bool(input("Premium_subscription: "))
                    continueorderid = 1
                elif column.lower() == "Username".lower():
                    print("You cannot change username")
                    continue

                row[column] = input("Enter the value for %s: " % column)

            # Update columns specified by user, not all
            for column in columns:
                cur.execute("UPDATE Users SET %s = '%s' WHERE Username = '%s';" % (column, row[column], UserName))


            print("Data updated successfully")
        
        else:
            print("Are you sure you want to set this as your username(y/n): ")
            if(input().lower() == "y"):
                row[0] = UserName
            else:
                inp = input("Enter new username: ")
                row[0] = inp
                UserName = inp
                
            row[1] = input("Phone_number: ")
            row[2] = input("First_name: ")
            row[3] = input("middle_name: ")
            row[4] = input("Last_name: ")
            row[5] = input("Email: ")
            row[6] = input("Password: ")
            # convert the input to boolean
            row[7] = bool(input("Premium_subscription(0 or 1): "))
            row[8] = input("Address_Line1: ")
            row[9] = input("Address_Line2: ")
            row[10] = input("Pincode: ")

            # Insert the data
            cur.execute("INSERT INTO Users VALUES(%s, %s, %s, %s, %s, %s, %s, %d, %s, %s, %s);" %
            (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10]))

        con.commit()

        print("Updated your details")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return


def FilterCategory():
    """
    Function to filter the category
    """
    global CategoryFilter, CategoryList
    filter = input("Enter the category: ")

    # Check if the category exists    
    if filter in CategoryList:
        CategoryFilter.append(filter)
    else:
        print("Invalid option: press 7 to list all categories")


def ListCategory():
    """
    Function to list all the categories
    """
    global CategoryList

    print("List of categories:")
    for category in CategoryList:
        print(category)

def RemoveCategory():
    global CategoryFilter
    inp = input("Enter category to be removed (all if you want to remove all filters): ")
    if(inp == "all"):
        CategoryFilter = []
    elif inp in CategoryFilter:
        CategoryFilter.remove(inp)
    else:
        print("Invalid option %s", inp)


def ListPrice():
    """
    Function to list the price range
    """
    print("Price Range: ", end="")
    for bound in enumerate (PriceUpperBounds):
        if( bound[0] == 0):
            print("< %d" % bound[1])
        elif( bound[0] == len(PriceUpperBounds) - 1):
            print("> %d" % bound[1])
        else:
            print("%d - %d" % (PriceUpperBounds[bound[0]-1], bound[1]))


def FilterPrice():
    """
    Function to add price filter
    """
    global PriceFilter
    inp = input("Enter the price range(a-b): ")
    inp = inp.split("-")
    if(len(inp) == 2):
        try:
            inp = [ int(inp[0]), int(inp[1]) ]
            if(inp[0] > inp[1]):
                inp[0], inp[1] = inp[1], inp[0]
            
            # closest upper bound to inp[0] and inp[1]
            inp[0] = PriceUpperBounds[bisect.bisect_left(PriceUpperBounds, inp[0])]
            inp[1] = PriceUpperBounds[bisect.bisect_right(PriceUpperBounds, inp[1])]

            PriceFilter = inp 
        except:
            print("error adding price filter")
    else:
        print("Invalid price range")

def RemovePrice():
    global PriceFilter
    PriceFilter = (MIN, MAX)
    print("removed")
    
def Insert_Order_Details():
    try:
        var=0
        while(var==0):
            row = {}
            cur.execute("SELECT EXISTS(SELECT * FROM Orders WHERE Order_id = %s);" % (Orders.Order_id))
            check = next( iter((cur.fetchone()).values()) )
            #check = cur.fetchone()[0]
            if( check <= 0 ):
                print("There is already an order with the order_ID '%s',Please give unique one\n" % (Orders.Order_id))
            else:
                x=0
                while(x==0):
                    row[0] = input("Enter Username: ")
                    #print(row[0])
                    cur.execute("SELECT EXISTS(SELECT * FROM Users WHERE Username = '%s');" % (row[0]))
                    check = next( iter((cur.fetchone()).values()) )
                    if(check<=0):
                        print("User with the username %s doesn't exist in the database\n" % row[0])
                    else:
                        break
                while(x==0):
                    row[1] = input("Enter Product ID: ")
                    cur.execute("SELECT EXISTS(SELECT * FROM Products WHERE Product_ID= '%s');" % (row[1]))
                    check_productid = next( iter((cur.fetchone()).values()) )
                    if(check_productid<=0):
                        print("Product with the Product_ID %s doesn't exist in the database\n" % row[1])
                    else:
                        break 
                while(x==0):
                    row[2] = input("Enter Supplier ID: ")
                    cur.execute("SELECT EXISTS(SELECT * FROM Suppliers WHERE SupplierID= '%s');" % (row[2]))
                    check_supplierid = next( iter((cur.fetchone()).values()) )
                    if(check_supplierid<=0):
                        print("Supplier with this Supplier_ID %s doesn't exist in the database\n" % row[2])
                    else:
                        break 
                while(x==0):
                    row[3] = input("Enter Agency ID: ")
                    cur.execute("SELECT EXISTS(SELECT * FROM Delivery_Agency WHERE Agency_ID = '%s');" % (row[3]))
                    check_agencyid = next( iter((cur.fetchone()).values()) )
                    if(check_agencyid<=0):
                        print("Agency with this Agency_ID %s doesn't exist in the database\n" % row[3])
                    else:
                        break 
                while(x==0):
                    row[4] = input("Enter the date in format 'yy/mm/dd': ")
                    year, month, day = row[4].split('-')
                    year = int(year)
                    month = int(month)
                    day = int(day)
                    if(year>=0 and year<=2022 and month>=0 and month <=12 and day>=0 and day<=31):
                        break
                while(x==0):
                    row[5] = input("Enter Amount_Paid: ")
                    row[5] = int(row[5])
                    p = int(row[5]);                   
                    if(row[5]!=p):
                        print("Provide valid Amount Paid\n")
                    else:
                        break
                row[6] =0
                row[7] = "NULL"
                row[8] = orderid

                cur.execute("INSERT INTO Orders VALUES('%s', '%s', 0, NULL, '%s', '%s', '%s', '%s', '%s');" %
                (row[4], row[5],row[3], row[2], row[0], row[1], row[8]))
                con.commit()
                cur.execute("INSERT INTO Purchase_Transaction VALUES('%s', '%s', '%s', '%s', '%s');" %
                (row[3], row[2], row[0], row[1], row[8]))
                con.commit()
                print("Updated your details")
                break
                

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return



def Insert_Return_Order_Details():
    try:
        var=0
        while(var<0):
            row = {}
            return_orderid = input("Return_ID: ")
            # Check if the orderId is unique or not
            cur.execute("SELECT EXISTS(SELECT * FROM Return_Order WHERE Return_ID = %s);" % (return_orderid))
            check = cur.fetchone()[0]
            if( check > 0 ):
                print("There is already an return order with the Returnorder_ID %s,Please give unique one\n" % (return_orderid))
            else:
                row[0] = return_orderid
                x=0
                while(x<0):
                    row[1] = print("Enter Date_of_order: ")
                    if type(row[1]) !="date":
                        print("Provide valid date\n")
                    else:
                        break
                    
                while(x<0):
                    row[2] = print("Enter Product ID: ")
                    cur.execute("SELECT EXISTS(SELECT * FROM Products WHERE Product_ID= %s);" % (row[2]))
                    check_productid = cur.fetchone()[0]
                    if(check_productid<=0):
                        print("Product with this Product_ID doesn't exist in the database\n")
                    else:
                        break 
                while(x<0):
                    row[5] = print("Enter Supplier ID: ")
                    cur.execute("SELECT EXISTS(SELECT * FROM Suppliers WHERE SupplierID= %s);" % (row[5]))
                    check_supplierid = cur.fetchone()[0]
                    if(check_supplierid<=0):
                        print("Supplier with this Supplier_ID doesn't exist in the database\n")
                    else:
                        break 
                while(x<0):
                    row[4] = print("Enter Agency ID: ")
                    cur.execute("SELECT EXISTS(SELECT * FROM Delivery_Agency WHERE Agency_ID = %s);" % (row[4]))
                    check_agencyid = cur.fetchone()[0]
                    if(check_agencyid<=0):
                        print("Agency with this Agency_ID doesn't exist in the database\n")
                    else:
                        break 
                while(x<0):
                    row[6] = print("Enter Username: ")
                    cur.execute("SELECT EXISTS(SELECT * FROM Users WHERE Username = %s);" % (row[6]))
                    check_username = cur.fetchone()[0]
                    if(check_username<=0):
                        print("User with this username doesn't exist in the database\n")
                    else:
                        break
                while(x<0):
                    row[3] = print("Enter Refund Amount: ")
                    if type(row[3])!="int":
                        print("Provide valid Refund Amount\n")
                    else:
                        break
                 # Insert the data
                cur.execute("INSERT INTO Return_Order VALUES(%s, %s, %s, %s, %s, %s, %s);" %
                (row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
                con.commit()
                cur.execute("INSERT INTO Return_Transaction VALUES(%s, %s, %s, %s, %s);" %
                (row[4], row[5], row[6], row[2], row[0]))
                con.commit()
                print("Updated your details")
                

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return
def Orders_Yet_ToBe_Returned():
    try:
        var=0
        while(var<0):
            Username = print("Enter Username: ")
            cur.execute("SELECT EXISTS(SELECT * Users FROM  WHERE Username = %s);" % (Username))
            check = cur.fetchone()[0]
            if( check <= 0 ):
                print("There is no user with the Username %s" % (Username))
            else:
                query = 'SELECT O_Username,Order_ID,O_Product_ID,O_Agency_ID,O_SupplierID,Amount_Paid,Placed_Date FROM Orders WHERE R_Username=%s AND Is_it_delivered=0' % (Username)
                cur.execute(query)
                break
    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return


def Orders_Queued():
    try:
        var=0
        while(var<0):
            Username = print("Enter Username: ")
            cur.execute("SELECT EXISTS(SELECT * Users FROM  WHERE Username = %s);" % (Username))
            check = cur.fetchone()[0]
            if( check <= 0 ):
                print("There is no user with the Username %s" % (Username))
            else:
                cur.execute("SELECT O_Username,Order_ID,O_Product_ID,O_Agency_ID,O_SupplierID,Amount_Paid,Placed_Date,Date_of_Delivery,Is_it_delivered FROM Orders WHERE R_Username=%s ORDER BY Placed_Date",Username)
                break
    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return

def dispatch(ch):
    """
    Function that maps helper functions to option entered
    """

    if(ch == 1):
        UpdateUserDetails()
    elif(ch == 2):
        Insert_Order_Details()
    elif(ch == 3):
        Insert_Return_Order_Details()
    elif(ch == 4):
        pass
    elif(ch == 5):
        FilterCategory()
    elif(ch == 6):
        RemoveCategory()
    elif(ch == 7):
        ListCategory()
    elif(ch == 8):
        ListPrice()
    elif(ch == 9):
        FilterPrice()
    elif(ch == 10):
        RemovePrice()
    elif(ch == 11):
        Orders_Yet_ToBe_Returned()
    elif(ch == 12):
        Orders_Queued()
    else:
        print("Error: Invalid Option")


# Global
while(1):
    tmp = sp.call('clear', shell=True)
    
    # Can be skipped if you want to hardcode username and password
    # username = input("Username: ")
    # passwd = input("Password: ")

    try:
        # Set db name accordingly which have been create by you
        # Set host to the server's address if you don't want to use local SQL server 
        con = pymysql.connect(host='localhost',
                              user="root",
                              password="pass",
                              port=30306,
                              db=dbName,
                              cursorclass=pymysql.cursors.DictCursor)
        tmp = sp.call('clear', shell=True)

        if(con.open):
            print("Connected")
        else:
            print("Failed to connect")

        tmp = input("Enter any key to CONTINUE>")

        with con.cursor() as cur:
            cur.execute("SHOW TABLES;")
            tables = cur.fetchall()

            # check if "Category" substring is present in the tables list
            # if present, then add the category name to the CategoryList
            for tbl in tables:
                if "Category" in tbl:
                    CategoryList.append(tbl)

            input()
            while(1):
                tmp = sp.call('clear', shell=True)
                
                # updates
                print("1. Update Your Details/Create Account") 
                print("2. Make an Order") 
                print("3. Return an Order") 
                print("4. Option 4") 

                # queries
                print("5. Add a category <category_names> filter")
                print("6. Remove a category filter")
                print("7. List all categories")
                print("8. List all price ranges")
                print("9. Add a price range filter")
                print("10.Remove a price range filter")
                print("11.")
                print("12.")

                print("13. exit")

                ch = int(input("Enter choice> "))
                tmp = sp.call('clear', shell=True)
                if ch == 13:
                    exit()
                else:
                    dispatch(ch)
                    tmp = input("Enter any key to CONTINUE>")

    except Exception as e:
        tmp = sp.call('clear', shell=True)
        print(e)
        # print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")
        tmp = input("Enter any key to CONTINUE>")
