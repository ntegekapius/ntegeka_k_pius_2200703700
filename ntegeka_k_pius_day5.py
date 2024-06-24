#defining functions

#function syntax and perimeters
#return values
#function lambdas

#Functions in python are define using the 'def'key word, followed by the function name and then the parethesis(),inside the parenthesis you can put the parameter name, and the colon
#example1
def multiply(a,b):
    return a*b

result = multiply(5,10)
print(result)

#example2 multiple return values
def get_coordinates():
    return 10,20
x,y = get_coordinates()
print(x,y)

#exercise1
#define a function greet with parameter name, set to 'guest', and print a message 'iam a software programmer' 

def greet(name='steka'):
    print(f"I am a software programmer",{name})
greet()  

#example3: return multiple return values

def get_name_and_position():
    name = 'steka p'
    position = "iam a software programmer"
    return name,position
name,position = get_name_and_position()
print(name,position)

"""_summary_
    def: keyword to define a function
    function name: name of the function
    parameters: optional
    """
    #syntax for defining a function
    #def function_name (parameters)

    #lambda functions
    #lambda functions are small anonymous functions defined using the lambda keyword
    #they are restricted to a single expression

    #syntax for a lambda
    #example 4: create a lambda function to add two numbers
def add(a,b) : return a+b 

print (add(45,70))

#example 5:use cases of lamba function for sorting
coordinates = [(1,2),(2,3),(3,1),(5,0)]
coordinates.sort(key=lambda coordinate:coordinate[1]) 
print(coordinates)

#map, filter and reduce
#example 6:get the squares of 1 to 5 using, map, filter and reduce
number_squares = [1,2,3,4,5]
squares = list(map(lambda x: x**2, number_squares))
print(squares)

#exercise4: define a function to get a user info that accepts arbitrary keyword arguments and prints each key value pair
def get_user_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Example usage
get_user_info(name="steka", age=30, occupation="Software Developer", location="New York")



