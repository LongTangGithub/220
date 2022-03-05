def encode(message, key):
    msg = message
    k = key

    cipher = "".join(chr(ord(c) + int(k)) for c in msg)
    return cipher


def encode_better(message, key):
    msg = message
    k = key

    newEncoded = []  # initialize list
    newResult = " "

    for i in range(len(msg)):  # loop every character of message and key
        newEncoded.append(((ord(msg[i]) - 65) + (ord(k[i % len(k)]) - 65)) % 58)  # add the unicode of the
        # first index i in the message and key together then mod 58

    for i in newEncoded:
        newResult += chr(int(i) + 65) + ""  # take the new result from newEncoded, apply chr, and 65; "" to make it
        # no space

    return newResult  # make the new result return as a string
