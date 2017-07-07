def get_array_from_file( str_name_of_bad_file='log.log', int_max_size_of_read_string=2000 ):
    import os
    int_max_size_of_read_string = int(int_max_size_of_read_string)  # int_max_count_of_read_char = 2000 для примера
    str_name_of_bad_file = str(str_name_of_bad_file)  # str_name_of_bad_file = 'log.log' для примера
    array_from_file = []
    if os.path.exists(str_name_of_bad_file):
        print("File %s is exist" % str_name_of_bad_file)
        objBadLogFile = open(str_name_of_bad_file, 'r')
        str_one_bad_string = True
        while str_one_bad_string:
            str_one_bad_string = objBadLogFile.readline(int_max_size_of_read_string)  # считать файл по одной строке
            array_from_file.append(
                str_one_bad_string.strip())  # созадь массив под одной строке и убрать пробелы по бокам и \n
        objBadLogFile.close()
    else:
        print("File is No exist")
    return array_from_file


def delete_char_from_string( str_one_bad_string ):
    ''' функция получает строку и возвращает строку , она удаляет плохие элементы массива '''
    str_one_bad_string = str_one_bad_string.replace('\\r', ' ')
    str_one_bad_string = str_one_bad_string.replace('\\n', ' ')
    str_one_bad_string = str_one_bad_string.replace('\r', ' ')
    str_one_bad_string = str_one_bad_string.replace('\n', ' ')
    #str_one_bad_string = str_one_bad_string.replace('>', ' ')
    #str_one_bad_string = str_one_bad_string.replace('<', ' ')
    str_one_bad_string = str_one_bad_string.replace('\0', ' ')
    # str_one_bad_string = str_one_bad_string.replace('-', ' ')
    str_one_good_string = str_one_bad_string
    return str(str_one_good_string)


def delete_char_from_array( array_of_bad_strings ):
    ''' функция получает массив и возвращает массив, она удаляет плохие элементы массива '''
    array_of_good_strings = []
    for str_one_bad_string in array_of_bad_strings:
        str_one_good_string = delete_char_from_string(str_one_bad_string)
        array_of_good_strings.append(str_one_good_string.strip())
    return array_of_good_strings


def delete_empty_element_from_array( array_of_bad_strings ):
    ''' функция получает массив и возвращает массив, она удаляет плохие элементы массива '''
    array_of_bad_strings = list(array_of_bad_strings)
    str1 = ''
    str2 = ' '
    array_of_good_strings = []
    for str_one_element in array_of_bad_strings:
        if str_one_element != str1 and str_one_element != str2:
            array_of_good_strings.append(str_one_element)
    return array_of_good_strings


def put_array_to_file( array_of_good_strings: list, str_name_of_good_file: str = 'normal.log',
                       PRINT: bool = True ) -> None:
    objNormalLogFile = open(str_name_of_good_file,'w')
    for str_one_element in array_of_good_strings:
        #str_one_element = str_one_element + '\n'
        objNormalLogFile.write(str_one_element)
        if PRINT == True:
            print(str_one_element)
    objNormalLogFile.close()
    return None
