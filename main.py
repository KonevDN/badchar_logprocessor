from lib import file
from lib import parsing

''' глобальные переменные '''
str_name_of_bad_file = 'bad.log'
str_name_of_good_file = 'normal.log'
int_max_count_of_read_char = 2000




''' работа '''
array_from_file = file.get_array_from_file(str_name_of_bad_file, int_max_count_of_read_char)
#print(array_from_file)

array_of_good_strings = parsing.delete_char_from_array(array_from_file)
#print(array_of_good_strings)

array_of_good_strings = parsing.delete_empty_element_from_array(array_of_good_strings)
#print(array_of_good_strings)

array_of_good_strings = parsing.combine_all_strings(array_of_good_strings)
#print(array_of_good_strings)

array_of_good_strings = parsing.insert_white_space(array_of_good_strings, '-=D_RUN APPL FM3=-', 15)
#print(array_of_good_strings)

array_of_good_strings = parsing.delete_at_commands(array_of_good_strings)

#newfunction
#at+ceng?
#at+cdsds=
# 17:20:43.915     at+cdsds=1
dict_of_atcommands = {
                         'at+ceng':'Switch on or off Engineering Mode',
                         'at+cmee':'Report mobile equipment error',
                         'at+gmm':'Request TA Model Identification',
                         'at+gmr':'Request TA Revision Identification of Software Release',
                         'at+gsn':'Request TA Serial Number Identification(IMEI)',
                         'at+cnetscan':'Perform a Net Survey to Show All the Cells’ Information',
                         'at+cdsds':'Set default SIM',
                         'at+cfun':'Set Phone Functionality',
                         'at+ccid':'Show ICCID',
                         'at+cpin':'Enter PIN',
                         'at+cipmux':'Start Up Multi-IP Connection',
                         'at+ciphead':'Add an IP Head at the Beginning of a Package Received',
                         'at+cmgf':'Select SMS Message Format',
                         'at+csq':'Signal Quality Report',
                         'at+creg':'Network Registration',
                         'at+cgatt':'Attach or Detach from GPRS Service',
                         'at+cimi':'',
                         'at+cstt':'',
                         'at+ciicr':'',
                         'at+cifsr':'',
                         'at+cipstatus':'',
                         'at+cipstart':'',
                         'at+cipsend':'',
                         'at+cmgl':'',
                         'at+cipclose':'',
                         'at+cpowd':'',
                         'at+spic':'',
                         'at+cspn':'',
                         'at+cmgda':'',
}
# print(dict_of_atcommands.keys())
# print(dict_of_atcommands.values())

import re
array_of_current_strings = array_of_good_strings
array_of_command_list = []
objTemplateOfString = re.compile(r'^(\s)?(\d\d:\d\d:\d\d.\d\d\d)(>)?(\s){1,10}(at\+\w+)' )  #

for index in range(len(array_of_current_strings)):
    objMatch = objTemplateOfString.search(array_of_current_strings[index])
    if (objMatch != None):
        str_found_string = objMatch.group(5)
        str_found_string
        if str_found_string not in array_of_command_list:
            array_of_command_list.append(str_found_string)
        continue
print(array_of_command_list)

print(len(array_of_command_list))






file.put_array_to_file(array_of_good_strings, PRINT=False)

