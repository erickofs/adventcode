"""
--- Day 4: The Ideal Stocking Stuffer ---
Santa needs help mining some AdventCoins (very similar to bitcoins) to use as gifts for all the economically forward-thinking little girls and boys.

To do this, he needs to find MD5 hashes which, in hexadecimal, start with at least five zeroes. 
The input to the MD5 hash is some secret key followed by a number in decimal. 
To mine AdventCoins,find Santa the lowest positive number that produces such a hash.

For example:

If key is abcdef, the answer is 609043, because the MD5 hash of the combination is 000001db..., 
and it is the lowest such number to do so.
If your secret key is pqrstuv, the lowest number is 1048970 
that is, the MD5 hash of pqrstuv1048970 looks like 000006136ef....
"""

import hashlib as hl

INPUT_STR = 'iwrupvqb'
INPUT_INT = 1
INPUT = INPUT_STR + str(INPUT_INT)
INPUT = hl.md5(INPUT.encode())
INPUT_STR = 'iwrupvqb'
INPUT_INT = 1
INPUT = INPUT_STR + str(INPUT_INT)
INPUT = hl.md5(INPUT.encode())

while INPUT.hexdigest()[:5] != '00000':
    INPUT_INT += 1
    INPUT = INPUT_STR + str(INPUT_INT)
    INPUT = hl.md5(INPUT.encode())

print(f'The lowest number is: {INPUT_INT}')

"""
--- Part Two ---
Now find one that starts with six zeroes.
"""

INPUT = INPUT_STR + str(INPUT_INT)
INPUT = hl.md5(INPUT.encode())
while INPUT.hexdigest()[:6] != '000000':
    INPUT_INT += 1
    INPUT = INPUT_STR + str(INPUT_INT)
    INPUT = hl.md5(INPUT.encode())
print(f'The number that produces a hash starting with six zeroes is: {INPUT_INT}')
