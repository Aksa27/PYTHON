fruits=['apple','banana','pear','apricoat','orange']
def alpha(s,k):
    if s[0]=='a':
        k.append(s)
    return k
result=map(alpha,fruits)
print(list(result))    