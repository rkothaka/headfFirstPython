paranoid_android = "Marvin, the paranoid Android"
letters = list(paranoid_android)

for char in letters[:6]:
    print('\t', char)

# extracts the sliced objects from letters
# return a copy of objects to the for loop
for char in letters[-7:]:
    char = chr(ord(char) + 1)
    print('\t'*2, char)

print("".join(letters))
