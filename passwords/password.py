import random

def generate_password(length=12):
    if length < 6:
        raise ValueError("Password length should be at least 6 characters.")

    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits = '0123456789'

    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits)
    ]

    all_chars = lowercase + uppercase + digits
    password += random.choices(all_chars, k=length - 3)

    random.shuffle(password)

    return ''.join(password)

print("Generated password:", generate_password(12))
