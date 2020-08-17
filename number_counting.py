#a number counting game, where a number the computer tries to guess the number you are thinking
#a number is presented, say from 1 - 100
#the player can say higher, lower or correct
#if higher or lower then the pc has to correct its search. so if 1 and player says higher, 
#it must search from 2-100, and so on
#once correct, it will print a message like "yay I guessed it"


#display a random number from the list
import random 

number = [0, 1, 2, 3]

print(random.randint(number))

#let the player answer higher or lower
txt = raw_input("higher or lower: ")
print txt 

#have the computer confirm or update the displayed number
