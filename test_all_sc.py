from Converter import convert_numeral

def test_uniquename():
    assert convert_numeral(1) == 'I'
    assert convert_numeral(4) == 'IV'
    assert convert_numeral(5) == 'V'
    assert convert_numeral(10) == 'X'
    assert convert_numeral(14) == 'XIV'
    assert convert_numeral(15) == 'XV'
    assert convert_numeral(19) == 'XIX'
    assert convert_numeral(45) == 'XLV'
    assert convert_numeral(56) == 'LVI'
    assert convert_numeral(89) == 'LXXXIX'
    assert convert_numeral(99) == 'XCIX'
    assert convert_numeral(100) == 'C'
    assert convert_numeral(296) == 'CCXCVI'
    assert convert_numeral(1024) == 'MXXIV'
    assert convert_numeral(3999) == 'MMMCMXCIX'
    assert convert_numeral(77) == "LXXVII"
    assert convert_numeral(66) == "LXVI"
    assert convert_numeral(55) == "LV"
    assert convert_numeral(8) == "VIII"
    assert convert_numeral(1200) == "MCC"
    assert convert_numeral(34) == "XXXIV"
    assert convert_numeral(65) == "LXV"
    assert convert_numeral(3) == "III"
    assert convert_numeral(21) == "XXI"
    assert convert_numeral(99) == "XCIX"
    assert convert_numeral(40) == "XL"
    assert convert_numeral(3999) == "MMMCMXCIX"
    #assert convert_numeral(4000) == "MMMM"
    # assert convert_numeral("ASD") == "MML"
