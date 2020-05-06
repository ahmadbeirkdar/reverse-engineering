import random
import string

key = ""
ascii_sum = 0
for i in range(11):
    rnd_char = string.ascii_lowercase[random.randint(0,len(string.ascii_lowercase) - 1)]
    ascii_sum += ord(rnd_char)
    key += rnd_char
    if len(key) > 7 and len(key) < 11:
        if ascii_sum < 1000:
            pass
        else:
            print(key)

