#include <stdio.h>

int main(int argc, char const *argv[])
{
	int a[20]={2,9,2,9,8,9};
	int n = 6;
	int i = n-1;
	a[i] +=1;
	if (a[i]>9)
		{
			a[i]=0;
			i--;
			while (i>0)
			{
				a[i]+=1;
				if(a[i]<10)
					break;
				else
					a[i]=0;
				i--;
			}

		}
	for(i=0;i<n;i++)
		printf("%d\t",a[i]);

	return 0;
}