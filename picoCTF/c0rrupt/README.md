# c0rrupt

## Description
We found this file. Recover the flag.
> 250 points

## Hints
Try fixing the [file](https://jupiter.challenges.picoctf.org/static/ab30fcb7d47364b4190a7d3d40edb551/mystery) header

## [*] - Step 1
    
      python2 PCRT.py -v -i mystery

<div align="center">
  Lets start with the PNG header
  
| Hex value | Ascii |  
|:--:   | :--: |   
| `89 50 4E 47` | `. P N G`|
  
<img src="https://user-images.githubusercontent.com/83420725/174030397-7f43c078-c770-44f6-94cd-c4d1d66070ed.png">
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
      
      pngcheck mystery
<div align="center">
  <img src="https://user-images.githubusercontent.com/83420725/174035622-5e413827-c72c-4fbc-98ab-d3ddda53848e.png">
  Correcting the IDAT chunk 
  
| Hex value | Ascii |  
|:--:   | :--: |   
| `49 44 41 54` | `I D A T`|
  

</div>


