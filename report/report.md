---
title: Lab 02 – Learning Python
author: [Estella Kinzel, Jonas Trenkler]
date: '2023-04-23'
lang: 'en-US'
keywords: [info3, list, python]
output:
    pdf_document:
        template: eisvogel.latex
        pandoc_args: ["--listings"]
---

# Lab 02 – Learning Python

Group: Estella Kinzel, Jonas Trenkler

Repository: <https://github.com/JonasTrenkler/info3-lab02>

## Part 1 - Learning Python with Unit Tests

### Topics and Issues

Instance Creation, Estella: <https://github.com/htw-imi-info3/python-learning/issues/10> 

Dictionaries, Jonas T.: <https://github.com/htw-imi-info3/python-learning/issues/7>

## Part 2 - Small Python Exercises

**1.** List Comprehensions were new to us, so we started reading the [Python Tutorial](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions) on it, linked in the assignment.
We started with a list that we filled using a for loop and worked through the examples using lambda syntax and eventually the List Complesension as short form.
We played around these in the iPython REPL and came up with the following lines [28, 32]:

```python
In [1]: list1 = []

In [2]: for i in range(1, 21):
   ...:     list1.append(i)
   ...: 

In [3]: list1
Out[3]: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

In [28]: list1 = [x**2 for x in range(1, 21)]

In [29]: list1
Out[29]: 
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400]

In [32]: list2 = [x for x in list1 if x%2 == 0]

In [33]: list2
Out[33]: [4, 16, 36, 64, 100, 144, 196, 256, 324, 400]
```

It took a while to figure out the lambda syntax, but the resulting list comprehensions were easier to read.
Another thing to keep in mind is that the upper bound of range is exclusive, the lower one inclusive.


