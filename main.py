#THIS IS A BUDGET PLANNER FOR RASBERRY PI PROJECT !!!!!
import pandas as pd
import csv
import os
from datetime import date
from header import logo
import function

def today():
  print(date.today())


def header():
  print (logo)


def clear():
  os.system("clear")
  print(header())

def add():
  pass

def view():
  pass

header()

Name = []
Shop = []
Groceries = []
Travel = []
Amount = []


name = input ("Please enter your name : ")
shop_name = input(f"Please enter a shop name : ")
food = input ("please enter an ammount: ")
car = input("please enter an ammount for Petrol : ")

money = int(food) + int(car)
Groceries.append(food)
Travel.append(car)
Shop.append(shop_name)
Amount.append(money)

clear()

print(f"The Total Ammount you have spent on {date.today()} is {Amount} ")







