#addition_str is a string with a list of numbers separated by the + sign. Write code that uses the accumulation pattern to take the sum of all of the numbers and assigns it to sum_val (an integer). (You should use the .split("+") function to split by "+" and int() to cast to an integer).

addition_str = "2+5+10+20"
print(addition_str.split("+"))

print (int("2"))
print (int("5"))
print (int("10"))
print (int("20"))

sum_val = sum(map(int,addition_str.split("+")))
print(sum_val)
