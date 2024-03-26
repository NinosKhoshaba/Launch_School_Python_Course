# 1: What is the official place to find Python documentation?
# Python Official Documentation

# 2: Determine whether Python has a method to lowercase a string, for example converting 'Aloha, World!' into 'aloha, world!.

print('Aloha, World!'.lower())

# 3: Use the Python documentation for the str class to determine which method can be used to right justify a str object.
# https://docs.python.org/3/library/stdtypes.html#integer-string-conversion-length-limitation
# str.rjust()

# 4: Is there a method to reverse a string, for example turning 'hello' into 'olleh'?
# no but we can do it like this:
text = "hello world"[::-1]
print(text)

# 5: Locate the documentation for the list built-in object in Python Documentation.
# How can we access the second element ('and') in the list ['fish', 'and', 'chips']?
print(['fish', 'and', 'chips'][1])

# 6: How would you determine the index of the fruit "cherry" in this list?
fruits = ["apple", "banana", "cherry", "peach", "watermelon"]
print(fruits.index("cherry"))

# 7: What happens if we take the list ['fish', 'and', 'chips'] and try to access the element at index position 10? First try to determine what will happen by consulting the documentation, then verify your understanding in the Python REPL.

# I believe it will raise an error as we would be attempting to access an index that is greater than the length that we have
# ['fish', 'and', 'chips'][10]

# 8: Using the Python documentation, determine how you can write large numbers in a way that makes them easier to read.

# using underscores to seperate groups of digits

# 9: Referring to the official Python documentation, how would you identify the data type of the following values?

print(type(23.5))
print(type('Call me Ishmael.'))
print(type(False))
print(type(0))
print(type(None))