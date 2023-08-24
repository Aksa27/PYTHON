import re
url="https://www.digitalwelling.com/news/football/up/2016/09/02"
x= re.findall("\d\d\d/+/d",url)
print(x)