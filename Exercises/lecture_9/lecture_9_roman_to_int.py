def romanToInt(self, s):
    """
    Given a roman numeral, convert it to an integer.
    Input is guaranteed to be within the range from 1 to 3999.
    :type s: str
    :rtype: int
    """

    mapping = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    ret_val = 0

    if len(s) == 1:
        assert s in mapping, 'Unknown Roman numeral {}'.format(s)
        return mapping[s]

    while len(s):
        if len(s) == 1:
            ret_val += mapping[s]
            s = []
        else:
            curr_letter, next_letter = s[0:2]

            if mapping[curr_letter] < mapping[next_letter]:
                ret_val += mapping[next_letter] - mapping[curr_letter]
                s = s[2:]
            else:
                ret_val += mapping[curr_letter]
                s = s[1:]
    return ret_val

# # debug
# assert romanToInt('I') == 1
# assert romanToInt('LIV') == 54
# assert romanToInt('XCIX') == 99
# assert romanToInt('CIII') == 103
# assert romanToInt('M') == 1000

