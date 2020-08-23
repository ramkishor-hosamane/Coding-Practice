'''
Find second largest element in a binary search tree
'''
class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.data = val

class BinarySearchTree:
    def __init__(self):
        self.root = None


    def insert(self, val):

        if(self.root == None):
            self.root = Node(val)
            return

        p = self.root
        q = None
        while p!=None:
            q = p
            if val < p.data:
                p = p.left
            else:
                p = p.right

                    
        if val < q.data:
            q.left = Node(val)
        else:
            q.right = Node(val)




    def find_largest(self,node):
        while node.right:
            node = node.right

        return node.data

    def secondLargest(self): 
        if self.root==None or (self.root.left is None and self.root.right is None):
            print("Invalid case")
            return

        current = self.root
        while current:
            #Case 1: if there is no right subtree then result will be the right most element of left subtree
            if not current.right and current.left:
                return self.find_largest(current.left)

            #Case 2: if right child is leafnode then current node is the result
            if not current.right.left and not current.right.right:
                return current.data   
            current = current.right      


  
#         50  
#       /    \  
#     30      70  
#     / \    / \  
#    20 40  60 80 

B = BinarySearchTree()
B.insert(50)  
B.insert(30) 
B.insert(20)  
B.insert(40)  
B.insert(70)  
B.insert(60)  
B.insert(80)  
print(B.secondLargest())  


