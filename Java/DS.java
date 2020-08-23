
class Node
{
	int data;
	Node right;
	Node left;

	Node(int val)
	{
		data = val;
		right = null;
		left = null;
	}
}


class BinaryTree
{
	Node root;
	BinaryTree()
	{
		root = null; 
	}

	void insert(int val)
	{
		if(root==null)
			{
				root =new  Node(val);
				return;
			}

		Node p =  root;
		Node q =  null;
		while(p!=null)
		{
			
			q = p;
				
			if(val >= p.data)
			{
				p=  p.right;
			}
			else
			{	
				p = p.left;
			}

		}

			if(val >= q.data)
			{
				q.right= new Node(val);
			}
			else
			{	
				q.left =new  Node(val);
			}

	}


	void inorder(Node node)
	{
		if(node==null)
			return;

		inorder(node.left);
		System.out.print(node.data+" ");
		inorder(node.right);

	}



}





public class DS
{
	public static void main(String[] args) {
		BinaryTree T = new BinaryTree();
		T.insert(10);
		T.insert(80);
		T.insert(90);
		T.insert(72);
		T.insert(95);
		T.inorder(T.root);

		
		
		
	}
}