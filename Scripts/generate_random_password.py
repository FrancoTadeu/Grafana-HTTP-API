import secrets
import string

def generate_random_password(length):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    return password

# Gerar um senha de 10 a 20 caracteres aleatoria
random_password = generate_random_password(secrets.choice(range(10, 21)))

print(random_password)

# In this example:

# The string.ascii_letters provides all ASCII letters (both uppercase and lowercase).
# The string.digits provides all digit characters.
# The string.punctuation provides all ASCII punctuation characters.
# secrets.choice(range(10, 21)) generates a random length between 10 and 20 characters.
#
#
# This function creates a random password by choosing characters 
#from the defined character set and repeating the process for the specified length.