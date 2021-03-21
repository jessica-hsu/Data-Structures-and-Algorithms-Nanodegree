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
longest_duration = 0
telephone = ''
durations = {}
for call in calls:
    current_duration = int(call[3])
    phone_1 = call[0]
    phone_2 = call[1]
    # add data for phone1 to dictionary
    if (phone_1 in durations):
        current = durations[phone_1]
        durations[phone_1] = current + current_duration
    else:
        durations[phone_1] = current_duration
    # add data for phone2 to dictionary
    if (phone_2 in durations):
        current = durations[phone_2]
        durations[phone_2] = current + current_duration
    else:
        durations[phone_2] = current_duration
    # find current longest duration
    if (durations[phone_1] > longest_duration):
        longest_duration = durations[phone_1]
        telephone = phone_1
    if (durations[phone_2] > longest_duration):
        longest_duration = durations[phone_2]
        telephone = phone_2
        
print(f"{telephone} spent the longest time, {longest_duration} seconds, on the phone during September 2016.")