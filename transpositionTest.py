import random, sys, transpositionEncrypt, transpositionDecrypt

#A program to test our encryption/decryption program

def main():
    #a starter so it will be able to generate random
    #number using random.randint()
    random.seed(42)

    #loop 20 times
    for i in range(20):
        #stored string (A-Z) * random in var message 
        message = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' * random.randint(4,40)
        #stored each string in list
        message = list(message)
        #randomly shuffle the order of each character of string in list
        random.shuffle(message)
        #combine all list in message
        message = ''.join(message)

        #print all output of message until 50 character
        print('Test #%s: "%s..."' % (i + 1, message[:50]))

        #for loop of possible key from 1 until half of message
        for key in range(1,int(len(message)/2)):
            #call encrypt function to encrypt message and store in encrypted
            encrypted = transpositionEncrypt.encryptMessage(key,message)
            #call decrypt function to decrypt message and store in decrypted
            decrypted = transpositionDecrypt.decryptMessage(key,encrypted)

            #if value of decrypted and original message is not same:
            #Means program encryption or decryption didnt work
            if message!= decrypted:
                print('Mismatch with key %s and message %s.' % (key,message))
                print('Decrypted as: ' + decrypted)
                sys.exit()
                
    print('Transposition cipher test passed.')

if __name__ == '__main__':
    main()