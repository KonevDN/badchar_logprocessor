import re
import parsing

''' глобальные переменные '''
str_name_of_bad_file='log.log'
str_name_of_good_file='normal.log'
int_max_count_of_read_char=2000


''' работа '''
array_from_file = parsing.get_array_from_file(str_name_of_bad_file, int_max_count_of_read_char)
print(array_from_file)

array_of_good_strings = parsing.delete_char_from_array(array_from_file)
print(array_of_good_strings)

array_of_good_strings = parsing.delete_empty_element_from_array(array_of_good_strings)
print(array_of_good_strings)


mass = ['a','b','c','d']
newmass=[]

objTimeTemplate = re.compile(r'\d\d:\d\d:\d\d.\d\d\d>')
size = len(array_of_good_strings)
for index in range(len(array_of_good_strings)):
    if index==60:
        stop=index
    if index<size-1:
        match1 = objTimeTemplate.search(array_of_good_strings[index])
        match2 = objTimeTemplate.search(array_of_good_strings[index+1])
        if match1!=None and match2==None:
            newmass.append('\n'+match1.group()+' '*5+array_of_good_strings[index+1])
            x1=match1.group()
            x2=array_of_good_strings[index+1]
            s=newmass
print(newmass)
array_of_good_strings = newmass

parsing.put_array_to_file(array_of_good_strings, PRINT=False)


