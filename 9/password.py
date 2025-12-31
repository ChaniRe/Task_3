import re

def is_strong_password(password):
    #Minimum length of 8 characters
    if len(password) < 8:
        return False

    #Check for lowercase, uppercase, and digits
    if not any(c.islower() for c in password): return False
    if not any(c.isupper() for c in password): return False
    if not any(c.isdigit() for c in password): return False
    
    #Check for at least 1 special character using 're'
    #This looks for any character that is NOT a letter or a number
    if not re.search(r"[^a-zA-Z0-9]", password): 
        return False

    #Check that a character is not repeated more than twice (e.g., no "aaa")
    for i in range(len(password) - 2):
        if password[i] == password[i+1] == password[i+2]:
            return False

    #Check for sequences of 3 consecutive characters (e.g., no "abc" or "123")
    for i in range(len(password) - 2):
        char1 = ord(password[i])
        char2 = ord(password[i+1])
        char3 = ord(password[i+2])
        if char2 == char1 + 1 and char3 == char2 + 1:
            return False

    return True

# Test
password_input = "A!bc12aa"
print(is_strong_password(password_input))