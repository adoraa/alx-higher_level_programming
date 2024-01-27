def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    result = 0
    last_val = 0

    for r_num in reversed(roman_string):
        val = roman_numerals.get(r_num, 0)
        if val < last_val:
            result -= val
        else:
            result += val
        last_val = val
    return result
