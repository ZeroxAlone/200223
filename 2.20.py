# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 14:15:59 2020

@author: lisa_
"""


#s16-23-Q3
#a
def Decrypt(Lookup, CipherChar):
    Index = 0
    Found = False
    while Found == False:
        if Lookup[Index] == CipherChar:
            Found = True
        else:
            Index += 1
    OriginalChar = chr(Index)
    return OriginalChar
#b
'''
StartIndex = int(input("Enter a start index: "))
NumberToOutput = int(input("Enter a number to output: "))
for Index in range(StartIndex, StartIndex + NumberToOutput -1):
    OriginalChar = chr(Index)
    CipherChar = Lookup[Index]
    print("Index ", Index, ": Character "+ OriginalChar+" has substitute character "+CipherChar)
'''
#w17-21-Q3a
def BubbleSort():
    Boundary = 100
    while True:
        NoSwaps = True
        for i in range(Boundary-1):
            FirstID = UserNameArray[i]
            SecondID= UserNameArray[i+1]
            if FirstID>SecondID:
                Temp = UserNameArray[i]
                UserNameArray[i] = UserNameArray[i+1]
                UserNameArray[i+1] = Temp
                NoSwaps = False
        Boundary -= 1
        if NoSwaps == True:
            break
    print(UserNameArray)
#w17-21-Q3b
def FindRepeats():
    RepeatCount = 0
    for i in range(1,100):
        FirstID = UserNameArray[i-1]#[:6]
        SecondID= UserNameArray[i]#[:6]
        if FirstID == SecondID:
            RepeatCount += 1
            print(UserNameArray[i])
    if RepeatCount == 0:
        print("The array contains no repeated UserIDs.")
    else:
        print("There are", RepeatCount, "repeated UserIDs.")
#s19-21-Q3

    
    
    
    
    
    
    
    
    
    