class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        temp = self.head
        for _ in range(self.length-1):
            temp = temp.next
        temp.next = new_node
        self.tail = new_node
        self.length += 1

    def find_middle_node(self):
        size = 0
        temp = self.head
        while (temp != None):
            temp = temp.next
            size += 1
        print(str(size)+" is the size of the linked list")


myLinkedList = LinkedList(0)
myLinkedList.append(1)
myLinkedList.append(2)
myLinkedList.find_middle_node()
