'''
5. Convert a binary tree to its mirror
'''

class Node:
	def __init__(self,val):
		self.data = val
		self.right = None
		self.left = None
class BinaryTree:
	def __init__(self):
		self.root = None

	def inorder(self,node):
		if node!=None:
			self.inorder(node.left)
			print(node.data,end=" ")
			self.inorder(node.right)

	def display(self,mode="inorder"):
		if mode=="inorder":
			self.inorder(self.root)

		print()

	def convert_to_mirror(self):
		if self.root == None:
			return
		self.trav(self.root)

		
	def trav(self,node):
		if not node:
			return

		node.right ,node.left = node.left,node.right

		self.trav(node.left)
		self.trav(node.right)


#Driver program
#Building binary tree
b = BinaryTree()
b.root = Node(1)
b.root.left = Node(2)
b.root.right = Node(3)
b.root.left.left = Node(4)
b.root.left.right = Node(5)
b.root.left.right.left = Node(6)
b.root.right.right = Node(7)

b.display()
b.convert_to_mirror()
b.display()	


