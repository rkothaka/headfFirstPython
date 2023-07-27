<h3>How Are Modules Found</h3>
1. current working directory
2. interpreter's site-packages locations
3. standard library locations

Getting a Module into Site-packages</br>
Don't add or remove your own modules to/from the standard library. However, adding or removing modules to your site-packages is positively encouraged.

<b>Using "setuptools" to install into site-packages</b></br>
1. Create a distribution description - create two descriptive files for our module: setup.py and README.txt
2. Generate a distribution file - using Python at the cmd line, create a shareable distribution file
3. Install the distribution file - using Python at the cmd line, install the distribution file into site-packages.


<h4>Call-by-Value Semantics </h4>
If argument passed to the function is immutable .</br>
Strings, integers, and tuples (being immutable) are awlays passed into a function by value - any changes to the variable within the function are private to the function and are not reflected in the calling code.</br>


<h4>Call-by-reference Semantics </h4>
If argument passed to the function is mutable. </br>
List, dict, sets(being mutable) are always passed into a function by reference - any changes made to the variable's data structure within the function's suite are reflected in the calling code.

Strange case:</br>
nums = [1, 2, 3]</br>
def times2(nums: List[int]) -> None:</br>
&nbsp;&nbsp;&nbsp;&nbsp;nums = nums*2</br>

Calling times2(nums) doesn't change nums on the calling function even though nums is mutable List. </br>

Inside the function new list is created [1, 2, 3, 1, 2, 3] and it's reference is assigned to nums. However, older reference is still held outside the function.

