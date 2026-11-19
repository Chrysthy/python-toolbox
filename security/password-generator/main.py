import string
import secrets


print('=== Password Generator ===')

characters = string.ascii_letters + string.digits + string.punctuation
num_characters = int(input('Quantos caracteres deseja na senha? '))
password = ''


print(f'Caracteres disponíveis: {characters}')
# print(len(characters))

# Quando precisamos apenas repetir uma operação, existe uma convenção em Python que utiliza _ (underscore) no lugar de uma variável cujo valor não será utilizado.
for _ in range(num_characters):
    password += secrets.choice(characters)


print(f'Senha Gerada: {password}')
print(f'Quantidade de caracteres: {len(password)}')
