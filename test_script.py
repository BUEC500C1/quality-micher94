from Converter import convert_numeral 
import pytest

#don't know why the pytest is showing up as no tests run

def test_values():
	#convert_numeral(2150)
	assert convert_numeral(2150) == "MMCL"
	assert convert_numeral(2123) == ""MMCXXIII"
	assert convert_numeral(-1023) == 0
	assert convert_numeral(1.2) == 0

