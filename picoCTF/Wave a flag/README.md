# Wave a flag

## Description
Can you invoke help flags for a tool or binary? [This program]() has extraordinarily helpful information...
> 10 points

## Hint
This program will only work in the webshell or another Linux computer.

To get the file accessible in your shell, enter the following in the Terminal prompt: `$ wget https://mercury.picoctf.net/static/beec4f433e5ee5bfcd71bba8d5863faf/warm`

Run this program by entering the following in the Terminal prompt: `$ ./warm`, but you'll first have to make it executable with `$ chmod +x warm`

-h and --help are the most common arguments to give to programs to get more information from them!

Not every program implements help features like -h and --help.

    wget https://mercury.picoctf.net/static/beec4f433e5ee5bfcd71bba8d5863faf/warm
    chmod +x warm
    ./warm
    ./warm -h

> picoCTF{b1scu1ts_4nd_gr4vy_616f7182}
