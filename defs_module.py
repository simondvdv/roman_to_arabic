def roman_to_arabic_converter(roman_number):
    try:
        if roman_number in ROMAN_DICT.values():
            return ROMAN_DICT_REVERSE[roman_number]
        elif ROMAN_DICT_REVERSE[roman_number[0]] >= ROMAN_DICT_REVERSE[roman_number[1]]:
            return ROMAN_DICT_REVERSE[roman_number[0]] + roman_to_arabic_converter(roman_number[1:])
        else:
            return (ROMAN_DICT_REVERSE[roman_number[1]] - ROMAN_DICT_REVERSE[roman_number[0]]
                    + roman_to_arabic_converter(roman_number[2:]))
    except IndexError:
        return ROMAN_DICT_REVERSE[roman_number[1]] - ROMAN_DICT_REVERSE[roman_number[0]]


ROMAN_DICT = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
ROMAN_DICT_REVERSE = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

# print(roman_to_arabic_converter('I'))
# print(roman_to_arabic_converter('II'))
# print(roman_to_arabic_converter('III'))
# print(roman_to_arabic_converter('IV'))
# print(roman_to_arabic_converter('V'))
# print(roman_to_arabic_converter('VI'))
# print(roman_to_arabic_converter('VII'))
# print(roman_to_arabic_converter('VIII'))
# print(roman_to_arabic_converter('IX'))
# print(roman_to_arabic_converter('X'))
# print(roman_to_arabic_converter('XI'))
# print(roman_to_arabic_converter('XII'))
# print(roman_to_arabic_converter('XIII'))
# print(roman_to_arabic_converter('XIV'))
# print(roman_to_arabic_converter('XV'))
# print(roman_to_arabic_converter('XVI'))
# print(roman_to_arabic_converter('XVII'))
# print(roman_to_arabic_converter('XIX'))
# print(roman_to_arabic_converter('XX'))
# print(roman_to_arabic_converter('XXI'))
# print(roman_to_arabic_converter('XXII'))
# print(roman_to_arabic_converter('XXIII'))
# print(roman_to_arabic_converter('XXIV'))
# print(roman_to_arabic_converter('XXV'))
# print(roman_to_arabic_converter('XXVI'))
# print(roman_to_arabic_converter('XXVII'))
# print(roman_to_arabic_converter('XXVIII'))
# print(roman_to_arabic_converter('XXIX'))
# print(roman_to_arabic_converter('XXX'))
# print(roman_to_arabic_converter('XXVIII'))
# print(roman_to_arabic_converter('XXIX'))
# print(roman_to_arabic_converter('LXXXVII'))
