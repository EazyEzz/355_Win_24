# Queens College
# Internet and Web Technology (CSCI 355)
# Winter 2024
# Assignment 9 - Error Detection and Correction
# Essmer Sanchez
# Collaboration: Worked With Class
from random import random, randint


# [1] Define a function random_bits(n, p = 0.5) that computes a random bit string of length n. The additional,
# optional parameter p specifies the probability of generating a 1, defaulted to 0.5
def random_bits(n, p):
    return "".join(["1" if random() < p else "0" for _ in range(n)])


# [2] Define functions that implement each of the four error-detection algorithms:
#
# ed_parity_1d
# ed_parity_2d
# ed_checksum
# ed_crc
def ed_parity_1d(bits, even=True):
    parity_even = (sum([int(b) for b in bits]) % 2) == 0
    parity_bit = 0 if parity_even == even else 1
    print("ed_parity_1d", bits, even, parity_bit)
    return parity_bit


def ed_parity_2d(bits, width, even=True):
    n = len(bits)
    cols = width
    rows = n // cols  # floor division
    rect_1 = [bits[i * cols: (i + 1) * cols] for i in range(rows)]
    rect_2 = ["".join(rect_1[i][j] for i in range(len(rect_1))) for j in range(cols)]
    parity_rows = [ed_parity_1d(s, even) for s in rect_1]
    parity_cols = [ed_parity_1d(s, even) for s in rect_2]
    print("ed_parity_2d", bits, even, parity_rows, parity_cols)
    return parity_rows, parity_cols


def ed_checksum(bits):
    n = len(bits)
    m = n // 2
    r1, r2 = bits[:m], bits[m:]
    c = 0
    res = ""
    for j in range(m - 1, -1, -1):
        b1, b2 = int(r1[j]), int(r2[j])
        s = b1 + b2 + c
        c = 1 if s > 1 else 0
        s = s - 2 * c
        res = str(s) + res
    comp = "".join(["1" if res[i] == "0" else "0" for i in range(len(res))])
    print("ed_checksum", bits, res, comp)
    return comp


def xor(a, b):
    return [0 if a[i] == b[i] else 1 for i in range(1, len(b))]


def mod2div(dividend, divisor):
    pick = len(divisor)
    tmp = dividend[0: pick]
    while pick < len(dividend):
        if tmp[0] == 1:
            tmp = xor(divisor, tmp) + [dividend[pick]]
        else:
            tmp = xor([0] * pick, tmp) + [dividend[pick]]
        pick += 1
    if tmp[0] == 1:
        tmp = xor(divisor, tmp)
    else:
        tmp = xor([0] * pick, tmp)
    checkword = tmp
    return checkword


def ed_crc(bits, key):
    data = [int(b) for b in bits]
    key = [int(k) for k in key]
    l_key = len(key)
    new_data = data + [0] * (l_key - 1)
    remainder = mod2div(new_data, key)
    codeword = data + remainder
    print("ed_crc", bits, key, "Remainder: ", remainder, "Encoded Data (Data + Remainder): ", codeword)


def change_bits(bits, m):
    list_bits = [*bits]
    for i in range(m):
        j = randint(0, len(list_bits) - 1)
        list_bits[j] = "1" if list_bits[j] == "0" else "0"
    return "".join(list_bits)


def main():
    # chapter 6, slide 13, ex 1
    bits = "0111000110101011"
    ed_parity_1d(bits, True)
    print()

    # chapter 6 slides 13 ex 2
    bits_2 = "10101" + "11110" + "01110"
    parity_rows, parity_cols = ed_parity_2d(bits_2, 5, True)
    bits_2c = change_bits(bits_2, 1)
    parity_rows_c, parity_cols_c = ed_parity_2d(bits_2c, 5, True)
    for i in range(len(parity_rows)):
        if parity_rows[i] != parity_rows_c[i]:
            print("Mismatch Found In Row: ", i+1)
    for j in range(len(parity_cols)):
        if parity_cols[j] != parity_cols_c[j]:
            print("Mismatch Found In Col: ", j+1)
    print()

    # chapter 3 slide 38
    bits_3 = "1110011001100110" + "1101010101010101"
    ed_checksum(bits_3)
    print()

    # https://www.geeksforgeeks.org/modulo-2-binary-division/
    bits_4 = "100100"
    key = "1101"
    ed_crc(bits_4, key)


if __name__ == '__main__':
    main()
