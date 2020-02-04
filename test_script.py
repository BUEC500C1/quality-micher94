from Converter import convert_numeral 
import pytest

#don't know why the pytest is showing up as no tests run

def test_values():
	#convert_numeral(2150)
	assert convert_numeral(2150) == "MMCL"
	assert convert_numeral(10123)
	assert convert_numeral(-1023)
	assert convert_numeral(1.2)

