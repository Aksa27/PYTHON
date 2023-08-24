import re
text="the quick brown frog jumps over the lazy dog"
x=r"\b\w{3,4}\b"
s=re.findall(x,text)
print(s)