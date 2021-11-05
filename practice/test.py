from LinkedList import LinkedList, DoublyLinkedList

""" linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(4)

print("printing each value: ")
node = linked_list.head
while node:
    print(node.value)
    node = node.next

print("print linked list as as list")
new_list = linked_list.to_list()
print(new_list)

linked_list_2 = DoublyLinkedList()
linked_list_2.append(1)
linked_list_2.append(-2)
linked_list_2.append(4)
linked_list_2.append(0)
linked_list_2.append(7)
linked_list_2.append(-9)

print("Going forward through the list, should print 1, -2, 4")
node = linked_list_2.head
while node:
    print(node.value)
    node = node.next

print("\nGoing backward through the list, should print 4, -2, 1")
node = linked_list_2.tail
while node:
    print(node.value)
    node = node.previous """

# Test prepend
linked_list = LinkedList()
linked_list.prepend(1)
linked_list.prepend(2)
linked_list.prepend(3)
linked_list.prepend(4)
linked_list.prepend(5)
linked_list.prepend(6)
print("Linked list prepend: ")
print(linked_list.to_list())

# Test search function
print(linked_list.search(3).value if linked_list.search(3) is not None else "Does not exist")
print(linked_list.search(8).value if linked_list.search(8) is not None else "Does not exist")
print(linked_list.search(1).value if linked_list.search(1) is not None else "Does not exist")

# Test remove function
print("Removing items...")
""" linked_list.remove(1)
linked_list.remove(4)
linked_list.remove(6) """
print(linked_list.to_list())

# test Pop
p = linked_list.pop()
print("popped: " + str(p))
p = linked_list.pop()
print("popped: " + str(p))
