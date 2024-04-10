class Node:
    """ A singly-linked node. """
    def __init__(self, data=None):
        self.data = data
        self.next = None

'''A singly linked list can be created using a simple class to hold the list. We start with a constructor 
that holds a reference to the very first node in the list (that is head in the following code). Since 
this list is initially empty, we will start by setting this reference to None:'''
class SinglyLinkedList:
    def __init__ (self):
        self.head = None
        self.size = 0
        
    def append(self, data):
        # Encapsulate the data in a Node 
        node = Node(data) #we encapsulate data in a node so that it has the next pointer attribute '''From here, we check if there are any existing nodes in the list (that is, whether self.head points to a Node). If there is None, this means that initially, the list is empty and the new node will be the first node.So, we make the new node the first node of the list; otherwise, we find the insertion point by traversing the list to the last node and updating the next pointer of the last node to the new node'''
        if self.head is None:   
            self.head = node    
        else: 
            current = self.head 
            while current.next:
                current = current.next 
            current.next = node 
            
            
            
words = SinglyLinkedList()
words.append('egg')
words.append('ham')
words.append('spam')
words.append('bhai kha le ab, Me to vegitarian hu to nahi khaunga')

current = words.head
while current:
    print(current.data)
    current = current.next
'''this implementation is not very efficient, and there is a drawback with the append method. In 
this, we have to traverse the entire list to find the insertion point. This may not be a problem when 
there are just a few items in the list, but it will be very inefficient when the list is long, as it will 
have to traverse the whole list to add an item every time. Let us discuss a better implementation 
of the append method.'''