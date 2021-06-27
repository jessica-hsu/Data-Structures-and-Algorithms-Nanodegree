"""
Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal. You're not allowed to use any sorting function that Python provides.
"""

def swap(index_a, index_b, input_list):
    temp = input_list[index_a]
    input_list[index_a] = input_list[index_b]
    input_list[index_b] = temp

def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    low = 0 # any index below this index will be 0
    mid = 0
    high = len(input_list) - 1 # any index above this index will be 2

    while (mid <= high):
        if (input_list[mid] == 0):
            # swap with number at index low. then increase low and mid by 1
            swap(mid, low, input_list)
            low += 1
            mid += 1
        elif (input_list[mid] == 2): 
            # swap with number at index high. then decrease high by 1
            swap(mid, high, input_list)
            high -= 1
        else:
            # input_list[mid] == 1. don't do anything. only increase mid by 1
            mid += 1

    return input_list # array sorted in place, can return original

def test_function(test_case):
    if (test_case is None):
        print("Please enter a valid array with just 0s, 1s, and 2s")
        return
    sorted_array = sort_012(test_case)
    #print(f"test case: {test_case}")
    #print(f"results: {sorted_array}")

    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

# normal case 1
test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2]) # Pass

# normal case 2
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1]) # Pass

# normal case 3
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]) # Pass

# edge case 1: None input
test_function(None) # Please enter a valid array with just 0s, 1s, and 2s

# edge case 2: empty input array
test_function([]) # Pass

# edge case 3: only one kind of number
test_function([0, 0, 0, 0, 0, 0, 0]) # Pass

# edge case 4: only two different kinds number
test_function([0, 1, 0, 1, 0, 1, 0]) # Pass
