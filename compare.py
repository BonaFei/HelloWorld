#!/usr/bin/env python

lucky_number = 7

while True:
    try:
        input_number = int(input("Please enter a number to guess: "))
    except Exception:
        print("Please input a number")
        continue
    if input_number == lucky_number:
        print("Bingo")
        break
    elif input_number < lucky_number:
        print("Too small, please try again!")
        continue
    elif  input_number > lucky_number:
        print ("Too big, please try again!")
        continue
