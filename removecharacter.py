import re
def remove_character(input_strings):
    pattern = r'[^\w\s]'
    result_string=re.sub(pattern,'',input_strings)
    return result_string
input_strings="abcfg$$%hh#@"
output_string=remove_character(input_strings)
print(output_string)
    