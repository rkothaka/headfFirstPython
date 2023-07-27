<h3>Dictionary</h3>
Insertion order is NOT maintained. </br>
Access is maintained using keys and it doesn't matter to maintain an order.</br>

Frequency/Counter

Specifying the ordering of a dictionary on output</br>
for k in sorted(d):</br>
&nbsp;&nbsp;&nbsp;&nbsp;...

Iterating over Dict with "items"
for k, v in sorted(d.items()):</br>
&nbsp;&nbsp;&nbsp;&nbsp;...

Avoid key error by using "in" verification or setting default:</br>
found = {}</br>
found.setdefault(letter, 0)  # Initialize if needed</br>
found[letter] += 1

<h3>Sets</h3>
Sets don't allow duplicates. Uses hashing concept for searches; thus faster lookup than lists.</br>
Creating sets from sequences: vowels = set('aeeiouu')</br>
Other Operations:</br>
1. u = v.union(w) # u contains all the unique items from both sets v, w
2. u = v.difference(w) # u contains items in v that are not in w
3. u = v.intersection(w) # items common to v, w

<h3>Tuple</h3>
Tuples are immutable: they cannot change.</br>
User cases:</br>
1. Guard against side efects by ensuring some data never changes.</br>
2. Constant lists. Reducing the overhead of extra list processing code.</br>
Every tuple needs to include at least one comma between the parentheses: t = ('example',)</br>


Table: Dictionary of Dictionaries