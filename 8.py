'''
8.Reverse a linked list in groups of size k
'''

class Node:
	def __init__(self,val=None):
		self.data = val
		self.next = None		
class Linked_List:
	def __init__(self):
		self.head = None

	def insert(self,val):
		cur = self.head
		if cur==None:
			self.head = Node(val)
		else:
			while cur.next!=None:
				cur = cur.next

			cur.next = Node(val)

	def reverse(self,K):
		past = None
		present = self.head
		future = present.next
		while future:
			count = 0
			while future!=None and count<K:
				present.next = past
				past = present
				present = future
				future = future.next
				count += 1

		present.next = past


		self.head = past

	def display(self):
		cur = self.head
		while cur:
			print(cur.data,end=" -> ")
			cur = cur.next

		print("None")

L = Linked_List()
for i in range(1,9):
	L.insert(i)

L.display()
L.reverse(3)
L.display()