#########
#
# Ceasar cypher
# A change
#######

# encoding function

def encode(string):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    output = ''
    for letter in sentence:
        #print(letter)
        index = alphabet.find(letter)
        new_index = index + 3
        output += alphabet[new_index]
        # list of the alphabet

        # for each letter, find the index

        # new index = letter index - key

        # Find the letter for the new key

    print (output)
# decoding funciton

def decode(string):
    print ("decode function")


repeat = True
#main program
while repeat == True:
    # input the sentence
    sentence = input("What is the phrase? ")
    # input The key or the offset
    key = input("What is the key? ")

    # Choice
    option = input("Please choose e to encode or d to decode ")
    if option == "e":
        encode(sentence)
    elif option == 'd':
        decode(sentence)
    else:
        print ("not a valid option")

    again = input("do you want to try again y/n?")
    if again == "y":
        repeat = True
    else:
        print ("bye")
        repeat = False





