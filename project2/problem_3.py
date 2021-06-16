# Huffman Coding

import sys
import json
import heapq

def huffman_encoding(data):    
    # determine frequency of each letter
    if (data == "" or data is None):
        print("ERROR: please enter a valid string")
        return None, None
    frequencies = {}
    for letter in data:
        if (letter in frequencies):
            current = frequencies[letter]
            frequencies[letter] = current + 1
        else:
            frequencies[letter] = 1

    #print(json.dumps(frequencies, indent=2))

    # put frequencies in priority queue. sorted
    queue = []
    for letter in frequencies:
        # (frequency, letter, left child, right child)
        heapq.heappush(queue, (frequencies[letter], letter, None, None))
    # pop 2 nodes with lowest frequency from queue and combine to make new node and put node back in tree. Resort queue. Repeat until only 1 element left in queue
    while (len(queue) != 1):
        # pop two nodes with lowest frequency
        node_1 = heapq.heappop(queue)
        node_2 = heapq.heappop(queue)
        # combine to make new node with center as sum of node_1 value + node_2 value and left child is node_1/2 with lower frequency than the other. right child is the other node with higher frequency
        sum = node_1[0] + node_2[0]
        new_letter = node_1[1] + node_2[1]
        # (frequency, letter, left child, right child)
        new_node = (sum, new_letter, (node_1, 0), (node_2, 1))
        # put new node back in queue
        heapq.heappush(queue, new_node)
        #print(queue)
    #print('Done stripping')
    # final huffman tree is the last item left in priority queue
    tree = heapq.heappop(queue)
    #print(tree)

    # if tree only has root node and no childen, set to 0 automatically and return
    if (tree[2] is None and tree[3] is None):
        encoded_string = ''
        for letter in data:
            encoded_string = encoded_string + '0'
        return encoded_string, tree

    # traverse tree and create unique binary code for each letter
    codes = {} # dictionary with letter to binary
    stack = []
    parent_map = {}
    stack.append((tree, '')) # (tree node, bit)
    while (len(stack) != 0):
        current = stack.pop() # (tree node, bit)
        current_node = current[0]
        current_bit = current[1]
        current_letter = current_node[1]
        left_child = current_node[2]
        right_child = current_node[3]
        if (left_child is None and right_child is None):
            bit = str(current_bit)
            current_child = current_letter
            binary = bit    # begin with the bit for the found letter
            parent = None
            while (bit != ''):
                parent = parent_map[current_child][0]
                bit = str(parent_map[current_child][1])
                binary = bit + binary
                current_child = parent
            codes[current_letter] = binary
        else:
            stack.append(left_child)
            stack.append(right_child)
            left_child_node = left_child[0]
            left_child_letter = left_child_node[1]
            right_child_node = right_child[0]
            right_child_letter = right_child_node[1]
            if (left_child_letter not in parent_map):
                parent_map[left_child_letter] = (current_letter, current_bit)
            if (right_child_letter not in parent_map):
                parent_map[right_child_letter] = (current_letter, current_bit)
    #print(json.dumps(codes, indent=2))

    # replace each letter with binary code
    encoded_string = ''
    for letter in data:
        bit = codes[letter]
        encoded_string = encoded_string + bit

    return encoded_string, tree
        

def huffman_decoding(data,tree):

    # if tree only has root node and no childen, set to turn 0 back to letter in tree
    if (tree[2] is None and tree[3] is None):
        letter = tree[1]
        decoded_string = ''
        for bit in data:
            decoded_string = decoded_string + letter
        return decoded_string

    #print(tree)
    decoded_string = ''
    current_node = (tree, '')
    for bit in data:
        #print(current_node)
        direction = "right"    
        if (bit == '0'): # go left if 0
            current_node = current_node[0][2]
            direction = "left"
        else: # go right if 1
            current_node = current_node[0][3]
            # if reach leaf node (no more children), get the letter and repeat process  
        #print(f"found a {bit}. Go {direction} to {current_node[0][1]}")    
        if (current_node[0][2] is None and current_node[0][3] is None):
            letter = current_node[0][1]
            # build decoded string
            decoded_string = decoded_string + letter
            #print(f"Letter: {letter}")
            # reset back to tree head
            current_node = (tree, '')  
    return decoded_string

if __name__ == "__main__":
    codes = {}
    # case 1

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence))) # 69
    print ("The content of the data is: {}\n".format(a_great_sentence)) # The bird is the word

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2)))) # 36
    print ("The content of the encoded data is: {}\n".format(encoded_data)) # 1110000100011011101010100111111001001111101010001000110101101101001111

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data))) # 69
    print ("The content of the encoded data is: {}\n".format(decoded_data)) # The bird is the word

    print("#################################################################################################")

    # case 2
    sentence = "Hi. My name is le foo."
    print ("The size of the data is: {}\n".format(sys.getsizeof(sentence))) # 71
    print ("The content of the data is: {}\n".format(sentence)) # Hi. My name is le foo.
    encoded_data, tree = huffman_encoding(sentence)
    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2)))) # 36
    print ("The content of the encoded data is: {}\n".format(encoded_data)) # 11000111110110111001101001001011010000111100111110011010000111001110111001001011
    decoded_data = huffman_decoding(encoded_data, tree)
    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data))) # 71
    print ("The content of the encoded data is: {}\n".format(decoded_data)) # Hi. My name is le foo.

    print("#################################################################################################")

    # case 3
    sentence = ""
    print ("The size of the data is: {}\n".format(sys.getsizeof(sentence))) # 49
    print ("The content of the data is: {}\n".format(sentence)) # 
    encoded_data, tree = huffman_encoding(sentence) # ERROR: please enter a valid string
    
    print("#################################################################################################")

    # case 4
    sentence = None
    print ("The size of the data is: {}\n".format(sys.getsizeof(sentence))) # 16
    print ("The content of the data is: {}\n".format(sentence)) # None
    encoded_data, tree = huffman_encoding(sentence)  # ERROR: please enter a valid string

    print("#################################################################################################")

    # case 5
    sentence = "AAAAA"
    print ("The size of the data is: {}\n".format(sys.getsizeof(sentence))) # 54
    print ("The content of the data is: {}\n".format(sentence)) # AAAAA
    encoded_data, tree = huffman_encoding(sentence)
    print(f"ENCODED DATA: {encoded_data}") # 00000
    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2)))) # 54
    print ("The content of the encoded data is: {}\n".format(encoded_data)) # 00000
    decoded_data = huffman_decoding(encoded_data, tree)
    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data))) # 54
    print ("The content of the encoded data is: {}\n".format(decoded_data)) # AAAAA
    