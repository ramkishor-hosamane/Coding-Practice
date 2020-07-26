'''
20. On the occasion of the “KarnatakaRajyotsava”, a school is preparing a dance recital with a team
comprising of primary school and High school students. One of the patterns in this dance recital
requires this team of students to form a circular pattern with each child holding the hand of the child
on its either side. The dance teacher formed the circular pattern with all the primary school students
being next to each other followed by the high school students with the last high school student holding
the hand of the first primary school student. However, on seeing the rehearsal the principal felt that
it would be better if the primary school students and the High school students are interleaved i.e
neither two primary school students nor two high school students will be next to each other in this
formation. Develop a program which will convert the first pattern to the second pattern assuming that
there are 5 primary school students and 5 high school students. Assume the names of the primary
school students are (a,b,c,d,e) and those of the High school students are (A,B,C,D,E) respectively.
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
			self.head.next = self.head
		else:
			node = Node(val)
			x = cur.next 
			cur.next =node 
			node.next = x
			self.head = node

	def display(self):
		cur = self.head.next
		while cur!=self.head:
			print(cur.data,end=" -> ")
			cur = cur.next
		print(self.head.data)


L = Linked_List()
primary_school = ['a','b','c','d','e']

high_school = ['A','B','C','D','E']

for x in primary_school:
	L.insert(x)
for x in high_school:
	L.insert(x)
'''
L.insert(10)
L.insert(20)
'''
L.display()

#Changing pattern
#find middle element
node2 = L.head.next
p =  l.head.next
