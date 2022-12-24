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

def add():
  with open("expenses.csv", "w")as f:
    writer = csv.writer(f)


def view():
  with open("expenses.csv", "r")as f:
    csv_reader = csv.reader(f)



header()

Name = []
Shop = []
Groceries = []
Travel = []
Amount = []


name = input (f"Please enter your name : ")
shop_name = input(f"Please enter a shop name : ")
food = float(input (f"please enter an ammount: "))
car = float(input(f"please enter an ammount for Petrol : "))

money = food + car

Groceries.append(food)
Travel.append(car)
Shop.append(shop_name)
Amount.append(money)


<<<<<<< HEAD
print (f"The Total Ammount you have spent on {date.today()} is {Amount}  /n")

print(f"Please choose from the following :)")
=======
#test
>>>>>>> a14538c59f486fcca32068ed0b317806c1afc12b

while True:
  mode = input(f"If you would like to add then type (add) \n"
  "if you would like to view your transaction then type (view) \n"
  "If you would like to quit then type (quit) \n" 
  "Enter Your mode : ").lower()

  if mode == "q":
    print(f"HAVE A BEAUTIFUL DAY !!")
    exit()
  elif mode == "add":
    add()
  elif mode == "view":
    view()
  else :
    continue


