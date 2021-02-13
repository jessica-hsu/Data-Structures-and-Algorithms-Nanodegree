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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

# find first record of text
first_text = texts[0]
print(f"First record of texts, {first_text[0]} texts {first_text[1]} at time {first_text[2]}")

# find last record of calls
last_call = calls[-1]
print(f"Last record of calls, {last_call[0]} calls {last_call[1]} at time {last_call[2]}, lasting {last_call[3]} seconds")


"""
Run time Analysis:
Worst case scenario for run time is O(1). The calls and texts were read from csv and then put into an array.
Worst case lookup for arrays are O(1).  Array lookups were used to determine first text and last call (two lookups).
Three more lookups were used to text sender, text receiver, and text time. Four lookups were used to get
caller, receiver, call time, and call length. Total of 2 + 3 + 4 = 9 lookups were made. 9 x O(1) is stil O(1).

"""