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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

possible_telemarketers = set()
for call in calls:
    possible_telemarketers.add(call[0])
for call in calls:
    if call[1] in possible_telemarketers:
        possible_telemarketers.remove(call[1])
for text in texts:
    if text[0] in possible_telemarketers:
        possible_telemarketers.remove(text[0])
    if text[1] in possible_telemarketers:
        possible_telemarketers.remove(text[1])

print("These numbers could be telemarketers: ")
for number in sorted(possible_telemarketers):
    print(number)

# Big O Notation
# The time complexity of this function is O(n) where n is the number of calls and texts in the calls and texts list.
# The function iterates through the calls list twice and the texts list once.

