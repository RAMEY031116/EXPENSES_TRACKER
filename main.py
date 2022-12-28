#THIS IS A EXPENSES TRACKER PYTHON APPLICATION FOR RASBERRY PI PROJECT !!!!!
from backend import add, save, clear, search, view
from headers import logo
print(logo)



while True:
  clear()
  print(logo)
  print(f"\n Please choose from the following :)" "\n")
  mode_first = input(f"[0] If you would like to search then press 0 \n"
  "[1]If you would like to add your transaction then press 1 \n"
  "[2] If you woule like to view your transaction then press 2 \n"
  "Enter your mode: ").lower()
  if mode_first == "0":

    clear()
    print(logo)
    search()
  elif mode_first == "1":
    name,shop_name,food,car,total_amount = add()
  elif mode_first == "2":
    clear()
    print(logo)
    view()
  else:
    continue
  mode_second= input ("\n""[1] If you would like to save your transaction then press 1 \n"
  "[2] if you would like to view your transaction then press 2 \n"
  "[3] If you would like to quit press 3 \n" 
  "Enter Your mode : ").lower()
  clear()
  if mode_second == "3":
    print(f"HAVE A BEAUTIFUL DAY !!")
    exit()
  elif mode_second == "1":
    save(name,shop_name,food,car,total_amount)
  elif mode_second== "2":
    view()
  else :
    continue


