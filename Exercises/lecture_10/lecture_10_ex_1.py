fw = open('reverse.txt', 'w')

with open('new.txt', 'r') as fr:
    words = fr.readlines()
    for word in words:
        fw.write(word[-1::-1])
fw.close()

fa = open('reverse.txt', 'a')
with open('new.txt', 'r') as fr:
    fa.write('\n')
    fa.writelines(fr.readlines())
fa.close()
