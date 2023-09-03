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

    # input  : int value
    # output : returns node

    # so head index will be 0 and so on where length of the linked list will be (tail-index + 1)
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        # returns the node , the value should be obtained using the . operator
        return temp

    # input  : int index , int value
    # outptu : returns node (updated value node)
    def set_value(self, index, value):
        # writing this method without the get method
        # if index < 0 or index >= self.length:
        #     return None
        # temp = self.head
        # for _ in range(index):
        #     temp = temp.next
        # temp.value = value
        # return temp
        # writing this method with the help of get method
        temp = self.get(index)
        if temp:  # this is actually another way of writing if temp != None:
            temp.value = value
            return True
        return False

    def insert(self, index, value):  # add node inbetween nodes
        if index < 0 or index >= self.length:
            return False
        if index == 0:
            return self.prepend(value)
        new_node = Node(value)
        temp = self.head
        for _ in range(index-1):
            temp = temp.next
        previous_node = temp
        temp = temp.next
        next_node = temp
        previous_node.next = new_node
        new_node.next = next_node
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length-1:
            return self.pop()
        prev = self.get(index-1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after


myLinkedList = LinkedList(1)
myLinkedList.prepend(0)
myLinkedList.append(2)
myLinkedList.append(3)
myLinkedList.append(4)

myLinkedList.reverse()
myLinkedList.print_list()
