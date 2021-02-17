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

def DisplayOneAccount(Cname):

    # sql statement
    sql = "select * from account where Company = %s"

    # execute command with the company name
    mycursor.execute(sql, (Cname,))

    # fetch result
    result = mycursor.fetchone()

    print(result)

def AddAccount(company, userId, userPw):

    # sql statement
    sql = "insert into account (id, password, company) VALUES (%s, %s, %s)"

    # put in values
    myAccount = (userId, userPw, company)

    # execute sql command
    mycursor.execute(sql, myAccount)

    mydb.commit()
    print("Added a",company,"account")

def main():

    numInput = input("Enter 1 to add a new account or Enter 2 to check an account: ")
    print(numInput)
    # when 1
    if(numInput != 2):

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

########fix######
    # when 2
    #elif(numInput != 1):

        # get company name from user
     #   cname = input("What is the Company name: ")

        # Display that account
      #  DisplayOneAccount(cname)


main()


