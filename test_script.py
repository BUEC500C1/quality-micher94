from Converter import convert_numeral 
import pytest

#don't know why the pytest is showing up as no tests run

def main():
	#convert_numeral(2150)
	assert convert_numeral(2150) == "MMCL"
	#convert_numeral(10123)
	#convert_numeral(-1023)
	#convert_numeral(1.2)
