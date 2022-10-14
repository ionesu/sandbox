def Encrypt(message, key):
    alphabet = sorted(key)
    encryption = ''

    for i in message:
        if i.islower():
            a_index = alphabet.index(i.upper())
            encryption += key[a_index].lower()
        elif i.isupper():
            a_index = alphabet.index(i)
            encryption += key[a_index]
        else:
            encryption += i

    return encryption


def Decrypt(message, key):
    alphabet = sorted(key)
    decrypted = ""

    for i in message:
        if i.islower():
            a_index = key.index(i.upper())
            decrypted += alphabet[a_index].lower()
        elif i.isupper():
            a_index = key.index(i)
            decrypted += alphabet[a_index]
        else:
            decrypted += i

    return decrypted
