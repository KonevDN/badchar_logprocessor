import os
import parsing

intStringSize = 2000
strNameOfBadFile = 'log.log'


if os.path.exists(strNameOfBadFile):
    print("File is exist")

    objNormalLogFile = open('normal.log', 'w')
    objBadLogFile = open(strNameOfBadFile, 'r')

    arrayOfGoodStrings = []
    strBadString = True
    while strBadString:
        strBadString = objBadLogFile.readline(intStringSize)  # считать файл по одной строке
        strWithoutBadChar = parsing.deleteChar(strBadString)  # очистить одну строку от плохих символов
        arrayOfGoodStrings.append(strWithoutBadChar.strip())  # созадь массив под одной строке
        print(strWithoutBadChar)
        objNormalLogFile.write(strWithoutBadChar+'\n')

    #s = parsing.deleteEmptyElement(arrayOfGoodStrings)
    #print(s)

    objBadLogFile.close()
    objNormalLogFile.close()

else:
    print("File is No exist")

