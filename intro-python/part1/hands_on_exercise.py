"""Intro to Python - Part 1 - Hands-On Exercise."""


import math
import random


# TODO: Write a print statement that displays both the type and value of `pi`
pi = math.pi
type(pi)
print(pi)


# TODO: Write a conditional to print out if `i` is less than or greater than 50
i = random.randint(0, 100)
if (i > 50 ):
    print("i is greater than 50")
elif (i == 50 ):
    print("i equal to 50")
else:
    print("i is less than 50")


# TODO: Write a conditional that prints the color of the picked fruit
picked_fruit = random.choice(['orange', 'strawberry', 'banana'])
print(picked_fruit)
#if (picked_fruit == )


# TODO: Write a function that multiplies two numbers and returns the result
# Define the function here.
def Two_Num_Multiplies(num1,num2):
    result = num1 * num2
    return result

#print("input firstnum")
#num1 = input("")

# TODO: Now call the function a few times to calculate the following answers

print("12 x 96 =", Two_Num_Multiplies(12,96))

print("48 x 17 =",Two_Num_Multiplies(48,17))

print("196523 x 87323 =",Two_Num_Multiplies(196523,87323))
