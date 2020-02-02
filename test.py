from Converter.py import convert_numeral 
import pytest

def first_test():
	#convert_numeral(2150)
	assert convert_numeral(2150) == "MMCL"
	#convert_numeral(10123)
	#convert_numeral(-1023)
	#convert_numeral(1.2)
