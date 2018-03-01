# Enumerate

kaishen, 1st Mar, 2018

One of the common used **Build-in Functions**. 

> returns a tuple containing a count (from *start* which defaults to 0) and the values obtained from iterating over *iterable*.

The detailed description can be found [here in the Standard doc](https://docs.python.org/3/library/functions.html#enumerate). 

Take a quick look at the following code snippet. 

## Code Snippet

```python
seasons = ['Spring','Summer','Fall','Winter']
print(list(enumerate(seasons)))
print(list(enumerate(seasons,start=2)))

for index, element in enumerate(seasons):
    print("Now the index is {} and the element is {}".format(index,element))
```

The returned result is

```
[(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
[(2, 'Spring'), (3, 'Summer'), (4, 'Fall'), (5, 'Winter')]
Now the index is 0 and the element is Spring
Now the index is 1 and the element is Summer
Now the index is 2 and the element is Fall
Now the index is 3 and the element is Winter
```

As shown in the above code snippet, we can also choose the **count** start from where, i.e. 0 or 1 or 2, etc.