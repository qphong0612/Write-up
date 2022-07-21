import argparse
import itertools, io, os

from PIL import Image


KEY_LEN = 16

def parse_arguments():
    parser = argparse.ArgumentParser(description='This python script to solve JavaScript Kiddie!')
    parser.add_argument('-p', '--path', default='./bytes.txt', help='specify file contain a list of bytes')
    parser.add_argument('-o', '--out', default='./out', help='specify the place to store files out') 
    return parser.parse_args()

def generate_png(bytes_arr, key, path):
    if not os.path.isdir(path):
        raise Exception (f'The folder \033[36m{path}\033[0m doesn\'t exist!')
    # [ 0, 0, 0, 0, 0, 0, 0, 0 ... ]
    result = [0] * len (bytes_arr) 

    for i in range (KEY_LEN):
        shifter = int(key[i])
        for j in range (len(bytes_arr) // KEY_LEN):
            result[(j * KEY_LEN) + i] = bytes_arr[(((j + shifter) * KEY_LEN) % len(bytes_arr)) + i]
    
    img_bytes = io.BytesIO(bytes(result))
    try:
        img = Image.open(img_bytes)
        img.save(os.path.join(path, "{}.png".format(key)))
        print (f"[\033[36m*\033[0m] Key {key} is valid")
    except IOError:
        print (f"[\033[31m!\033[0m] Key {key} is invalid")



if __name__ == '__main__':
    args = parse_arguments()
    # a png file start with a magic signature of eight bytes (89 50 4E 47 0D 0A 1A 0A)
    # the next eight bytes is the first chunk that called IHDR and has length of 0x0D (00 00 00 0D 49 48 44 52): 4 bytes length and 4 byte of chunk type
    expected = [0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A, 0x00, 0x00, 0x00, 0x0D, 0x49, 0x48, 0x44, 0x52]
    
    shifters = []
    for i in range (KEY_LEN):
        shifters.append([])

    with open("bytes.txt") as f:
        # convert to list [128, 252, 182 ... ]
        bytes_arr = list(map(int, f.read().split(" ")))
        for i in range(KEY_LEN):
            for shifter in range(10):
                j = 0
                offset = (((j + shifter) * KEY_LEN) % len(bytes_arr)) + i
                if bytes_arr[offset] == expected[i]:
                    shifters[i].append(shifter)    

    for p in itertools.product(*shifters):
        key = "".join("{}".format(n) for n in p)
        generate_png(bytes_arr=bytes_arr,key=key, path=args.out)

