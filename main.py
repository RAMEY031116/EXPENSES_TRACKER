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



def add_expenses():

  names = []
  shop = []
  groceries = []
  travel = []
  amount = []

  name = input (f"Please enter your name : ")
  shop_name = input(f"Please enter a shop name : ")
  food = float(input (f"Please enter an amount: "))
  car = float(input (f"please enter an ammount for Petrol : "))
  total_amount = food+car
  
  groceries.append(food)
  travel.append(car)
  shop.append(shop_name)
  amount.append(total_amount)
  names.append(name)

  print (f"The Total Ammount you have spent on {date.today()} is {total_amount}  \n")


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
  mode = input ("[1] If you would like to add your transaction to excel then press 1 \n"
  "[2] if you would like to view your transaction then press 2 \n"
  "[3] If you would like to quit press 3 \n" 
  "Enter Your mode : ").lower()

  if mode == "3":
    print(f"HAVE A BEAUTIFUL DAY !!")
    exit()
  elif mode == "1":
    add_expenses()
  elif mode == "2":
    view()
  else :
    continue


