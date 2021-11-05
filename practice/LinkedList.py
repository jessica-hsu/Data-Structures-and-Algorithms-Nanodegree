class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class DoubleNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None 

class LinkedList:
    def __init__(self):
        self.head = None

    # append at tail of linked list
    def append(self, value):
        # list doesn't exist yet
        if (self.head is None):
            self.head = Node(value)
        else: # list exists, move to tail and add new node
            current = self.head
            while (current.next):
                current = current.next
            current.next = Node(value)
        return

    # convert linked list to regular python list
    def to_list(self):
        the_list = []
        current = self.head
        while (current):
            the_list.append(current.value)
            current = current.next
        return the_list

    # append at head of list
    def prepend(self, value):
        if (self.head is None): # list doesn't exist yet
            self.head = Node(value)
        else:  # list exists. make new head and attach the rest of the list
            remaining = self.head
            self.head = Node(value)
            self.head.next = remaining
        return
    
    # Search the linked list for a node with the requested value and return the node.
    def search(self, value):
        current = self.head # start at head
        while (current):
            if (current.value == value):
                return current
            else:
                current = current.next
        return None #if not in list, return None

    # Remove first occurrence of value
    # 1. remove head 2. remove tail 3. remove in between 4. no matches
    def remove(self, value):
        # if value is the head, remove head and make 2nd item the new head
        if (self.head.value == value):
            second_item = self.head.next
            self.head = second_item
            return

        current = self.head # start at head
        previous = None 
        while (current):
            if (current.value == value): # reach value to remove
                remaining = current.next # get the remaining list
                previous.next = remaining
                return
            else:
                previous = current
                current = current.next
        return

    # Return the first node's value and remove it from the list.
    def pop(self):
        value = self.head.value
        second = self.head.next
        self.head = second
        return value

    # Insert value at pos position in the list. If pos is larger than the length of the list, append to the end of the list.
    def insert(self, value, pos):
        return
    
    # Return the size or length of the linked list.
    def size(self)

    # Reverse the inputted linked list
    def reverse(self)

    def isCircular()

    def flatten

    

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    # add to tail of the list
    def append(self, value):
        if self.head is None:
            self.head = DoubleNode(value)
            self.tail = self.head
            return
        # we already keep track of tail    
        self.tail.next = DoubleNode(value)
        self.tail.next.previous = self.tail
        self.tail = self.tail.next # make new node the tail
        return

            
