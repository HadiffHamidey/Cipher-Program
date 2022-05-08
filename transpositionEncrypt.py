#Transposition cipher encryption

import pyperclip

#The function to set message and key when called
def main():
    message = "Lets try encrypt this"
    key = 8

    ciphertext = encryptMessage(key,message)
    print(ciphertext + '|')

    pyperclip.copy(ciphertext)

#The actual function that encrypt the message
def encryptMessage(key,message):
    #create an empty list
    ciphertext = [''] * key

    #loop through each key from 0 to 7
    for column in range(key):
        #set value of currentIndex to column
        currentIndex = column #eg;0

        #currentindex cannot be more than length of message
        while currentIndex < len(message):
            
            #store value of index in message into ciphertext list
            #eg ; message[0] = 's' , message[1] = 'e'
            # store in ciphertext[0] = 'se'
            ciphertext[column] += message[currentIndex]
            
            #plus key(8) into currentindex to go to +8th position in message
            currentIndex +=key
    
    #join all string in list and return
    return ''.join(ciphertext)

#To reuse function encryptmessage() by other program without calling the main function
if __name__ == '__main__':
    main()