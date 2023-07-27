<h3>Everything is an Object</h3>
Python as more object-based as opposed to purely object-oriented. </br>
<i>Everything is an object in Python, and any object can be assigned to a variable.</i></br>
Objects can have state (attributes or values) and behavior(methods).</br>
</br>
Four built in data structure: </br>
<b>Built-in</b>: they do not need to be imported. <b> list, tuple, dict, and set </b></br>
<h3> Ordered Collections are Mutable/Immutable</h3>
1. List: an ordered mutable collection of objects. Dynamic, heterogeneuous, mutable
2. Tuple: an ordered immutable collection of objects.
<h3> Unordered Data Structures</h3>
3. Dictionary: an unordered set of key/value pairs. Mutable.
4. Set: an unordered set of unique objects. Lets you perform unions, intersections, and differences.


<h3>List</h3>
in/ not in</br>
remove: removes the first occurrence of the input</br>
pop: takes the optional argument for index</br>
extend([])</br>
insert(idx, val)</br>

first = [1, 2, 3, 4]</br>
second = first # reference to the list is shared among first and second</br>
third = second.copy()</br>
<i> don't use the assignment operator to copy a list; use the "copy" method instead.</i></br>


Slicing: letters[start:stop:step] - slice notation can be use on any sequence in Python</br>
For loop and Slicing:</br>
When the interpreter sees the slice specification, it extracts the sliced objects from letters and returns a copy of the objects to the for loop. the original list is unaffected by these slices.
