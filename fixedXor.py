__author__ = 'freak'
import binascii


inputstr = '1c0111001f010100061a024b53535009181c'
xorstr = '686974207468652062756c6c277320657965'
outputexpected = '746865206b696420646f6e277420706c6179'


def fixedxor(str1, str2):
	hextoascii = str1.decode("hex")

	ip = binascii.unhexlify(str1)
	xorip = binascii.unhexlify(str2)
  	out = binascii.b2a_uu(ip ^ xorip)
  	print(out)
  	return out




if __name__ == '__main__':
	output = fixedxor(inputstr, xorstr)

	if outputexpected == output:
		print('success')
	else:
		print('failure...!!!')


	