import random
import string

def generate_password(length=12, use_uppercase=True, use_numbers=True, use_special=True):
    """Generate a secure random password."""
    
    # Start with lowercase letters
    characters = string.ascii_lowercase
    
    # Add character types based on options
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_special:
        characters += string.punctuation
    
    # Ensure at least one character from each selected type
    password = []
    if use_uppercase:
        password.append(random.choice(string.ascii_uppercase))
    if use_numbers:
        password.append(random.choice(string.digits))
    if use_special:
        password.append(random.choice(string.punctuation))
    
    # Fill remaining length with random characters
    remaining_length = length - len(password)
    password.extend(random.choice(characters) for _ in range(remaining_length))
    
    # Shuffle to randomize position
    random.shuffle(password)
    
    return ''.join(password)

def generate_password(length=12, use_uppercase=True, use_numbers=True, use_special=True):
    """Generate a secure random password."""
    
    # Start with lowercase letters
    characters = string.ascii_lowercase
    
    # Add character types based on options
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_special:
        characters += string.punctuation
    
    # Ensure at least one character from each selected type
    password = []
    if use_uppercase:
        password.append(random.choice(string.ascii_uppercase))
    if use_numbers:
        password.append(random.choice(string.digits))
    if use_special:
        password.append(random.choice(string.punctuation))
    
    # Fill remaining length with random characters
    remaining_length = length - len(password)
    password.extend(random.choice(characters) for _ in range(remaining_length))
    
    # Shuffle to randomize position
    random.shuffle(password)
    
    return ''.join(password)

def main():
    """Main function to run the password generator."""
    print("=" * 50)
    print("🔐 Secure Password Generator 🔐")
    print("=" * 50)
    
    try:
        # Get user input
        length = int(input("\nEnter password length (8-50): "))
        
        if length < 8 or length > 50:
            print("❌ Length must be between 8 and 50 characters!")
            return
        
        # Get preferences
        use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
        use_nums = input("Include numbers? (y/n): ").lower() == 'y'
        use_special = input("Include special characters? (y/n): ").lower() == 'y'
        
        # Generate password
        password = generate_password(
            length=length,
            use_uppercase=use_upper,
            use_numbers=use_nums,
            use_special=use_special
        )
        
        # Display result
        print("\n" + "=" * 50)
        print(f"✅ Your Generated Password:")
        print(f"   {password}")
        print("=" * 50)
        
    except ValueError:
        print("❌ Invalid input! Please enter a number for length.")
    except Exception as e:
        print(f"❌ An error occurred: {e}")

if __name__ == "__main__":
    main() 
    """Main function to run the password generator."""
    print("=" * 50)
    print("🔐 Secure Password Generator 🔐")
    print("=" * 50)
    
    try:
        # Get user input
        length = int(input("\nEnter password length (8-50): "))
        
        if length < 8 or length > 50:
            print("❌ Length must be between 8 and 50 characters!")
    
        
        # Get preferences
        use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
        use_nums = input("Include numbers? (y/n): ").lower() == 'y'
        use_special = input("Include special characters? (y/n): ").lower() == 'y'
        
        # Generate password
        password = generate_password(
            length=length,
            use_uppercase=use_upper,
            use_numbers=use_nums,
            use_special=use_special
        )
        
        # Display result
        print("\n" + "=" * 50)
        print(f"✅ Your Generated Password:")
        print(f"   {password}")
        print("=" * 50)
        
    except ValueError:
        print("❌ Invalid input! Please enter a number for length.")
    except Exception as e:
        print(f"❌ An error occurred: {e}")

if __name__ == "__main__":
    main()
