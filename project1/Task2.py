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
longest_duration = calls[0][3]
telephone = calls[0][0]
for call in calls:
    current_duration = call[3]
    if (current_duration > longest_duration):
        longest_duration = current_duration
        telephone = call[0]

print(f"{telephone} spent the longest time, {longest_duration} seconds, on the phone during September 2016.")