import os
import parsing

intStringSize = 2000
strNameOfBadFile = 'log.log'

if os.path.exists(strNameOfBadFile):
    print("File is exist")

    objNormalLogFile = open('normal.log', 'w')
    objBadLogFile = open(strNameOfBadFile, 'r')

    arrayOfStrings = []

    oneString = True
    while oneString:
        oneString = objBadLogFile.readline(intStringSize)  # читаю файл по одной строке
        arrayOfStrings = arrayOfStrings + [oneString]  # создаю массив под одной строке
        tempString = parsing.deleteChar(oneString)  # очищаю одну строку от плохих символов
        print(tempString)
        objNormalLogFile.write(tempString)
    objBadLogFile.close()
    objNormalLogFile.close()
else:
    print("File is No exist")



