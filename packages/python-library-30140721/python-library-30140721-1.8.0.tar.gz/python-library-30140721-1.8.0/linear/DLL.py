from nodes.DNode import Node

class DLL:
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
            self.head.prev = node
            self.head = node
        self.size += 1

    def InsertTail(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
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
            node.prev = current
            current.next.prev = node
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
        while current is not None and current.next is not None:
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
            node.prev = prev
            current.prev.next = node
            current.prev = node
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
            self.head.prev = None
        self.size -= 1

    def DeleteTail(self):
        if self.head is None:
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.size -= 1

    def Delete(self, node):
        if self.head is None:
            return
        if node == self.head:
            self.DeleteHead()
        elif node == self.tail:
            self.DeleteTail()
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
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
        while self.tail.next is not None:
            self.tail = self.tail.next
        return self

    def insert_sorted_helper(self, sorted_head, node):
        if sorted_head is None:
            node.next = None
            node.prev = None
            return node

        if node.data <= sorted_head.data:
            node.next = sorted_head
            node.prev = None
            sorted_head.prev = node
            return node

        current = sorted_head
        while current.next is not None and current.next.data < node.data:
            current = current.next

        node.next = current.next
        node.prev = current
        if current.next is not None:
            current.next.prev = node
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
   
if __name__ == '__main__':
    # create a new doubly linked list
    dll = DLL()

    # Insert nodes at head, tail and position
    node1 = Node(10)
    node2 = Node(20)
    node3 = Node(30)
    dll.InsertHead(node1)
    print("Inserting node at head: ", node1.data)
    dll.Print()
    dll.InsertTail(node2)
    print("Inserting node at tail: ", node2.data)
    dll.Print()
    print("Inserting node at position 2: ", node3.data)

    dll.Insert(node3, 2)
    dll.Print()

    # Insert nodes in sorted order
    node4 = Node(15)
    node5 = Node(25)
    node6 = Node(5)
    dll.SortedInsert(node4)
    dll.SortedInsert(node5)
    dll.SortedInsert(node6)
    print("Inserting node in sorted order: ", node4.data, node5.data, node6.data)

    # print the contents of the list
    dll.Print()

    # Search for a node
    search_node = Node(30)
    result = dll.Search(search_node)
    if result is not None:
        print("Node found: ", result.data)
    else:
        print("Node not found")
    print()

    # delete nodes
    dll.DeleteHead()
    print("Deleting node at head")
    dll.Print()
    dll.DeleteTail()
    print("Deleting node at tail")
    dll.Print()
    dll.Delete(node4)
    print("Deleting node: ",node4.data)

    # print the contents of the list
    dll.Print()

    # Clear the list
    print("Clearing the list")
    dll.Clear()

    # print the contents of the list
    dll.Print()
