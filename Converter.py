# Michaela Reardon
# EC500: Homework 1

#import numpy as np
import math

def convert_numeral(num):
	romans=[1000,500,100,50,10,5,1]
	letters=['M','D','C','L','X','V','I']

	teststr = str(num)
	for charac in teststr:
		if charac == '.' or charac == '-':
			return 0

	j=0
	remainder=100
	ans = ''
	while remainder>1 and num>0:
		# print('j is', j)
		# print('numeral is', romans[j])
		rem = num/romans[j]
		# print('dividend is', rem)
		if rem<1:
			# print('not me')
			j=j+1
		else:
			remainder=rem
			# print('remainder is', rem)
			# print('og number is', num)
			num = num-(romans[j]*math.floor(rem))
			for i in range(0,math.floor(rem)):
				ans = ans + letters[j]
			# print('the new number is', num)
			# print('the roman numeral is', ans)
	return ans;


def main():
	convert_numeral(2150)

if __name__ == '__main__':
    main()
