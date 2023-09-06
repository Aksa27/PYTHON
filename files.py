f = open("demofile.txt", "a")
f.write("now the has more content")
f.close()

f = open("demofile.txt", "r")
print(f.read())
