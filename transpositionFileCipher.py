import time, os, sys, smtplib, transpositionEncrypt, transpositionDecrypt

def main():
    inputfile = 'Diam song.txt'
    outputfile = 'encryptedfile.txt'
    key = 10
    mode = 'encrypt'

    if not os.path.exists(inputfile):
        print(('File %s didnt exists') % (inputfile))
        sys.exit()

    if os.path.exists(outputfile):
        print('This will output the file %s. (C)ontinue or (Q)uit?' % 
        (outputfile))
        response = input('Ans:')
        if not response.lower().startswith('c'):
            sys.exit()

    fileObj = open(inputfile)
    content = fileObj.read()
    fileObj.close()

    print('%sing...' % (mode.title()))

    startTime = time.time()
    if mode == 'encrypt':
        translated = transpositionEncrypt.encryptMessage(key,content)
    elif mode == 'decrypt':
        translated = transpositionDecrypt.decryptMessage(key, content)
            
    totalTime = round(time.time() - startTime,2)
    print('%sion time: %s seconds' % (mode.title(), totalTime))

    outputFileObj  = open(outputfile,'w')
    outputFileObj.write(translated)

    print('Done %sing %s (%s characters).' % (mode, inputfile,len(content)))
    print('%sed file is %s.' % (mode.title(), outputfile))

if __name__ == '__main__':
    main()   
