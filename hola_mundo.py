# Indicar al usuario que ingrese una palabra
# y asignarlo a la variable user_word.
user_word = input("Ingrese una palabra:")
user_word = user_word.upper()
for letter in user_word:
    if letter == 'A':
        continue
    if letter == 'E':
        continue
    if letter == 'I':
        continue
    if letter == 'O':
        continue
    if letter == 'U':
        continue
    print(letter)
    # Completa el cuerpo del bucle for.