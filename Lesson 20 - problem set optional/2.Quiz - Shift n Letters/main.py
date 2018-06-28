# Write a procedure, shift_n_letters which takes as its input a lowercase
# letter, a-z, and an integer n, and returns the letter n steps in the
# alphabet after it. Note that 'a' follows 'z', and that n can be positive,
#negative or zero.

def shift_n_letters(letter, n):
    letter_index = ord(letter) - ord('a') # one of 0, 1, 2, ..., 25
    shifted_index = (letter_index + n) % 26 # still one of 0, 1, 2, ..., 25
    return chr(ord('a') + shifted_index)



print shift_n_letters('s', 1)
#>>> t
print shift_n_letters('s', 2)
#>>> u
print shift_n_letters('s', 10)
#>>> c
print shift_n_letters('s', -10)
#>>> i
