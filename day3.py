#python operators
"""_summary_
name of the operator     symbol with example
addition                   x+y
subtraction                x-y
multiplication             x*y
division                   x/y
modulus                    x%y
exponentiation             x**Y
floor division             x//y

#example of comparison operator
name of the operator              symbol with example
equal                             x==y
not equal                         x!=y
greater than                      x>y
less than                         x<y
greater than or equal to          x>=y
less than or equal to             x<=y

#example of python logical operators
name                      symbol with example
and                        and &&
or                         or  !
not                        not ~

#example of membership operators
name               symbol with example
in                  xiny
not in              x not in y
"""

#comprehensions(list, dictionary, comprehensions)
"""_summary_
coprehensions provide a concise way to create lists and dictionaries
what is the symbol for
lists       []square brackets //used to store multiple items in a single variable
dictionary  {}curly braces //used to store data values in key:value pairs

"""
#example: basic list comprehensions
#create a list of squares in range of 10
list_of_squares = [x**2 for x in range (10)]
print(list_of_squares)

#exercise1: create a list of even squares in the range of 20
even_squares = [x**2 for x in range(20) if (x**2) % 2 == 0]
print(even_squares)

#example2: dictionary comprehension
#create a dictionary comprehension for favorate cars and count the length of the characters
favorate_cars = ['BMW', 'jeep', 'mercedes', 'fordraptor']
car_lengths = {car: len(car) for car in (favorate_cars)}
print(car_lengths)

#exercise2: create a list of turple where each turple contains a number and  its cube for numbers between 1 and 10 using a dictionary comprehesion
cubes_dict = {x: x**3 for x in range(1, 11)}
cubes_list_of_tuples = list(cubes_dict.items())
print(cubes_list_of_tuples)


