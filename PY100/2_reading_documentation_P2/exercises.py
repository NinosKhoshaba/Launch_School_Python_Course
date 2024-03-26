# 1 Given the following variables:
name = "Victor"
profession = "programmer"

# 1.1: How can you print the string "Hello, Victor. You are a programmer."" using the str.format method? You should fill in the name and profession in a string literal that contains the rest of the text.
# 1.2 How can you achieve the same result using an f-string?
'''
print('Hello {}. You are a {}.'.format(name, profession))
print(f'Hello {name}. You are a {profession}.')
'''
# 3 : In the following code snippet, find all violations of the PEP8 style guide. Rewrite it so that it conforms with the guide.
'''
iceCreamDensity=10 # ice_cream_density = 10

while iceCreamDensity>0 : # while iceCreamDensity > 0:
    print('Drip...')
    iceCreamDensity-=1 # iceCreamDensity -= 1

print('The ice cream melted.')
'''
# 4: Find the Python Documentation on operator precedence, and use it to determine the result of evaluating 4 * 5 + 3**2 / 10.

'''
In order: 3**2, 4*5, (3**2)/10, (4*5) + (3**2)
1: Exponentiation 3**2 = 9
2: Multiplication 4 * 5 = 20
3: Division: 9 / 10 = 0.9
4: Addition: 20 + 0.9 = 20.9
'''

# 5: Using the datetime module in Python, how would you obtain the current date and time?
# import datetime 

# print(datetime.datetime.today())

# 6: What is the difference between the year attribute and the isocalendar method?
'''
from datetime import date

today = date.today()

today_year = today.year # just returns the year
iso_year = today.isocalendar()[0] # returns a tuple containing ISO year/week number/ weekday
'''
# 7: How many arguments does the str.join method expect? What happens if you call it with fewer or more arguments?
'''
It is used to concatenate all elements from an iterable, so just one argument.
'''

# 8: Using the official Python documentation, can you determine how to check whether a string contains a specific substring?
"""
string = "Hello, World!"
print("World" in string)  # True
print("Python" in string) # False
"""

# 9: What does a SyntaxError indicate? Try running the above code, then use the resulting error message to fix the error.
'''
speed_limit = 60
current_speed = 80

if current_speed > speed_limit:
    print('"People are so bad at driving cars that '
          "computers don\'t have to be that good to be "
          'much better." -- Marc Andreessen')
    
# the SyntaxError indicates that the program expected a ":" following the conditional
'''

# 10: What does a TypeError indicate? Try running the above code, then use the resulting error message to determine exactly what is wrong. (You don't have to fix this code.)

tweet = 'Woohoo! :-)'

if len(tweet) > 140:
    print('Tweet is too long!')

length_of_tweet = len(tweet + 5)

# you cannot concatenate a str and an int inside of the length_of_tweet parenthesis
