__author__ = 'freak'
import string

inputstr = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
hexlist = "0123456789abcdef"
charlist = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
#How?
#Devise some method for "scoring" a piece of English plaintext. Character frequency is a good metric.
#Evaluate each output and choose the one with the best score.
hexxor = []
charxor = []

def decodehex():
    for c in range(0, 15):
        a = ''
        out = [a + str(unichr(int(hexlist[c], 16) ^ int(inputstr[i], 16))) for i in range(0, len(inputstr)-1)]
        hexxor.append((''.join(out)))
        

def decodeascii():
    hextoascii = inputstr.decode("hex")
    for c in range(0, len(charlist)-1):
        a = ''
        out = [a + str(unichr(ord(charlist[c]) ^ int(inputstr[i], 16))) for i in range(0, len(inputstr)-1)]
        charxor.append(''.join(out))



def score():
    for s in charxor:
        pass
    pass

if __name__ == '__main__':
    decodehex()
    decodeascii()
    #print(hexxor)
    print(charxor)

