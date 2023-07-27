phrase = "Don't panic!!"
plist = list(phrase)
print(phrase)
print(plist)

plist.remove("D")
plist[2] = " "
plist[4] = "a"
for _ in range(6):
    plist.pop()

new_phrase = ''.join(plist)
print(plist)
print(new_phrase)
