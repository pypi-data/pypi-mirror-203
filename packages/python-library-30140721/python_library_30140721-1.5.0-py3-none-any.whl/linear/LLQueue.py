from SLL import SLL
from nodes.SNode import Node

class LLQueue(SLL):

    def __init__(self):
        super().__init__()

    def enque(self, node):
        self.InsertTail(node)

    def InsertHead(self, node):
        return 
    
    def Insert(self, node, position):
        return
    
    def SortedInsert(self, node):
        return
    
    def isSorted(self):
        return
    
    def DeleteTail(self):
        return 
    
    def Delete(self, position):
        return
    
    def Sort(self):
        return
    
    
    def deque(self):
        if self.head is None:
            print("Queue is empty")
            return None
        else:
            node = self.head
            self.DeleteHead()
            return node
        
    def peek(self):
        if self.head is None:
            print("Queue is empty")
            return None
        else:
            return self.head.data
        
    def isEmpty(self):
        return self.head is None

    def Clear(self):
        super().Clear()

    def Print(self):
        print("The length of the queue is", self.size)
        current = self.head
        print("The contents of the queue are:", end=" ")
        for i in range(self.size):
            print(current.data, end=" ")
            current = current.next
        print()
        print()

if __name__ == "__main__":
    # Create a new LLQueue object
    queue = LLQueue()

    # Test enque() method
    node1 = Node(1)
    queue.enque(node1)
    node2 = Node(2)
    queue.enque(node2)
    queue.Print()
    node3 = Node(3)
    queue.enque(node3)
    node4 = Node(4)
    queue.enque(node4)
    queue.Print()

    # Test peek() method
    print("Peek:", queue.peek())  # Output: Peek: 1

    # Test deque() method
    dequeued_node = queue.deque()
    print("Dequeued Node:", dequeued_node.data)  # Output: Dequeued Node: 1
    print()
    queue.Print()
    # Test isEmpty() method
    print("Is Empty:", queue.isEmpty())  # Output: Is Empty: False

    # Test DeleteHead() method
    queue.Clear()
    print()
    print('After Clear()')
    print("Is Empty:", queue.isEmpty())  # Output: Is Empty: True    
