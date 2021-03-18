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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

# filter for bangalore callers
bangalore_callers_filter = filter(lambda c: c[0][0:5] == "(080)", calls)
bangalore_callers = list(bangalore_callers_filter)

# Find unique list of codes made from bangalore callers
unique_codes = {
  "140": 0
}
for call in bangalore_callers:
  other_person = call[1]
  # fixed line
  if (other_person[0] == "("):
    if (other_person[1:4] not in unique_codes):
      unique_codes[other_person[1:4]] = 1
    else:
      unique_codes[other_person[1:4]] += 1

  # telemarketers
  elif (other_person[0:3] == "140"):
    unique_codes["140"] += 1
  else: # mobile
    if (other_person[0:4] not in unique_codes):
      unique_codes[other_person[0:4]] = 1
    else:
      unique_codes[other_person[0:4]] += 1
  
# Find percentages of calls made to other fixed lines in bangalore
to_other_bangalore_fixed_lines = unique_codes["080"]
percentage = round((to_other_bangalore_fixed_lines/len(bangalore_callers))*100, 2)

# print messages
print("The numbers called by people in Bangalore have codes:")
unique_codes = sorted(unique_codes)
for code in unique_codes:
  print(code)
print(f"{percentage} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")