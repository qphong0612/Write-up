# ELF x86 - Stack buffer overflow basic 4
Get challenge: https://www.root-me.org/en/Challenges/App-System/ELF-x86-Stack-buffer-overflow-basic-4

```c
int main(void)
{
  struct EnvInfo env;
   
  printf("[+] Getting env...\n");
  env = GetEnv();
   
  printf("HOME     = %s\n", env.home);
  printf("USERNAME = %s\n", env.username);
  printf("SHELL    = %s\n", env.shell);
  printf("PATH     = %s\n", env.path);
   
  return 0;  
}
```

