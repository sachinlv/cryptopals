__author__ = 'freak'
import string

input_string = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"

#How?
#Devise some method for "scoring" a piece of English plaintext. Character frequency is a good metric.
#Evaluate each output and choose the one with the best score.
bin_str = ''
key_str = string.ascii_letters + string.digits #'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

for char in input_string:
    bin_str = bin_str + bin(int(char, 16)).split('b')[1]

#print(len(bin_str) % 7)
if len(bin_str) % 7 != 0:
    bin_str = bin_str.ljust(len(bin_str) + (7 - len(bin_str) % 7), '0')

bin_str_tmp = bin_str
for key in key_str:
    bin_str = bin_str_tmp
    tmp = ''
    char_str = ''
    while len(bin_str) > 0:
        tmp = bin_str[0:6]
        bin_str = bin_str[6:]
        tmp = int(tmp, 2) ^ ord(key)
        char_str = char_str + chr(tmp)


    print(char_str)