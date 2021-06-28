"""
In this problem, we will look for smallest and largest integer from a list of unsorted integers. 
The code should run in O(n) time. Do not use Python's inbuilt functions to find min and max.

"""

def get_min_max(ints):
    if (isinstance(ints, list) is False):
        print("Please enter a valid list of unsorted integers")
        return
    if (len(ints) < 1):
        print("No max and min in an empty list of integers")
        return
    min = ints[0]
    max = ints[0]
    for number in ints:
        if (number < min):
            min = number
        if (number > max):
            max = number
    return (min, max)
## Example Test Case of Ten Integers
import random

# normal case 1
l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)
print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail") # Pass

# normal case 2
l = [i for i in range(55, 889)]  # a list containing 0 - 888
random.shuffle(l)
print ("Pass" if ((55, 888) == get_min_max(l)) else "Fail") # Pass

# edge case: array is None
get_min_max(None) # Please enter a valid list of unsorted integers

# edge case: empty array
get_min_max([]) # No max and min in an empty list of integers

# edge case: only one element in array
print ("Pass" if ((1, 1) == get_min_max([1])) else "Fail") # Pass
