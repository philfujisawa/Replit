print("Best Movies of your life!")
print("We need to know what is your favorite movie from that below:")
print("Mad Max, Godfather")
movie = input("""Type here: 
""")
if movie == "Mad Max":
  print("Good one!")
  favchar = input("""What is your favorite main character actor from both versions? Mel Gibson or Tom Hardy?
  """)
  if favchar == "Mel Gibson":
    print("Old School Rules")
  elif favchar == "Tom Hardy":
    print("New man, new moves!")
  else:
    print("I don't think that was my question.")
elif movie == "Godfather":
  print("Old but gold!!!")
else:
  print("I don't ask about other movies!!!")