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

# find unique list of outgoing callers and call receivers
outgoing_callers = []
received_calls = []
for call in calls:
    caller = call[0]
    callee = call[1]
    if (caller not in outgoing_callers):
        outgoing_callers.append(caller)
    if (callee not in received_calls):
        received_calls.append(callee)

# find unique list of text senders and text receivers
text_senders = []
text_recievers = []
for text in texts:
    texter = text[0]
    textee = text[1]
    if (texter not in text_senders):
        text_senders.append(texter)
    if (textee not in text_recievers):
        text_recievers.append(textee)

# iterate through list of outgoing callers and see if they exist in the remaining three lists. If they do, remove
for caller in outgoing_callers:
    if (caller in received_calls or caller in text_senders or caller in text_recievers):
        outgoing_callers.remove(caller)

# print statement
outgoing_callers = sorted(outgoing_callers)
print("These numbers could be telemarketers: ")
for caller in outgoing_callers:
    print(caller)