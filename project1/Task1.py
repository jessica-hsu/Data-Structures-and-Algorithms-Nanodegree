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


"""
Run time Analysis:
Worst case scenario for run time is O(1). The calls and texts were read from csv and then put into an array.
Worst case lookup for arrays are O(1).  Array lookups were used to determine first text and last call (two lookups).
Three more lookups were used to text sender, text receiver, and text time. Four lookups were used to get
caller, receiver, call time, and call length. Total of 2 + 3 + 4 = 9 lookups were made. 9 x O(1) is stil O(1).

"""