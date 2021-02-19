# Author: Tae Kweon
# This program is used to store and keep track of my online ID's and passwords

import mysql.connector
import os

# connect to the local database
mydb = mysql.connector.connect(
        host="localhost",
        user= os.environ.get("DB_USER"),
        passwd= os.environ.get("DB_PASS"),
        database="account_database"
)

mycursor = mydb.cursor()



def DisplayAccount():

    mycursor.execute("select * from account")

    result = mycursor.fetchall()

    for row in result:
        print(row)

def DisplayOneAccount(cname):

    # sql statement
    sql = "select id, password from account where Company = %s"

    # execute command with the company name
    mycursor.execute(sql, (cname,))

    # fetch result
    result = mycursor.fetchone()

    print(result)

def AddAccount(cname, userId, userPw):

    # sql statement
    sql = "insert into account (id, password, company) VALUES (%s, %s, %s)"

    # put in values
    myAccount = (userId, userPw, cname)

    # execute sql command
    mycursor.execute(sql, myAccount)

    mydb.commit()
    print("Added a",cname,"account")

def DeleteAccount(cname):

    #sql statement
    sql = "delete from account where Company = %s"

    #execute sql command
    mycursor.execute(sql, (cname,))

    mydb.commit()

    print("Removed the",cname,"account")

def main():

    myInput = input("look, add, delete, or all?: ")

    # adding a new account
    if(myInput == "add"):

        print("\nAdding a new account: \n")

        # get user input to add a new account
        companyInput = input("Company Name: ")
        loginInput = input("Login ID: ")
        pwInput = input("Password: ")

        # add the account
        AddAccount(companyInput, loginInput, pwInput)

        # print all current accounts
        print("Your current accounts:\n")
        DisplayAccount()
        print("\n")


    # looking for id and pw
    elif(myInput == "look"):

        # get company name from user
        cname = input("Which account are you looking for?: ")

        # Display that account
        DisplayOneAccount(cname)

    # display all accounts
    elif(myInput == "all"):
        DisplayAccount()

    # remove an account
    elif(myInput == "delete"):

        #get company name input
        cname = input("Which account do you want to remove?: ")

        #delete
        DeleteAccount(cname)

        #display all accounts
        DisplayAccount()

main()


