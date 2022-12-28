def is_password_good(password):
    if len(password) >= 8:
        if any(i.isupper() for i in password):
            if any(j.islower() for j in password):
                if any(k.isdigit() for k in password):
                    return True
    return False

print(is_password_good(input()))