# coding=utf-8
''' код для узнавания даты создания файла '''
import os
from datetime import datetime
stat = os.stat('normal.log')
str1 = datetime.fromtimestamp(stat.st_atime)
str2 = datetime.date(str1)



''' код для вытаскивания из лога FM3 а точнее из массива array_of_good_strings вот такого 
массива всевозможных используемых команд с очисткой от их дублиррования ['at+ceng', 'at+cmee', 'at+gmm', ... '''

'''
import re
array_of_current_strings = array_of_good_strings
array_of_command_list = []
objTemplateOfString = re.compile(r'^(\s)?(\d\d:\d\d:\d\d.\d\d\d)(>)?(\s){1,10}(at\+\w+)' )  #
for index in range(len(array_of_current_strings)):
    objMatch = objTemplateOfString.search(array_of_current_strings[index])
    if (objMatch != None):
        str_found_string = objMatch.group(5)
        str_found_string # отладка
        if str_found_string not in array_of_command_list:
            array_of_command_list.append(str_found_string)
        continue
'''


