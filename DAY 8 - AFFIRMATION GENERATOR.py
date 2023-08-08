print("Hello. Welcome to your daily quotes generator.")
name = input("""What is your name?
""")
print()
if name == "Jonas" or name == "jonas":
  print("You are from the Brothers?")
  dow = input("""Please input day of the week:
  """)
  if dow == "Monday" or dow == "monday":
    print("Let's start the week!")
  if dow == "Tuesday" or dow == "tuesday":
    print("Oh God! How much days for friday?!?")
  if dow == "Wednesday" or dow == "wednesday":
    print("Did you watch Adams family?")
  if dow == "Thursday" or dow == "thursday":
    print("It's almost ending!!!")
  if dow == "Friday" or dow == "friday":
    print("TGIF")
  else:
    print("You don't know what are week days?!?")
elif name == "Phil" or name == "phil":
  dow = input("""Please input day of the week:
  """)
  if dow == "Monday" or dow == "monday":
    print("Time to begin your studies and gym!")
  if dow == "Tuesday" or dow == "tuesday":
    print("Home office day")
  if dow == "Wednesday" or dow == "wednesday":
    print("Middle of the week...")
  if dow == "Thursday" or dow == "thursday":
    print("It's almost ending!!!")
  if dow == "Friday" or dow == "friday":
    print("TGIF! Home Office day")
else:
 print("I do not know your name, but I hope you are having a great day!")