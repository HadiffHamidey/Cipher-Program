#Encryption and decryption using caesarcipher

import pyperclip

message = input('Enter message to be encrypted:')
key = 13

# Whether the program encrypts or decrypts:
mode = 'encrypt'

 # Every possible symbol that can be encrypted:
symbols = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

# Store the encrypted/decrypted form of the message:
translated = ''

#loop go through each character in string message
for symbol in message:
    #if character in message is also in string symbols
    if symbol in symbols:
        #find the index number where symbol is stored in symbols
        symbolIndex = symbols.find(symbol)

        #if the mode set to encrypt
        if mode == 'encrypt':
            #plus index number of symbol with 13(shift right)
            translatedIndex = symbolIndex + key
        
        #if the mode set to decrypt
        elif mode == 'decrypt':
            #minus index number of symbol with 13(shift left)
            translatedIndex = symbolIndex - key

        #if added index number > length, minus length to return to beginning
        if translatedIndex >= len(symbols):
            #eg; 54 + 13 = (67) - 66[length] = 1 = (B)
            translatedIndex = translatedIndex - len(symbols)
        
        #if minus number < 0, plus length to return to the end
        elif translatedIndex < 0:
            #eg; 11 - 13 = (-2) + 66[length] = 64 = (?)
            translatedIndex = translatedIndex + len(symbols)

        #Lastly, find the value of character with new index number(after added/minus) in symbols.
        translated = translated + symbols[translatedIndex]

    #if character is not in symbols(eg; %), it will be stored in translated without being encrypted/decrypted
    else:
        translated = translated + symbol

print(translated)
#to copy translated into clipboard
pyperclip.copy(translated)


