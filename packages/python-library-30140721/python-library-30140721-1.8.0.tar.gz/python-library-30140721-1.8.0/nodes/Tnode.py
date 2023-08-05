class Tnode:

  #Initilaizing data members
    def __init__(self, data=None, balance=None, parent=None, left=None, right=None):
        self.data = data
        self.balance = balance
        self.parent = parent
        self.left = left
        self.right = right


#Getters and setters of all data members
    def getData(self):
        return self.data

    def setData(self, data):
        self.data = data

    def getBalance(self):
        return self.balance

    def setBalance(self, balance):
        self.balance = balance

    def getParent(self):
        return self.parent

    def setParent(self, parent):
        self.parent = parent

    def getLeft(self):
        return self.left

    def setLeft(self, left):
        self.left = left

    def getRight(self):
        return self.right

    def setRight(self, right):
        self.right = right


#Print method --> prints node information in a user friendly format
    def print(self):
        print("Data: ", self.data, ", Balance: ", self.balance, "Parent: ", self.parent, "Left node: ", self.left, "Right node: ", self.right)


#toString Method --> returns data as a string
    def toString(self):
        return str(self.data)



#Default constructor
    def default_constructor(cls):
        return cls()



#Overload Constructor
    def overload_constructor(cls, data, balance, P, L, R):
        return cls(data, balance, P, L, R)


