from datetime import date
import os
import csv
from headers import logo

def today():
  return date.today()

def clear():
  os.system("clear")
  

def search():
  date = input(f"Enter your transaction date  YYYY-MM-DD : ")
  
  try:
    
    with open("expenses.csv","r+") as f:
        for row in f:
            if date == row[1]:
                print(row)
  except FileNotFoundError:
    print(f"This file doesnot exists so please add your transaction and save to create a new file :)")

def add():
  try:
    
    name = input (f"Please enter your name : ")
    shop_name = input(f"Please enter a shop name : ")
    food = float(input (f"Please enter an amount: £"))
    car = float(input (f"please enter an ammount for Petrol : £"))
    total_amount = food+car
    clear()
    print(logo)
    print (f"Name:{name}\nShop:{shop_name}\nCategory:£{food}\nPetrol:£{car}\n")
    print(f"The Total Ammount you have spent on {today()} is £{str(round(total_amount, 2))}\n")
    return name,shop_name,food,car,total_amount
  except ValueError and TypeError:
    print(f"YOU HAVE NOT ENTERED ANYTHING SO PLEASE ADD YOUR TRANSACTION !!")

  
 

def save(name,shop_name,food,car,total_amount):
    try:
      
        expenses_all = {
        "names":name,
        "shop":shop_name,
        "groceries":food,
        "travel":car,
        "amount":total_amount,
        "date":today(),
        }
        
    
        with open("expenses.csv", "a")as f:
            writer = csv.writer(f)
            writer.writerow([today(),expenses_all["names"],expenses_all["shop"],expenses_all["groceries"],expenses_all["travel"],expenses_all["amount"]])
    except NameError:
        print(f"hello world")


def view():
    try:
        with open("expenses.csv", "r")as f:
            reader = csv.reader(f)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print(f"This file doesnot exists so please add your transaction and save to create a new file :")


def delete():
  if os.path.exists("expenses.csv"):
    os.remove("expenses.csv")
    print(f"YOUR FILE HAS BEEN SUCESSFULLY DELETED")
  else:
    print("The file does not exist") 

