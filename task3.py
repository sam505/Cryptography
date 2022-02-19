import string


def generate_key(string, key):
    """
    Generateds the enc/dec key
    """
    key = list(key)
    if len(string) == len(key):
        return key
    else:
        for i in range(len(string) -
                       len(key)):
            key.append(key[i % len(key)])
    return "".join(key)


def encode(string, key):
    """
    Encode function
    """
    cipher_text = []
    for i in range(len(string)):
        x = (ord(string[i]) +
             ord(key[i])) % 26
        x += ord('A')
        cipher_text.append(chr(x))
    return "".join(cipher_text)


def decode(cipher_text, key):
    """
    Decode function
    """
    orig_text = []
    for i in range(len(cipher_text)):
        x = (ord(cipher_text[i]) -
             ord(key[i]) + 26) % 26
        x += ord('A')
        orig_text.append(chr(x))
    return "".join(orig_text)


def main():
    """
    Driver code
    """
    msg = "We have a very hot summer in Saudi Arabia."
    msg = msg.translate(str.maketrans('', '', string.punctuation))  # Remove punctuation
    msg = msg.upper()
    msg = msg.replace(" ", "")
    key = "KATHYBLAQ"
    key = generate_key(msg, key)
    cipher_text = encode(msg, key)
    print("Ciphertext :", cipher_text)
    print("Decrypted Text :", decode(cipher_text, key))


if __name__ == "__main__":
    main()
