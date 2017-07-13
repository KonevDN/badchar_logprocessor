def delete_char_from_string( str_one_bad_string ):
    ''' функция получает строку и возвращает строку , она удаляет плохие элементы массива '''
    str_one_bad_string = str_one_bad_string.replace('\\r', ' ')
    str_one_bad_string = str_one_bad_string.replace('\\n', ' ')
    str_one_bad_string = str_one_bad_string.replace('\r', ' ')
    str_one_bad_string = str_one_bad_string.replace('\n', ' ')
    #str_one_bad_string = str_one_bad_string.replace('>', ' ')
    #str_one_bad_string = str_one_bad_string.replace('<', ' ')
    str_one_bad_string = str_one_bad_string.replace('\0', ' ')
    str_one_bad_string = str_one_bad_string.replace('< 0 >', ' ')
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


def delete_empty_element_from_array(array_of_bad_strings: list):
    ''' функция получает массив и возвращает массив, она удаляет плохие элементы массива '''
    array_of_bad_strings = array_of_bad_strings
    str_empty_string1 = ''
    str_empty_string2 = ' '
    array_of_good_strings = []
    for str_one_element in array_of_bad_strings:
        if str_one_element != str_empty_string1 and str_one_element != str_empty_string2:
            array_of_good_strings.append(str_one_element)
    return array_of_good_strings


def combine_all_strings(array_of_good_strings: list):
    ''' функция перебирает строки массива и убирает беспорядочные переносы строк,которые есть в иcходнике '''
    import re
    array_of_new_good_strings = []  # инициальизация нового пустого массива
    objTemplateOfTimeString = re.compile(
        r'^\d\d:\d\d:\d\d.\d\d\d')  # это шаблон регуляр.выражения для поиска строки начинающейся с времени, например, 10:18:22.456 ; . если добавить > то тогда эта скобка не отфильтруется.
    objTemplateOfIdealString = re.compile(r'^(\d\d:\d\d:\d\d.\d\d\d)(>)?(\s){1,10}(.+)')  # [a-zA-Z0-9_=:-]
    size = len(array_of_good_strings)  # узнать размер всего исходного массива - количество строк
    for index in range(len(array_of_good_strings)):  # создать цикл по неизменяемому  массиву
        if index < size - 1:  # если индекс меньше количества строк в массиве, то далее можно применить констуркцию index+1
            str_current_string = array_of_good_strings[index]  # это текущая строка взятая из массива
            match1 = objTemplateOfTimeString.search(
                array_of_good_strings[index])  # взять по шаблону первую строку из массива
            match2 = objTemplateOfTimeString.search(
                array_of_good_strings[index + 1])  # взять по шаблону вторую строку из массива
            match3_ideal_string = objTemplateOfIdealString.search(
                array_of_good_strings[index])  # искать по шаблону идеальную строку в элементе массива
            if (
                    match1 != None and match2 == None):  # если первая строка соответствует шаблну, а вторая - нет, то их надо объединить
                array_of_new_good_strings.append('\n' + match1.group() + ' ' * 5 + array_of_good_strings[
                    index + 1])  # соединить первуб и вторую строку, тк именно их надо соединить
            if (match3_ideal_string != None):
                array_of_new_good_strings.append(
                    '\n' + match3_ideal_string.group(1) + ' ' * 5 + match3_ideal_string.group(
                        4))  # соединить первуб и вторую строку, тк именно их надо соединить
    #print(array_of_new_good_strings)  # вывести в консоль для отладочной цели
    #array_of_good_strings = array_of_new_good_strings  # теперь в хороший массив записываются новые данные вместо старых, это типа return
    return array_of_new_good_strings


def insert_white_space(array_of_strings:list, str_search_string:str='-=D_RUN APPL FM3=-', int_count_of_white_space:int=15):
    """ функция находит требуемую строку в массиве и перед ней ставит требуемое количество пустых строк
    для форматирования текста, чтобы удобно было читать,  в частночит это применяется для того, чтобы
    визуально легко отделить один старт маяка от другого старта маяка \n
    str_search_string - строка в массиве, которую нужно найти и поставить перед ней пробелы, но у меня пока не получлось передать значение этой переменной в re.compile, поэтому эта переменная пока является бесполезной
    array_of_strings - массив, который надо обработать
    int_count_of_white_space - количество белых строк,которое надо добавить
    """
    import re   # импорт модуля, будем работать с регулярными выражениями
    array_of_new_strings = []   # новый массив, который создаст и вернет данная функция
    array_of_current_strings = array_of_strings    # принятый массив сделаем текущим
    objTemplateOfRunString = re.compile(r'^(\s)(\d\d:\d\d:\d\d.\d\d\d)(>)?(\s){1,10}(%s)' % str_search_string)  #
    for index in range(len(array_of_current_strings)):
        objMatch = objTemplateOfRunString.search(array_of_current_strings[index])
        if (objMatch != None):
            str_found_string = objMatch.group().strip()
            str_found_string = '\n' * int_count_of_white_space + str_found_string
            array_of_current_strings[index] = str_found_string
        array_of_new_strings = array_of_current_strings
    return array_of_new_strings

def delete_at_commands(array_of_strings:list):
    """ # 18:39:06.790> [+] GSM: at+cmgl=4 """

    import re  # импорт модуля, будем работать с регулярными выражениями
    array_of_new_strings = []   # новый массив, который создаст и вернет данная функция
    array_of_current_strings = array_of_strings    # принятый массив сделаем текущим
    objTemplateOfString = re.compile(r'^(\s)(\d\d:\d\d:\d\d.\d\d\d)(>)?(\s){1,10}\[\+|t\](.)+' )  #
    for index in range(len(array_of_current_strings)):
        # str1 = array_of_current_strings[index] отладка
        objMatch = objTemplateOfString.search(array_of_current_strings[index])
        if objMatch != None:
            # str_found_string = objMatch.group()
            continue
        else:   # if None
            array_of_new_strings.append(array_of_current_strings[index])

    return array_of_new_strings


def insert_information_for_atcommands(array_of_bad_strings:list, dict_of_atcommands: dict)->list:
    # 17:20:43.915     at+cdsds=1 пример для отладки
    import re
    from copy import copy
    array_of_current_strings = copy(array_of_bad_strings)
    array_of_new_good_strings = copy(array_of_bad_strings)
    objTemplateOfSearchString = re.compile(r'^(\s)?(\d\d:\d\d:\d\d.\d\d\d)(>)?(\s){1,10}(at\+\w+)')
    for index in range(len(array_of_current_strings)):
        objMatch = objTemplateOfSearchString.search(array_of_current_strings[index])
        if (objMatch != None):
            str_found_command_name = objMatch.group(5)  # взять 5ю группу, там содержится полное имя найденной Ат-команды
            # str_found_full_string = objMatch.group()    # взять всю строку, в которой найдена АТ-команда
            if str_found_command_name in dict_of_atcommands:
                str_help_string = array_of_current_strings[index] + ' '*10 + 'help: ' + dict_of_atcommands[str_found_command_name] # составляется строка с подсказкой о назначении АТ-команды взамен текущей строки массива
                array_of_new_good_strings[index] = str_help_string # тут строка с подсказкой о назначении АТ-команды запихивается в новый массив, чтобы не испортить текущий массив. новый массив будет возвращаться функцией
                continue
            continue
        continue
    return array_of_new_good_strings