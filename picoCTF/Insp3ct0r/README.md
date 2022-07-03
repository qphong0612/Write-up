# Insp3ct0r

## Desciption
Kishor Balan tipped us off that the following code may need inspection: https://jupiter.challenges.picoctf.org/problem/41511/ (link) or http://jupiter.challenges.picoctf.org:41511
> 50 points
## Hint
1. How do you inspect web code on a browser?
2. There's 3 parts

## [*] - Step 1
Inspect to view the source code and I get the one third of the flag `picoCTF{tru3_d3`
<div align='center'>
     <img src='https://user-images.githubusercontent.com/83420725/177031535-eabac237-a695-4ff1-9589-9c774608443a.png'>
</div>
      
      <!-- Html is neat. Anyways have 1/3 of the flag: picoCTF{tru3_d3 -->

## [*] - Step 2
The second part of the flag comes from the referenced `mycss.css` file
    
      /* You need CSS to make pretty pages. Here's part 2/3 of the flag: t3ct1ve_0r_ju5t */

## [*] - Step 3
The last part comes from the `myjs.js` file
  
    /* Javascript sure is neat. Anyways part 3/3 of the flag: _lucky?832b0699} */

> picoCTF{tru3_d3t3ct1ve_0r_ju5t_lucky?832b0699}
