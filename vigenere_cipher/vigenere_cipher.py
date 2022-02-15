import random
import datetime
from names import *
from words import *


def merge_dictionaries(d1, d2):
    result = []
    for key in d1.keys():
        result.append(d1[key].upper())
    for key in d2.keys():
        result.append(d2[key].upper())
    return result


combined_keys = merge_dictionaries(names, five_letter_words)

#dict(names.items() + five_letter_words.items())

#dict(list(names.values()) + list(five_letter_words.values()))

print(combined_keys)

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

FREQUENCY_OF_CIPHER_CHARACTERS = {}
FREQUENCY_OF_ENGLISH_CHARACTERS = {}

# Taken from: https://en.wikipedia.org/wiki/Most_common_words_in_English
# increase the probability that the solution is right by checking for these
COMMON_WORDS = ["AND", "IS", "THE", "BE", "THAT", "TO", "ON", "AS", "BUT"]

CODE = "TSMVM MPPCW CZUGX HPECP RFAUE IOBQW PPIMS FXIPC TSQPK \
SZNUL OPACR DDPKT SLVFW ELTKR GHIZS FNIDF ARMUE NOSKR \
GDIPH WSGVL EDMCM SMWKP IYOJS TLVFA HPBJI RAQIW HLDGA \
IYOUX"

CODE = CODE.replace(" ", "")

KEY_LENGTH = 5  # Would this be possible without this hint?

# Found from: https://www3.nd.edu/~busiforc/handouts/cryptography/letterfrequencies.html
ENGLISH_FREQUENCY_PERCENT_DICT = {
    "A": 0.084966,
    "B": 0.020720,
    "C": 0.045388,
    "D": 0.033844,
    "E": 0.111607,
    "F": 0.018121,
    "G": 0.024705,
    "H": 0.030034,
    "I": 0.075448,
    "J": 0.001965,
    "K": 0.011016,
    "L": 0.054893,
    "M": 0.030129,
    "N": 0.066544,
    "O": 0.071635,
    "P": 0.031671,
    "Q": 0.001962,
    "R": 0.075809,
    "S": 0.057351,
    "T": 0.069509,
    "U": 0.036308,
    "V": 0.010074,
    "W": 0.012899,
    "X": 0.002902,
    "Y": 0.017779,
    "Z": 0.002722,
}

ENGLISH_FREQUENCY_DICT = {
    "A": 43.31,
    "B": 10.56,
    "C": 23.13,
    "D": 17.25,
    "E": 56.88,
    "F": 9.24,
    "G": 12.59,
    "H": 15.31,
    "I": 38.45,
    "J": 1.00,
    "K": 5.61,
    "L": 27.98,
    "M": 15.36,
    "N": 33.92,
    "O": 36.51,
    "P": 16.14,
    "Q": 1.00,
    "R": 38.64,
    "S": 29.23,
    "T": 35.43,
    "U": 18.51,
    "V": 5.13,
    "W": 6.57,
    "X": 1.48,
    "Y": 9.06,
    "Z": 1.39,
}


def ceasar_shift(shift, alphabet):
    result = []
    for i in range(len(alphabet)):
        c = alphabet[i]
        r = ALPHABET.index(c)
        r2 = (r + shift) % len(alphabet)
        result.append(alphabet[r2])
    return result


def create_alphabet_matrix():
    """Create a 26x26 matrix containing the alphabet as rows and columns"""
    matrix = []
    for i in range(26):
        temp_result = ceasar_shift(i, ALPHABET)
        matrix.append(temp_result)


def inititalize_frequency_lists():
    return dict(zip(ALPHABET, range(len(ALPHABET))))


def generate_english_character_frequencies(src_dictionary, text):
    for char in text.upper():
        if char in ALPHABET:
            index = ALPHABET.index(char)
            FREQUENCY_OF_ENGLISH_CHARACTERS[char] += 1


def generate_cipher_character_frequencies(text, list):
    global FREQUENCY_OF_CIPHER_CHARACTERS
    for char in text.upper():
        if char in ALPHABET:
            index = ALPHABET.index(char)
            FREQUENCY_OF_CIPHER_CHARACTERS[char] += 1


