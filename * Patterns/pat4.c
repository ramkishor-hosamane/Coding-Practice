#include <stdio.h>

int main(int argc, char const *argv[])
{
	int n=6;
	int s=1;
	int i,j,r,q,space,count=1;
	int k=1;
	for(i=1;i<=n;i++)
	{	
		for(j=1;j<=i;j++)
		{
			printf("%d ",k++);
		}
		
		printf("\n");
	}





	return 0;
}