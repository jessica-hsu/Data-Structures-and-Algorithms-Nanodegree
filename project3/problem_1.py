# Find the square root of the integer without using any Python library. You have to find the floor value of the square root.
# expected O(logN) time
# ie. given 16, return 4. Given 27, return 5

def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if (isinstance(number, int) is False):
        return "Cannot find square root of non integers."
    if (number == 0):
        return 0
    if (number < 0):
        return "Cannot find square root of negative number."
    low = 1
    high = number
    while (low <= high) :
        target = (low + high) // 2 # double / becomes integer division in python 3
        squared = target * target
        #print(f"Lo: {low}, Hi: {high}, Target: {target}, Squared: {squared}")
        if (squared == number):
            return target
        elif (squared > number):
            if ((target-1) * (target-1) < number): # if target too high, check one num down to see if too low. If too low, then return target-1. For finding floor num of sqrt with decimals
                return target-1
            high = target 
        else:
            low = target

print ("Pass" if  (3 == sqrt(9)) else "Fail") # Pass
print ("Pass" if  (0 == sqrt(0)) else "Fail") # Pass
print ("Pass" if  (4 == sqrt(16)) else "Fail") # Pass
print ("Pass" if  (1 == sqrt(1)) else "Fail") # Pass
print ("Pass" if  (5 == sqrt(27)) else "Fail") # Pass
print ("Pass" if  ("Cannot find square root of negative number." == sqrt(-1)) else "Fail") # Pass
print ("Pass" if  ("Cannot find square root of non integers." == sqrt(9.99)) else "Fail") # Pass
print ("Pass" if  ("Cannot find square root of non integers." == sqrt("hello")) else "Fail") # Pass




