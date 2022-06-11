# GET aHEAD

## Description
Find the flag being held on this server to get ahead of the competition http://mercury.picoctf.net:21939/ 
> 20 points

## Hints
Maybe you have more than 2 choices

Check out tools like Burpsuite to modify your requests and look at the responses

<div align="center">
  <img src="https://user-images.githubusercontent.com/83420725/173170572-df45e673-1961-4d28-b4ae-a29fc5a7c9f8.png">
</div>

Burp suite

       HEAD /index.php HTTP/1.1

Or
      
       curl -I HEAD -i http://mercury.picoctf.net:53554/index.php


Preference: https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods

> picoCTF{r3j3ct_th3_du4l1ty_6ef27873}
