'''
Given a list of 10 numbers. Write an algorithm for creating another list of the same set of 10
numbers such that the numbers which occupy the “odd” positions in the first list are put in the first
half of the new list and those which occupy the “even” positions in the first list are put in the second
half of the new list without altering their relative order.
'''

class Node:
	def __init__(self,val = None):
		self.data = val
		self.next = None
		self.prev = None


class DoublyLinkedList:
	def __init__():
		self.head = None


	def insert(self,value):
		node = self.head
		if not node:
			self.head = Node(val)
			self.head.next = None
			self.head.prev = None
			return

		while node.next!=None:
			node = node.next
		node_to_add = Node(value)
		node.next = node_to_add
		node_to_add.prev = node
		node_to_add.next = None




def solve(L):
	Result = DoublyLinkedList()
	odd = L.head
	even = L.head.next
	
	while odd!=None:
		Result.insert(odd.data)
	while even!=None:
		Result.insert(even.data)

	return Result

