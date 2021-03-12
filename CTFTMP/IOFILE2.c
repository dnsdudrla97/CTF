#include <stdio.h>
int main()
{
	char buf[128];
	int ret;
	FILE *fp;
	
	strcpy(buf, "AAAA");
	fp = fopen("testfile","r");
	fread(buf, 1, 128, fp);
	printf("%s",buf);
	fclose(fp);
}