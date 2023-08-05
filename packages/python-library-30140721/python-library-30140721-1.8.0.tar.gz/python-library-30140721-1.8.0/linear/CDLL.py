import sys
sys.path.append('..')
sys.path.append('../nodes')

from DLL import DLL
from nodes.DNode import Node

class CDLL(DLL):
    def __init__(self, head=None):
        super().__init__(head)
        if head is not None:
            head.prev = self.tail
            head.next = self.tail


    def InsertHead(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            node.prev = self.tail
            node.next = self.tail
        else:
            node.next = self.head
            node.prev = self.tail
            self.head.prev = node
            self.tail.next = node
            self.head = node
        self.size += 1

    def InsertTail(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            node.prev = self.tail
            node.next = self.tail
        else:
            node.prev = self.tail
            node.next = self.head
            self.tail.next = node
            self.head.prev = node
            self.tail = node
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
            node.prev = prev
            current.prev.next = node
            current.prev = node
            self.size += 1

    def Search(self, node):
        super().Search(node)
        if self.tail is not None and self.tail.data == node.data:
            return self.tail
        return None

    def DeleteHead(self):
        if self.head is None:
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = self.tail
            self.tail.next = self.head
        self.size -= 1

    def Sort(self):
        if self.head is None or self.head == self.tail:
            return
        sorted_head = None
        current = self.head
        for i in range(self.size):
            next_node = current.next
            sorted_head = self.insert_sorted_helper(sorted_head, current)
            current = next_node
        self.head = sorted_head

        # find the new tail node
        self.tail = self.head
        while self.tail.next is not None and self.tail.next != self.head:
            self.tail = self.tail.next
        return self

    def insert_sorted_helper(self, sorted_head, node):
        if sorted_head is None:
            node.next = node
            node.prev = node
            return node

        if node.data <= sorted_head.data:
            node.next = sorted_head
            node.prev = sorted_head.prev
            sorted_head.prev.next = node
            sorted_head.prev = node
            return node

        current = sorted_head
        while current.next is not None and current.next != sorted_head and current.next.data < node.data:
            current = current.next

        node.next = current.next
        node.prev = current
        if current.next is not None and current.next != sorted_head:
            current.next.prev = node

        current.next = node

        return sorted_head

if __name__ == '__main__':
    # create a new doubly linked list
    cdll = CDLL()

    # Insert nodes at head, tail and position
    node1 = Node(10)
    node2 = Node(20)
    node3 = Node(30)
    cdll.InsertHead(node1)
    print("Inserting node at head: ", node1.data)
    cdll.Print()
    cdll.InsertTail(node2)
    print("Inserting node at tail: ", node2.data)
    cdll.Print()
    print("Inserting node at position 2: ", node3.data)

    cdll.Insert(node3, 2)
    cdll.Print()

    # Insert nodes in sorted order
    node4 = Node(15)
    node5 = Node(25)
    node6 = Node(5)
    cdll.SortedInsert(node4)
    cdll.SortedInsert(node5)
    cdll.SortedInsert(node6)
    print("Inserting node in sorted order: ", node4.data, node5.data, node6.data)

    # print the contents of the list
    cdll.Print()

    # Search for a node
    search_node = Node(30)
    result = cdll.Search(search_node)
    if result is not None:
        print("Node found: ", result.data)
    else:
        print("Node not found")
    print()

    # delete nodes
    cdll.DeleteHead()
    print("Deleting node at head")
    cdll.Print()
    cdll.DeleteTail()
    print("Deleting node at tail")
    cdll.Print()
    cdll.Delete(node4)
    print("Deleting node: ",node4.data)

    # print the contents of the list
    cdll.Print()

    # Clear the list
    print("Clearing the list")
    cdll.Clear()

    # print the contents of the list
    cdll.Print()

# if __name__ == '__main__':
#     # create a new doubly linked list
#     cdll = CDLL()

#     # Insert nodes at head, tail and position
#     node1 = Node(10)
#     node2 = Node(20)
#     node3 = Node(30)
#     cdll.InsertHead(node1)
#     cdll.InsertTail(node2)
#     cdll.Insert(node3, 2)

#     cdll.Print()

#     # Insert nodes in sorted order
#     node4 = Node(15)
#     node5 = Node(25)
#     node6 = Node(5)
#     cdll.SortedInsert(node4)
#     cdll.SortedInsert(node5)
#     cdll.SortedInsert(node6)

#     # print the contents of the list
#     cdll.Print()

#     # Search for a node
#     search_node = Node(30)
#     result = cdll.Search(search_node)
#     if result is not None:
#         print("Node found: ", result.data)
#     else:
#         print("Node not found")

#     # delete nodes
#     cdll.DeleteHead()
#     cdll.DeleteTail()
#     cdll.Delete(node4)

#     # print the contents of the list
#     cdll.Print()

#     # Clear the list
#     cdll.Clear()
    

#     # print the contents of the list
#     cdll.Print() 
