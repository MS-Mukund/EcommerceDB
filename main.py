from os import uname
import subprocess as sp
import pymysql
import pymysql.cursors

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
        query = "SELECT EXISTS(SELECT * FROM Users WHERE Username = '%s');" % (UserName)
        cur.execute(query)

        check = next( iter((cur.fetchone()).values()) )
        print(check)

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
                row[column] = input("Enter the value for %s: " % column)
                
                if(column.lower() == "Premium_subscription".lower()):
                    if( row[column] == 1):
                        row[column] = 0x01
                    else:
                        row[column] = 0x00    
                    continue
                elif column.lower() == "Username".lower():
                    print("You cannot change username")
                    return
                elif column.lower() == "phone_number" or column.lower() == "pincode":
                    if row[column].isdigit() == False:
                        print("Invalid phone number or pincode")
                        return                    

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
            if row[1].isdigit() == False:
                print("Invalid phone number")
                return
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

            if row[10].isdigit() == False:
                print("Invalid pincode")
                return

            # Insert the data
            cur.execute("INSERT INTO Users VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', %d, '%s', '%s', '%s');" %
            (UserName, row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10]))

        con.commit()

        print("Updated your details")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return

def Search_Products_by_Name():
    """
    Useful to search for products by name. The Output will be all such items, sorted in descending Order of relevance to the searched Keyword
    """

    try:
        #Take Keyword as input.
        keyword  = input("Enter the Keyword to search for: ")
        cur.execute("SELECT * FROM Products WHERE Name LIKE '%%%s%%' LIMIT 10 ;" %(keyword))
        check = cur.fetchall() #warranty company price and name
        j=1
        for i in check:
            if i['Price'] > PriceFilter[0] and i['Price'] < PriceFilter[1]:
                print(j,". Product Name: " ,i['Name'], "\t Product Warranty: ",i['Warranty'],"\t Brand: ",i['Company'],"\t Price: ",i['Price'])
            j=j+1
    except Exception as e:
        con.rollback()
        print("Failed to Retrieve Products-List from database")
        print(">>>>>>>>>>>>>", e)
        return


def FilterCategory():
    """
    Function to filter the category
    """
    global CategoryFilter, CategoryList
    filter = input("Enter the category: ")

    # Check if the category exists    
    if filter in CategoryList and filter not in CategoryFilter:
        CategoryFilter.append(filter)
        print("Added filter")
    elif filter in CategoryFilter:
        print("Filter already present")
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
        print("Removed all filters")
    elif inp in CategoryFilter:
        CategoryFilter.remove(inp)
        print("Removed")
    else:
        print("Invalid option %s", inp)


def ListPrice():
    """
    Function to list the price range
    """
    print("Price Range: ", end="")
    for bound in enumerate (PriceUpperBounds):
        if( bound[0] == 0):
            print("     < %d" % bound[1])
        elif( bound[0] == len(PriceUpperBounds) - 1):
            print("     > %d" % bound[1])
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
    if PriceFilter != (MIN, MAX):
        PriceFilter = (MIN, MAX)
        print("removed")
    
def Insert_Order_Details():
    try:
        var=0

        orderid = 1
        cur.execute("SELECT MAX(Order_ID) FROM Orders;")
        
        orderid = next( iter((cur.fetchone()).values()) ) + 1

        while(var==0):
            row = {}
            cur.execute("SELECT EXISTS(SELECT * FROM Orders WHERE Order_ID = '%s');" % (orderid))
            check = next( iter((cur.fetchone()).values()) )
            #check = cur.fetchone()[0]
            if( check > 0 ):
                print("There is already an order with the order_ID '%s',Please give unique one\n" % (orderid))
                break
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
                    row[4] = input("Enter the date in format 'yyyy-mm-dd': ")
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

    
def Orders_Yet_ToBe_Returned():
    try:
        var=0
        while(var==0):
            Username = input("Enter Username: ")
            cur.execute("SELECT EXISTS(SELECT * FROM Users WHERE Username = '%s');" % (Username))
           
            check_username = next( iter((cur.fetchone()).values()) )
           
            if( check_username <= 0 ):
                print("There is no user with the Username %s" % (Username))
            else:
                cur.execute("SELECT O_Username,Order_ID,O_Product_ID,O_Agency_ID,O_SupplierID,Amount_Paid,Placed_Date FROM Orders WHERE O_Username= '%s' AND Is_it_delivered=0" % (Username))
                #P = cur.fetchmany("SELECT O_Username,Order_ID,O_Product_ID,O_Agency_ID,O_SupplierID,Amount_Paid,Placed_Date FROM Orders WHERE O_Username= '%s' AND Is_it_delivered=0" % (Username))
                P = cur.fetchall()
                
                for i in P:
                    print("Username: ",i['O_Username'],"Order_ID: ",i['Order_ID'],"Product_ID: ",i['O_Product_ID'] ,"Agency_ID: ", i['O_Agency_ID'], "SupplierID: ", i['O_SupplierID'],"Amount_Paid: ", i['Amount_Paid'],"Placed_Date: ",i['Placed_Date'])
                break
    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return


