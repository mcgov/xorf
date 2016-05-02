import chrxor as x
import sys
#de-super-encipher
#author: mcgov   contact mgmcgove@buffalo.edu

def dse( inp ):
	"""de-super-encipher an output from se.py. Pipe input from stdin, args should be the keys."""
	#print sys.argv[1]
	inp = x.chrxor( inp, sys.argv[1], x.ld_hex_of_len, 2, x.ascii_str, None, x.hex_to_int, x.ascii_ord)
	#print inp
	for i in range( 2, len(sys.argv)):
		#print i
		inp = x.chrxor( inp, sys.argv[i], x.int_array, None, x.ascii_str, None, x.integer, x.ascii_ord) 
	return inp

if __name__ == "__main__":
    instr = sys.stdin.read()
    result =  dse(instr)
    ret_str = ""
    for i in result:
    	ret_str += chr(i)
    print(ret_str)
