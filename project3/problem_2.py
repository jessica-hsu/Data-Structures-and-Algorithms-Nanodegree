# You are given a sorted array which is rotated at some random pivot point.
# Example: [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]
# You are given a target value to search. If found in the array return its index, otherwise return -1.
# You can assume there are no duplicates in the array and your algorithm's runtime complexity must be in the order of O(log n).
# Example Input: nums = [4,5,6,7,0,1,2], target = 0, Output: 4

def binary_search(lo, hi, input_list, number):
    while (lo <= hi):
        target = (lo + hi) // 2
        test = input_list[target]
        #print(f"Lo: {lo}, Hi: {hi} Target: {target}, Test: {test}")
        if (test < number):
            if (lo == target):
                return hi if input_list[hi] == number else -1
            lo = target
        elif (test > number):
            if (lo == hi):
                return -1
            hi = target
        else:
            return target
    return -1

def find_rotated_index(lo, hi, input_list):
    while (lo <= hi):
        target = (lo + hi) // 2
        num = input_list[target]
        t1 = target - 1
        t2 = target + 1
        first = input_list[0]
        #print(f"Lo: {lo}, Hi: {hi} Target: {target}, Num: {num}, t1: {t1}, t2: {t2}")
        if (t1 > -1 and t2 < len(input_list)):
            num_1 = input_list[t1]
            num_2 = input_list[t2]
            #print(f"Num: {num}, t1: {t1}, Num_1: {num_1}, Num_2: {num_2}")
            if (num_1 < num and num_2 < num):
                return target
            elif (first < num and target + 2 < len(input_list)): # go right
                lo = target
            elif (first < num and target + 2 == len(input_list)): # array not pivoted, return -1. all is in order
                return -1
            elif (first > num): # go left
                hi = target
        elif (t1 < 0 and input_list[t2] < num):
            #print(f"Lo: {lo}, Hi: {hi} Target: {target}, Num: {num}, , Num_2: {input_list[t2]}")
            return target

    return -1

def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    # find the index where array was rotated
    lo = 0
    hi = len(input_list)-1
    rotated_index = find_rotated_index(lo, hi, input_list)
    #print(f"Rotated index: {rotated_index}")
    if (rotated_index == -1): # array not rotated. all in order
        return binary_search(lo, hi, input_list, number)
    else:
        array_1 = input_list[0:rotated_index+1]
        array_2 = input_list[rotated_index+1:len(input_list)]
        #print(f"Array 1: {array_1}")
        #print(f"Array 2: {array_2}")
        # search for number in first array
        lo = 0
        hi = len(array_1)-1
        index = binary_search(lo, hi, array_1, number)
        #print(f"Index at attempt 1: {index}")
        if (index == -1):
            # not in first array. search second array
            hi = len(array_2) - 1
            index = binary_search(lo, hi, array_2, number)
            #print(f"Index at attempt 2: {index}")
            if (index == -1):
                return -1
            else:
                return index + len(array_1) # must add to get index of original array
        else: # number found, return index
            return index


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    if (isinstance(input_list, list) is False):
        print("Input list must be a list")
        return

    #print(input_list)
    number = test_case[1]
    if (number is None):
        print("Please input a valid target")
        return

    #print(number)
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6]) # Pass
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1]) # Pass
test_function([[6, 7, 8, 1, 2, 3, 4], 8]) # Pass
test_function([[6, 7, 8, 1, 2, 3, 4], 1]) # Pass
test_function([[6, 7, 8, 1, 2, 3, 4], 10]) # Pass

# edge case: array not pivoted
test_function([[1,2,3,4,5,6], 4]) # Pass

# edge case: pivoted at point where one array has 1 element only
test_function([[4,5,1], 4]) # Pass

# edge case: empty array
test_function([[], 4]) # Pass

# edge case: None as array
test_function([None, 4]) # Input list must be a list

# edge case: None as given number
test_function([[1,2,3], None]) # Please input a valid target

#test_function([[4], 4])
""" test_function([[1,2,3,4,5], 4])
test_function([[7,8,9,23], 4])
test_function([[5,6,7,8,9], 5])
test_function([[5,6,7,8,9], 9]) """

#test_function([[6,7,8,9,10,1,2,3,4], 4])
#test_function([[6,7,8,9,10,1,2], 4])
#test_function([[6,7,1,2,3,4,5], 4])
# test_function([[4,5,1], 4])
#test_function([[4,1,2], 4])
#test_function([[1,2,3,4,5,6], 4])
