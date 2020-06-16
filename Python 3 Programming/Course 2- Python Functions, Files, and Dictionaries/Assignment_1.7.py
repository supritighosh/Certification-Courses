#Assign the first 33 characters from the textfile, travel_plans.txt to the variable first_chars.

f = open('travel_plans.txt', 'r')
first_chars = f.read(33)
print(first_chars)
