/*
'''

Find the occurrences of a digit d in a given range from 0 to n

'''
*/
class Occurence
{	
	static int get_count(int n,int d)
	{
		int count=0;
		int r;
		while(n!=0)
		{
			r = n % 10;
			if(r==d)
			{
				count++;

			}
			n = n/10;
		}
		return count;
	}
	static int get_occurence(int n,int d)
	{
		int count=0;
		for(int i=1;i<=n;i++)
		{
			count+= get_count(i,d);
		}

		return count;
	}

	public static void main(String[] args) {
		
		int d = 2;
		int n = 22;
		int res = get_occurence(n,d);

		System.out.println(res);
	}
}
