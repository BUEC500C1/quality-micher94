from Converter import convert_numeral 
import pytest

def test_values():
	#convert_numeral(2150)
	
	assert convert_numeral(13) == "XIII"
	assert convert_numeral(163) == "CLXIII"
	assert convert_numeral(862) == "DCCCLXII"
	assert convert_numeral(2150) == "MMCL"
	assert convert_numeral(2123) == "MMCXXIII"
	assert convert_numeral(-1023) == False
	assert convert_numeral(1.2) == False
	assert convert_numeral('word') == False

