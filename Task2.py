"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

phone_time = {}
for call in calls:
    if call[0] in phone_time:
        phone_time[call[0]] += int(call[3])
    else:
        phone_time[call[0]] = int(call[3])
    if call[1] in phone_time:
        phone_time[call[1]] += int(call[3])
    else:
        phone_time[call[1]] = int(call[3])
longest_time = 0
telephone_number = None
for phone, time in phone_time.items():
    if time > longest_time:
        longest_time = time
        telephone_number = phone

print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(telephone_number, longest_time))

# Big O Notation
# The time complexity of this function is O(n) where n is the number of calls in the calls list.
