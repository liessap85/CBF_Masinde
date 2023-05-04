{"filter":false,"title":"caesar4.py","tooltip":"/caesar4.py","undoManager":{"mark":10,"position":10,"stack":[[{"start":{"row":0,"column":0},"end":{"row":55,"column":24},"action":"insert","lines":["# Module Lab: Caesar Cipher Program Bug #4","#","# In a previous lab, you created a Caesar cipher program. This version of","# the program is buggy. Use a debugger to find the bug and fix it.","","# Double the given alphabet","def getDoubleAlphabet(alphabet):","    doubleAlphabet = alphabet + alphabet","    return doubleAlphabet","","# Get a message to encrypt","def getMessage():","    stringToEncrypt = input(\"Please enter a message to encrypt: \")","    return stringToEncrypt","","# Get a cipher key","def getCipherKey():","    shiftAmount = input(\"Please enter a key (whole number from 1-25): \")","    return shiftAmount","","# Encrypt message","def encryptMessage(message, cipherKey, alphabet):","    encryptedMessage = \"\"","    uppercaseMessage = \"\"","    uppercaseMessage = message.upper()","    for currentCharacter in uppercaseMessage:","        position = alphabet.find(currentCharacter)","        newPosition = position + int(cipherKey)","        if currentCharacter in alphabet:","            encryptedMessage = encryptedMessage + alphabet[newPosition]","        else:","            encryptedMessage = encryptedMessage + currentCharacter","    return encryptedMessage","","# Decrypt message","def decryptMessage(message, cipherKey, alphabet):","    decryptKey = -1 * int(cipherKey)","    return encryptMessage(message, decryptKey, alphabet)","","# Main program logic","def runCaesarCipherProgram():","    myAlphabet=\"ABCDEFGHIJKLMNOPQRSTUVWXYZ\"","    print(f'Alphabet: {myAlphabet}')","    myAlphabet2 = getDoubleAlphabet(myAlphabet)","    print(f'Alphabet2: {myAlphabet2}')","    myMessage = getMessage()","    print(myMessage)","    myCipherKey = getCipherKey()","    print(myCipherKey)","    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2)","    print(f'Encrypted Message: {myEncryptedMessage}')","    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, myAlphabet2)","    print(f'Decrypted Message: {myEncryptedMessage}')","","# Main logic","runCaesarCipherProgram()"],"id":1}],[{"start":{"row":52,"column":34},"end":{"row":52,"column":35},"action":"remove","lines":["E"],"id":2}],[{"start":{"row":52,"column":34},"end":{"row":52,"column":35},"action":"insert","lines":["D"],"id":3},{"start":{"row":52,"column":35},"end":{"row":52,"column":36},"action":"insert","lines":["e"]}],[{"start":{"row":52,"column":36},"end":{"row":52,"column":37},"action":"remove","lines":["n"],"id":4}],[{"start":{"row":52,"column":35},"end":{"row":52,"column":36},"action":"remove","lines":["e"],"id":5},{"start":{"row":52,"column":34},"end":{"row":52,"column":35},"action":"remove","lines":["D"]}],[{"start":{"row":52,"column":34},"end":{"row":52,"column":35},"action":"insert","lines":["E"],"id":6},{"start":{"row":52,"column":35},"end":{"row":52,"column":36},"action":"insert","lines":["n"]}],[{"start":{"row":52,"column":32},"end":{"row":52,"column":50},"action":"remove","lines":["myEncryptedMessage"],"id":7},{"start":{"row":52,"column":32},"end":{"row":52,"column":50},"action":"insert","lines":["myEncryptedMessage"]}],[{"start":{"row":52,"column":35},"end":{"row":52,"column":36},"action":"remove","lines":["n"],"id":8},{"start":{"row":52,"column":34},"end":{"row":52,"column":35},"action":"remove","lines":["E"]}],[{"start":{"row":52,"column":34},"end":{"row":52,"column":35},"action":"insert","lines":["~"],"id":9},{"start":{"row":52,"column":35},"end":{"row":52,"column":36},"action":"insert","lines":["D"]},{"start":{"row":52,"column":36},"end":{"row":52,"column":37},"action":"insert","lines":["e"]}],[{"start":{"row":52,"column":36},"end":{"row":52,"column":37},"action":"remove","lines":["e"],"id":10},{"start":{"row":52,"column":35},"end":{"row":52,"column":36},"action":"remove","lines":["D"]},{"start":{"row":52,"column":34},"end":{"row":52,"column":35},"action":"remove","lines":["~"]}],[{"start":{"row":52,"column":34},"end":{"row":52,"column":35},"action":"insert","lines":["D"],"id":11},{"start":{"row":52,"column":35},"end":{"row":52,"column":36},"action":"insert","lines":["e"]}]]},"ace":{"folds":[],"scrolltop":672.5,"scrollleft":0,"selection":{"start":{"row":54,"column":12},"end":{"row":54,"column":12},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":34,"state":"start","mode":"ace/mode/python"}},"timestamp":1677343360765,"hash":"59ccac96631ec234ff7a94780656a56e25fb3b92"}