#Challenge: Create a list called emotions that contains the first word of every line in emotion_words.txt.

fileref = open ("emotion_words.txt","r")
line = fileref.readlines()
emotions = []
for words in line:
    word = words.split()
    emotions.append(word[0])
print (emotions)