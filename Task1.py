"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

telephone_numbers_list = [record[0] for record in telephone_numbers] + [record[1] for record in telephone_numbers]
unique_telephone_numbers = set(telephone_numbers_list)
count = len(unique_telephone_numbers)
print("There are {} different telephone numbers in the records.".format(count))

# Big O Notation
# The time complexity of this function is O(n) where n is the number of records in the telephone_numbers list.