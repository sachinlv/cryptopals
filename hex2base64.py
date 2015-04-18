__author__ = 'freak'
import base64

input_string = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
output_expected = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'

hextoascii = input_string.decode("hex")
output = base64.b64encode(hextoascii)

if output_expected == output:
	print('encode success')
else:
	print('conversion failure...!!!')