#    assert convert_numeral(3.5) == "III"
#    assert convert_numeral(-2) == "VIII"
    assert convert_numeral(3) == "III"
    assert convert_numeral(1) == "I"
    assert convert_numeral(10) == "X"
    assert convert_numeral(9) == "IX"
    assert convert_numeral(40) == "XL"
    assert convert_numeral(1000) == "M"
    assert convert_numeral(100) == "C"
    assert convert_numeral(5) == "V"
    assert convert_numeral(4) == "IV"
    assert convert_numeral(7) == "VII"
    assert convert_numeral(2013) == "MMXIII"
    assert convert_numeral(1975) == "MCMLXXV"
    assert convert_numeral(3999) == "MMMCMXCIX"    
    assert convert_numeral(1) == "I"
    assert convert_numeral(2) == "II"
    assert convert_numeral(3) == "III"
    assert convert_numeral(4) == "IV"
    assert convert_numeral(10) == "X"
    assert convert_numeral(50) == "L"
    assert convert_numeral(90) == "XC"
    assert convert_numeral(3) == "III"
    assert convert_numeral(4) == "IV"
    assert convert_numeral(8) == "VIII"
    assert convert_numeral(9) == "IX"
    assert convert_numeral(20) == "XX"
    assert convert_numeral(40) == "XL"
    assert convert_numeral(80) == "LXXX"
    assert convert_numeral(90) == "XC"
    assert convert_numeral(300) == "CCC"
    assert convert_numeral(900) == "CM"
    assert convert_numeral(1999) == "MCMXCIX"
    assert convert_numeral(2)=="II"
    assert convert_numeral(4)=="IV"
    assert convert_numeral(9)=="IX"
    assert convert_numeral(20)=="XX"
    assert convert_numeral(58)=="LVIII"
    assert convert_numeral(1994)=="MCMXCIV"
    assert convert_numeral(1) == "I"
    assert convert_numeral(3) == "III"
    assert convert_numeral(4) == "IV"
    assert convert_numeral(9) == "IX"
    assert convert_numeral(48) == "XLVIII"
    assert convert_numeral(999) == "CMXCIX"
    assert convert_numeral(1986) == "MCMLXXXVI"
    assert convert_numeral(1996) == "MCMXCVI"
    assert convert_numeral(2020) == "MMXX"
    assert convert_numeral(1) == 'I'
    assert convert_numeral(1)=="I"
    assert convert_numeral(2)=="II"
    assert convert_numeral(3)=="III"
    assert convert_numeral(4)=="IV"
    assert convert_numeral(5)=="V"
    assert convert_numeral(6)=="VI"
    assert convert_numeral(9)=="IX"
    assert convert_numeral(10)=="X"
    assert convert_numeral(13)=="XIII"
    assert convert_numeral(14)=="XIV"
    assert convert_numeral(15)=="XV"
    assert convert_numeral(19)=="XIX"
    assert convert_numeral(20)=="XX"
    assert convert_numeral(40)=="XL"
    assert convert_numeral(50)=="L"
    assert convert_numeral(80)=="LXXX"
    assert convert_numeral(99)=="XCIX"
    assert convert_numeral(199)=="CXCIX"
    assert convert_numeral(3333)=="MMMCCCXXXIII"
    assert convert_numeral(2) == 'II'
    assert convert_numeral(3000) == 'MMM'
    assert convert_numeral(50) == 'L'
    assert convert_numeral(2) == 'II'
    assert convert_numeral(8) == 'VIII'
    assert convert_numeral(9) == 'IX'
    assert convert_numeral(20) == 'XX'
    assert convert_numeral(999) == 'CMXCIX'
    assert convert_numeral(3999) == 'MMMCMXCIX'
    #assert convert_numeral("1") == "I"
    #assert convert_numeral("230") == "CCXXX"
    assert convert_numeral(1) == "I"
    assert convert_numeral(2) == "II"
    assert convert_numeral(4) == "IV"
    assert convert_numeral(999) == "CMXCIX"
    assert convert_numeral(1024) == "MXXIV"
    assert convert_numeral(1) == 'I'
    assert convert_numeral(2) == 'II'
    assert convert_numeral(3) == 'III'  
    assert convert_numeral(3999) == 'MMMCMXCIX'
    assert convert_numeral(123) == 'CXXIII' 
    assert convert_numeral(4) == 'IV'
    assert convert_numeral(1)=="I"
    assert convert_numeral(4)=="IV"
    assert convert_numeral(9)=="IX"
    assert convert_numeral(16)=="XVI"
    assert convert_numeral(25)=="XXV"
    assert convert_numeral(36)=="XXXVI"
    assert convert_numeral(1) == "I"
    assert convert_numeral(3) == "III"
    assert convert_numeral(4) == "IV"
    assert convert_numeral(9) == "IX"
    assert convert_numeral(20) == "XX"
    assert convert_numeral(24) == "XXIV"
    assert convert_numeral(24) == "XXIV"
    assert convert_numeral(99) == "XCIX"
    assert convert_numeral(104) == "CIV"
    assert convert_numeral(999) == "CMXCIX"
    assert convert_numeral(1021) == "MXXI"
    assert convert_numeral(3000) == "MMM"
    assert convert_numeral(3932) == "MMMCMXXXII"
    assert convert_numeral(3999) == "MMMCMXCIX"
    assert convert_numeral(1) == 'I';
    assert convert_numeral(3) == 'III';
    assert convert_numeral(10) == 'X';
    assert convert_numeral(62) == 'LXII';
    assert convert_numeral(110) == 'CX';
    assert convert_numeral(185) == 'CLXXXV';
    assert convert_numeral(2002) == 'MMII';
    assert convert_numeral(33) == "XXXIII"
    assert convert_numeral(3999) == "MMMCMXCIX"
    assert convert_numeral(33) == "XXXIII"
    assert convert_numeral(3999) == "MMMCMXCIX"
    assert convert_numeral(1) == "I"
    assert convert_numeral(3) == "III"
    assert convert_numeral(4) == "IV"
    assert convert_numeral(28) == "XXVIII"
    assert convert_numeral(49) == "XLIX"
    assert convert_numeral(999) == "CMXCIX"
    assert convert_numeral(1000) == "M"
    assert convert_numeral(1999) == "MCMXCIX"
    assert convert_numeral(3999) == "MMMCMXCIX"
    assert convert_numeral(1) == "I"
    assert convert_numeral(10) == "X"
    assert convert_numeral(12) == "XII"
    assert convert_numeral(19) == "XIX"
    assert convert_numeral(105) == "CV"
    assert convert_numeral(137) == "CXXXVII"
    assert convert_numeral(1390) == "MCCCXC"
    assert convert_numeral(3) == "III"
    #assert convert_numeral(4178) == "MMMMCLXXVIII" # quality-chrisjj12
    assert convert_numeral(25) == "XXV"
    assert convert_numeral(2384) == "MMCCCLXXXIV"
    #assert convert_numeral(4999) == "MMMMCMXCIX"
    assert convert_numeral(100) == "C"
    assert convert_numeral(4) == "IV"
    assert convert_numeral(5) == "V"
    assert convert_numeral(10) == "X"
    assert convert_numeral(35) == "XXXV"
    assert convert_numeral(994) == "CMXCIV"
    assert convert_numeral(1995) == "MCMXCV"
    assert convert_numeral(100) == "C"
    assert convert_numeral(3999) == "MMMCMXCIX"
    assert convert_numeral(12) == "XII"
    assert convert_numeral(1213) == "MCCXIII"
    assert convert_numeral(932) == "CMXXXII"
    assert convert_numeral(1001) == "MI"
    assert convert_numeral(384) == "CCCLXXXIV"
    assert convert_numeral(1) == 'I'
    assert convert_numeral(100) == 'C'
    assert convert_numeral(3999) == 'MMMCMXCIX'
    assert convert_numeral(1) == "I"
    #assert convert_numeral(4000) == "MMMM"
    assert convert_numeral(7) == 'VII'
    assert convert_numeral(67) == 'LXVII'
    assert convert_numeral(1) == 'I'
    assert convert_numeral(3999) == 'MMMCMXCIX'
    #assert convert_numeral(4999) == 'MMMMCMXCIX'
    assert convert_numeral(6) == 'VI'
    assert convert_numeral(3987) == 'MMMCMLXXXVII'
    # assert convert_numeral('I love the romans') == ''
    assert convert_numeral(55) == "LV"
    assert convert_numeral(14) == "XIV"
    assert convert_numeral(99) == "XCIX"
    assert convert_numeral(1) == "I"
    assert convert_numeral(2) == "II"
    assert convert_numeral(3) == "III"
    assert convert_numeral(4) == "IV"
    assert convert_numeral(5) == "V"
    assert convert_numeral(6) == "VI"
    assert convert_numeral(7) == "VII"
    assert convert_numeral(8) == "VIII"
    assert convert_numeral(9) == "IX"
    assert convert_numeral(10) == "X"
    assert convert_numeral(1) == "I"
    assert convert_numeral(10) == "X"
    assert convert_numeral(100) == "C"
    assert convert_numeral(49) == "XLIX"
    assert convert_numeral(143) == "CXLIII"
    assert convert_numeral(99) == "XCIX"
    assert convert_numeral(1000) == "M"
    assert convert_numeral(2019) == "MMXIX"
    assert convert_numeral(3999) == "MMMCMXCIX"
    assert convert_numeral(1) == "I"
    assert convert_numeral(2) == "II"
    assert convert_numeral(3) == "III"
    assert convert_numeral(4) == "IV"
    assert convert_numeral(5) == "V"
    assert convert_numeral(6) == "VI"
    assert convert_numeral(7) == "VII"
    assert convert_numeral(8) == "VIII"
    assert convert_numeral(9) == "IX"
    assert convert_numeral(20) == "XX"
    assert convert_numeral(203) == "CCIII"
    # assert convert_numeral(V)DCCLI"
    # assert convert_numeral(C)"
    # assert convert_numeral(C)DC"
    # assert convert_numeral(C)MXL"
    assert convert_numeral(5) == "V"
    assert convert_numeral(4) == "IV"
    assert convert_numeral(3999) == "MMMCMXCIX"
    assert convert_numeral(148) == "CXLVIII"
    assert convert_numeral(1) == "I"
    assert convert_numeral(4) == "IV"
    assert convert_numeral(5) == "V"
    assert convert_numeral(10) == "X"
    assert convert_numeral(40) == "XL"
    assert convert_numeral(50) == "L"
    assert convert_numeral(90) == "XC"
    assert convert_numeral(100) == "C"
    assert convert_numeral(900) == "CM"
    assert convert_numeral(1000) == "M"
    assert convert_numeral(2020) == "MMXX"
    assert convert_numeral(1014) == 'MXIV'
    assert convert_numeral(6) == 'VI'
    assert convert_numeral(1)=="I"
    assert convert_numeral(2)=="II"
    assert convert_numeral(3)=="III"
    assert convert_numeral(4)=="IV"
    assert convert_numeral(5)=="V"
    assert convert_numeral(6)=="VI"
    assert convert_numeral(9)=="IX"
    assert convert_numeral(10)=="X"
    assert convert_numeral(13)=="XIII"
    assert convert_numeral(14)=="XIV"
    assert convert_numeral(20)=="XX"
    assert convert_numeral(40)=="XL"
    assert convert_numeral(50)=="L"
    assert convert_numeral(80)=="LXXX"
    assert convert_numeral(99)=="XCIX"
    assert convert_numeral(199)=="CXCIX"
    assert convert_numeral(3333)=="MMMCCCXXXIII"
    assert convert_numeral(1000) == "M"
    assert convert_numeral(900) == "CM"
    assert convert_numeral(100) == "C"
    assert convert_numeral(90) == "XC"
    assert convert_numeral(50) == "L"
    assert convert_numeral(40) == "XL"
    assert convert_numeral(10) == "X"
    assert convert_numeral(9) == "IX"
    assert convert_numeral(5) == "V"
    assert convert_numeral(4) == "IV"
    assert convert_numeral(1) == "I"
    # assert convert_numeral(0) == "I" #expect an input of 0 to be changed to 1 by default
    # assert convert_numeral(-1) == "I" #expect a negative value to use the absolute value of the input instead
    assert convert_numeral(1) == 'I'
    assert convert_numeral(4) == 'IV'
    assert convert_numeral(5) == 'V'
    assert convert_numeral(9) == 'IX'
    assert convert_numeral(10) == 'X'
    assert convert_numeral(40) == 'XL'
    assert convert_numeral(50) == 'L'
    assert convert_numeral(90) == 'XC'
    assert convert_numeral(100) == 'C'
    assert convert_numeral(900) == 'CM'
    assert convert_numeral(1000) == 'M'
    assert convert_numeral(13) == 'XIII'
