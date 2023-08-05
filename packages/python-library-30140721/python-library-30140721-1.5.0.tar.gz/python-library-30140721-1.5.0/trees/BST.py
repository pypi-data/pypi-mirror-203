from Tnode import Tnode
from collections import deque

class BST:
#Initilaizing data member
  def __init__(self, root = None):
    self.root = root



#Default constrcuctor
  def default_constructor(cls):
    return cls



#Overload constrcuctor 1
  def overload_constructor_val(self, val):
    self.root = Tnode(val)



#Overload constrcutor 2
  def overload_constructor_obj(self, obj):
    self.root = obj



#Getter/Setter for root

  def get_root(self):
    return self.root

  def set_root(self, root):
    self.root = root



# Both insert functions

  def insert(self, val):
      new_node = Tnode(val)
      self.insert_node(new_node)

    



  def insert_node(self, node):
    if self.root is None:
        self.root = node
    else:
        curr_node = self.root
        while True:
            if node.data < curr_node.data:
                if curr_node.left is None:
                    curr_node.left = node
                    break
                else:
                    curr_node = curr_node.left
            elif node.data > curr_node.data:
                if curr_node.right is None:
                    curr_node.right = node
                    break
                else:
                    curr_node = curr_node.right
            else:
                # node with the same value already exists, do nothing
                break





#For Deletion

  def Delete(self, val):
      if self.root is None:
          print("Value not found in tree")
      else:
          self.root = self.delete_node(self.root, val)
    
  def delete_node(self, node, val):
      if node is None:
          return node
      
      if val < node.data:
          node.left = self.delete_node(node.left, val)
      elif val > node.data:
          node.right = self.delete_node(node.right, val)
      else:
          if node.left is None:
              temp = node.right
              node = None
              return temp
          elif node.right is None:
              temp = node.left
              node = None
              return temp
          
          temp = self.get_min_value_node(node.right)
          node.data = temp.data
          node.right = self.delete_node(node.right, temp.data)
          
      return node



  def get_min_value_node(self, node):
      curr_node = node
      while curr_node.left is not None:
          curr_node = curr_node.left
      return curr_node




#Search function

  def Search(self, val):
    curr_node = self.root
    while curr_node is not None:
        if curr_node.data == val:
            return curr_node
        elif curr_node.data > val:
            curr_node = curr_node.left
        else:
            curr_node = curr_node.right
    return None




#Printing elements in ascending order

  def printInOrder(self, node=None):
      if node is None:
          node = self.root
      if node is not None:
          if node.left is not None:
              self.printInOrder(node.left)
          print(node.data, end=" ")
          if node.right is not None:
              self.printInOrder(node.right)



#BreadthFirst function

  def printBF(self):
      if self.root is None:
          return
      
      queue = deque()
      queue.append(self.root)
      
      while queue:
          level_size = len(queue)
          for i in range(level_size):
              curr_node = queue.popleft()
              print(curr_node.data, end=" ")
              if curr_node.left is not None:
                  queue.append(curr_node.left)
              if curr_node.right is not None:
                  queue.append(curr_node.right)
          print() 

