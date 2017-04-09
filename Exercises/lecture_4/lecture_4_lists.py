# ===== str =====
s1 = 'aaa'
s2 = 'a1a'
s3 = '111'
s4 = '1@a'
s5 = '@#$'
s6 = '&12'
s7 = 'rt$'

all_str = [s1, s2, s3, s4, s5, s6, s7]

# print('='.join(all_str))

# for s in all_str:
    # print(s, s.isalnum())
    # print(s, s.split('1'))
    # print(s, s.replace('a', 'A'))
    # print(s, s.count('a'))
    # print(s, s.find('a'))
    # print(s, s.index('a'))

# isalnum - checks whether the string consists of alphanumeric characters.
# split - splits string at separator
# replace - replaces inner str with another
# join - joins all strings with separator
# count - counts occurrences of substring in string, -1 if N\A
# find - returns index of first occurrence of substring in string
# index - returns index of substring in string, crashes if N\A

# ===== List =====
l1 = [1, 2, 3]
l2 = ['a', 'b', 'c']
l3 = ['5', 'horse', -500]
l4 = [1, 22, 3]

print('=== append ===')
print('before - {}'.format(l1))
l1.append(5)
print('after - {}'.format(l1))

print('=== extend ===')
print('before - {}'.format(l1))
l1.extend(l1)
print('after - {}'.format(l1))

print('=== pop ===')
print('before - {}'.format(l1))
print(l1.pop(5))
print('after - {}'.format(l1))

print('=== insert ===')
print('before - {}'.format(l1))
l1.insert(5, 'dog')
print('after - {}'.format(l1))

print('=== sort ===')
print('before - {}'.format(l4))
l4.sort()
print('after - {}'.format(l4))

print('=== index ===')
print(l4.index(3))

print('=== count ===')
print(l1.count(3))

print('=== range ===')
for i in range(5):
    print(i)

print('=== find ===')
print('hello'.find('l'))



