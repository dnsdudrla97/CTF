#include <stdio.h>
#include <stdlib.h>
#include <memory.h>
#include <sys/mman.h>

#define TEST_DATA_FILE		"testData"
#define TEST_DATA_SIZE		5
#define TEST_VECTOR_SIZE	10

//240 bytes
unsigned long long shellcode(unsigned long long* weight, int* percent)
{
	int i;
	unsigned long long temp = 0;
	unsigned long long sum = 0;
	unsigned long long remain;

	for (i = 0; i < TEST_VECTOR_SIZE; i++)
	{
		temp = weight[i] * percent[i];
		sum += temp / 100;
		remain += temp % 100;
	}
	return sum + (remain / 100);
}
/*
//164 bytes
unsigned long long shellcode(unsigned long long* weight, int* percent)
{
	int i;
	__int128 sum = 0;

	for (i = 0; i < TEST_VECTOR_SIZE; i++)
	{
		sum += (__int128)(weight[i] * percent[i]);
	}
	return (unsigned long long)(sum / 100);
}
*/

int main(int argc, char** argv)
{
	int i, j;
	unsigned long long weight[TEST_VECTOR_SIZE];
	int percent[TEST_VECTOR_SIZE];
	unsigned long long ans1, ans2;

	char buf[64];
	int sclen;
	char* mem = (char*)mmap(0, 512,7, 34, -1, 0LL);
	FILE* fp;

	//check arguments
	if (argc < 2)
	{
		printf("Usage: %s your_shellcode_file\n", argv[0]);
		printf(" example: %s ./payload (when your shellcode is stored in a file named 'payload'.)\n", argv[0]);
		printf(" Please keep in mind that this file is provided only for test.\n");
		printf(" The binary in the server, for grading, is much more strict than this.\n\n");
		printf("To submit your shellcode, send it as a base64 encoded form.\n");
		printf(" example: echo `base64 -w 0 your_shellcode_file` | nc expectedvalue.sstf.site 1337;\n\n");
		exit(-1);
	}

	//read shellcode file
	fp = fopen(argv[1], "r");
	sclen = fread(mem, 1, 256, fp);
	fclose(fp);

	//check payload
	if (sclen > 128)
	{
		printf("[Warning]Too long shellcode (max 128 bytes)\n");
		printf("[Warning]Your shellcode cannot pass the server's validation.\n");
	}

	//read test data file
	fp = fopen(TEST_DATA_FILE, "r");
	if (fp == NULL)
	{
		printf("[Err]Cannot find " TEST_DATA_FILE ".\n");
		exit(-1);
	}

	//test payload
	for (i = 0; i < TEST_DATA_SIZE; i++)
	{
		fgets(buf, 64, fp);
		buf[19] = 0;
		ans1 = strtoll(buf + 21, NULL, 10);

		//read test vectors
		FILE* tv = fopen(buf, "r");
		for (j = 0; j < TEST_VECTOR_SIZE; j++)
		{
			fgets(buf, 64, tv);
			weight[j] = strtoll(buf, NULL, 10);
			fgets(buf, 64, tv);
			percent[j] = atoi(buf);
		}
		fclose(tv);

		//call your shellcode
		ans2 = (*(unsigned long long (*)(unsigned long long* weight, int* percent))mem)(weight, percent);
		if (ans1 == ans2)
			printf("Success!\n");
		else
			printf("Fail %llu %llu\n", ans1, ans2);
	}
	fclose(fp);

	return 0;
}
