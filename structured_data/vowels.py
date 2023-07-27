vowels = ['a', 'e', 'i', 'o', 'u']
word = input("Provide a word to search for vowels: ")

# found = {v: 0 for v in vowels}
found = {}

for letter in word:
    if letter in vowels:
        found.setdefault(letter, 0)  # Initialize if needed
        found[letter] += 1

for k, v in sorted(found.items()):
    print(k, 'was found', v, 'time(s).')
