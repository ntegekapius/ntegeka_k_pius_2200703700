#dictionaries
#creating and using dictionaries
#dictionary methods and operations
"""_summary_
dictionaries in python are collections of keys and values
-unordered
-mutable and 
-indexed by keys
"""
#example 1: create a dictionary
#create a dictionary of a student pursuing software engineering, the key must be your name, age, technology interest course and year of study, put your own details
student_dict = {
    'name' : 'steka',
    'age' : '23',
    'technology' : 'AI and MI',
    'course' : 'BSSE', 
    'year' : '3'
     
}
print(student_dict['age'])
#access value
#exercise1
#modify age and technology
student_dict['age'] = 40
print(student_dict['age'])

student_dict['technology'] = 'web developing'
print(student_dict['technology'])

#example2: adding keys and values
student_dict['email'] = 'stekapius7@gmail.com'
print(student_dict['email'])

#exercise2
#remove key and value
del student_dict['course']
print(student_dict) 

#common dictionary methods
"""_summary_
get()//returns the value for the specified key if the key is in the dictionary
if not it returns the default value
update() //updates the dictionary with the elements from another dictionary
pop() //removes the specified key and return the corresponding value

"""
#example3: use the get method to get the value
print(student_dict.get('technology'))

#exercise3: use the update method to change value in age
student_dict.update({'age': '24'})
print(student_dict)
#exercise4: use the if to check if the key 'age' is present in the dictionary
# Check if 'age' key is present
if 'age' in student_dict:
    # Update the age
    student_dict['age'] = '24'
else:
    print("The key 'age' is not present in the dictionary.")

    #keys(), values(), items() methods
    print(student_dict.keys())
    print(student_dict.values())
    print(student_dict.items())

    """_summary_
    key() //returns a view of objects that displays a list of all keys 
    value() //returns a view of objects that displays a list of all values
    items() //returns a view of objects that displays a list of dicitonary keys and value

    
    """
    #exercise 5
    #use the update method to change the course and add a new key like "whatsapp_number"to the dictionary
    student_dict = {
    'name': 'steka',
    'age': '23',
    'technology': 'AI and MI',
    'course': 'BSSE', 
    'year': '3'
}
    student_dict.update({'year': 'PAYO', 'whatsapp_number': '0763217749'})

# Print the updated dictionary
print(student_dict)