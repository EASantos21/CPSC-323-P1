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