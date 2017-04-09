def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    # anagram - same letters in different order
    # count number of letters in s, check if t has same letters with same numbers

    def letter_count(str):
        letter_counter = {}
        for letter in str:
            if letter in letter_counter.keys():
                letter_counter[letter] += 1
            else:
                letter_counter[letter] = 1
        return letter_counter

    return letter_count(s) == letter_count(t)

isAnagram('a', 'b')