#Assign to the variable num_lines the number of lines in the file school_prompt.txt.

num_lines = sum(1 for line in open('school_prompt.txt'))