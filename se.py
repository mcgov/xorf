import binascii
import sys
import chrxor as x

##Super Encipher
##author: mcgov,  contact mgmcgove@buffalo.edu


inp = sys.stdin.read()

def se(plain, keys):
	"""super encipher with an arbitrary amount of keys"""
	plain = x.chrxor( plain, keys[1], x.ascii_str, None, x.ascii_str, None, x.ascii_ord, x.ascii_ord  )
	
	for i in range( 2, len(keys)):
		plain = x.chrxor( plain, keys[i], x.int_array, None, x.ascii_str, None, x.dec_str_to_int, x.ascii_ord  )
		#print "i: " + str(i) + " " + print_as_hex(plain)
	return plain

def print_as_hex(list):
	outp = ""
	for i in list:
		hstr = hex(i)[2:]
		if len(hstr) == 1:
			hstr = '0'+hstr
		outp += hstr
	return outp


stgone = se( inp, sys.argv )
#print stgone
sys.stdout.write( print_as_hex(stgone) + '\n')
