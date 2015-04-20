__author__ = 'freak'
import string

inptutstr = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
hexlist = "0123456789abcdef"
charlist = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
#How?
#Devise some method for "scoring" a piece of English plaintext. Character frequency is a good metric.
#Evaluate each output and choose the one with the best score.
hexxor = []
charxor = []

def decodehex():
    for c in range(0,15):
        a = ''
        out = [a + str(int(hexlist[c],16) ^ int(inptutstr[i], 16)) for i in range(0,len(inptutstr)-1)]
        hexxor.append((''.join(out)))
        


def decodeascii():
    for c in range(0, len(charlist)-1):
        a = ''
        out = [a + str(ord(charlist[c]) ^ int(inptutstr[i], 16)) for i in range(0,len(inptutstr)-1)]
        charxor.append(''.join(out))




if __name__ == '__main__':
    decodehex()
    decodeascii()
    print(hexxor)