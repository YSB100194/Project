# The worst-case running time of the append operation can be reduced from O(n) to O(1) using this method

class Node:
    """ A singly-linked node. """
    def __init__(self, data=None):
        self.data = data
        self.next = None

        
class SinglyLinkedList:
    def __init__ (self):
        self.tail = None
        self.head = None
        self.size = 0
        
    def append(self, data):
        node = Node(data)
        if self.tail:
            self.tail.next = node 
            self.tail = node
        else:
            self.head = node 
            self.tail = node

            
words = SinglyLinkedList()
words.append('egg')
words.append('ham')
words.append('spam')
words.append('bhai kha le ab, Me to vegitarian hu to nahi khaunga')

current = words.head
while current:
    print(current.data)
    current = current.next
