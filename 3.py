'''
3. Find the middle element of the linked lists in a single pass (you can only traverse the
list once).
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

	def get_middle_element(self):
		turtle = self.head
		rabbit = self.head

		if turtle.next == None:
			while rabbit != None:
				rabbit = rabbit.next.next
				turtle = turtle.next
		
		return turtle.data



