#hack the caesar cipher with brute force

message = input('Enter message to be encrypted:')

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

#use every number from 0 to 66(length of SYMBOLS) as key
for key in range(len(SYMBOLS)):
    translated = ''

    #loop go through each character in string message
    for symbol in message:
        #if character in message is also in string symbols
        if symbol in SYMBOLS:
            #find the index number where symbol is stored in symbols
            symbolIndex = SYMBOLS.find(symbol)

            #Since we are decrypting, #minus index number of symbol 
            #with key(shift left)
            translatedIndex = symbolIndex - key
            
            #if minus number < 0, plus length to return to the end
            if translatedIndex < 0:
                #eg; 11 - 13 = (-2) + 66[length] = 64 = (?)
                translatedIndex = translatedIndex + len(SYMBOLS)

            #Lastly, find the value of character with 
            #new index number(after added/minus) in symbols
            #and stored in translated.
            translated = translated + SYMBOLS[translatedIndex]

        #if character is not in symbols(eg; %), it will be stored in translated without being encrypted/decrypted
        else:
            translated = translated + symbol

    #print every possible output could be
    print('Key #%s: %s' % (key, translated))
