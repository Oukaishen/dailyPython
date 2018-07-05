## if list 

Use collection name to detect whether the collection is empty

<br>

Under this [Truth Value Testing](https://docs.python.org/3.6/library/stdtypes.html#truth-value-testing), it is said that 

> Any object can be tested for truth value, for use in an **if** or **while** condition or as operand of the Boolean operations below.
>
> By default, an object is considered true unless its class defines either a [`__bool__()`](https://docs.python.org/3.6/reference/datamodel.html#object.__bool__) method that returns `False` or a [`__len__()`](https://docs.python.org/3.6/reference/datamodel.html#object.__len__) method that returns zero, when called with the object. [[1\]](https://docs.python.org/3.6/library/stdtypes.html#id12) Here are most of the built-in objects considered false:

- constants defined to be false: `None` and `False`.
- zero of any numeric type: `0`, `0.0`, `0j`, `Decimal(0)`, `Fraction(0, 1)`
- empty sequences and collections: `''`, `()`, `[]`, `{}`, `set()`, `range(0)`

Operations and built-in functions that have a Boolean result always return `0` or `False` for false and `1`or `True` for true, unless otherwise stated. (Important exception: the Boolean operations `or` and `and`always return one of their operands.)



```python
if list:
    ## this means that this list is not empty, has some element
```

