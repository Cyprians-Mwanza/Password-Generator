import string

def check_password_strength(password):
    # Check if the password contains at least one uppercase letter
    has_upper = any(c.isupper() for c in password)
    # Check if the password contains at least one lowercase letter
    has_lower = any(c.islower() for c in password)
    # Check if the password contains at least one digit
    has_digit = any(c.isdigit() for c in password)
    # Check if the password contains at least one special character
    has_special = any(c in string.punctuation for c in password)

    # If the password is shorter than 8 characters, it's considered weak
    if len(password) < 8:
        return "Weak (too short)"
    # If the password contains at least one uppercase letter, one lowercase letter,
    # one digit, and one special character, it's considered strong
    if all([has_upper, has_lower, has_digit, has_special]):
        return "Strong"
    # If the password does not meet all strong criteria but is longer than 8 characters,
    # it's considered moderate
    return "Moderate"
