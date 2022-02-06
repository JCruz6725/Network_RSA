import json

def format_data_to_int_array(data):
    temp = ''
    int_array = []
    #print(s)
    for char in data:
        #print (char)
        if (char != ','):
            temp += char
        else:
          int_array.append(temp)
          temp = ''

    return int_array


def to_int_array (string_array):
    num = [int(num, base=10) for num in string_array]
    return num


def data_to_json(data):
    in_data = {'data':data}
    json_data = json.dumps(in_data)


    return json_data


def string_to_int_array(string_text):
    int_array = []
    for char in string_text:   
        int_array.append(ord(char))

    return int_array


def int_array_to_srting(int_array):
    string = ''
    for char in int_array:   
        string += (chr(char))

    return string
