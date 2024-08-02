import random
import string

def generate_random_name(length=10):
    name = ''.join(random.choices(string.ascii_uppercase, k=1))
    name += ''.join(random.choices(string.ascii_lowercase, k=length - 1))
    return name

def generate_random_email(length=10):
    username_length = random.randint(5, length - 5)
    domain_length = length - username_length
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=username_length))
    domain = ''.join(random.choices(string.ascii_lowercase, k=domain_length))
    email = f"{username}@{domain}.com"
    return email

def generate_random_password(length=10):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(characters, k=length))
    return password

name = generate_random_name(random.randint(10, 20))
email = generate_random_email(random.randint(10, 20))
password = generate_random_password(random.randint(10, 20))

print(f"Nombre aleatorio: {name}")
print(f"Correo aleatorio: {email}")
print(f"Contraseña aleatoria: {password}")
