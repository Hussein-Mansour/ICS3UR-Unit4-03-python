#!/usr/bin/env python3

# Created by: Hussein Mansour
# Created on: Sat/May15/2021
# This program uses a for loop


def main():
    # this function accepts a positive integer
    # calculates the square of each integer from 0 to the user input

    # input
    positive_number = input("Enter a positive integer:")

    # process  & output
    try:
        positive_number_int = int(positive_number)

        if (positive_number_int < 0):
            print("you did not enter a positive number")
        elif (positive_number_int == 0):
            print("0² = 0")
        else:
            for loop_counter in range(positive_number_int + 1):
                power = loop_counter * loop_counter
                print("{0}² = {1}".format(loop_counter, power))

    except Exception:
        print("You did not enter a integer")
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
