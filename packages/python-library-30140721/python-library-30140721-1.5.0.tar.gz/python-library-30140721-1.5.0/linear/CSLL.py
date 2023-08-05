from SLL import SLL

from nodes.SNode import Node

class CSLL(SLL):
    def __init__(self, head=None):
        super().__init__(head)
        if head is not None:
            head.next = head
    

    def InsertHead(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            node.next = node
        else:
            node.next = self.head
            self.head = node
            self.tail.next = self.head
        self.size += 1

    def InsertTail(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            node.next = node
        else:
            node.next = self.head
            self.tail.next = node
            self.tail = node
        self.size += 1

    def SortedInsert(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            node.next = node
            self.size = 1
        else:
            if self.isSorted():
                self.insert_sorted(node)
            else:
                self.Sort()
                self.insert_sorted(node)

    def insert_sorted(self, node):
        current = self.head
        prev = None
        length=self.size
        while length!=0 and current.data < node.data:
            prev = current
            current = current.next
            length-=1
            if current == self.head:
                break
        if prev is None:
            self.InsertHead(node)
        elif current is None or current == self.head:
            self.InsertTail(node)
        else:
            node.next = current
            prev.next = node
            self.size += 1

    def Sort(self):
        if self.head is None or self.head == self.head.next:
            return

        sorted_head = None
        current = self.head
        while current.next != self.head:
            next_node = current.next
            sorted_head = self.insert_sorted_helper(sorted_head, current)
            current = next_node
        sorted_head = self.insert_sorted_helper(sorted_head, current)  # Handle tail node separately

        self.head = sorted_head

        # Find the new tail node
        self.tail = self.head
        while self.tail.next != self.head:
            self.tail = self.tail.next

    def insert_sorted_helper(self, sorted_head, node):
        if sorted_head is None:
            node.next = node
            return node

        if node.data <= sorted_head.data:
            temp = sorted_head
            while temp.next != sorted_head:
                temp = temp.next
            node.next = sorted_head
            temp.next = node
            return node

        current = sorted_head
        while current.next != sorted_head and current.next.data < node.data:
            current = current.next

        node.next = current.next
        current.next = node
        return sorted_head

    
    def SortedInsert(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            self.size = 1
            node.next = self.head # Make it circular
        else:
            if self.isSorted():
                self.insert_sorted(node)
            else:
                self.Sort()
                self.insert_sorted(node)

    def isSorted(self):
        if self.head is None or self.head == self.tail:
            return True
        current = self.head
        while current.next != self.head:
            if current.data > current.next.data:
                return False
            current = current.next
        return True

    def DeleteHead(self):
        if self.head is None:
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.tail.next = self.head
        self.size -= 1

    def DeleteTail(self):
        if self.head is None:
            return

        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            current = self.head
            while current.next != self.tail:
                current = current.next
            current.next = self.head  # Update next pointer to make it circular
            self.tail = current
        self.size -= 1


# Test for CSLL class
def test_csll():
    # Create an empty CSLL
    cll = CSLL()

    # Test InsertHead() and Print()
    print("Test InsertHead():")
    for i in range(5):
        node = Node(i)
        cll.InsertHead(node)
    cll.Print()  # Expected output: "4 3 2 1 0"

    # Test InsertTail() and Print()
    print("Test InsertTail():")
    for i in range(5, 10):
        node = Node(i)
        cll.InsertTail(node)
    cll.Print()  # Expected output: "4 3 2 1 0 5 6 7 8 9"

    # Test insert() and Print()
    print("Test insert():")
    node = Node(10)
    cll.Insert(node, 6)
    cll.Print()  # Expected output: "4 3 2 1 0 10 5 6 7 8 9"

    # Test SortedInsert() and Print()
    print("Test SortedInsert():")
    node = Node(3)
    cll.SortedInsert(node)
    print('The function of Sort() takes place in SortedInsert()')
    print()
    cll.Print()  # Expected output: "4 3 3 2 1 0 10 5 6 7 8 9"


    # Test Search() and Delete()
    print("Test Search() and Delete():")
    node = Node(5)
    found = cll.Search(node)
    if found:
        print("Found: ", found.data)
        cll.Delete(found)
    cll.Print()  # Expected output: "4 3 3 2 1 0 10 6 7 8 9"

    # Test DeleteHead() and Print()
    print("Test DeleteHead():")
    cll.DeleteHead()
    cll.Print()  # Expected output: "3 3 2 1 0 10 6 7 8 9"

    # Test DeleteTail() and Print()
    print("Test DeleteTail():")
    cll.DeleteTail()
    cll.Print()  # Expected output: "3 3 2 1 0 10 6 7 8"

    # Test clear() and Print()
    print("Test clear():")
    cll.Clear()
    cll.Print()  # Expected output: "The length of the list is 0\nThe list is sorted\nThe contents of the list are:\n"

test_csll()
