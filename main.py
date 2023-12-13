from string import ascii_letters

ALPHABET = list(ascii_letters)

message = input("Введите сообщение: ")
key = input("Введите приватный ключ: ")

key_message = (key * 10)[:len(message)]
encrypted_message = ''

for i in range(len(message)):
    letter_index_message = ALPHABET.index(message[i])
    letter_index_key = ALPHABET.index(key_message[i])
    letter_index = letter_index_message + letter_index_key

    if letter_index > len(ALPHABET):
        letter_index -= len(ALPHABET)

    encrypted_message += ALPHABET[letter_index]

print(f'Зашифрованное сообщение: {encrypted_message}')