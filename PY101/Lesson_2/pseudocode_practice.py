# Problem 1: a function that returns the sum of two numbers
'''
Given two integers

Create a function named sum that takes in two parameters
    The two parameters are for the two numbers
    return the result of adding the two integers
'''

# Problem 2: a function that takes a list of strings, and returns a string that is all those strings concatenated together
'''
Given a collection of strings

Create a function named concatenate that takes in a parameter
    The parameter is for the list of strings
    Create a value called complete_string and set it equal to an empty string
    Iterate throught the collection one by one
        for each iteration, add the value to complete_string
    
After iterating through the collection, return complete_string
'''

# Problem 3: a function that takes a list of integers, and returns a new list with every other element from the original list, starting with the first element
'''
Given a collection of integers

Create an function every_other_int that takes in one parameter, a list
    Create an empty list, every_other
    Iterate through the original collection one by one
        Append the value to every_other
        The iteration goes up by two

Return every_other
'''

# Problem 4: a function that determines the index of the 3rd occurrence of a given character in a string. For instance, if the given character is 'x' and the string is 'axbxcdxex', the function should return 6 (the index of the 3rd 'x'). If the given character does not occur at least 3 times, return None.
'''
Giving a string and a character

Create a function that takes two arguments, a character and a string
    Create a variable count and initialize the value to 0
    Create a variable seperated and initialize the value to list(string)
    Iterate through seperated one by one
        for each iteration, compare the value with the character
        if the comparison is true
            increment count
            check if count is equal to three
                if that is true, return the index 
        if the comparison is not true
            move to the next value in the collection
    After iterating through the collection
        If count is less than three
            return None
'''
# Problem 5: a function that takes two lists of numbers and returns the result of merging the lists. The elements of the first list should become the elements at the even indexes of the returned list, while the elements of the second list should become the elements at the odd indexes.
'''
Given two collections of numbers

Create a function called merge that takes in two arguments, two collections
    Create a variable named merged_list and initialize it to an empty list
    Iterate through a passed in collection
        Use append() to add the index from the first list to merged_list
        Use append() to add the index from the second list to merged_list
        
After iterating through the list, return merged_list
'''