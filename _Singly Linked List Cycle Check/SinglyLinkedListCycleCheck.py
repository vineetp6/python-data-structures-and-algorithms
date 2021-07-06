class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList(object):
    def __init__(self):
        self.head = None

    def append(self, data):
        # Empty Linked List
        if self.head is None:
            self.head = Node(data)
            self.head.next = self.head
        
        else:
            new_node = Node(data)
            current_node = self.head
            while current_node.next != self.head:
                current_node = current_node.next
            current_node.next = new_node
            new_node.next = self.head

    def prepend(self, data):
        new_node = Node(data)
        current_node = self.head
        new_node.next = self.head
        
        if self.head is None:
            new_node.next = new_node
        else:
            while current_node.next != self.head:
                current_node = current_node.next
            current_node.next = new_node
        self.head = new_node

    def print(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next
            if current_node == self.head:
                break
    
    def remove(self, key):
        if self.head.data == key:
            current_node = self.head
            while current_node.next != self.head:
                current_node = current_node.next
            current_node.next = self.head.next
            self.head = self.head.next
        else:
            current_node = self.head
            prev = None
            while current_node.next != self.head:
                prev = current_node
                current_node = current_node.next
                if current_node.data == key:
                    prev.next = current_node.next
                    current_node = current_node.next

    def __len__(self):
        current_node = self.head
        count = 0
        while current_node:
            count += 1
            current_node = current_node.next
            if current_node == self.head:
                break
        return count

    def is_circular_linked_list(self, input_list):
        current = input_list.head
        while current.next:
            current = current.next
            if current.next == input_list.head:
                return True
        return False

circularLinkedList = CircularLinkedList()
circularLinkedList.append("A")
circularLinkedList.append("B")
circularLinkedList.append("C")
circularLinkedList.append("D")
