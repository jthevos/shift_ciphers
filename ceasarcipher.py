string = "TEBKFKQEBZLROPBLCERJXKBSBKQP"

ALPHABET="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for shift in range(1, len(ALPHABET), 1):
    result = []
    for i in range(len(string)):
        c = string[i]
        r = ALPHABET.index(c)
        r2 = (r + shift) % len(ALPHABET)
        result.append(ALPHABET[r2])

    print("Shift =", shift, "".join(map(str,result)), "\n")

#

# For N from 1 to Text Length Do
#
# Take C = Nth character of Text
#
# Calculate R = the rank of C in the alphabet
#
# Calculate R2 = (R + Shift) Modulo 26
#
# Write the letter with rank R2 in the alphabet
#
# End For Loop
