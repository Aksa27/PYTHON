import re
text="carrot and apple followed in rabit ab and "
s=r"\ba\w*b\b"
x=re.findall(s,text)
print(x)