__author__ = 'freak'
import string

inputstr = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
hexlist = "0123456789abcdef"
charlist = string.printable 

#'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
#How?
#Devise some method for "scoring" a piece of English plaintext. Character frequency is a good metric.
#Evaluate each output and choose the one with the best score.
hexxor = []
charxor = []
scores1 = {}
scores2 = {}

def decodehex():
    for c in range(0, 15):
        a = ''
        out = [a + str(unichr(int(hexlist[c], 16) ^ int(inputstr[i], 16))) for i in range(0, len(inputstr)-1)]
        hexxor.append((''.join(out)))
    print(hexxor)


def decodeascii():
    hextoascii = inputstr.decode("hex")
    for c in range(0, len(charlist)-1):
        a = ''
        out = [a + str(unichr(ord(charlist[c]) ^ int(inputstr[i], 16))) for i in range(0, len(inputstr)-1)]
        charxor.append(''.join(out))

    print(charxor)


def score1():
    for s in charxor:
        for c in charlist:
            if c not in scores1.keys():
                scores1[c] = s.count(c)

            elif s.count(c) > scores1[c]:
                scores1[c] = s.count(c)

    print(scores1)
    print(max(scores1, key=scores1.get))


def score2():
    for i in range(0,len(charlist)-1):
        c = charlist[i]
        scores2[c] = charxor[i].count(c)

    print(scores2)
    print(max(scores2, key=scores2.get))

if __name__ == '__main__':
    #decodehex()
    decodeascii()
    score1()
    score2()
