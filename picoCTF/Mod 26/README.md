# Mod 26
## Description
Cryptography can be easy, do you know what ROT13 is? `cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_jdJBFOXJ}`
> 10 points

## Hint
This can be solved online if you don't want to do it by hand!


```python 
#!/usr/bin/python3
from string import ascii_lowercase, ascii_uppercase

flag = 'cvpbPGS{arkg_gvzr_V\'yy_gel_2_ebhaqf_bs_ebg13_jdJBFOXJ}'
temp = ''
for f in flag:
    if f in ascii_lowercase:
        temp += ascii_lowercase[(ascii_lowercase.index(f) + 13) % 26]
    elif f in ascii_uppercase:
        temp += ascii_uppercase[(ascii_uppercase.index(f) + 13) % 26]
    else:
        temp += f
print (temp)
```
> picoCTF{next_time_I'll_try_2_rounds_of_rot13_wqWOSBKW}
