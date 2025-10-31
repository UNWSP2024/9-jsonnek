# Jonathan Sonnek
# October 30 2025
# Program #1: Item Counter

# Assume a file containing a series of names (as strings) is named names.txt 
# (Use the included example file names.txt) and exists on the computer's disk.
# Write a program that displays the number of names that are stored in the file.

def count_file_lines():
    ######################
    total_names = 0
    names = open("names.txt", "r")
    for line in names:
      total_names += 1
    names.close()
    ######################
    print('In the count_file_lines function there are ' +  str(total_names) + ' names total')



# You don't need to change anything below this line:
if __name__ == '__main__':
    count_file_lines()