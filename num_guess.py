#!/usr/bin/env python3
# Created by: Logan Sweeney
# Created on: Dec 8, 2021
# This program asks the user to guess a number
# and if they are incorrect it will tell them, and end the game.
import constants


def main():
    # Get number from user
    number_guessed = int(input("Guess my favorite number from 0-9: "))
    print("")

    # Check to see if they got the right number or wrong
    if number_guessed == constants.CORRECT_NUMBER:
        print("Correct!!")
    else:
        print("Incorrect... my favorite number is {}. "
              .format(constants.CORRECT_NUMBER))


if __name__ == "__main__":
    main()
