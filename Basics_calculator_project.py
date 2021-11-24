# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 17:14:31 2021
@author: Ayer,Flora,Shiv,Wallace

GOAL:
    BUILD A BASIC CALCULATOR THAT DOES THE 4 MATHS OPERATIONS (+ - * /).
    USER INPUTS THE LIST OF NUMBERS AND SELECTS AN OPERATION.
    THE PROGRAM BELOW SHOULD WORK ON THESE LIST OF NUMBERS IN SEQUENCE APPLYING
    THE OPERATION SELECTED.
TOPICS LEARNT:
    VARIABLES - INT, FLOAT, STRING, BOOLEAN, LIST
    INPUT FROM USER AND OUPUT TO SCREEN
    BOOLEAN TRUTH TABLES - AND, OR, NOT, NOT AND, NOT OR
    IF ELSE STATEMENTS
    LOOPS - WHILE LOOP AND FOR LOOP
    FUNCTIONS
"""
# IMPORTING PACKAGES THAT ALLOW FOR SOME COOL FUNCTIONS
import sys

# GET THE INPUTS FROM THE USER -- LIST OF NUMBERS TO WORK ON AND THE OPERATION
# LIST OF NUMBERS ARE SPACE SEPERATED AND NOT SPACE AT THE END
input_numbers = input("Enter numbers: ")
input_function = input("Add/Subtract/Multiply/Divide? ")

# SPLIT THE STRING INPUT FROM USER INTO A LIST OF STRINGS
number_list = input_numbers.split(" ")

# #########################################################################
# MODIFY BELOW LINE 40 TO ALLOW USER TO INPUT INTERGERS OR DECIMAL VALUES #
# ALLOW USER TO TYPE '1 2 5 10' OR '1.0 2.0 5.0 10.0', OR '1 2.0 5 10.0'  #
# IN ALL THE ABOVE CASE, THE number_list SHOULD HAVE [1.0,2.0,5.0,10.0]   #
#                                                                         #
# THE BELOW 'try... except' IS TO CATCH ANY ERROR AND CONTROL WHAT THE    #  
# USER SEES. INSTEAD OF AN UGLY ERROR, THROW A MORE USER FRIENDLY ERROR   #
# AND QUIT.                                                               #
# #########################################################################
try:
    number_list = list(map(int, number_list))
except:
    print("Sorry! One of the input is not a number! Bye!")
    sys.exit()

# CHECKS IF THE OPERATION SELECTED IS EITHER ADD, SUBTRACT, MULTIPLY, OR DIVIDE
if not(input_function == "Add" or 
       input_function == "Subtract" or 
       input_function == "Multiply" or 
       input_function == "Divide"):
    print("Option does not exist!")
    sys.exit()

# PRINT ALL THE INPUTS AS VERIFICATION THAT THE INPUTS ARE ACCEPTABLE
print("Numbers entered: " + input_numbers)
print("Function Selected: " + input_function)

# FUNCITON TO ADD THE LIST OF NUMBERS AND RETURN THE VALUE
def add_numbers_in_list(l):
    total = 0
    for i in l:
        total = total + i
    return total

# FUNCITON TO SUBTRACT NUMBERS FROM THE FIRST NUMBER
def Subtract_number_in_list(l):
    # SET THE FIRST NUMBER TO BE THE TOTAL
    Ans = l[0] 
    # LOOP THROUGH THE REST OF THE LIST AND SUBTRACTS FROM THE TOTAL
    for i in l[1:]: # STARTING FROM THE SECOND ITEM IN LIST
        Ans=Ans-i
    return Ans

# FUNCTION TO MULTIPLE NUMBERS
def multiply_number_in_list(l):
    # SETTING THE FIRST NUMBER TO BE THE STARTING NUMBER
    Ans = l[0]
    # LOOP THROUGH THE REST OF THE LIST AND KEEP MULTIPLYING
    for i in l[1:]:
        Ans=Ans*i
    return Ans

# FUNCTION TO DIVIDE NUMBERS FROM THE FIRST NUMBER
# CATERS FOR THE CASE TO AVOID DIVIDING BY 0
def divide_number_in_list(l):
    a = l[0]
    for i in l[1:]:
        if (i==0):
            print("cannot divide by zero!!!")
            sys.exit()
        a = a / i
    return a

# CHOOSE THE REQUIRED FUNCTION BASED ON THE OPERATION SELECTED BY USER
if input_function == "Add":
    print(add_numbers_in_list(number_list))
elif input_function == "Subtract":
    print(Subtract_number_in_list(number_list))
elif input_function == "Multiply":
    print(multiply_number_in_list(number_list))
else:
    print(divide_number_in_list(number_list))

# ###########################################################################
# CHALLENGE:                                                                #
# MODIFY THE CODE TO ALLOW USERS TO CHOOSE IF THEY WANT TO TRY AGAIN        #
# IF ANSWER IS 'y', RESET AND ALLOW THE USER TO TRY AGAIN                   #
# IF ANSWER IS 'n', QUIT THE PROGRAM                                        #
# HINT:                                                                     #
# THIS IS REQUIRE YOU TO MOVE CERTAIN CODE AROUND WITHOUT CHANGING THEM     #
# AND ADDING SOME EXTRA INPUTS AND LOOPS                                    #
# ###########################################################################
