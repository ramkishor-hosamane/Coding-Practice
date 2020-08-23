


class Stack:
	def __init__(self):
		q1 = Queue()
		q2 = Queue()

	def push(self,val):
		q1.insert(val)


	def pop(self):
		if len(q1)==0:
			print("Stack underflow")
			return
		while len(q1)!=1:
			q2.insert(q1.remove())
		
		x = q1.remove()

		while len(q2)!=0:
			q1.insert(q2.remove())

		return x
