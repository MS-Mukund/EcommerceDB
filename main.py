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

def option2():
    """
    Function to implement option 1
    """
    pass


def option3():
    """
    Function to implement option 2
    """
    pass


def option4():
    """
    Function to implement option 3
    """
    pass


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
                    continue
                elif column.lower() == "Username".lower():
                    print("You cannot change username")
                    continue

                row[column] = input("Enter the value for %s: " % column)

            # Update columns specified by user, not all
            for column in columns:
                cur.execute("UPDATE Users SET %s = '%s' WHERE Username = '%s';" % (column, row[column], UserName))


            print("Data updated successfully")
        
        else:
            row[0] = uname
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

def dispatch(ch):
    """
    Function that maps helper functions to option entered
    """

    if(ch == 1):
        UpdateUserDetails()
    elif(ch == 2):
        option2()
    elif(ch == 3):
        option3()
    elif(ch == 4):
        option4()
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
    else:
        print("Error: Invalid Option")


# Global
while(1):
    tmp = sp.call('clear', shell=True)
    
    # Can be skipped if you want to hardcode username and password
    username = input("Username: ")
    passwd = input("Password: ")

    try:
        # Set db name accordingly which have been create by you
        # Set host to the server's address if you don't want to use local SQL server 
        con = pymysql.connect(host='localhost',
                              port=30306,
                              user=username,
                              password=passwd,
                              db=dbName,
                              cursorclass=pymysql.cursors.DictCursor)
        tmp = sp.call('clear', shell=True)

        if(con.open):
            print("Connected")
        else:
            print("Failed to connect")

        tmp = input("Enter any key to CONTINUE>")

        con.cursor().execute("SHOW TABLES")
        tables = con.cursor().fetchall()

        # check if "Category" substring is present in the tables list
        # if present, then add the category name to the CategoryList
        for tbl in tables['Tables_in_' + dbName]:
            if "Category" in tbl:
                CategoryList.append(tbl)

        with con.cursor() as cur:
            while(1):
                tmp = sp.call('clear', shell=True)
                
                # updates
                print("1. Update Your Details/Create Account") 
                print("2. Option 2") 
                print("3. Option 3") 
                print("4. Option 4") 

                # queries
                print("5. Add a category <category_names> filter")
                print("6. Remove a category filter")
                print("7. List all categories")
                print("8. List all price ranges")
                print("9. Add a price range filter")
                print("10.Remove a price range filter")

                print("11. exit")

                ch = int(input("Enter choice> "))
                tmp = sp.call('clear', shell=True)
                if ch == 11:
                    exit()
                else:
                    dispatch(ch)
                    tmp = input("Enter any key to CONTINUE>")

    except Exception as e:
        tmp = sp.call('clear', shell=True)
        print(e)
        print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")
        tmp = input("Enter any key to CONTINUE>")
