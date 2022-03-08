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

def writeToFile():
    # Opening newdata file to write to
    newFile = open('newdata.txt', 'r+')

    # Defining lists to keep track of the strings we plan to change
    newLines = []
    newFileLines = []

    with open('data.txt', 'r+') as file:
        # Deleting comments and unnecessary space
        for line in file:
            if not line.isspace():
                if COMMENTS not in line:
                    newLines.append(line)
                else:
                    currentLine = line.split(COMMENTS)[0]
                    newLines.append(currentLine + "\n")
        
        # Deleting space inbetween words/characters
        for i in newLines:
            if not i.isspace():
                newFileLines.append(''.join(i.split()))
        
        # Writing to newdata.txt
        for i in newFileLines:
            newFile.write(i + "\n")

if __name__ == "__main__":
    writeToFile()