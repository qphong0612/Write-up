# Transformation
## Description
I wonder what this really is... enc `''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])`
> 20 points

## Hint 
You may find some decoders online


``` python
#!/bin/usr/python3
enc = open('enc').read()
temp = ''
for c in enc:
    temp += hex(ord(c)).lstrip('0x')
    
print(bytes.fromhex(temp).decode('utf-8'))

```
> picoCTF{16_bits_inst34d_of_8_75d4898b}
 
