# Who are you?

## Description
Let me in. Let me iiiiiiinnnnnnnnnnnnnnnnnnnn http://mercury.picoctf.net:1270/
> 100 points

## Hints
It ain't much, but it's an RFC https://tools.ietf.org/html/rfc2616

[*] - Step 1: 
    
      User-Agent: PicoBrowser
[*] - Step 2:
    
      Referer: http://mercury.picoctf.net:1270/
[*] - Step 3:
      
      Date: Wed, 21 Oct 2015 07:28:00 GMT
      
[*] - Step 4: 
      
      DNT: 1 #DNThttps://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/DNT
[*] - Step 5:
    
      X-Forwarded-For: 103.177.248.12 #Sweden ip addr
[*] - Step 6:
      
      Accept-Language: sv

> picoCTF{http_h34d3rs_v3ry_c0Ol_much_w0w_f56f58a5}

## Preference
Referer header: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Referer

Date header: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Date

DNT header: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/DNT

X-Forwarded-For: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Forwarded-For
      
      
      
