# -*- coding: utf-8 -*-
"""

@author: naikpradnya
"""

import sqlite3
import sys
import os
os.system("")
from time import sleep
class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'
    END      = '\33[0m'
    ORANGE ='\033[43m'
# Connect to the database
def connectDB():
    return sqlite3.connect("moviedata.db")
db=connectDB()
cursor=connectDB().cursor()

## Function to insert Data Into Database
def dataInsert(db):
    movie_name=input("Enter the Movie: ")
    actor=input("Enter the Actor name: ")
    actress=input("Enter the actress name: ")
    director=input("Enter the director name: ")
    year=input("Enter year of release: ")
    cmd=("""INSERT INTO database (movie,actor,actress,director,year) VALUES (?,?,?,?,?);""")
    parms=(movie_name,actor,actress,director,year)
    cursor.execute(cmd,parms)
    db.commit()
    print(  "\nData saved successfully!!" )


## Function to Remove data from Database
def removeData(db):
    cursor.execute("""DELETE FROM database;""").fetchall()
    db.commit()
    print(style.PURPLE + "Data Deleted !" + style.END)


## Function to Find Movies By an Actor
def actor():
    act=str(input("Enter Actor Name : "))
    c=cursor.execute("""SELECT movie FROM database WHERE actor=(?);""",(act,)).fetchall()
    db.commit()
    for i in c:
        print(i,end='')
    if c==[]:
        print(style.PURPLE + "Actor Not Found : (" + style.END)   


## Function to Find Movies By an Actress
def actress():
    act=str(input("Enter the Actress Name : "))
    c=cursor.execute("""SELECT movie FROM database WHERE actress=(?);""",(act,)).fetchall()
    db.commit()
    for i in c:
        print(i,end='')
    if c==[]:
         print(style.RED + " Actress Not Found : (" + style.END)  



## Function to Find Movies By a Director
def director():
    director=str(input("Enter the director name : "))
    c=cursor.execute("""SELECT movie FROM database WHERE director=(?);""",(director,)).fetchall()
    db.commit()
    for i in c:
        print(i,end='')
    if c==[]:
         print(style.RED + "Directors Not Found : (" + style.END)  

## Function to Find Movies By a Year             
def year():
    year=str(input("Enter the release year : "))
    c=cursor.execute("""SELECT movie FROM database WHERE year=(?);""",(year,)).fetchall()
    db.commit()
    for i in c:
        print(i,end='')
    if c==[]:
         print(style.RED + "Movies not Found : (" + style.END)



## List the Database
def displayDB():
    Movie =  []  
    Actor = []
    Actress  = [] 
    Director = []
    Year = []
    data=cursor.execute("""SELECT * FROM database; """).fetchall()
    print("Movie" + " | " + "Actor" +" | " +  "Actress" + " | " + "Director"  + " | " +  "Year" )
    #print(data)
    for row in data:
        Movie.append(row[0])
        Actor.append(row[1])
        Actress.append(row[2])
        Director.append(row[3])
        Year.append(row[4])
    print("Movie = ", Movie)
    print("Actor = ", Actor)
    print("Actress  = ",Actress)
    print("Director  = ", Director)
    print("Year  = ", Year)


#Function to create Table
def createTable(db):
    t=cursor.execute("""SELECT * FROM sqlite_master WHERE type='table' and name="database" ; """).fetchall()
    if t==[]:
        cursor.execute("""CREATE TABLE IF NOT EXISTS database(movie VARCHAR(50),actor VARCHAR(20), actress VARCHAR(20), director VARCHAR(20),year INT);""")
        print(style.BLUE + 'Table Created !' + style.END)
        db.commit()
    else:
        print(style.PURPLE  +'Table Already Exist : (' +   style.END)

## Function to check Database connection
def testCon():
    if connectDB() is not None:
        print("Connected..." )
        createTable(connectDB())
    else:
        print("Sorry,, No DB not connected...." )
def clrscr():
    os.system('cls' if os.name=='nt' else 'clear')


## Main Function
def main():
    while(1):
        clrscr()
        print(style.RED +" MENU"+ style.END)
        print(" 1. Is the DataBase Connected ? createTable: Error   ")
        print(" 2. Insert details                                     ")
        print(" 3. Delete details                                      ")
        print(" 4. Show movie details                                        ")
        print(" 5. Movie by the Actor                                  ")
        print(" 6. Movie by the Actress                                ")
        print(" 7. Movie by the Director                               ")
        print(" 8. Movies of the year                                   ")
        print(" 9. Exit                                             ")
        
        choice=input("\nEnter your choice ")
        
        if choice=='1':
            clrscr()
            testCon()
            sleep(2)
        elif choice=='2':
            clrscr()
            dataInsert(connectDB())
            sleep(2)
        elif choice=='3':
            clrscr()
            removeData(connectDB())
            sleep(2)
        elif choice=='4':
            clrscr()
            displayDB()
            sleep(10)
        elif choice=='5':
            clrscr()
            actor()
            sleep(2)
        elif choice=='6':
            clrscr()
            actress()
            sleep(2)
        elif choice=='7':
            clrscr()
            director()
            sleep(2)
        elif choice=='8':
            clrscr()
            year()
            sleep(2)
        elif choice=='9':
            clrscr()
            print("GoodBye...")
            sleep(2)
            exit()
            break
        else:
            clrscr()
            print(style.GREEN  + "Enter Valid Choice!!" + style.END)
            sleep(2)
main()
