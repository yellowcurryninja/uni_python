# Complete the following tutorials using Pseudocode. 

# 1.	Write a program that takes a user's name as input and prints a greeting message.
# ------------------------------------------------------------------------------------------
# START 
# GET USERNAME 
# DISPLAY USERNAME 
# ------------------------------------------------------------------------------------------


userName = input("What is your user name ").title().strip()
print("Welcome! " + userName)

# 2.	The program will takes two numbers as input from the user and prints their sum.
# ------------------------------------------------------------------------------------------
# GET FIRST NUMBER 
# GET SECOND NUMBER
# ADD FIRST NUMBER TO SECOND NUMBER
# DISPLAY THE SUM
# ------------------------------------------------------------------------------------------
inputOne = float(input("Give me the first number "))
inputTwo = float(input("Give me the second number "))

print("The sum of the numbers is: ", inputOne + inputTwo)


# 3.	Write a program that checks whether a given number is positive, negative, or zero.
# ------------------------------------------------------------------------------------------
# GET NUMBER
# CHECK NUMBER IF ITS LESS THAN ZERO
# CHECK NUMBER IF ITS MORE THAN ZERO
# CHECK NUMBER IF ITS EQUALS TO ZERO
# DISPLAY THE NUMBER ACORDING TO OUR RULE
# ------------------------------------------------------------------------------------------
number = float(input("Give me a number "))
if number < 0:
    print("The given number is Negative")
elif number > 0:
    print("The given number is Positive")
elif number == 0:
    print("The given number is zero")
else: 
    print("Invalid input, please insert a number")
    


# 4.	Write a program that checks whether a given number is even or odd.
# ------------------------------------------------------------------------------------------
# GET NUMBER
# CHECK IF NUMBER HAS ANY REMAINDER IF DIVEDED BY TWO
# IF IT HAS THEN ITS ODD
# IF NOT THEN ITS EVEN
# DISPLAY ANSWER
# ------------------------------------------------------------------------------------------
givenNumber = float(input("Give me a number "))
if givenNumber % 2 == 0:
    print("The given number is even")
elif givenNumber % 2 != 0:
    print("The given number is Odd")
else:
    print("Please put a valid number")

# 5.	The program that determines the largest among three numbers entered by the user.

# ------------------------------------------------------------------------------------------
# GET THREE NUMBERS
# CHECK IF NUMBER ONE IS BIGGER THAN NUMBER TWO AND THREE
# CHECK IF NUMBER TWO IS BIGGER THAN NUMBER ONE AND THREE
# CHECK IF NUMBER THREE IS BIGGER THAN NUMBER ONE AND TWO
# DISPLAY THE ANSWER
# ------------------------------------------------------------------------------------------
largestNumber_1 = float(input("I will need three numbers, give me number one: "))
largestNumber_2 = float(input("I will need three numbers, give me number two: "))
largestNumber_3 = float(input("I will need three numbers, give me number three: "))

if largestNumber_1 > largestNumber_2 and largestNumber_1 > largestNumber_3:
    print("Number one is the largest")
elif largestNumber_2 > largestNumber_1 and largestNumber_2 > largestNumber_3:
    print("Number two is the largest")
elif largestNumber_3 > largestNumber_1 and largestNumber_3 > largestNumber_2:
    print("Number three is the largest")
else:
    print("Please put a valid number")
