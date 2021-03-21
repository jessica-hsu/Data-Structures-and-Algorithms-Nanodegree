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

telemarketers = set()
not_telemarketers = set()

# text senders and recievers are definitely not telemarketers
for text in texts:
    texter = text[0]
    textee = text[1]
    not_telemarketers.add(texter)
    not_telemarketers.add(textee)

# callees are not telemarketers
for call in calls:
    callee = call[1]
    not_telemarketers.add(callee)

# go through all calls again. If caller not in not_telemarketers, add to telemarketer list
for call in calls:
    caller = call[0]
    if (caller not in not_telemarketers):
        telemarketers.add(caller)

print("These numbers could be telemarketers:")
for t in sorted(telemarketers):
    print(t)