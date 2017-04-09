from random import randint
import urllib.request

rand_num = randint(0, 1000)
filename = str(rand_num) + '.png'
url = r'http://www.she-codes.org/sc/wp-content/uploads/2014/11/logo-copy200.png'

local_filename, headers = urllib.request.urlretrieve(url, filename)
