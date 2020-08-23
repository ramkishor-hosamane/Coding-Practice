#include <stdio.h>

int main(int argc, char const *argv[])
{
	int n=10;
	int k=1,num=n;
	int i,j,r,q,space,count=1;
	for(i=1;i<=n;i++)
	{	
		//spaces
		for(space=1;space<=2*i-2;space++)
		{
			printf(" ");
		}
		q=  count+num;
		for(j=count;j<q;j++)
		{
			printf("%d*",j);
			count++;
		}

		for(j=1;j<=num;j++)
		{	
			printf("%d*",k+num*num);
			k++;
		}
		
		printf("\b \n");
		num--;
	}




	return 0;
}