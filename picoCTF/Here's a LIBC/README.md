# Here's a LIBC
## Description
I am once again asking for you to pwn this binary vuln libc.so.6 Makefile nc mercury.picoctf.net 62289

> 90 points

## Hint
PWNTools has a lot of useful features for getting offsets.

``` makefile
all:
        gcc -Xlinker -rpath=./ -m64 -fno-stack-protector -no-pie -o vuln vuln.c

clean:
        rm vuln
```

```console
┌──(kali㉿kali)-[/tmp/herelibc]
└─$ checksec vuln 
[*] '/tmp/herelibc/vuln'
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      No PIE (0x400000)
    RUNPATH:  b'./'
```

```note
picoCTF{1_<3_sm4sh_st4cking_  8652b55904cb7c}
```
