#include<stdio.h>
#include<stdlib.h>

void call_me(){
	system("sh");//open a shell
}

int main(){

	char buf[0x30];
	gets(buf);
	
	return 0;
}
