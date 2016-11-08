# Variables

# Getting the USER input
#INPUT Variables
userInput = input("Enter your sentence: ")
vowels="AEIOUaeiou"

# OUTPUT Variables
displayVowels=""
displayConsonants=""

# PROCESS
for letter in userInput:
    if letter in vowels:
        displayVowels = displayVowels + letter
    else:
        displayConsonants = displayConsonants + letter


print("Vowels: " + displayVowels)
print("Consonants: " + displayConsonants)

