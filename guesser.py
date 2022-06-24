#!/usr/bin/env python3

import random
randnum = random.randint(1,101)
def computer_guess(num1,num2):
    #I initilized randnum_computer so, computer can get in loop
    randnum_computer = 0
    count = 0
    while randnum_computer != randnum:
        count+=1
        randnum_computer = random.randint(num1,num2)
        if randnum > randnum_computer:
            num1 = randnum_computer
            randnum_computer = random.randint(num1,num2)
        elif randnum < randnum_computer:
            num2 = randnum_computer
            randnum_computer = random.randint(num1,num2)
        else:
            return str(count)+" times loop worked and number was: " + str(randnum)

print(computer_guess(1,101))
