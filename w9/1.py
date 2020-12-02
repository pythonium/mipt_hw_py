class BinTree:
    """docstring for BinTree."""

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return f"{self.data}"

    def add(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = BinTree(data)
                else:
                    self.left.add(data)
            elif data > self.data:
                if self.right is None:
                    self.right = BinTree(data)
                else:
                    self.right.add(data)
        else:
            self.data = data

    def __iter__(self):
        if self.left:
            for leaf in self.left:
                yield leaf
        yield self
        if self.right:
            for leaf in self.right:
                yield leaf

'''
a = BinTree(12)
a.add(6)
a.add(14)
a.add(3)

b = iter(a)
print(next(b))
print(next(b))
print(next(b))
print(next(b))
'''
