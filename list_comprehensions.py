""" This file summarizes the list Comprehension part of lab2, part 2.
The syntax is taken from the tutorial: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions """

list1 = []

for i in range(1, 21):
    list1.append(i)

print("Careful with the `for i in range` syntax in python, \
this has a side effect and creates a persisting variable, i:", i)
print("list1:", list1)

# approach using a function to square
def square(x):
    return x**2
# the map function returns a 'map object' that can be cast to a list
list_squares = list(map(square, range(1, 21)))
print("list_squares:", list_squares)

# it is possible to write this without defining the function square,
# we can write this with an anonymous fuction, a lambda

list_squares = list(map(lambda x: x**2, range(1, 21)))
print("list_squares:", list_squares)

# This is the basis for a List Comprehension which is basically just
# a short form of the above, we leave out the lambda and map function.
# It also uses square brackets, as when defining a list, instead of a cast
# The keyword `in` is used to point to the mapping iterable

list_squares = [x**2 for x in range(1, 21)]
print("list_squares:", list_squares)

# We can also filter the values with the keyword if, or iterate over more
# than one variable. This can be thought of as nested loops and if statements

list_even_squares = [x**2 for x in range(1, 21) if x**2 % 2 == 0]
print("list_even_squares:", list_even_squares)

# or using the list we created before as iterable, which seems more readable
list_squares = [x**2 for x in range(1, 21)]
list_even_squares = [x for x in list_squares if x % 2 == 0]
print("list_even_squares:", list_even_squares)

# x should not be defined at this point,
# the above statements are all free of side effects
try:
    print(x)
except NameError:
    print("x is not defined here, List Comprehensions are free of side effects")

# This is great for simpler lists, but might become less readable
# if complex conditions are used, concatenated with `and`, `or` ...
# In this case it might be useful to move the condition checks into a function.

def complex_condition(x):
    # do some precalculations here ... or use many different conditions or cases
    # then apply complex condition, False is implicit when None is returned
    if x <= 200 and x**2 % 2 == 0:
        return True
    elif x == 400:
        return True

list_squares = [x**2 for x in range(1, 21)]
list_complex_filter = [x for x in list_squares if complex_condition(x)]
print("list_complex_filter:", list_complex_filter)
