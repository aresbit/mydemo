# Asks the user for a message and then prints the
# number of times each letter appears in the message

def letter_counter():

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    message = input("Enter a message.\n")

    for i in range(26):
        letter = alphabet[i]
        numLetters = count(letter, message)
        if numLetters > 0:
            print(letter + " " + str(numLetters))
        

def count(ch, text):
    counter = 0
    
    for i in range(len(text)):
        if text[i] == ch:
            counter = counter + 1
            
    return counter


letter_counter()
