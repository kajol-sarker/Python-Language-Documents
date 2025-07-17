#Python Text Based Adventure Game 

userinput = input("Do you wanna play this game?: ")
# print(userinput)

if userinput == "Yes":
   print("Welcome to the game!")
   userinput = input("Do you wanna go to Jungle or Cave or Anywhere else?: ")
   if userinput == "Jungle":
      print("You see a Hungry Tiger. The Tiger will eat you and the game will be closed.")
   elif userinput == "Cave":
      print("You see a bear in front of cave.")
      userinput = input("Do you wanna run or fight with the bear?: ")
      if userinput == "run":
         print("I successfully run from the bear into the cave.")
      elif userinput == "fight":
         print("The bear is too Strong. You never win")
else:
   print("The game is closed.You exist the game now")