def Orders_Queued():
    try:
        var=0
        while(var==0):
            Username = input("Enter Username: ")
            cur.execute("SELECT EXISTS(SELECT * FROM Users WHERE Username = '%s');" % (Username))
           
            check_username = next( iter((cur.fetchone()).values()) )
           
            if( check_username <= 0 ):
                print("There is no user with the Username %s" % (Username))
            else:
                cur.execute("SELECT O_Username,Order_ID,O_Product_ID,O_Agency_ID,O_SupplierID,Amount_Paid,Placed_Date FROM Orders WHERE O_Username= '%s' ORDER BY Placed_Date" % (Username))
                #P = cur.fetchmany("SELECT O_Username,Order_ID,O_Product_ID,O_Agency_ID,O_SupplierID,Amount_Paid,Placed_Date FROM Orders WHERE O_Username= '%s' AND Is_it_delivered=0" % (Username))
                P = cur.fetchall()
                
                for i in P:
                    print("Username: ",i['O_Username'],"Order_ID: ",i['Order_ID'],"Product_ID: ",i['O_Product_ID'] ,"Agency_ID: ", i['O_Agency_ID'], "SupplierID: ", i['O_SupplierID'],"Amount_Paid: ", i['Amount_Paid'],"Placed_Date: ",i['Placed_Date'])
                break
    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return

def categorical_func():
    cur.execute("SHOW TABLES;")
    tables = cur.fetchall()

    for tbl in tables:
        if "Category" in next( iter(tbl.values()) ):
            CategoryList.append(next( iter(tbl.values()) ))

def dispatch(ch):
    """
    Function that maps helper functions to option entered
    """

    if(ch == 1):
        UpdateUserDetails()
    elif(ch == 2):
        Insert_Order_Details()
    elif(ch == 3):
        pass
    elif(ch == 4):
        Search_Products_by_Name()
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
    # tmp = sp.call('clear', shell=True)
    
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
        # tmp = sp.call('clear', shell=True)

        if(con.open):
            print("Connected")
        else:
            print("Failed to connect")

        tmp = input("Enter any key to CONTINUE>")

        with con.cursor() as cur:

            if len(CategoryList) == 0:
                categorical_func()

            while(1):
                # tmp = sp.call('clear', shell=True)
                
                # updates
                print("1. Update Your Details/Create Account") 
                print("2. Make an Order") 
                print("3. Return an Order") 
                print("4. Search Product List By Name and Relevance") 

                # queries
                print("5. Add a category <category_names> filter")
                print("6. Remove a category filter")
                print("7. List all categories")
                print("8. List all price ranges")
                print("9. Add a price range filter")
                print("10.Remove a price range filter")
                print("11.Orders which are yet to be delivered")
                print("12.Orders made by user for all time")

                print("13. exit")

                ch = int(input("Enter choice> "))
                # tmp = sp.call('clear', shell=True)
                if ch == 13:
                    exit()
                else:
                    dispatch(ch)
                    tmp = input("Enter any key to CONTINUE>")

    except Exception as e:
        # tmp = sp.call('clear', shell=True)
        print(e)
        # print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")
        tmp = input("Enter any key to CONTINUE>")