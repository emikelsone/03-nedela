def is_email_valid(email):
    """Pārbaude, vai šis ir derīgs e-pasta formāts."""
    if '@' in email and '.' in email:
        return True
    return False
print(is_email_valid("test@example.com"))
print(is_email_valid("annina"))
print(is_email_valid("john.doe@domain"))

def is_password_strong(password):
    """Pārbaude, vai parole ir stipra (vismaz 8 simboli, lielie un mazie burti, cipari)."""
    if len(password) < 8:
        return False
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    return has_upper and has_lower and has_digit
print(is_password_strong("Parole123"))
print(is_password_strong("weakpass"))
print(is_password_strong("Short1"))

def is_phone_number(text):
    """Pārbauda, vai tas ir Latvijas tel. numurs (var sākties ar +371 un satur tikai ciparus)."""
    if text.startswith('+371 '):
        text = text[5:]

        if len(text) == 8 and text.isdigit():
            return True
    return False

print(is_phone_number("+371 12345678"))
print(is_phone_number("12345678"))
print(is_phone_number("+371 1234abcd"))

def is_valid_age(age):
    """Pārbauda, vai vecums ir skaitlis starp 0 un 120."""
    if isinstance(age, int) and 0 <= age <= 120:
        return True
    return False

print(is_valid_age(25))
print(is_valid_age(-5))
print(is_valid_age(150))

def is_valid_date(text):
    """Pārbauda, vai datums ir formātā DD/MM/YYYY."""
    import re
    pattern = r'^\d{2}/\d{2}/\d{4}$'
    if re.match(pattern, text):
        return True
    return False

print(is_valid_date("01/01/2020"))
print(is_valid_date("32/01/2020"))
print(is_valid_date("01/01/20"))
