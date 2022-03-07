'''
    Name: Ethan Santos
    Course: CPSC 323
    Assignment: Project 1
    File: prog2.py
    Purpose: Given a text file “data.txt”, write a program to copy the file into file “newdata.txt” 
             by removing all comment lines (lines that begin with //) and extra spaces.
'''
# Defining symbols, keywords, and white space
DATATYPES = ['int']
OPERATORS = [',', ';', '=', '+','/']
INTEGERS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
COMMENTS = '//'
tokens = []
def analyze(sourceCode):
    for i in sourceCode:
        # Will check if i is a datatype
        if i in DATATYPES:
            tokens.append(['DATATYPE', i])
        elif i in OPERATORS:
            tokens.append(['OPERATOR', i])
        elif i in INTEGERS:
            tokens.append(['INTEGER', i])
        elif COMMENTS in i:
            tokens.append(['COMMENT', i])
        else:
            tokens.append(['IDENTIFIER', i])
    print(tokens)

if __name__ == "__main__":
    # Reading in input txt, assigning contents to a string, and splitting the string
    with open('data.txt', 'r') as file:
        sourceCode = file.read().rstrip()

    sourceCode = sourceCode.split()

    analyze(sourceCode)