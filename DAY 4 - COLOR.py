print("Welcome to your adventure simulator. I am going to ask you a bunch of questions and then create an epic story with you as the star!")
print()
name = input("""\033[34m What is your name?
""")
enemy = input("""\033[31m What is your worst enemy's name?
""")
power = input("""\033[32m What is your superpower?
""")
house = input("""\033[33m Where do you live?
""")
food = input("""\033[35m What is your favorite food?
""")
print()
print("\033[0m Hello", name,"!", "Your ability to", power, "will make sure you never have to look at", enemy, "again. Go eat", food, "as you walk down the streets of", house, "and use", power, "for good and not evil!")