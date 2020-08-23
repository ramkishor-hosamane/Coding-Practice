#include <stdio.h>

int main(int argc, char const *argv[])
{
	int n=9;
	int s=1;
	int i,j,r,q,space,count=1;
	int k=1;
	for(i=1;i<=n;i++)
	{	
		for(j=1;j<=k;j++)
		{
			printf("%d",s);
		}
		k++;
		s++;
		printf("\n");
	}
	s--;
	k--;
	for(i=1;i<=n;i++)
	{	
		for(j=1;j<=k;j++)
		{
			printf("%d",s);
		}
		k--;
		s--;
		printf("\n");
	}





	return 0;
}