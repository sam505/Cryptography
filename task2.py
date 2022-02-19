"""
Playfair Encryption and Decryption
"""

import string

key = "Kathy"
cipher_text = ""
decoded_text = ""


def matrix(x, y, initial):
    """
    Make the matrix
    :param x:
    :param y:
    :param initial:
    :return:
    """
    return [[initial for i in range(x)] for j in range(y)]


result = list()
for c in key.upper():  # storing key
    if c not in result:
        if c == 'J':
            result.append('I')
        else:
            result.append(c)
flag = 0
for i in range(65, 91):  # storing other character
    if chr(i) not in result:
        if i == 73 and chr(74) not in result:
            result.append("I")
            flag = 1
        elif flag == 0 and i == 73 or i == 74:
            pass
        else:
            result.append(chr(i))
k = 0
enc_matrix = matrix(5, 5, 0)  # initialize matrix
for i in range(0, 5):  # making matrix
    for j in range(0, 5):
        enc_matrix[i][j] = result[k]
        k += 1


def locate_index(c):  # get location of each character
    """
    Locates index of characters
    :param c:
    :return:
    """
    loc = list()
    if c == 'J':
        c = 'I'
    for i, j in enumerate(enc_matrix):
        for k, l in enumerate(j):
            if c == l:
                loc.append(i)
                loc.append(k)
                return loc


def encrypt():  # Encryption
    """
    Encryption function
    """
    global cipher_text
    msg = "We have a very hot summer in Saudi Arabia."
    msg = msg.translate(str.maketrans('', '', string.punctuation))  # Remove punctuation
    msg = msg.upper()
    msg = msg.replace(" ", "")
    print(msg)
    i = 0
    for s in range(0, len(msg) + 1, 2):
        if s < len(msg) - 1:
            if msg[s] == msg[s + 1]:
                msg = msg[:s + 1] + 'X' + msg[s + 1:]
    if len(msg) % 2 != 0:
        msg = msg[:] + 'X'
    print("CIPHER TEXT:", end=' ')
    while i < len(msg):
        loc = list()
        loc = locate_index(msg[i])
        loc1 = list()
        loc1 = locate_index(msg[i + 1])
        if loc[1] == loc1[1]:
            cipher_text += "{}{} ".format(enc_matrix[(loc[0] + 1) % 5][loc[1]], enc_matrix[(loc1[0] + 1) % 5][loc1[1]])
        elif loc[0] == loc1[0]:
            cipher_text += "{}{} ".format(enc_matrix[loc[0]][(loc[1] + 1) % 5], enc_matrix[loc1[0]][(loc1[1] + 1) % 5])
        else:
            cipher_text += "{}{} ".format(enc_matrix[loc[0]][loc1[1]], enc_matrix[loc1[0]][loc[1]])
        i += 2
    print(cipher_text)


def decrypt():
    """
    Decryption
    """
    global decoded_text
    msg = cipher_text
    msg = msg.upper()
    msg = msg.replace(" ", "")
    print("PLAIN TEXT:", end=' ')
    i = 0
    while i < len(msg):
        loc = list()
        loc = locate_index(msg[i])
        loc1 = list()
        loc1 = locate_index(msg[i + 1])
        if loc[1] == loc1[1]:
            decoded_text += "{}{}".format(enc_matrix[(loc[0] - 1) % 5][loc[1]], enc_matrix[(loc1[0] - 1) % 5][loc1[1]])
        elif loc[0] == loc1[0]:
            decoded_text += "{}{}".format(enc_matrix[loc[0]][(loc[1] - 1) % 5], enc_matrix[loc1[0]][(loc1[1] - 1) % 5])
        else:
            decoded_text += "{}{}".format(enc_matrix[loc[0]][loc1[1]], enc_matrix[loc1[0]][loc[1]])
        i += 2

    print(decoded_text)


def main():
    """
    Main function
    """
    encrypt()
    decrypt()


if __name__ == "__main__":
    main()
