"""
Title: caeser_cipher.py
Author: Dr Leanne J Dong
Description: This program is to develop basic coding skill by making a small game
to replicate the classic caesar encryption& decryption. This program utilises previously
learned concepts such as variables, operations, conditional statements, loops and function
"""

"""
coding logic:
Encryption: iterate through plaintext and replace each letter with its corresponding letter from the key
Decryption: Just call the encrypt with -shifting backward to decrypt
"""

def caesar_encrypt(plaintext,shift):
    """
    Encrypt plaintext using Caesar

    """
    ciphertext = ''
    for char in plaintext: #look over each letter in our original msg one by one
      if char.isalpha():   # check if the current thing is a letter (a-z or A-Z) 
        start = ord('a') if char.islower() else ord('A') #figure out small or big letter to know where to count from
        #the clever part does the shifting. 
        shifted_char = chr((ord(char)-start + shift)%26 + start)
        ciphertext +=shifted_char
                           
      elif char.isdigit(): #check if the number within (0-9)
        shifted_digit = str((int(char)+shift)%10) #does the similar shift by wrap around 9
        ciphertext+=shifted_digit
      else:
        ciphertext +=char #if it is not a letter or number we just keep it same
    return ciphertext  #binggo your secret message
 								
def caesar_decrypt(ciphertext, shift):
	return caesar_encrypt(ciphertext, -shift)
								
								
# -- let's try!---
            
message = "Hello Brisbane farm"
key = 3
encrypted_message = caesar_encrypt(message,key)
print(f"Original message:{message}")
print(f"Encrypted message (shift{key}): {encrypted_message}")

decrypted_message = caesar_decrypt(encrypted_message, key)
print(f"Decrypted message:{decrypted_message}")						   










# --- Let's test it ---

messaage = " Good Morning Brisbane 3"
key = 3
encrypted_msg = caesar_encrypt(message,key)
print(f"Original message:{message}")
