# information

## Description 
Files can always be changed in a secret way. Can you find the flag? [cat.jpg](https://mercury.picoctf.net/static/b4d62f6e431dc8e563309ea8c33a06b3/cat.jpg)
> 10 points

## Hints

Look at the details of the file

Make sure to submit the flag as picoCTF{XXXXX}


<div align="center">
  <img src="https://user-images.githubusercontent.com/83420725/173191577-f0bdc071-4714-4cf3-86ce-4ebc6430b46e.png">
</div>

To see detail meta data use `exiftools`
    
      sudo apt install libimage-exiftool-perl
<div align="center">
  <img src="https://user-images.githubusercontent.com/83420725/173191919-f5c26a22-429d-4fce-9bdb-7ba4bcdeda05.png">
  <br>
  <br>
<img src="https://user-images.githubusercontent.com/83420725/173192051-2a771698-c805-4674-a229-40e9a0cd10e3.png">

</div>

> picoCTF{the_m3tadata_1s_modified}  
