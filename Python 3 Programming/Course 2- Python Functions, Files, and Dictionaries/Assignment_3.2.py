#Create a dictionary, freq, that displays each character in string str1 as the key and its frequency as the value.

from collections import Counter

str1 = "peter piper picked a peck of pickled peppers"
freq = Counter(str1)

for i in str1:
    print(i, freq[i])