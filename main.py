import os
import parsing

''' глобальные переменные '''
str_name_of_bad_file='log.log'
str_name_of_good_file='normal.log'
int_max_size_of_read_string=2000

''' работа '''
array_from_file = parsing.get_array_from_file(str_name_of_bad_file, int_max_size_of_read_string)
print(array_from_file)

array_of_good_strings = parsing.delete_char_from_array(array_from_file)
print(array_of_good_strings)

array_of_good_strings = parsing.delete_empty_element_from_array(array_of_good_strings)
print(array_of_good_strings)

parsing.put_array_to_file(array_of_good_strings, PRINT=True)


