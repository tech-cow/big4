# Description:
#
# For building the encrypted string:
# Take every 2nd char from the string, then the other chars, that are not every 2nd char, and concat them as new String.
# Do this n times!

# Example
#"This is a test!", 1 -> "hsi  etTi sats!"
#"This is a test!", 2 -> "hsi  etTi sats!" -> "s eT ashi tist!"

# What I learned?
    # 1. :: explain:   https://stackoverflow.com/questions/3453085/what-is-double-colon-in-python-when-subscripting-sequences/3453102#3453102
    # 2. usage of _ in a for loop: to temporarily holds an index for formating that won't be using in a loop
    
def decrypt(text, n):
    if not text: return text
    i, l = len(text) / 2 , list(text)
    for _ in range(n):
        l[1::2], l[::2] = l[:i], l[i:]
    return ''.join(l)


def encrypt(text, n):
    if not text: return text
    for _ in range(n): #brilliant use of _, because index isn't used, _ is to fill
        text = text[1::2] + text[::2]
    return text
