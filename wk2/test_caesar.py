from ccipher import caesar_encrypt
from ccipher import caesar_decrypt

def test_caeser_encrypt():
    assert caesar_encrypt("ABC",1) == "BCD"
    assert caesar_encrypt("abc",3) == "def"
    assert caesar_encrypt("Hello, World!", 5) == "Mjqqt, Btwqi!"
    
def test_caeser_decrypt():
    assert caesar_decrypt("BCD", 1) == "ABC"
    assert caesar_decrypt("def", 3) == "abc"
    assert caesar_decrypt("Mjqqt, Btwqi!", 5) == "Hello, World!"
    
