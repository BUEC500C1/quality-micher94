# Michaela Reardon
# EC500: Homework 1

#import numpy as np
import math

def convert_numeral(num):
	romans=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
	letters=['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']

	# Tests for inputs that will cause an error: negative numbers, strings, or floating point
	teststr = str(num)
	for charac in teststr:
		if not charac.isnumeric():
			return False
		#https://www.programiz.com/python-programming/methods/string/isalpha
		if charac.isalpha() == True:
			return False
		
	# Calculates the roman numeral
	j=0
	remainder=100
	ans = ''
	while remainder>1 and num>0:
		rem = num/romans[j]
		if rem<1:
			j=j+1
		else:
			remainder=rem
			num = num-(romans[j]*math.floor(rem))
			for i in range(0,math.floor(rem)):
				ans = ans + letters[j]
	return ans;


