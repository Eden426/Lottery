#I'm trying to build a lottery that makes user guess 3X
"""import random

for i in range(3):
    try:
        print("please enter number with 6 digit")
        inputs = int(input())
        weight = [10, 3, 20, 50, 5, 25]
        target = random.choice(inputs,weights=weight,k=6)
        if inputs:
            print("Well you have have won the lottery")
        else:
            print("Please try again")

    except ValueError as e:
        print(f"ERROR CODE: {e}")
    except TypeError as e:
        print(f"ERROR CODE: {e}")
    except IndexError as e:
        print(f"ERROR CODE: {e}")


import random

TimetoTry= 3
print("Please enter number with 6 digit")
weights = [10,30,4,6,7,8]
population= range(1,7)
k=6

for _ in range(TimetoTry):
    try:

        inputs = int(input())
        ranD = random.choice(population ,weights =weights ,k=k)
        if inputs==ranD:
            print("You have won the lottery ❤️")
        else:
            print("please try again")
    except ValueError as e:
        print(f"ERROR CODE: {e}")
    except TypeError as e:
        print(f"ERROR CODE: {e}")
"""
import random
TimeofTry = 3
Population = [134675,567402,650825,839264,647282,231678]
weights =[10,56,4,30,13,6]
randomN = random.choices(Population, weights=weights, k=1)[0]

try:
    for _ in range(TimeofTry):
        print("Enter 6-digit number!!!")
        inputs = int(input())
        if len(str(inputs)) !=6:
            print("Invalid length of number")
            continue


        if inputs==randomN:
            print("Congratulation🎉🎉🎉 YOU ARE THE WINNER")
            break
        else:
            print("Try next time.")
    print(f"The winner number was {randomN} ")

except ValueError as e:
    print(f"Error Code: {e}")












