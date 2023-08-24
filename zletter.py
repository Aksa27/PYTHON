import re
text="this is a sample zambia text with some words containg the letter z."
x=r"\b\w*z\w*\b"
s=re.findall(x,text)
print(s)