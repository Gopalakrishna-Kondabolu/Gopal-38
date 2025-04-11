import random
import string
import time
import sys

# Function to generate a strong password based on user requirements
def generate_password(length=12, use_uppercase=True, use_numbers=True, use_special=True):
    # Create a pool of characters based on the user's choices
    characters = string.ascii_lowercase  # Start with lowercase letters
    
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_special:
        characters += string.punctuation
    
    # Generate a random password from the selected pool of characters
    return ''.join(random.choice(characters) for i in range(length))

# Function to ask the user for their password requirements
def get_user_requirements():
    # Ask for the password length
    while True:
        try:
            length = int(input("Enter desired password length (e.g., 12): "))
            if length < 8:  # Minimum length for a strong password
                print("Password length should be at least 8 characters.")
            else:
                break
        except ValueError:
            print("Please enter a valid number.")
    
    # Ask whether to include uppercase letters
    use_uppercase = input("Include uppercase letters? (yes/no): ").strip().lower() == 'yes'
    
    # Ask whether to include numbers
    use_numbers = input("Include numbers? (yes/no): ").strip().lower() == 'yes'
    
    # Ask whether to include special characters
    use_special = input("Include special characters? (yes/no): ").strip().lower() == 'yes'
    
    return length, use_uppercase, use_numbers, use_special

# Function for animated password generation based on user's input
def animated_password_generator():
    print("Welcome to the Animated Password Generator!")
    
    # Get the user's password requirements
    length, use_uppercase, use_numbers, use_special = get_user_requirements()

    # Generate the password based on user's input
    password = generate_password(length, use_uppercase, use_numbers, use_special)
    
    # Start the animated typing effect
    print("\nGenerating your password...\n")
    
    animated_str = ""
    for i in range(len(password) + 1):
        animated_str = password[:i]
        sys.stdout.write("\rPassword: " + animated_str)
        sys.stdout.flush()  # Ensure the output is printed immediately
        time.sleep(0.1)  # Delay for animation effect
    
    print("\n\nPassword generated successfully!")
    print(f"Your password is: {password}")

# Run the password generator with animation
animated_password_generator()
