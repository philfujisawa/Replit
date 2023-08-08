login = input("Username >>> ")
password = input("Password >>> ")
print()
if login == "jonas" and password == "brothers":
  print("\033[35m Hello! Jonas my friend!")
elif login == "iron" and password == "maiden":
  print("\033[31m Do you have fear of the dark? Welcome!")
elif login == "tio" and password == "san":
  print("\033[34m Time is money! Oh Yeah!!!")
else: 
  print("\033[0m Not recognized. Please try again.")