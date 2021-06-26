""" Rearrange Array Elements so as to form two number such that their sum is maximum. Return these two numbers. 
You can assume that all array elements are in the range [0, 9]. The number of digits in both the numbers cannot differ by more than 1. 
You're not allowed to use any sorting function that Python provides and the expected time complexity is O(nlog(n)).
"""

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while (left_index < len(left) and right_index < len(right)):
        left_num = left[left_index]
        right_num = right[right_index]
        if (left_num >= right_num): # if left number is bigger, put in new array
            merged.append(left_num)
            left_index += 1
        else:   # right number is bigger. put in new array
            merged.append(right_num)
            right_index += 1
    
    # left array finished first and right array has leftovers. Append rest of right array
    if (left_index == len(left) and right_index < len(right)):
        merged = merged + right[right_index:]
    elif (right_index == len(right) and left_index < len(left)): # right array finished first and left array has leftovers. Append rest of left array
        merged = merged + left[left_index:]

    return merged

def merge_sort(input):
    if (len(input) <= 1): # base case. if array of 1 element, no need to merge sort
        return input
    
    # split array into two pieces
    middle = len(input) // 2
    left = input[0:middle]
    right = input[middle:]
    #print(f"left: {left}")
    #print(f"right: {right}")

    # merge sort each side
    left = merge_sort(left)
    right = merge_sort(right)

    # combine sorted left and right sides
    combined = merge(left, right)
    return combined

def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    # sort descending order first
    sorted_list = merge_sort(input_list)

    # if only one element in input_list
    if (len(sorted_list) == 1):
        return sorted_list[0], 0
        
    # first number: form number with element on every even index
    first_number = ''
    for i in range(0, len(sorted_list), 2):
        first_number += str(sorted_list[i])

    # second number: form second number with element on every odd index
    second_number = ''
    for i in range(1, len(sorted_list), 2):
        second_number += str(sorted_list[i])

    return int(first_number), int(second_number)
    

def test_function(test_case):
    #print(f"test case: {test_case[0]}")
    input_list = test_case[0]
    solution = test_case[1]
    if (input_list is None):
        print("Please enter a valid input list")
        return

    if (input_list == [] and solution == []):
        print("Pass")
        return
    elif (input_list == [] and solution != []):
        print("Fail")
        return

    if (solution is None):
        print("Please enter a valid solution")
        return

    output = rearrange_digits(input_list)
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


# normal case 1
test_function([[1, 2, 3, 4, 5], [542, 31]]) # Pass

# normal case 2
test_function([[4, 6, 2, 5, 9, 8], [964, 852]]) # Pass

# 2 elements in input list
test_function([[4,5], [4,5]]) # Pass

# 1 element in input list
test_function([[5], [5]]) # Pass

# edge case: empty given array
test_function([[], []]) # Pass

# edge case: empty given array
test_function([[], [33,44]]) # Fail

# edge case: none type for given array
test_function([None, []]) # Please enter a valid input list

# edge case: none type for results
test_function([[1,2,3,4], None]) # Please enter a valid solution