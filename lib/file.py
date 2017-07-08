import os


def get_array_from_file( str_name_of_bad_file='log.log', int_max_size_of_read_string=2000 ):
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


def put_array_to_file( array_of_good_strings: list, str_name_of_good_file: str = 'normal.log',
                       PRINT: bool = True ) -> None:
    objNormalLogFile = open(str_name_of_good_file, 'w')
    for str_one_element in array_of_good_strings:
        # str_one_element = str_one_element + '\n'
        objNormalLogFile.write(str_one_element)
        if PRINT == True:
            print(str_one_element)
    objNormalLogFile.close()
    return None
