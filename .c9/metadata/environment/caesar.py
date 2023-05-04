{"filter":false,"title":"caesar.py","tooltip":"/caesar.py","undoManager":{"mark":17,"position":17,"stack":[[{"start":{"row":0,"column":0},"end":{"row":55,"column":24},"action":"insert","lines":["# Module Lab: Caesar Cipher Program Bug #1","#","# In a previous lab, you created a Caesar cipher program. This version of","# the program is buggy. Use a debugger to find the bug and fix it.","","# Double the given alphabet","def getDoubleAlphabet(alphabet):","    doubleAlphabet = alphabet + alphabet","    return doubleAlphabet","","# Get a message to encrypt","def getMessage():","    stringToEncrypt = input(\"Please enter a message to encrypt: \")","    return stringToEncrypt","","# Get a cipher key","def getCipherKey():","    shiftAmount = input(\"Please enter a key (whole number from 1-25): \")","    return shiftAmount","","# Encrypt message","def encryptMessage(message, cipherKey, alphabet):","    encryptedMessage = \"\"","    uppercaseMessage = \"\"","    uppercaseMessage = message.upper()","    for currentCharacter in uppercaseMessage:","        position = alphabet.find(currentCharacter)","        newPosition = position + cipherKey","        if currentCharacter in alphabet:","            encryptedMessage = encryptedMessage + alphabet[newPosition]","        else:","            encryptedMessage = encryptedMessage + currentCharacter","    return encryptedMessage","","# Decrypt message","def decryptMessage(message, cipherKey, alphabet):","    decryptKey = -1 * int(cipherKey)","    return encryptMessage(message, decryptKey, alphabet)","","# Main program logic","def runCaesarCipherProgram():","    myAlphabet=\"ABCDEFGHIJKLMNOPQRSTUVWXYZ\"","    print(f'Alphabet: {myAlphabet}')","    myAlphabet2 = getDoubleAlphabet(myAlphabet)","    print(f'Alphabet2: {myAlphabet2}')","    myMessage = getMessage()","    print(myMessage)","    myCipherKey = getCipherKey()","    print(myCipherKey)","    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2)","    print(f'Encrypted Message: {myEncryptedMessage}')","    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, myAlphabet2)","    print(f'Decrypted Message: {myDecryptedMessage}')","","# Main logic","runCaesarCipherProgram()"],"id":1}],[{"start":{"row":27,"column":22},"end":{"row":27,"column":23},"action":"insert","lines":["i"],"id":2},{"start":{"row":27,"column":23},"end":{"row":27,"column":24},"action":"insert","lines":["n"]},{"start":{"row":27,"column":24},"end":{"row":27,"column":25},"action":"insert","lines":["t"]},{"start":{"row":27,"column":25},"end":{"row":27,"column":26},"action":"insert","lines":["("]}],[{"start":{"row":27,"column":34},"end":{"row":27,"column":35},"action":"insert","lines":[")"],"id":3}],[{"start":{"row":27,"column":25},"end":{"row":27,"column":26},"action":"remove","lines":["("],"id":4},{"start":{"row":27,"column":24},"end":{"row":27,"column":25},"action":"remove","lines":["t"]},{"start":{"row":27,"column":23},"end":{"row":27,"column":24},"action":"remove","lines":["n"]},{"start":{"row":27,"column":22},"end":{"row":27,"column":23},"action":"remove","lines":["i"]}],[{"start":{"row":27,"column":30},"end":{"row":27,"column":31},"action":"remove","lines":[")"],"id":5}],[{"start":{"row":27,"column":33},"end":{"row":27,"column":34},"action":"insert","lines":["i"],"id":6},{"start":{"row":27,"column":34},"end":{"row":27,"column":35},"action":"insert","lines":["n"]},{"start":{"row":27,"column":35},"end":{"row":27,"column":36},"action":"insert","lines":["t"]},{"start":{"row":27,"column":36},"end":{"row":27,"column":37},"action":"insert","lines":["("]}],[{"start":{"row":27,"column":46},"end":{"row":27,"column":47},"action":"insert","lines":[")"],"id":7}],[{"start":{"row":27,"column":35},"end":{"row":27,"column":36},"action":"remove","lines":["t"],"id":8},{"start":{"row":27,"column":34},"end":{"row":27,"column":35},"action":"remove","lines":["n"]}],[{"start":{"row":27,"column":34},"end":{"row":27,"column":35},"action":"remove","lines":["("],"id":9},{"start":{"row":27,"column":33},"end":{"row":27,"column":34},"action":"remove","lines":["i"]}],[{"start":{"row":27,"column":42},"end":{"row":27,"column":43},"action":"remove","lines":[")"],"id":10}],[{"start":{"row":17,"column":18},"end":{"row":17,"column":19},"action":"insert","lines":["i"],"id":11},{"start":{"row":17,"column":19},"end":{"row":17,"column":20},"action":"insert","lines":["n"]},{"start":{"row":17,"column":20},"end":{"row":17,"column":21},"action":"insert","lines":["t"]},{"start":{"row":17,"column":21},"end":{"row":17,"column":22},"action":"insert","lines":["("]}],[{"start":{"row":17,"column":76},"end":{"row":17,"column":77},"action":"insert","lines":[")"],"id":12}],[{"start":{"row":17,"column":21},"end":{"row":17,"column":22},"action":"remove","lines":["("],"id":13},{"start":{"row":17,"column":20},"end":{"row":17,"column":21},"action":"remove","lines":["t"]},{"start":{"row":17,"column":19},"end":{"row":17,"column":20},"action":"remove","lines":["n"]},{"start":{"row":17,"column":18},"end":{"row":17,"column":19},"action":"remove","lines":["i"]}],[{"start":{"row":17,"column":72},"end":{"row":17,"column":73},"action":"remove","lines":[")"],"id":14}],[{"start":{"row":27,"column":33},"end":{"row":27,"column":34},"action":"insert","lines":["i"],"id":15},{"start":{"row":27,"column":34},"end":{"row":27,"column":35},"action":"insert","lines":["t"]}],[{"start":{"row":27,"column":34},"end":{"row":27,"column":35},"action":"remove","lines":["t"],"id":16}],[{"start":{"row":27,"column":34},"end":{"row":27,"column":35},"action":"insert","lines":["n"],"id":17},{"start":{"row":27,"column":35},"end":{"row":27,"column":36},"action":"insert","lines":["t"]},{"start":{"row":27,"column":36},"end":{"row":27,"column":37},"action":"insert","lines":["("]}],[{"start":{"row":27,"column":46},"end":{"row":27,"column":47},"action":"insert","lines":[")"],"id":18}]]},"ace":{"folds":[],"scrolltop":780,"scrollleft":0,"selection":{"start":{"row":24,"column":38},"end":{"row":24,"column":38},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":8,"state":"start","mode":"ace/mode/python"}},"timestamp":1677342388830,"hash":"784b51fb871369e13629689d31afef974e3daef1"}