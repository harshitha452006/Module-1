""" Question 11: atbash_encrypt """
"""
Input: string
Output: string encoded using atbash encryption
"""
import string
def convert_char(c):
    if not c.isalpha():
        return c
    if c.islower():
        alph = string.ascii_lowercase
    else:
         alph = string.ascii_uppercase
    reverse_alph = alph[::-1]

    index = alph.find(c)
    enc_char = reverse_alph[index] 
    return enc_char



def atbash_encrypt(message):
    result = ""
    for c in message:
        result += convert_char(c)
    return result 

""" Test 11 """
def test_atbash_encrypt():
    print("Testing atbash_encrypt...", end='')
    assert(atbash_encrypt("Hello") == "Svool")
    assert(atbash_encrypt("night!") == "mrtsg!")
    assert(atbash_encrypt("Coding is fun :)") == "Xlwrmt rh ufm :)")
    assert(atbash_encrypt("") == "")
    print("... done!")

if __name__ == '__main__':
    test_atbash_encrypt()