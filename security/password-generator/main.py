import string
import secrets


print('=== Password Generator ===')

characters = ''
password = ''
num_characters = int(input('Quantos caracteres deseja na senha? ').strip())
include_lowercase = input('Incluir letras minúsculas? (s/n) ').strip().lower()
include_uppercase = input('Incluir letras maiúsculas? (s/n) ').strip().lower()
include_numbers = input('Incluir números? (s/n) ').strip().lower()
include_symbols = input('Incluir símbolos? (s/n) ').strip().lower()



if include_lowercase == 's':
    characters += string.ascii_lowercase

if include_uppercase == 's':
    characters += string.ascii_uppercase

if include_numbers == 's':
    characters += string.digits

if include_symbols == 's':
    characters += string.punctuation

print(f'Caracteres Selecionados: {characters}')


# Quando precisamos apenas repetir uma operação, existe uma convenção em Python que utiliza _ (underscore) no lugar de uma variável cujo valor não será utilizado.
for _ in range(num_characters):
    password += secrets.choice(characters)


print(f'Senha Gerada: {password}')
print(f'Quantidade de caracteres: {len(password)}')
