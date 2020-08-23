class Queue:
	def __init__(self):
		self.items = []

	def size(self):
		return len(self.items)

	def insert(self,val):
		self.items.append(val)

	def remove(self):
		if self.size()==0:
			print("Queue is empty")
		else:
			return self.items.pop(0)