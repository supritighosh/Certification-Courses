#Write code to create a list of word lengths for the words in original_str using the accumulation pattern and assign the answer to a variable num_words_list. (You should use the len function).

original_str = "The quick brown rhino jumped over the extremely lazy fox"

original_list = list(original_str.split())
num_words = len(original_list)
num_words_list = []
for i in original_list:
    num_words_list.append((len(i)))

print(num_words_list)