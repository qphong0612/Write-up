<h1 align="center"> Memory Forensics Challenge </h1>


# Challenge one
## [*] - Step 1:
    
     python2  vol.py -f Challenge.raw imageinfo
<div align="center">
  <img src="https://user-images.githubusercontent.com/83420725/173192576-dd0887f9-bb62-49ac-9945-54a201b081ab.png">
</div>

## [*] - Step 2:
      
      python2 vol.py -f Challenge.raw --profile=Win7SP1x86 pslist 
<div align="center">
  <img src="https://user-images.githubusercontent.com/83420725/173192730-4f87c98f-6f9e-4f8e-bf60-f9c1a413f224.png">
</div>

## [*] - Step 3:
      
      python2 vol.py -f Challenge.raw --profile=Win7SP1x86 cmdscan
<div align="center">
  <img src="https://user-images.githubusercontent.com/83420725/173192878-fc0332ff-082b-4616-9e77-7e4b6e4afc14.png">
</div>   

## [*] - Step 4:
      
      python2 vol.py -f Challenge.raw --profile=Win7SP1x86 consoles
<div align="center">
  <img src="https://user-images.githubusercontent.com/83420725/173192993-111b381b-d521-4e30-8e61-f28707871871.png">
</div>   

## [*] - Step 5:
To view the environment variables in a system, use the `envars` plugin
     
     python2 vol.py -f challenge/Challenge.raw --profile=Win7SP1x86 envars
<div align="center">
  <img src="https://user-images.githubusercontent.com/83420725/173193481-b42151a6-69c9-4f4c-b17e-d00415489e74.png">
</div>

The string certain in `C:\Python27\python.exe C:\Users\hello\Desktop\demon.py.txt` is `335d366f5d6031767631707f`

```python3
a = bytes.fromhex('335d366f5d6031767631707f').decode('utf-8')

for i in range(0, 255):
    b = ""
    for j in a:
        b = b + chr(ord(j) ^ i)
    if b[-1] == '}':
        print(b)
        break
```

## [*] - Step 6:

      python2 vol.py -f challenge/Challenge.raw --profile=Win7SP1x86 hashdump

<div align="center">
  <img src="https://user-images.githubusercontent.com/83420725/173194203-1c4fc114-4b7c-48a1-842d-4dd90f55c843.png">
</div>
    


> flag{you_are_good_but1_4m_b3tt3r}

Link for challenge [here](https://github.com/stuxnet999/MemLabs#resources-rocket)




