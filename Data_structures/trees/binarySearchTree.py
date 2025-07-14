class Node:
   def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data

   def insert(self, data):
      if self.data:
         if data > self.data:
            if self.right is None:
               self.right = Node(data)
            else:
               self.right.insert(data)
         else:
            if self.left is None:
               self.left = Node(data)
            else:
               self.left.insert(data)

   def inOrder(self):  # Left → Root → Right
      if self.left:
         self.left.inOrder()
      print(self.data)
      if self.right:
         self.right.inOrder()

   def postOrder(self):  # Left → Right → Root
      if self.left:
         self.left.postOrder()
      if self.right:
         self.right.postOrder()
      print(self.data)


# Create tree
root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)

print("Inorder Traversal:")
root.inOrder()

print("\nPostorder Traversal:")
root.postOrder()
