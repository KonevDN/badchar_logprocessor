def deleteSlashChar( varString ):
    array = list(varString)
    # print(mass)
    for index in range(len(array)):
        # print(index)
        if (array[index] == '\r') or (array[index] == '\n') or (array[index] == '>'):
            array[index] = ' '
    # print(mass)

    resultString = ''.join(array)
    # print(resultString)
    return resultString


def deleteChar(strbad:str):
    strbad = strbad.replace('\\r', ' ')
    strbad = strbad.replace('\\n', ' ')
    strbad = strbad.replace('\r', ' ')
    strbad = strbad.replace('\n', ' ')
    strbad = strbad.replace('>', ' ')
    strbad = strbad.replace('<', ' ')
    strgood = strbad
    return strgood





# inputString = '18:13:54.155>  \r \n+CIPSTATUS: 0,0,"TCP","91.228.154.22","18000","CONNECTED" \r \n'
# print(parsing.deleteSlashChar(inputString))
# print(parsing.deleteSlashChar('10:18:30.011   \r \n+CPIN: NOT INSERTED \r \n')+'\n')
