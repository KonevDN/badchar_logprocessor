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
        oneString = objBadLogFile.readline(intStringSize)  # считать файл по одной строке
        arrayOfStrings = arrayOfStrings + [oneString]  # созадь массив под одной строке
        strWithoutBadChar = parsing.deleteChar(oneString)  # очистить одну строку от плохих символов
        print(strWithoutBadChar)
        objNormalLogFile.write(strWithoutBadChar+'\n')
    objBadLogFile.close()
    objNormalLogFile.close()
else:
    print("File is No exist")