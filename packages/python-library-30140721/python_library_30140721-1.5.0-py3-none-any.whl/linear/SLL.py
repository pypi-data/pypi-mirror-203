from nodes.SNode import Node

class SLL:
    def __init__(self, head=None):
        self.head = head
        self.tail = head
        self.size = 0 if head is None else 1

    def InsertHead(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node
        self.size += 1

    def InsertTail(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1

    def Insert(self, node, position):
        if position == 1:
            self.InsertHead(node)
        elif position == self.size+1:
            self.InsertTail(node)
        elif position < 1 or position > self.size+1:
            print("Invalid position")
        else:
            current = self.head
            for i in range(1, position-1):
                current = current.next
            node.next = current.next
            current.next = node
            self.size += 1

    def SortedInsert(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            self.size = 1
        else:
            if self.isSorted():
                self.insert_sorted(node)
            else:
                self.Sort()
                self.insert_sorted(node)

    def isSorted(self):
        current = self.head
        for i in range(1,self.size):
            if current.data > current.next.data:
                return False
            current = current.next
        return True


    def insert_sorted(self, node):
        current = self.head
        prev = None
        while current is not None and current.data < node.data:
            prev = current
            current = current.next
        if prev is None:
            self.InsertHead(node)
        elif current is None:
            self.InsertTail(node)
        else:
            node.next = current
            prev.next = node
            self.size += 1

    def Search(self, node):
        current = self.head
        while current is not None:
            if current.data == node.data:
                return current
            current = current.next
        return None

    def DeleteHead(self):
        if self.head is None:
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
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
            current.next = None
            self.tail = current
        self.size -= 1

    def Delete(self, node):
        if self.head is None:
            return
        if node == self.head:
            self.DeleteHead()
        elif node == self.tail:
            self.DeleteTail()
        else:
            current = self.head
            while current.next != node:
                current = current.next
            current.next = node.next
            self.size -= 1

    def Sort(self):
        if self.head is None or self.head == self.tail:
            return
        sorted_head = None
        current = self.head
        while current is not None:
            next_node = current.next
            sorted_head = self.insert_sorted_helper(sorted_head, current)
            current = next_node
        self.head = sorted_head
        
        # find the new tail node
        self.tail = self.head
        for i in range(self.size-1):
            self.tail = self.tail.next
    
    def insert_sorted_helper(self, sorted_head, node):
        if sorted_head is None:
            node.next = None
            return node

        if node.data <= sorted_head.data:
            node.next = sorted_head
            return node

        current = sorted_head
        while current.next is not None and current.next.data < node.data:
            current = current.next

        node.next = current.next
        current.next = node
        return sorted_head
    
    def Clear(self):
        self.head = None
        self.tail = None
        self.size = 0

    def Print(self):
        print("The length of the list is", self.size)
        if self.isSorted():
            print("The list is sorted")
        else:
            print("The list is not sorted")
        current = self.head
        print("The contents of the list are:", end=" ")
        for i in range(self.size):
            print(current.data, end=" ")
            current = current.next
        print()
        print()

if __name__ == "__main__":
    sll = SLL()
    sll.Print()
    print("Inserting 1, 2, 3, 4 at the head")
    sll.InsertHead(Node(1))
    sll.InsertHead(Node(2))
    sll.InsertHead(Node(3))
    sll.InsertHead(Node(4))
    sll.Print()
    print("Inserting 5, 6 at the tail")
    sll.InsertTail(Node(5))
    sll.InsertTail(Node(6))
    sll.Print()
    print("Inserting 9 and 10 at position 1 and 5 respectively")
    sll.Insert(Node(9), 1)
    sll.Insert(Node(10), 5)
    sll.Print()
    if sll.Search(Node(6)):
        print("6 is Found")
    else:
        print("6 is Not found")
    print()
    print("Deleting 6")
    sll.Delete(sll.Search(Node(6)))
    sll.Print()

    print("Deleting Head and Tail")
    sll.DeleteHead()
    sll.DeleteTail()
    sll.Print()

    print('Clearing the list')
    sll.Clear()
    sll.Print()
    print("Inserting 1, 3, 2, 4 at the head")
    sll.InsertHead(Node(1))
    sll.InsertHead(Node(3))
    sll.InsertHead(Node(2))
    sll.InsertHead(Node(4))
    sll.Print()
    print("Sorting the list")
    sll.Sort()
    sll.Print()
    print('Clearing the list')
    sll.Clear()
    sll.Print()
    print('Inserting 1, 3, 5 in sorted way')
    sll.SortedInsert(Node(1))
    sll.SortedInsert(Node(3))
    sll.SortedInsert(Node(5))
    sll.Print()

