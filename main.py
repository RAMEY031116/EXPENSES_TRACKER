#THIS IS A BUDGET PLANNER FOR RASBERRY PI PROJECT !!!!!
import pandas as pd
import csv
import os
from datetime import date
from header import logo


def today():
  return date.today()


def header():
  print (logo)


def clear():
  os.system("clear")
  return header()

def search():
  date = input(f"Enter your transaction date  YYYY-MM-DD : ")
  
  search_file = csv.reader(open("expenses.csv","r"))

  for row in search_file:
    if date == row[0]:
      print(row)

def add():
  name = input (f"Please enter your name : ")
  shop_name = input(f"Please enter a shop name : ")
  food = float(input (f"Please enter an amount: "))
  car = float(input (f"please enter an ammount for Petrol : "))
  total_amount = food+car
  return name,shop_name,food,car,total_amount
  
 

def save(name,shop_name,food,car,total_amount):

  print (f"The Total Ammount you have spent on {today()} is {str(total_amount)}\n")

  names = []
  shop = []
  groceries = []
  travel = []
  amount = []

  groceries.append(food)
  travel.append(car)
  shop.append(shop_name)
  amount.append(total_amount)
  names.append(name)

  print (f"The Total Ammount you have spent on {today()} is {str(total_amount)}\n")


  with open("expenses.csv", "a")as f:
    writer = csv.writer(f)
    
    writer.writerow([today(),names,shop,groceries,travel,amount])
    
    


def view():
  with open("expenses.csv", "r")as f:
    reader = csv.reader(f)
    
    for row in reader:
      print(row)
    


header()

print(f"Please choose from the following :)" "\n")

while True:
  mode_first = input(f"[0] If you would like to search then press 0 \n"
  "[1]If you would like to add your transaction then press 1 \n"
  "[2] If you woule like to view your transaction then press 2 \n"
  "Enter your mode: ").lower()
  if mode_first == "0":
    search()
  elif mode_first == "1":
    name,shop_name,food,car,total_amount = add()
  elif mode_first == "2":
    view()
  else:
    continue

  mode_second= input ("\n""[1] If you would like to save your transaction then press 1 \n"
  "[2] if you would like to view your transaction then press 2 \n"
  "[3] If you would like to quit press 3 \n" 
  "Enter Your mode : ").lower()

  if mode_second == "3":
    print(f"HAVE A BEAUTIFUL DAY !!")
    exit()
  elif mode_second == "1":
    save(name,shop_name,food,car,total_amount)
  elif mode_second== "2":
    view()
  else :
    continue


