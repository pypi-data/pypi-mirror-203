class TNode:
    def __init__(self, data=0, balance=0, parent=None, left=None, right=None):
        self.data = data
        self.balance = balance
        self.left = left
        self.right = right
        self.parent = parent

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def set_balance(self, balance):
        self.balance = balance

    def get_balance(self):
        return self.balance

    def set_left(self, left):
        self.left = left

    def get_left(self):
        return self.left

    def set_right(self, right):
        self.right = right

    def get_right(self):
        return self.right

    def set_parent(self, parent):
        self.parent = parent

    def get_parent(self):
        return self.parent

    def print_info(self):
        print("Data:", self.data)
        print("Balance:", self.balance)
        print("Left Node:", self.left)
        print("Right Node:", self.right)
        print("Parent Node:", self.parent)

    def __str__(self):
        return str(self.data)
