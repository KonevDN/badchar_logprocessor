# coding=utf-8
from lib import file
from lib import parsing


''' глобальные переменные '''
str_name_of_bad_file = 'bad.log'
str_name_of_good_file = 'normal.log'
int_max_count_of_read_char = 2000
int_count_of_white_space = 30
dict_of_atcommands = {
                         'at+ceng':'Switch on or off Engineering Mode',
                         'at+cmee':'Report mobile equipment error',
                         'at+gmm':'Request TA Model Identification',
                         'at+gmr':'Request TA Revision Identification of Software Release',
                         'at+gsn':'Request TA Serial Number Identification(IMEI)',
                         'at+cnetscan':'Perform a Net Survey to Show All the Cells Information',
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
                         'at+cimi':'Request International Mobile Subscriber Identity',
                         'at+cstt':'Start Task and Set APN, USER NAME, PASSWORD',
                         'at+ciicr':'Bring Up Wireless Connection with GPRS or CSD',
                         'at+cifsr':'Get Local IP Address',
                         'at+cipstatus':'Query Current Connection Status',
                         'at+cipstart':'Start Up TCP or UDP Connection',
                         'at+cipsend':'Send Data Through TCP or UDP Connection',
                         'at+cmgl':'List SMS Messages from Preferred Store',
                         'at+cipclose':'Close TCP or UDP Connection',
                         'at+cpowd':'Power off',
                         'at+spic':'Times Remained to Input SIM PIN/PUK',
                         'at+cspn':'Get Service Provider Name from SIM',
                         'at+cmgda':'Delete All SMS',
                         'at+sapbr':'Settings for Applications Based on IP',
                         'at+httppara':'Set HTTP Parameters Value',
                         'at+httpaction':'HTTP Method Action',
                         'at+httpread':'Read the HTTP Server Response',
}


''' работа '''
array_from_file = file.get_array_from_file(str_name_of_bad_file, int_max_count_of_read_char)
array_of_good_strings = parsing.delete_char_from_array(array_from_file)
array_of_good_strings = parsing.delete_empty_element_from_array(array_of_good_strings)
array_of_good_strings = parsing.combine_all_strings(array_of_good_strings)
array_of_good_strings = parsing.insert_white_space(array_of_good_strings, '-=D_RUN APPL FM3=-', int_count_of_white_space)
array_of_good_strings = parsing.delete_at_commands(array_of_good_strings)
array_of_good_strings = parsing.insert_information_for_atcommands(array_of_good_strings, dict_of_atcommands)

file.put_array_to_file(array_of_good_strings, bool_need_print=False)

