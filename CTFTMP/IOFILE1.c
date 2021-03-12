#include <stdio.h>
#include <unistd.h>
#include <string.h>
int main()
{
	FILE *fp;
	char buf[128] = {0, };

	strcpy(buf, "_IO_File TEST\n");
	fp = fopen("testfile","wb");
	fwrite(buf, 1, strlen(buf), fp);
	fclose(fp);
	return 0;
}