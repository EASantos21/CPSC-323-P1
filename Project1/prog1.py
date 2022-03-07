'''
    Name: Ethan Santos
    Course: CPSC 323
    Assignment: Project 1
    File: prog1.py
    Purpose: Write a program to read from the user a string of characters, ending with $, 
             for the FA of the language L to determine whether the following words are accepted or rejected by L.
'''
# Making the DFA for L = (a|b)*bb*a over alphabet {a, b}
DFA = { 0:{'a':1, 'b':2},
        1:{'a':1, 'b':2},
        2:{'a':1, 'b':3},
        3:{'a':4, 'b':3},
        4:{'a':1, 'b':2}
}
INIT_STATE = 0
FINAL_STATE = {4}
# Function to check whether the input string will be accepted by language L
def isAccepted(DFA, initState, finalState, input):
    # currentState is set to the initial state
    currentState = initState

    # Keeping track of the currentState as we iterate through our DFA
    for i in input:  
        if i == '$':
            break
        else:
            currentState = DFA[currentState][i]
    
    # Comparing currentState with accepting/final state
    return currentState in finalState

if __name__ == "__main__":
    print("L = (a|b)*bb*a")
    inputStr = input("Please enter a string over alphabet {a, b}: ")
    print(isAccepted(DFA, INIT_STATE, FINAL_STATE, inputStr))
    
