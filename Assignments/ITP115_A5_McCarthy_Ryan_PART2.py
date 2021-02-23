# Ryan McCarthy, rbmccart@usc.edu
# ITP 115, Fall 2020
# Assignment 5
# Description:
# this program creates a unbreakable cipher for messages given by the user based on a shift amount
# also given by the user :)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
            'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b',
            'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

message = input("What is your message: ").lower()
shift = int(input("Enter a shift number (0-25): "))
encrypt = ""
decrypt = ""
l_message = list(message)

for char in message:
    try:
        pos = alphabet.index(char) + shift
        n_char = alphabet[pos]
        encrypt += n_char
    except ValueError:
        encrypt += char
        continue
    except IndexError:
        exit("Try again! Follow the rules for the shift!!!")
for char in encrypt:
    try:
        pos = alphabet.index(char) - shift
        n_char = alphabet[pos]
        decrypt += n_char
    except ValueError:
        decrypt += char
        continue

print("Encrypting...")
print("Encrypted message:", encrypt)
print("Decrypting...")
print("Decrypted message:", decrypt)
print("Original message:", message)
