# Write a procedure, shift, which takes as its input a lowercase letter,
# a-z and returns the next letter in the alphabet after it, with 'a' 
# following 'z'.

def shift(letter):
    alphabet = "abcdefghijklmnopqrstuvwxyza"
    return alphabet[alphabet.index(letter) + 1]

#another solution:

#def shift(letter):
    #if letter == 'z':
        #return 'a'
    #else:
        #return chr(ord(letter) + 1)


print shift('a')
#>>> b
print shift('n')
#>>> o
print shift('z')
#>>> a
