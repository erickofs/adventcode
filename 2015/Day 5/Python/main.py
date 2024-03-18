"""
--- Day 5: Doesn't He Have Intern-Elves For This? ---
Santa needs help figuring out which strings in his text file are naughty or nice.

A nice string is one with all of the following properties:

It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.
For example:

ugknbfddgicrmopn is nice because it has at least three vowels, a double letter, and none of the disallowed substrings.
aaa is nice because it has at least three vowels and a double letter, even though the letters used by different rules overlap.
jchzalrnumimnmhp is naughty because it has no double letter.
haegwjzuvuyypxyu is naughty because it contains the string xy.
dvszwmarrgswjxmb is naughty because it contains only one vowel.
"""
# AI Support: https://www.blackbox.ai/share/408eb65c-70bc-4bac-9525-9487263c3209
NICE_STRINGS = 0
vowels = ['a', 'e', 'i', 'o', 'u']
bad_pieces = ['ab', 'cd', 'pq', 'xy']
with open('input.txt') as f:
    string = f.readline().strip()
    while string:
        vowel_counts = {vowel: string.count(vowel) for vowel in vowels}
        if any(string.count(vowel) >= 3 for vowel in vowels):
            if any(string[i] == string[i+1] for i in range(len(string)-1)):
                if not any(piece in string for piece in bad_pieces):
                    NICE_STRINGS += 1
        string = f.readline().strip()






















print(f'The number of nice strings is {NICE_STRINGS}')

"""

"""
