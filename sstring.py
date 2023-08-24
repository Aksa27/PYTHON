string=["hello"]
counts={}
index=0
length = len(string)
while index < length:
    chr = string[index]
if chr in counts:
    counts[chr] += 1
else:
    counts[chr] = 1
index += 1