import math
import string

key = "123456789"


def encrypt(msg):
    """
    Encryption
    """
    cipher = ""

    idx = 0

    msg_len = float(len(msg))
    msg_lst = list(msg)
    key_lst = sorted(list(key))

    col = len(key)

    row = int(math.ceil(msg_len / col))

    fill_null = int((row * col) - msg_len)
    msg_lst.extend('_' * fill_null)

    matrix = [msg_lst[i: i + col]
              for i in range(0, len(msg_lst), col)]

    for _ in range(col):
        curr_idx = key.index(key_lst[idx])
        cipher += ''.join([row[curr_idx]
                           for row in matrix])
        idx += 1

    return cipher


def decrypt(cipher):
    """
    Decryption
    """
    msg = ""

    k_indx = 0

    msg_indx = 0
    msg_len = float(len(cipher))
    msg_lst = list(cipher)

    col = len(key)

    row = int(math.ceil(msg_len / col))

    key_lst = sorted(list(key))

    dec_cipher = []
    for _ in range(row):
        dec_cipher += [[None] * col]

    for _ in range(col):
        curr_idx = key.index(key_lst[k_indx])

        for j in range(row):
            dec_cipher[j][curr_idx] = msg_lst[msg_indx]
            msg_indx += 1
        k_indx += 1

    try:
        msg = ''.join(sum(dec_cipher, []))
    except TypeError:
        raise TypeError("This program cannot",
                        "handle repeating words.")

    null_count = msg.count('_')

    if null_count > 0:
        return msg[: -null_count]

    return msg


def main():
    """
    Driver Code
    """
    msg = "We have a very hot summer in Saudi Arabia."
    msg = msg.translate(str.maketrans('', '', string.punctuation))  # Remove punctuation
    msg = msg.upper()
    msg = msg.replace(" ", "")
    cipher = encrypt(msg)
    print("Cipher Text: {}".format(cipher))
    print("Decrypted Text: {}".format(decrypt(cipher)))


if __name__ == "__main__":
    main()
