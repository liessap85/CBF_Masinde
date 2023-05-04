myDict={}
myDict["one"]=1
myDict["two"]=45
myDict["three"]="Spam"
myDict[4]=4.5
myDict["Class"]="CBF Saturday"

#print(myDict["Class"])

for key, value in myDict.items():
    print(key, value)