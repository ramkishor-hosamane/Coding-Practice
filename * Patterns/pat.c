#include <stdio.h>

int main(int argc, char const *argv[])
{
	int n=10;
	int i,j,k,p;
	int count=0;
	for(i=1;i<=n;i++)
	{
		//1st line
		if(i%2==1)
			{
				
				k = count + i;
				for (j = count + 1 ; j<=k; ++j)
				{

					printf("%d*", j);
					count++;
				}


			}
		else
			{
				j = count + i;
				k = j-i;
				for (; j >k; --j)
				{
						printf("%d*", j);
					count++;
				}


			}
		printf("\b \n");
	}
	return 0;
}