from os import uname
import subprocess as sp
import pymysql
import pymysql.cursors


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
    This is a sample function implemented for the refrence.
    This example is related to the Employee Database.
    In addition to taking input, you are required to handle domain errors as well
    For example: the SSN should be only 9 characters long
    Sex should be only M or F
    If you choose to take Super_SSN, you need to make sure the foreign key constraint is satisfied
    HINT: Instead of handling all these errors yourself, you can make use of except clause to print the error returned to you by MySQL
    """
    try:
        # Take username as input
        # if username already exists, update the columns specified by user
        # else, ask for all the columns and insert the data into the database

        row = {}
        # columns = []
        uname = input("Username: ")

        # Check if the username already exists
        cur.execute("SELECT EXISTS(SELECT * FROM Users WHERE Username = %s);" % (uname))

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
            columns = input("Enter the columns: ").split(",")
            for column in columns:
                if(column == "Premium_subscription: "):
                    row[column] = bool(input("Premium_subscription: "))
                    continue
                
                row[column] = input("Enter the value for %s: " % column)

            # Update the data
            cur.execute("UPDATE Users SET %s WHERE Username = %s" % (row, uname))
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
            cur.execute("INSERT INTO Users VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);" %
            (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10]))

        con.commit()

        print("Updated your details")

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
        option2()
    elif(ch == 3):
        option3()
    elif(ch == 4):
        option4()
    else:
        print("Error: Invalid Option")


# Global
while(1):
    tmp = sp.call('clear', shell=True)
    
    # Can be skipped if you want to hardcode username and password
    username = input("Username: ")
    password = input("Password: ")

    try:
        # Set db name accordingly which have been create by you
        # Set host to the server's address if you don't want to use local SQL server 
        con = pymysql.connect(host='localhost',
                              port=30306,
                              user="root",
                              password="password",
                              db='COMPANY',
                              cursorclass=pymysql.cursors.DictCursor)
        tmp = sp.call('clear', shell=True)

        if(con.open):
            print("Connected")
        else:
            print("Failed to connect")

        tmp = input("Enter any key to CONTINUE>")

        with con.cursor() as cur:
            while(1):
                tmp = sp.call('clear', shell=True)
                # Here taking example of Employee Mini-world
                print("1. Update Your Details") 
                print("2. Option 2")  # Fire an Employee
                print("3. Option 3")  # Promote Employee
                print("4. Option 4")  # Employee Statistics
                print("5. Logout")
                ch = int(input("Enter choice> "))
                tmp = sp.call('clear', shell=True)
                if ch == 5:
                    exit()
                else:
                    dispatch(ch)
                    tmp = input("Enter any key to CONTINUE>")

    except Exception as e:
        tmp = sp.call('clear', shell=True)
        print(e)
        print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")
        tmp = input("Enter any key to CONTINUE>")
