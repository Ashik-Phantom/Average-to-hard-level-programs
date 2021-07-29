//find pattern yourself
/*
ip
hello world
op
lhnmo artmd
*/

#include <stdio.h>
int main()
{
	 char str[100];
	 scanf("%[^\n]s",str);
	 int len, i, count = 0;
	 for(len=0;str[len];len++);
	 for(i=len-1;i>=0;i--)
	 {
		 if(str[i]==' ')
			 count = 0;
		 else
		 {
			 if(str[i]+count > 122)
				 str[i] = str[i] + count -26;
			 else
				 str[i] = str[i] + count;
			 count++;
		 }
	 }
	 for(i=0;i<len;i++)
	 {
		 printf("%c",str[i]);
	 }
}
