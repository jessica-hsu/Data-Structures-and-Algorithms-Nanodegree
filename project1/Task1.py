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
# look up of all phones
all_phones = []

def add(num1, num2):
    if (num1 not in all_phones):
        all_phones.append(num1)
    if (num2 not in all_phones):
        all_phones.append(num2)

# read texts
for text in texts:
    sender = text[0]
    receiver = text[1]
    add(sender, receiver)

# read calls
for call in calls:
    caller = call[0]
    callee = call[1]
    add(caller, callee)

# Get size of all_phones
total = len(all_phones)

# Print statement
print(f"There are {total} different telephone numbers in the records.")

"""
Run time Analysis:


"""