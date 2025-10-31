# Jonathan Sonnek
# October 30 2025
# Program #3: Total Numbers

# Assume a file containing a series of integers is named numbers.txt and exists on the computer's disk.
# (please use the provided numbers.txt)
# Write a program that reads all of the numbers stored in the file and calculates their total.  

# The program should handle the following exceptions: 

# It should handle any IOError exceptions that are raised.
# It should handle any ValueError exceptions that are raised when the items that are read from the file 
# are converted to a number.

def sum_numbers_from_file():
    ######################
    # Open the numbers.txt file
    infile = open('numbers.txt', 'r')
    sum = 0
    try:
        # read the values from the file and add them
        for line in infile:
            amount = int(line)
            sum += amount
    except IOError:
        print("An error occurred trying to read this file.")
    except ValueError:
        print("Non-Numeric Data Found in this file")
    except:
        print("An Error Occurred")
    finally:
        infile.close()
        ######################
    print('The total of the numbers in the file was,' + str(sum))

# You don't need to change anything below this line:
if __name__ == '__main__':
    sum_numbers_from_file()