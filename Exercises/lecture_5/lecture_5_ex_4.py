def create_dict(shift):
    # chr(number) --> gives character whose ascii code is number
    # ord(letter) --> gives ascii code of letter
    lowercase_range = range(ord('a'), ord('z') + 1)
    uppercase_range = range(ord('A'), ord('Z') + 1)

    d_lower = shift_range(lowercase_range, shift)
    d_upper = shift_range(uppercase_range, shift)

    d = d_lower
    d.update(d_upper)
    return d


def shift_range(num_range, shift):
    d = {}
    for num in num_range:
        num_with_shift = num + shift
        if num_with_shift <= max(num_range):
            new_num = num_with_shift
        else:
            diff = num_with_shift - max(num_range)
            new_num = min(num_range) + diff - 1
        d[chr(num)] = chr(new_num)
    return d

encryption_dict = create_dict(13)
decryption_dict = {v: k for k, v in encryption_dict.items()}


def encode(string, d=encryption_dict):
    encoded_string = ''

    for s in string:
        if s in d.keys():
            encoded_string += d[s]
        else:
            encoded_string += s
    return encoded_string


def decode(string):
    return encode(string, decryption_dict)

str_to_decode = 'V NZ YRNEAVAT CLGUBA JVGU FUR PBQRF NPNQRZL'
print(decode(str_to_decode))