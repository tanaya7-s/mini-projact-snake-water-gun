import random

computer = random.choice([-1, 0 , 1])

youstr = input("Enter your choice :")
youDict = {"w": -1, "g" : 0, "s" : 1 }
reverseDict ={1 :"Snake" , 0 :"Gun", 1 : "Water" }


you = youDict[youstr]


print(f"You chose {reverseDict[you]} \n Computer chose {reverseDict[computer]}")

if (computer == you):
    print("It is a draw")

if((computer - you) == -1 or (computer - you) == 2):
    print("You Lose!")

else:
    print("You Win!")


    # Minus logic is applied