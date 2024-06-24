#if,elif,else
#exercise 1

# Define the base price of the movie
base_price = 2000

# Define a function to determine the movie price based on age
def determine_movie_price(age, base_price):

    if age < 13:
        price = base_price - 1000  # Discount for children under 13
    elif 13 <= age <= 18:
        price = base_price - 500  # Discount for teenagers between 13 and 18

    elif 18 < age < 60:
        price = base_price  # Full price for adults between 18 and 60
        
    else:
        price = base_price + 3000  # Increased price for senior citizens
    return price

# Get age input from the user
age = int(input("Enter your age: "))

# Determine the price based on the age
price = determine_movie_price(age, base_price)

# Print the price
print(f"The price of the movie ticket is: shs {price}")

#loops(for,while)
#exercise 2

# Define a list of favorite colors
favorite_colors = ["blue", "green", "red", "purple", "orange"]

# Use a for loop to print each color in the list
print("My favorite colors are:")
for color in favorite_colors:
    print(color)

#exercise3

# Input number
number = 12345

# Initialize the reversed number to 0
reversed_number = 0

# Process the number using a while loop
while number > 0:
    digit = number % 10  # Get the last digit
    reversed_number = reversed_number * 10 + digit  # Append the digit to the reversed number
    number = number // 10  # Remove the last digit from the original number

# Print the reversed number
print(f"The reversed number is: {reversed_number}")



