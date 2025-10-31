# Jonathan Sonnek
# October 30 2025
# Program #2: Random Number File Writer

# Write a program that writes a series of random numbers (up to 1000) to a file.
# Each random number should be in the range of 1 through 500. 
# The application should let the user specify how many random numbers the file will hold 
# (up to 1000).
import random

def edit_file ():
    # Open new file
    rand_numbers_file = open("rand_numbers.txt", "w")
    # Ask user how many numbers they want to enter
    num_values = int(input("How many numbers do you want to enter (less than 1000)? "))
    # Make sure they enter a value within the range
    while num_values != 0:
        if 0 < num_values < 1000:
            break
        else:
            print("Please enter an integer between 1 and 1000 or 0 to quit program.")
            num_values = int(input("How many numbers do you want to enter? "))
 #           if num_values == 0:
 #               break

    # Add Numbers to the file
    for num in range(num_values):
        rand_numbers_file.write(str(random.randint(0,500)) + "\n")

if __name__ == '__main__':
    edit_file()