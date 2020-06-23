# coding=utf8
dot = " "
space = " "
stringy = '''                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
'''

finalNum = ""
for i in range(0, len(stringy)):
    if(stringy[i] == dot):
        finalNum = finalNum + "1"
    if(stringy[i] == space):
        finalNum = finalNum + "0"

print(finalNum)
print(len(finalNum))