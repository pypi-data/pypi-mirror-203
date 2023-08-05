from Tnode import Tnode
from BST import BST


class AVL(BST):
    def __init__(self, val=None, obj=None):
        super().__init__()
        if val is not None:
            self.root = Tnode(val)
        elif obj is not None:
            self.root = obj
            self._create_balanced_tree(obj.left)
            self._create_balanced_tree(obj.right)
        else:
            self.root = None
        
    def setRoot(self, obj):
        self.root = obj
        self._create_balanced_tree(obj.left)
        self._create_balanced_tree(obj.right)
        
    def insert(self, val):
        super().insert(val)
        self.balance(self.root)

    def insert_node(self, node):
        super().insert_node(node)
        self.balance(self.root)

    def balance(self, node):
        if node is None:
            return
    
        if self.height(node.left) - self.height(node.right) > 1:
            if self.height(node.left.left) >= self.height(node.left.right):
                self.rotate_right(node)
            else:
                self.rotate_left(node.left)
                self.rotate_right(node)
        elif self.height(node.right) - self.height(node.left) > 1:
            if self.height(node.right.right) >= self.height(node.right.left):
                self.rotate_left(node)
            else:
                self.rotate_right(node.right)
                self.rotate_left(node)
            
        self.balance(node.left)
        self.balance(node.right)
      
    def rotate_right(self, node):
        newRoot = node.left
        node.left = newRoot.right
        newRoot.right = node
    
        if node is self.root:
            self.root = newRoot
        
    def rotate_left(self, node):
        newRoot = node.right
        node.right = newRoot.left
        newRoot.left = node
    
        if node is self.root:
            self.root = newRoot
        
    def height(self, node):
        if node is None:
            return -1
        else:
            return 1 + max(self.height(node.left), self.height(node.right))
    
    def search(self, val):
        return super().Search(val)



    def printInOrder(self, node=None):
      if node is None:
        node = self.root
      super().printInOrder(node)



    def printBF(self):
        super().printBF()

    def _create_balanced_tree(self, node):
        if node is None:
            return
        self.insert_node(node)
        self._create_balanced_tree(node.left)
        self._create_balanced_tree(node.right)




#################   Previous trials   ###########################




# from Tnode import Tnode
# from BST import BST

# class AVL(BST):
# #Initilaizing data member
#   def __init__(self, root = None):
#     self.root = root


# #Default constrcutor
#   def default_constrcutor(self):
#     self.root = None




# #Overload constrcuctor 1
#   def __init__2(self, val):
#     self.root = Tnode(val)


# #Overload constructor 2
#   def __init__(self, obj):
#       self.root = obj
#       if obj.left is not None or obj.right is not None:
#           self.balance()


# #Getter/Setter
#   def get_root(self):
#       return self.root

#   def set_root(self, node):
#       self.root = node
#       if node.left or node.right:
#           self.balance()


# #Balancing functions
#   def balance(self):
#       nodes = []
#       self.in_order(self.root, nodes)
#       self.root = self.balance_recursive(nodes, 0, len(nodes) - 1)
      
#   def in_order(self, node, nodes):
#       if node:
#           self.in_order(node.left, nodes)
#           nodes.append(node)
#           self.in_order(node.right, nodes)
          
#   def balance_recursive(self, nodes, start, end):
#       if start > end:
#           return None
#       mid = (start + end) // 2
#       node = nodes[mid]
#       node.left = self.balance_recursive(nodes, start, mid - 1)
#       node.right = self.balance_recursive(nodes, mid + 1, end)
#       return node



#   def height(self, node):
#           if node is None:
#               return -1
#           else:
#               return node.height

#   def update_height(self, node):
#       node.height = max(self.height(node.left), self.height(node.right)) + 1

#   def balance_factor(self, node):
#       if node is None:
#           return 0
#       else:
#           return self.height(node.left) - self.height(node.right)

#   def left_rotate(self, node):
#       pivot = node.right
#       node.right = pivot.left
#       pivot.left = node
#       self.update_height(node)
#       self.update_height(pivot)
#       return pivot

#   def right_rotate(self, node):
#       pivot = node.left
#       node.left = pivot.right
#       pivot.right = node
#       self.update_height(node)
#       self.update_height(pivot)
#       return pivot

#   def rebalance(self, node):
#       if self.balance_factor(node) == 2:
#           if self.balance_factor(node.left) == -1:
#               node.left = self.left_rotate(node.left)
#           return self.right_rotate(node)
#       elif self.balance_factor(node) == -2:
#           if self.balance_factor(node.right) == 1:
#               node.right = self.right_rotate(node.right)
#           return self.left_rotate(node)
#       else:
#           self.update_height(node)
#           return node

#   def _insert(self, val, node):
#       node = super()._insert(val, node)
#       return self.rebalance(node)

#   def _insert_node(self, node, parent):
#       parent = super()._insert_node(node, parent)
#       return self.rebalance(parent)



#   # def delete(self, val):
#   #     self.root = self._delete(val, self.root)

#   # def _delete(self, val, node):
#   #     if node is None:
#   #         print("Value not found")
#   #         return node
#   #     elif val < node.data:
#   #         node.left = self._delete(val, node.left)
#   #     elif val > node.data:
#   #         node.right = self._delete(val, node.right)
#   #     else:
#   #         if node.left is None and node.right is None:
#   #             node = None
#   #         elif node.left is None:
#   #             node = node.right
#   #         elif node.right is None:
#   #             node = node.left
#   #         else:
#   #             min_node = self.find_min_node(node.right)
#   #             node.data = min_node.data
#   #             node.right = self._delete(min_node.data, node.right)
      
#   #     if node is not None:
#   #         return self.rebalance(node)
#   #     else:
#   #         return node

#   # def find_min_node(self, node):
#   #     while node.left is not None:
#   #         node = node.left
#   #     return node








# #Search function
#   def Search(self, val):
#       return self.search_recursive(self.root, val)

#   def search_recursive(self, node, val):
#     if not node:
#       return None
#     if node.data == val:
#       return node
#     elif val < node.data:
#       return self.search_recursive(node.left, val)
#     else:
#       return self.search_recursive(node.right, val)


# #Print in order function
#   def printInOrder(self):
#     self.print_in_order_recursive(self.root)

#   def print_in_order_recursive(self, node):
#     if node is not None:
#       self.print_in_order_recursive(node.left)
#       print(node.data, end=' ')
#       self.print_in_order_recursive(node.right)


# #PrintBF function
#   def printBF(self):
#     self.print_bf_recursive(self.root)

#   def print_bf_recursive(self, node):
#     if node is None:
#       return
#     q = [node]
#     while len(q) > 0:
#       n = len(q)
#       for i in range(n):
#         curr = q.pop(0)
#         print(curr.data, end=' ')
#         if curr.left is not None:
#           q.append(curr.left)
#         if curr.right is not None:
#           q.append(curr.right)
#       print()






  # def insert_node(self, node):
  #     super().insert(node)
  #     self.balance(self.root)
      