#    assert convert_numeral(4999) == 'MMMMCMXCIX'
    assert convert_numeral(1) == "I"
    assert convert_numeral(6) == "VI"
    assert convert_numeral(11) == "XI"
    assert convert_numeral(23) == "XXIII"
    assert convert_numeral(178) == "CLXXVIII"
    assert convert_numeral(297) == "CCXCVII"
    assert convert_numeral(369) == "CCCLXIX"
    assert convert_numeral(1000) == "M"
    assert convert_numeral(1232) == "MCCXXXII"
    assert convert_numeral(1) == 'I'
    assert convert_numeral(4) == 'IV'
    assert convert_numeral(10) == 'X'
    assert convert_numeral(100) == 'C'
    assert convert_numeral(90) == 'XC'
    assert convert_numeral(1001) == 'MI'
    assert convert_numeral(2394) == 'MMCCCXCIV'
    assert convert_numeral(4) == "IV"
    assert convert_numeral(5) == "V"
    assert convert_numeral(310) == "CCCX"
    assert convert_numeral(17) == "XVII"
    assert convert_numeral(137) == "CXXXVII"
    assert convert_numeral(1998) == "MCMXCVIII"
    assert convert_numeral(270) == "CCLXX"
    assert convert_numeral(46) == "XLVI"
    assert convert_numeral(34) == 'XXXIV'
    assert convert_numeral(2) == 'II'
    assert convert_numeral(3964) == 'MMMCMLXIV'
    assert convert_numeral(77) == 'LXXVII'
    assert convert_numeral(66) == 'LXVI'
    assert convert_numeral(55) == 'LV'
    assert convert_numeral(8) == 'VIII'
    assert convert_numeral(1200) == 'MCC'
    assert convert_numeral(34) == 'XXXIV'
    assert convert_numeral(65) == 'LXV'
    assert convert_numeral(3) == 'III'
    assert convert_numeral(21) == 'XXI'
    assert convert_numeral(99) == 'XCIX'
    assert convert_numeral(2150) == "MMCL"
    assert convert_numeral(2123) == "MMCXXIII"
    assert convert_numeral(1) == "I"
    assert convert_numeral(49) == "XLIX"
    assert convert_numeral(1999) == "MCMXCIX"
    assert convert_numeral(1994) == "MCMXCIV"
    assert convert_numeral(30) == "XXX"
    assert convert_numeral(221) == "CCXXI"
    assert convert_numeral(7) == "VII"
    #assert convert_numeral(15) == "XVI"      ## WRONG
    assert convert_numeral(1) == 'I'
    assert convert_numeral(3999) == 'MMMCMXCIX'
    assert convert_numeral(123) == 'CXXIII'
    assert convert_numeral(4) == 'IV'
    assert convert_numeral(12) == "XII"
    assert convert_numeral(3) == "III"
    assert convert_numeral(12) == "XII"
    assert convert_numeral(27) == "XXVII"
    assert convert_numeral(32) == "XXXII"
    assert convert_numeral(45) == "XLV"
    assert convert_numeral(57) == "LVII"
    assert convert_numeral(69) == "LXIX"
    assert convert_numeral(77) == "LXXVII"
    assert convert_numeral(88) == "LXXXVIII"
    assert convert_numeral(93) == "XCIII"
    assert convert_numeral(139) == "CXXXIX"
    assert convert_numeral(295) == "CCXCV"
    assert convert_numeral(302) == "CCCII"
    assert convert_numeral(907) == "CMVII"
    assert convert_numeral(1054) == "MLIV"
    assert convert_numeral(2309) == "MMCCCIX"
    assert convert_numeral(1) == 'I';
    assert convert_numeral(4) == 'IV';
    assert convert_numeral(9) == 'IX';
    assert convert_numeral(59) == 'LIX';
    assert convert_numeral(94) == 'XCIV';
    assert convert_numeral(999) == 'CMXCIX';
    assert convert_numeral(1010) == 'MX';
    assert convert_numeral(3999) == 'MMMCMXCIX';
    assert convert_numeral(14) == 'XIV'
    assert convert_numeral(18) == 'XVIII'
    assert convert_numeral(80) == 'LXXX'
    assert convert_numeral(99) == 'XCIX'
    assert convert_numeral(199) == 'CXCIX'
    assert convert_numeral(3333) == 'MMMCCCXXXIII'
    assert convert_numeral(3999) == 'MMMCMXCIX'
    #assert convert_numeral(4975) == 'MMMMCMLXXV'
    assert convert_numeral(1) == 'I'
    assert convert_numeral(239) == 'CCXXXIX'
    assert convert_numeral(1213) == "MCCXIII"
    assert convert_numeral(20) == "XX"
    assert convert_numeral(384) == "CCCLXXXIV"
    assert convert_numeral(99) == "XCIX"
    assert convert_numeral(999) == "CMXCIX"
    assert convert_numeral(3000) == "MMM"
    assert convert_numeral(100) == "C"
    assert convert_numeral(3999) == "MMMCMXCIX"
    assert convert_numeral(12) == "XII"
    assert convert_numeral(1) == 'I'
    assert convert_numeral(1999) == 'MCMXCIX'
    assert convert_numeral(3999) == 'MMMCMXCIX'
