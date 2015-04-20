__author__ = 'freak'
import binascii


inputstr = '1c0111001f010100061a024b53535009181c'
xorstr = '686974207468652062756c6c277320657965'
outputexpected = '746865206b696420646f6e277420706c6179'


def fixedxor(str1, str2):
	hex2int1 = int(str1,16)
	hex2int2 = int(str2, 16)
	
	outint = hex2int1 ^ hex2int2	
	out = str(hex(outint))
	out = out.split('x')[1]
	
	return out[:-1]




if __name__ == '__main__':
	output = fixedxor(inputstr, xorstr)

	if outputexpected == output:
		print('success')
	else:
		print('failure...!!!')