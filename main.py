'''-1 :water
    0 :gun 
    1 : sanke'''

import random

computer = random.choice([-1, 0 , 1])

youstr = input("Enter your choice :")
youDict = {"w": -1, "g" : 0, "s" : 1 }
reverseDict ={1 :"Snake" , 0 :"Gun", -1 : "Water" }


you = youDict[youstr]


print(f"You chose {reverseDict[you]} \n Computer chose {reverseDict[computer]}")

if (computer == you):
    print("It is a draw")

else:
    if(computer == -1 and you == 1):      #-1 - 1 = -2
        print("You win!")

    elif(computer == -1 and you ==0):     #-1 - 0 = -1
        print("You Lose!")


    elif(computer == 1 and you ==-1):     #1 - -1 = 2
        print("You Lose!")

    elif(computer == 1 and you ==0):      #1 - 0 = 1
        print("You Win!")

    elif(computer == 0 and you ==-1):     #0 - -1 = 1
        print("You Win!")

    elif(computer == 0 and you ==1):      #0 - 1 = -1
        print("You Lose!")

    else:
        print("Something went wrong")
    


#or

# if((computer - you) == -1 or (computer - you) == 2):
#     print("You Lose!")

# else:
#     print("You Win!")