def map_value(value, min_value, max_value, min_result, max_result):
    # check if value is within the specified range
    if value < min_value or value > max_value:
        raise ValueError("do better")
    value = float(value)
    normal = (value - min_value) / (max_value - min_value)
    result = normal * (max_result - min_result) + min_result

    return format(result, "5f")


def key_with_max_value(src_dictionary):
    """a) create a list of the dict's keys and values;
    b) return the key with the max value"""
    v = list(src_dictionary.values())
    k = list(src_dictionary.keys())
    return [k[v.index(max(v))], max(v)]


def normalize_frequencies(src_dictionary):
    """Squishes the frequencies to the 0-1 range."""
    normalized_dict = inititalize_frequency_lists()
    max_key_value = key_with_max_value(src_dictionary)
    max_value = max_key_value[1]
    print("max_value", max_value)
    for key in src_dictionary.keys():
        normalized_value = map_value(src_dictionary[key], 0, max_value, 0, 1)
        entry = {key: normalized_value}
        normalized_dict.update(entry)

    return normalized_dict


def normalize_english_frequencies(src_dictionary):
    """Squishes the frequencies to the 0-1 range."""
    normalized_dict = inititalize_normalized_frequency_lists()

    for key in src_dictionary.keys():
        normalized_value = map_value(src_dictionary[key], 0, 56.88, 0, 1)
        entry = {key: normalized_value}
        normalized_dict.update(entry)

    return normalized_dict


def pretty_dictionary_print(src_dictionary_A, src_dictionary_B):
    for key in src_dictionary_A.keys():
        print(
            "English",
            key,
            src_dictionary_A[key],
            "Cipher",
            key,
            src_dictionary_B[key],
        )


# Taken from https://www.geeksforgeeks.org/vigenere-cipher/
def original_text(cipher_text, key):
    orig_text = []
    for i in range(len(cipher_text)):
        x = (ord(cipher_text[i]) - ord(key[i]) + 26) % 26
        x += ord("A")
        orig_text.append(chr(x))
    return "".join(orig_text)


def cipher_text(string, key):
    encoded_text = []
    for i in range(len(string)):
        x = (ord(string[i]) + ord(key[i])) % 26
        x += ord("A")
        encoded_text.append(chr(x))
    return "".join(encoded_text)


def main():
    t_zero = datetime.datetime.now()

    print("HELLO ->", cipher_text("HELLO", "ABDUL"))
    print("ABCDE ->", cipher_text("ABCDE", "ABDUL"))
    print("decipher_text(HELLO, ABDUL) -> ", original_text("HELLO", "ABDUL"))
    print("decipher_text(ABCDE, ABDUL) -> ", original_text("ABCDE", "ABDUL"))
    print(
        "decipher_text(HELLO, ABDUL) -> ",
        original_text(cipher_text("HELLO", "ABDUL"), "ABDUL"),
    )
    print("decipher_text(HELLO, ABDUL) -> ", original_text("DLGJW", "ABDUL"))
    print(
        "decipher_text(ABCDE, ABDUL) -> ",
        original_text(cipher_text("ABCDE", "ABDUL"), "ABDUL"),
    )

    global FREQUENCY_OF_CIPHER_CHARACTERS, FREQUENCY_OF_ENGLISH_CHARACTERS
    ALPHABET_MATRIX = create_alphabet_matrix()

    FREQUENCY_OF_CIPHER_CHARACTERS = inititalize_frequency_lists()
    FREQUENCY_OF_ENGLISH_CHARACTERS = inititalize_frequency_lists()

    data = CODE
    generate_cipher_character_frequencies(data, FREQUENCY_OF_CIPHER_CHARACTERS)

    normalized_cipher = normalize_frequencies(FREQUENCY_OF_CIPHER_CHARACTERS)
    normalized_english_dict = normalize_frequencies(ENGLISH_FREQUENCY_DICT)
    pretty_dictionary_print(normalized_english_dict, normalized_cipher)

    # Ensure the strings line up
    print(original_text(CODE, "ALICE" * len(CODE)))
    print(CODE)

    for key in combined_keys:
        # key = names[value].upper()
        scaled_key = key * len(CODE)
        deciphered_text = original_text(CODE, key * len(CODE))
        if "THE" == deciphered_text[0:3]:
            print("Key =", key, deciphered_text, "\n")


if __name__ == "__main__":
    main()
