# class LinkedList:
#     def __init__(self , value): #create new node
#     def append(self,value):     #create new node and add that node to end
#     def prepend(self , value):  #create new node and add that node to beginning
#     def insert(self, value):    #create new node insert node
# ---------------------------------------------------------------------------------
# if you look above class methods : all of them have one this in common which is to create a node
# and to not create a node each time we create a seperate calss just for creating a new node and
# we call it everytime we need a new node.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:

    def __init__(self, value):  # constructor which has 3 variables "new_node" , and head and tail which point to the same new_node initially
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):  # print out all elements fo the linked list
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):   # add node to end
        new_node_rear = Node(value)
        if self.head is None:
            self.head = new_node_rear
            self.tail = new_node_rear
        else:
            self.tail.next = new_node_rear
            self.tail = new_node_rear
        self.length += 1
        return True            # very optional

    def prepend(self, value):  # add node to beginning
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True  # very optional

    def pop(self):
        if self.length == 0:
            return None
        pre = self.head
        temp = self.head
        while (temp.next):     # this will be true until temp.next != None
            pre = temp
            temp = temp.next   # do not forget to update the temp
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    # def insert(self, index, value):    #add node inbetween nodes


myLinkedList = LinkedList(4)
myLinkedList.append(5)
myLinkedList.prepend(2)
print(myLinkedList.pop_first())
print(myLinkedList.pop_first())
print(myLinkedList.pop_first())
print(myLinkedList.pop_first())


# print(myLinkedList.pop())
# print(myLinkedList.pop())
# print(myLinkedList.pop())

myLinkedList.print_list()
