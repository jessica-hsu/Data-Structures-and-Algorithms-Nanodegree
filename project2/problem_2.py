"""
For this problem, the goal is to write code for finding all files under a directory (and all directories beneath it) that end with ".c"

"""
import os
import pathlib
def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    if (suffix == ""): # no suffix given
        return []
    #print(path)
    all_items = os.listdir(path)
    if (len(all_items) == 0): # nothing in directory
        return []
    #print(path)
    #print(all_items)
    suffix_files = []
    directories_to_check = []
    for item in all_items:
        p = f"{path}/{item}"
        #print(p)
        if (os.path.isdir(p)):
            #print(f"{item} is a directory")
            suffix_files.extend(find_files(suffix, p))
        elif (os.path.isfile(p)):
            #print(f"{item}")
            if (p.endswith(suffix)):
                #print(f"Found one: {p}")
                suffix_files.append(p)
        else:
            continue

    return suffix_files

path = f"{os.getcwd()}/testdir"

# test 1
print("Test 1:")
suffix = ".c"
my_files = find_files(suffix, path)
for f in my_files:
    print(f)
""" Expected output:
/Users/jessicahsu/Documents/GitHub/Data-Structures-and-Algorithms-Nanodegree/project2/testdir/subdir3/subsubdir1/b.c
/Users/jessicahsu/Documents/GitHub/Data-Structures-and-Algorithms-Nanodegree/project2/testdir/t1.c
/Users/jessicahsu/Documents/GitHub/Data-Structures-and-Algorithms-Nanodegree/project2/testdir/subdir5/a.c
/Users/jessicahsu/Documents/GitHub/Data-Structures-and-Algorithms-Nanodegree/project2/testdir/subdir1/a.c
"""
print("Test 2:")
# test 2
suffix = ".h"
my_files = find_files(suffix, path)
for f in my_files:
    print(f)
""" Expected output:
/Users/jessicahsu/Documents/GitHub/Data-Structures-and-Algorithms-Nanodegree/project2/testdir/subdir3/subsubdir1/b.h
/Users/jessicahsu/Documents/GitHub/Data-Structures-and-Algorithms-Nanodegree/project2/testdir/subdir5/a.h
/Users/jessicahsu/Documents/GitHub/Data-Structures-and-Algorithms-Nanodegree/project2/testdir/t1.h
/Users/jessicahsu/Documents/GitHub/Data-Structures-and-Algorithms-Nanodegree/project2/testdir/subdir1/a.h
"""

print("Test 3:")
# test 3
suffix = ""
my_files = find_files(suffix, path)
print(my_files)
# Expected output: []

print("Test 4:")
# test 3
suffix = ".html"
my_files = find_files(suffix, path)
print(my_files)
# Expected output: []