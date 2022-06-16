# c0rrupt

## Description
We found this file. Recover the flag.
> 250 points

## Hints
Try fixing the [file](https://jupiter.challenges.picoctf.org/static/ab30fcb7d47364b4190a7d3d40edb551/mystery) header

## [*] - Step 1
The first thing I try open the file in a hex editor and also use the script `PCRT.py` to detect image error.

      python2 PCRT.py -v -i mystery

<div align="center">
<img src="https://user-images.githubusercontent.com/83420725/174030397-7f43c078-c770-44f6-94cd-c4d1d66070ed.png">
</div>
I see that the file header is same PNG signature. The first eight bytes of mystery file can be fixed to correct png signature.
<div align="center">
<img src="https://user-images.githubusercontent.com/83420725/174077710-8f96631e-d325-4e80-88f9-f37ada08e229.png">
Lets start with the PNG header
    
| Hex value | Ascii |  
|:--:   | :--: |   
| `89 50 4E 47` | `. P N G`|
 
</div>


## [*] - Step 2

<div align="center">
<img src="https://user-images.githubusercontent.com/83420725/174034677-4317d0b7-7c2b-4d7e-83b8-f1de20774aa7.png">
  Correcting the IHDR chunk 
  
    
| Hex value | Ascii |  
|:--:   | :--: |   
| `49 48 44 52` | `I H D R`|
  
</div>

## [*] - Step 3
      
      pngcheck mystery![mystery](https://user-images.githubusercontent.com/83420725/174083098-da864e71-7abe-4dff-a238-510eb02ff59c.png)

<div align="center">
  <img src="https://user-images.githubusercontent.com/83420725/174035622-5e413827-c72c-4fbc-98ab-d3ddda53848e.png">
  Correcting the IDAT chunk 
  
| Hex value | Ascii |  
|:--:   | :--: |   
| `49 44 41 54` | `I D A T`|
  

</div>


```
89504E47 0D0A1A0A 0000000D 49484452 0000066A 00000447 08020000 007C8BAB 78000000 01735247 4200AECE 1CE90000 00046741 4D410000 B18F0BFC 61050000 00097048 5973AA00 16250000 16250138 D82C8200 00FFA549 44415478 5EECBD3F 8E64CD71 BD2D8B20 20809041 830208D0 F9ED40A0 F36E407B 90238F1E D7208B3E B7C10D70 0374B503 AE416BF8 BEA8FBDC 3E7D2A22 336FDE5B 55DD3D3D
```
<div align="center">
<img src="https://user-images.githubusercontent.com/83420725/174083446-c7161566-da9b-4db6-84fa-aa1e58981d2b.png">
</div>

> picoCTF{c0rrupt10n_1847995}
