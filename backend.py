from datetime import date
import os
import csv
from headers import logo

def today():
  return date.today()

def clear():
  os.system("clear")
  return logo

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
  print (f"The Total Ammount you have spent on {today()} is {str(total_amount)}\n")
  return name,shop_name,food,car,total_amount
  
 

def save(name,shop_name,food,car,total_amount):
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
    
    


def view():
  with open("expenses.csv", "r")as f:
    reader = csv.reader(f)
    
    for row in reader:
      print(row)