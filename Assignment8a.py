# Queens College
# Internet and Web Technology (CSCI 355)
# Winter 2024
# Assignment 8a - Encryption and Decryption Part A
# Essmer Sanchez
# Collaboration: Worked With Class
import math


# [1] Download the input file “Encrypted.txt” from Google Drive > Assignments and place it in your PyCharm folder.
# [2] Write a function read_file(file_name) which will read the file from your drive and return its contents as a
# string variable.
def read_file(file_name):
    with open(file_name) as f:
        return f.read()


def write_file(file_name, text):
    with open(file_name, "w") as f:
        f.write(text)


# [3] Create a letter-frequency list based on the chart at https://en.wikipedia.org/wiki/Letter_frequency:
# (The frequency of E has been adjusted from 13.0 to 12.581 to compensate for rounding of other frequencies)
freqs_expected = [8.2, 1.5, 2.8, 4.3, 12.581, 2.2, 2.0, 6.1, 7.0, 0.15, 0.77, 4.0, 2.4,
                  6.7, 7.5, 1.9, 0.095, 6.0, 6.3, 9.1, 2.8, 0.98, 2.4, 0.15, 2.0, 0.074]


# [4]  Write a function distance(x, y), defined as sqrt[(x[0] - y[0])2 + (x[1] - y[1])2 + … + (x[n-1] - y[n-1])2]
# where n is the length of x and y. Use a for-loop. You will need the sqrt function, so “import math” at the
# beginning of your code.
def distance(x, y):
    return math.sqrt(sum([(x[i] - y[i]) ** 2 for i in range(len(x))]))


# [5] Write a function count_letters(text) to determine the frequency of each letter and place it in a list called
# actual_freqs.
def calc_freqs(text):
    freqs = [0] * 26
    for c in text:
        freqs[ord(c) - ord('A')] += 1
    n = len(text)
    freqs = [100 * freqs[i] / n for i in range(26)]
    return freqs


# [6] Write a function shift_char(c, shift) that shifts a character c based on a given shift variable with syntax like.
# shifted_char = chr(ord(‘A’) + ((ord(c) - ord(‘A’) + shift) % 26))
def shift_char(c, shift):
    return chr(ord('A') + ((ord(c) - ord('A') + shift) % 26))


# [7] Write a function that shift_text(text, shift) that shifts a
# text based on a given shift variable by looping over the entire text and shifts
# each character using the shift_char function from the previous task.
def shift_text(text, shift):
    return "".join([shift_char(c, shift) for c in text])


# [8] Write a function find_best_shift(text) that iterates over all
# possible shifts 0 to 25, recounts the character frequencies after the shift,
# and computes the “distance” between the expected frequencies and actual frequencies.
# If the distance for that shift is better (smaller) than the best previous distance,
# then assume that is the best shift. Once you have found the best shift, that is your decrypted text!

# [9] Write a function write_file(file_name, text) that writes the contents of the string text to the specified file.
# In this case, your output file can be called decrypted.txt
def find_best_shift(text):
    best_shift = -1
    best_dist = 99999
    for shift in range(26):
        shifted_text = shift_text(text, shift)
        freqs_shifted = calc_freqs(shifted_text)
        dist_shifted = distance(freqs_shifted, freqs_expected)
        print(shift, dist_shifted)
        if dist_shifted < best_dist:
            best_shift = shift
            best_dist = dist_shifted
    return best_shift


def main():
    text_encrypted = read_file('Assignment08e.txt')
    best_shift = find_best_shift(text_encrypted)
    text_decrypted = shift_text(text_encrypted, best_shift)
    write_file('Assignment08d.txt', text_decrypted)


if __name__ == '__main__':
    main()
