def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """

    if len(digits) == 1:
        return [1, 0] if digits[0] == 9 else [digits[0] + 1]

    if digits[-1] == 9:
        return plusOne(digits[:-1]) + [0]
    else:
        digits[-1] += 1
        return digits


# test cases
assert plusOne([9]) == [1, 0]
assert plusOne([5, 1]) == [5, 2]
assert plusOne([9, 9, 9]) == [1, 0, 0, 0]
assert plusOne([8, 9, 9, 9]) == [9, 0, 0, 0]

