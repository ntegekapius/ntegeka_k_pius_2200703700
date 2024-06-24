#error handling in python
#exception handling with try, except, else, and finally
#custom exceptions

"""_summary_
notes
error handling in python helps to handle un expected situations and errors
1.try: contains code that might throw an exception
NB: if an exception occurs the reset of the code in the try block is skipped of ignored

2.except: catches and handles exceptions 
NB: you can specify different handlers of different exceptions type

3.else: the code runs if no exception occurs 
if no exception raised in the try block it runs

4.finally: it runs wheather an exception is raised/occured or not
NB: used for cleaning up actions
"""
#example1: handle exceptions with division by zero
try:
    number =  int (input('enter a number: '))
    result = 20 / number

except ValueError:
    print("Invalid number! please enter a valid number")

except ZeroDivisionError:
    print("Error: Division By Zero is not allowed")

else:
    print(f"result is {result}")

finally:
    print("execution completed successfully")

    #exercise1: write a function that converts a string to an integer and handle both valueError if the string can not be converted as an integer and the typeError if the input is not a string.use multiple except block to handle these exceptions

def convert_to_integer():
    input_value = input("Please enter a value to convert to an integer: ")
    try:
        # Attempt to convert the input value to an integer
        result = int(input_value)
    except ValueError:
        # Handle the case where the input is a string but cannot be converted to an integer
        print("ValueError: The provided string cannot be converted to an integer.")
        return None
    except TypeError:
        # Handle the case where the input is not a string
        print("TypeError: The provided input is not a string.")
        return None
    else:
        # Executed if no exception was raised
        return result
    finally:
        
        print("Execution of convert_to_integer function is complete.")

result = convert_to_integer()
if result is not None:
    print(f"The converted integer is: {result}")

    #custom exception handling
    #example2:exception raised for error in the input, if funds are insufficient

    class InsufficientFundsError(Exception):
      def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        self.message = f"Attempt to withdraw {self.amount} with only {self.balance} in account."
        super().__init__(self.message)

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount

try:
    balance = 20000
    amount_to_withdraw = 100000
    new_balance = withdraw(balance, amount_to_withdraw)
except InsufficientFundsError as e:
    print(f'Error: {e.message}')
else:
    print(f"Withdrawal successful! New balance is {new_balance}")
finally:
    print("Transaction completed")
 


#note
"""_summary_line_
defining a custom exception

class CustomError(Exception)
#Custom Exception for specific error cases

def_init_(self, message):
super(). _init_(message)
self.message = message

raising a custom exception


"""
#exercise2: create a custom exception InvalidAgeError and write a function that raises this exception if the given age is negative. handle this custom exception when calling thw function
class InvalidAgeError(Exception):
    def __init__(self, age, message="Age cannot be negative."):
        self.age = age
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message} Given age: {self.age}"
    
def check_age(age):
    if age < 0:
        raise InvalidAgeError(age)
    else:
        print(f"The provided age is: {age}")

def main():
    try:
        age = int(input("Please enter your age: "))
        check_age(age)
    except InvalidAgeError as e:
        print(f"InvalidAgeError: {e}")
    except ValueError:
        print("ValueError: Invalid input. Please enter a valid integer.")
    else:
        print("Age input was processed successfully.")
    finally:
        print("Execution of the age check is complete.")

if __name__ == "__main__":
    main()

























        
        
   

