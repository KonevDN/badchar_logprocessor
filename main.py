import re
import parsing

''' глобальные переменные '''
str_name_of_bad_file='bad.log'
str_name_of_good_file='normal.log'
int_max_count_of_read_char=2000


''' работа '''
array_from_file = parsing.get_array_from_file(str_name_of_bad_file, int_max_count_of_read_char)
print(array_from_file)

array_of_good_strings = parsing.delete_char_from_array(array_from_file)
print(array_of_good_strings)

array_of_good_strings = parsing.delete_empty_element_from_array(array_of_good_strings)
print(array_of_good_strings)



newmass=[]      # инициальизация нового пустого массива
objTemplateOfTimeString = re.compile(r'^\d\d:\d\d:\d\d.\d\d\d')      # это шаблон регуляр.выражения для поиска строки начинающейся с времени, например, 10:18:22.456 ; . если добавить > то тогда эта скобка не отфильтруется.
objTemplateOfIdealString = re.compile(r'^(\d\d:\d\d:\d\d.\d\d\d)(>)?(\s){1,10}(.+)') #[a-zA-Z0-9_=:-]
size = len(array_of_good_strings)       # узнать размер всего исходного массива - количество строк
for index in range(len(array_of_good_strings)):     # создать цикл по неизменяемому  массиву
    if index==60:       # для отладки
        stop=index      # для отладки
    if index<size-1:    # если индекс меньше количества строк в массиве, то lfktt можно применить констуркцию index+1
        str_current_string = array_of_good_strings[index] # это текущая строка взятая из массива
        match1 = objTemplateOfTimeString.search(array_of_good_strings[index])   # взять по шаблону первую строку из массива
        match2 = objTemplateOfTimeString.search(array_of_good_strings[index + 1]) # взять по шаблону вторую строку из массива
        match3_ideal_string = objTemplateOfIdealString.search(array_of_good_strings[index])     # искать по шаблону идеальную строку в элементе массива
        if (match1!=None and match2==None):       # если первая строка соответствует шаблну, а вторая - нет, то их надо объединить
            newmass.append('\n'+match1.group()+' '*5+array_of_good_strings[index+1])    # соединить первуб и вторую строку, тк именно их надо соединить
            x1=match1.group()       # для отладки
            x2=array_of_good_strings[index+1]       # для отладки
            s=newmass       # для отладки
        if  (match3_ideal_string!=None):
              newmass.append('\n'+ match3_ideal_string.group(1)+' '*5+match3_ideal_string.group(4))  # соединить первуб и вторую строку, тк именно их надо соединить
print(newmass)      # вывести в консоль для отладочной цели
array_of_good_strings = newmass     # теперь хороший массив получает новые данные вместо старых, это типа return

parsing.put_array_to_file(array_of_good_strings, PRINT=False)


