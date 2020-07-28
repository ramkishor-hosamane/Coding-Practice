#include <stdio.h>

int main(int argc, char const *argv[])
{
	int h1=10,h2=12;
	int m1=35,m2=38;

	int i,j,k;
	int hdiff = h2-h1;
	int mdiff;
	if(m2>=m1)
	{
		mdiff = m2-m1;
	}
	else
	{
		hdiff--;
		mdiff= 60 - (m1-m2);
	}
	printf("Time difference is  %d hours and %d minutes \n",hdiff,mdiff);

	return 0;
}