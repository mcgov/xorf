import unittest
from math import *
"""chrxor: some flexible xor cipher functions
	the main function is chrxor, which takes two strings (of things, whatever really), 
	two functions and their arguments to create iterable lists out of those things,
	and two functions to process the individual members of those lists.
	The results are xor'd together and returned as a comma seperated string of values.	
		author: mcgov
		email: mgmcgove@buffalo.edu
"""


def chrxor(st1, st2, strf1, ar1, strf2, ar2, fun1, fun2):
	"""Takes two strings and applies a function to each charater in the string.
		Function is some function that takes characters and turns them into integers.
		This could be something to turn them into ascii order, or simply map them to another range of integers.
	"""
	st1 = strf1(st1, ar1) ##take these things and process them into an  iterable list of things.
	st2 = strf2(st2, ar2) ##ditto
	ret = None
	l1 = len(st1)-1
	l2 = len(st2)-1
	if l1 == l2 or l1 < l2: # if our key is longer than the plain, we just encipher as much
		ret = [None]* len(st1)  # as the plain will allow.
		#print ret
		for i in range(0, l1+1):
			#print i
			ret[i] =  fun1(st1[i] ) ^ fun2(st2[i]) 
	else: #otherwise you need to repeat the shorter key.
		j = 0 
		ret = [None]* len(st1)
		for i in range(0,l1+1):
			#print i , ": "+ st1[i] + " " + st2[j]
			ret[i] =  fun1(st1[i]) ^ fun2(st2[j]) 
			j += 1
			if j > l2:
				j = 0
	return ret


def ascii_str(str, ar):
	"""function to process a string.
	"""
	retstr = [None] * len(str)
	for i in range(0, len(str)):
		retstr[i] = str[i]
	return retstr

def ascii_ord(ch):
	"""function to process a character, just return the ascii order.
	"""
	return ord(ch)

def int_array(inpu, nullarg):
	"""function to process an array of integers, in this case that's what we want anyway."""
	return inpu

def integer(ch):
	"""process an integer. We want integers! Just return it"""
	return ch

def ld_hex_of_len(str, hxlen):
	"""load a string of hex characters, with 'hxlen' characters representing one integer.
	"""
	retstr = [None] *  ( len(str) / hxlen )   
	#print retstr
	i = 0
	for i in range(0, len(retstr)):
		retstr[i] = str[i*hxlen:(i*hxlen)+hxlen]

	#print retstr
	#print retstr
	return retstr

def hex_to_int(ch):
	"""function to process hex characters. Just convert to ints."""
	return int(ch,16)


def list_of_ints(st1, blk):
	"""function to process a comma seperated list of ints."""
	st1 = st1.split(',')
	return st1

def dec_str_to_int(ch):
	"""function to process a decimal string into an integer."""
	return int(ch)


"""============================================================="""
"""Some (useful?) Unit Tests++++++++++++++++++++++++++++++++++ """
class TestChrXor(unittest.TestCase):

  def test_equal_length(self):
	  test_str = chrxor("same", "same", ascii_str, None, ascii_str, None, ascii_ord, ascii_ord)
	  self.assertEquals(test_str , [0,0,0,0])

  def test_unequal_length(self):
	  test_str = chrxor("TES", "POGO", ascii_str, None, ascii_str, None, ascii_ord, ascii_ord)
	  xorstr = ( [ ord('T') ^ ord('P') , 
	  			  ord("E") ^ ord('O') ,
	              ord("S") ^ ord('G') ]  )

	  self.assertEquals(test_str , xorstr )

  def test_unequal_length2(self):
	  test_str = chrxor("TEST", "POG", ascii_str, None, ascii_str, None, ascii_ord, ascii_ord)
	  xorstr =(  [ ord('T') ^ ord('P') ,
	   ord("E") ^ ord('O') ,
	   ord("S") ^ ord('G') ,
	   ord("T") ^ ord('P') ] )
	  self.assertEquals(test_str , xorstr)

  def test_hex_str_dissasemble(self):
	 test = "9A3B"
	 result=  ld_hex_of_len(test, 2)
	 self.assert_(result == ['9A', '3B'] )
	 test = "9A3B55"
	 result = ld_hex_of_len(test, 3)
	 self.assert_(result == ['9A3', 'B55' ] )
	 test = "9A352ER"
	 result = ld_hex_of_len(test, 7)
	 self.assert_( result == ['9A352ER'] )

  def test_hex_conversion(self):
	 test = "6675636B"
	 result = chrxor(test, "pass", ld_hex_of_len, 2 , ascii_str, None, hex_to_int, ascii_ord  )
	 xorstr = ( [ ord('f') ^ ord('p') ,
	              ord("u") ^ ord('a') ,
	              ord("c") ^ ord('s') ,
	              ord("k") ^ ord('s') ] )
	 self.assertEquals(result , xorstr )


"""==============other stuff=================="""
def force_bin_length(strn, length):
	assert len(strn) < length
	while len(strn) != length:
		strn = '0' + strn
	return strn

def ascii_to_bin_arr( string, num ):
	string = ascii_str( string, None)
	for i in range(0,len(string)):
		string[i] = ascii_ord(string[i])
	for i in range(0,len(string)):
		string[i] = force_bin_length( bin(string[i])[2:], num ) 
	return string # which is now an array


if __name__ == "__main__":
	unittest.main()
