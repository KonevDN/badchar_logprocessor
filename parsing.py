
def deleteChar(strbad):
    strbad = strbad.replace('\\r', ' ')
    strbad = strbad.replace('\\n', ' ')
    strbad = strbad.replace('\r', ' ')
    strbad = strbad.replace('\n', ' ')
    strbad = strbad.replace('>', ' ')
    strbad = strbad.replace('<', ' ')
    strbad = strbad.replace('\0', ' ')
    #strbad = strbad.replace('-', ' ')
    strgood = strbad
    return str(strgood)



def deleteEmptyElement(arrayOfString):
    ''' функция получает массив и возвращает массив, она удаляет плохие элементы массива '''
    arrayOfString = list(arrayOfString)
    str1=''
    str2=' '
    arrayOfNewElements = []
    for element in arrayOfString:
        element
        if element != str1 and element != str2:
            arrayOfNewElements.append(element)
    return arrayOfNewElements
