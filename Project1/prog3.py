'''
    Name: Ethan Santos
    Course: CPSC 323
    Assignment: Project 1
    File: prog2.py
    Purpose: Write a program to read from the user a single line (up to 255 characters) statement at a time 
             and determine whether each token is a number, identifier, a reserved word, or special character.
             A number is an unsigned integer or a signed integer. An identifier starts with a letter or _ followed by 
             any number of letters, _, and digits.
'''
# Using the given arrays defining reserved words and special symbols
RESERVED_WORDS = ["cout<<", "for", "int", "while"]
SPECIAL = ["<", "=" , "*" , "-" , ";" , "(" , ")" , "<=" ,"+", ","]
DIGITS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
if __name__ == "__main__":
    loopInput = 0
    
    while loopInput != 1:
        source = input("Enter statement: ")
        source = source.split()
        for i in source:
            if i in RESERVED_WORDS:
                print("RESERVED WORD: ", i)
            elif i in SPECIAL:
                print("SPECIAL: ", i)
            elif i.isdigit() or i.startswith('-') and i[1:].isdigit():
                print("INTEGER: ", i)
            else:
                print("IDENTIFIER: ", i)
        
        if(input("Continue? Y/N") == 'N'):
            loopInput = 1