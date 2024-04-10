
# Searching an element in a list
def search(self, data):
    for node in self.iter():
        if data == node:
            return True
        return False
   
    print(words.search('sspam'))
    print(words.search('spam'))


# Getting the size of the list
def size(self):
    count = 0
    current = self.head
    while current:
        count += 1
        current = current.next
    return count

class SinglyLinkedList:
    def __init__(self):
        self.head = data
        self.size = 0