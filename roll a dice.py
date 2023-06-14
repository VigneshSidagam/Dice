#ROLL A DICE
import random
print("1)Roll a dice")
print("2)Exit")
while True:
    user = input("Enter your choice:")
    if len(user)==0:
        print("YOU HAVE ENTERED NOTHING, PLEASE ENTER SOMETHING...!")
    else:
        if user=="1":
            print(random.randint(1,6))
        elif user=="2":
            print("Thankyou, Visit again")
            break
        else:
            print("Incorrect input, Try again")

