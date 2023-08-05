from SLL import SLL
from nodes.SNode import Node

class LLStack(SLL):

    def __init__(self):
        super().__init__()

    def push(self, node):
        self.InsertHead(node)

    def InsertTail(self, node):
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
    
    
    def pop(self):
        if self.head is None:
            print("Stack is empty")
            return None
        else:
            node = self.head
            self.DeleteHead()
            return node
        
    def peek(self):
        if self.head is None:
            print("Stack is empty")
            return None
        else:
            return self.head.data
        
    def isEmpty(self):
        return self.head is None

    def Clear(self):
        super().Clear()

    def Print(self):
        print("The length of the stack is", self.size)
        current = self.head
        print("The contents of the stack are:", end=" ")
        for i in range(self.size):
            print(current.data, end=" ")
            current = current.next
        print()
        print()

if __name__ == "__main__":
    lls=LLStack()
    lls.push(Node(1))
    lls.push(Node(2))
    lls.push(Node(6))
    lls.InsertHead(Node(4))
    lls.InsertTail(Node(5))
    lls.Print()
    print('The data at the top is',lls.peek())
    print()

    print()
    b=lls.pop()
    print('Popped data is',b.data)
    lls.Print()

    if lls.Search(Node(6)):
        print("6 is Found")
    else:
        print("6 is Not found")

    print()
    print('Clearing the stack')
    lls.Clear()
    if lls.isEmpty():
        print("Stack is empty")
    else:
        print("Stack is not empty")
    print()
    lls.Print()

