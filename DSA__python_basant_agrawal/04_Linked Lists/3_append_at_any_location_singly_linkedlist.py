'''When we want to insert a node in between two existing nodes, all we have to do is update two 
links. The previous node points to the new node, and the new node should point to the successor 
of the previous node'''

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
        # Encapsulate the data in a Node 
        node = Node(data)
        if self.head is None:
            self.head = node    
        else: 
            current = self.head 
            while current.next:
                current = current.next 
            current.next = node

    def append_at_a_location(self, data, index):  
        current = self.head  
        prev = self.head  
        node = Node(data) 
        count = 1 
        while current: 
            if count == 1:         
                node.next = current 
                self.head = node 
                print(count) 
                return 
            elif index == index: 
                node.next = current  
                prev.next = node 
                return 
            count += 1 
            prev = current 
            current = current.next 
        if count < index: 
            print("The list has less number of elements") 

     
            
            
            
words = SinglyLinkedList()
words.append('egg')
words.append('ham')
words.append('spam')

current = words.head
while current:
    print(current.data)
    current = current.next
    
    
    
words.append_at_a_location('new', 2) # need to check 

current = words.head
while current:
    print(current.data)
    current = current.next
    
'''The worst-case time complexity of the insert operation is O(1) when we have an additional 
pointer that points to the last node. Otherwise, when we do not have the link to the last node, 
the time complexity will be O(n) since we have to traverse the list to reach the desired position 
and in the worst case, we may have to traverse all the n nodes in the list.'''

