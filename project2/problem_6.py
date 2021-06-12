class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    # set of elements which are in A or B or both
    union_set = set()
    current = llist_1.head
    if (current is not None):
        while current.next:
            union_set.add(current.value)
            current = current.next

    current = llist_2.head
    if (current is not None):
        while current.next:
            union_set.add(current.value)
            current = current.next

    union_ll = LinkedList()
    for i in union_set:
        union_ll.append(i)
    return union_ll

def intersection(llist_1, llist_2):
    # set of elements in A and B
    set_a = set()
    intersection = set()
    current = llist_1.head
    if (current is not None):
        while current.next:
            set_a.add(current.value)
            current = current.next

    current = llist_2.head
    if (current is not None):
        while current.next:
            if (current.value in set_a):
                intersection.add(current.value)
            current = current.next

    intersection_ll = LinkedList()
    for i in intersection:
        intersection_ll.append(i)
    return intersection_ll

# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print(linked_list_1)
print (union(linked_list_1,linked_list_2)) # 32 -> 65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 9 -> 11 -> 21 -> 
print (intersection(linked_list_1,linked_list_2)) # 4 -> 6 ->

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4)) # 65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 ->
print (intersection(linked_list_3,linked_list_4)) # No output

# test 3: One list with values, one empty linked list
linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = [1,2,3,4,5]

for i in element_1:
    linked_list_5.append(i)

print(union(linked_list_5, linked_list_6)) # 1 -> 2 -> 3 -> 4 -> 
print(intersection(linked_list_5, linked_list_6)) # No output

# test 4: both empty linked lists
linked_list_7 = LinkedList()
linked_list_8 = LinkedList()

print(union(linked_list_7, linked_list_8)) # No output
print(intersection(linked_list_7, linked_list_8)) # No output