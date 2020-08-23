
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

	def display(self):
		cur = self.head
		while cur!=None:
			print(f"{cur.data} -> ",end="")
			cur = cur.next
		print("Null")

	def reverse(self):
		p = None
		q = self.head
		r = q.next
		while r!=None:
			q.next=p
			p=q
			q=r
			r= r.next
		q.next = p
		self.head = q

L=  Linked_List()
a = [10,20,30,40,50,60]
for x in a:
	L.insert(x)

L.display()
L.reverse()
L.display()
