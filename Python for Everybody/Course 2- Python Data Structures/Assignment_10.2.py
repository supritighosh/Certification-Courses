#Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

dictionary_hours = dict()               # Initialize variables
lst = list()

name = input('Enter file name: ')
try:
    hand = open(name)
except FileNotFoundError:
    print('File cannot be opened:', name)
    quit()

for line in hand:
    words = line.split()
    if len(words) < 2 or words[0] != 'From':
        continue

    col_pos = words[5].find(':')
    hour = words[5][:col_pos]
    if hour not in dictionary_hours:
        dictionary_hours[hour] = 1      # First entry
    else:
        dictionary_hours[hour] += 1     # Additional counts

for key, val in list(dictionary_hours.items()):
    lst.append((key, val))              # Fills list with hour, count of dict

lst.sort()                              # Sorts by hour

for key, val in lst:
    print(key, val)