text = "X-DSPAM-Confidence:    0.8475";
b = text.find(":") + 1
e = len(text) + 1
num = text[b:e]
num_f = float(num)
print (num_f)