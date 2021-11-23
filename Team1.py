"""
Question.
Check if two strings begins with the same letter and print True 
or you print out some words 
Make your code generic by using the input function
Note: uppercases != lowercases 
M != m
Goodluck!
e.g
Crocodile == Crab
Spider == Snake
Bee != Cat
"""

#Answer
Animal_a = input("Enter the first animal name: ")
Animal_b = input("Enter the second animal name: ")
if Animal_a[0] == Animal_b[0]:
    print("True")
else:
    print("False")