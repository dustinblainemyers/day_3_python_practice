#prompt the user for a number
#compare that number to a predefined value
# If the numbers match, tell the user they're a mind reader
# If they don't match, tell the user " thanks for playing"



user_input = int(input("What number am I thinking of? "))

MAGICNUMBER = 9

if user_input == MAGICNUMBER:
    print("Are you a mind reader? ")
else:
    print("Thanks for playing, that's not my number")