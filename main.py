from lib import file
from lib import parsing

''' глобальные переменные '''
str_name_of_bad_file = 'bad.log'
str_name_of_good_file = 'normal.log'
int_max_count_of_read_char = 2000

''' работа '''
array_from_file = file.get_array_from_file(str_name_of_bad_file, int_max_count_of_read_char)
print(array_from_file)

array_of_good_strings = parsing.delete_char_from_array(array_from_file)
print(array_of_good_strings)

array_of_good_strings = parsing.delete_empty_element_from_array(array_of_good_strings)
print(array_of_good_strings)

array_of_good_strings = parsing.combine_all_strings(array_of_good_strings)
print(array_of_good_strings)



import re
array_of_current_strings = []
array_of_new_strings = []
array_of_current_strings = array_of_good_strings
objTemplateOfRunString = re.compile(r'^(\s)(\d\d:\d\d:\d\d.\d\d\d)(>)?(\s){1,10}(-=D_RUN APPL FM3=-)')  #
for index in range(len(array_of_current_strings)):
    objMatch = objTemplateOfRunString.search(array_of_current_strings[index])
    if (objMatch != None):
        str_found_string = objMatch.group().strip()
        str_found_string = '\n'*15 + str_found_string
        array_of_current_strings[index] = str_found_string
array_of_good_strings = array_of_current_strings





file.put_array_to_file(array_of_good_strings, PRINT=False)

