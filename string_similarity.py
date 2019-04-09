from string_util import string2code
from  edit_distance import minEditDist

def similarity(string1,string2):
    code_string1 = string2code(string1)
    code_string2 = string2code(string2)
    distance = minEditDist(code_string1,code_string2)
    return 1 - distance/max(len(code_string1),len(code_string2))
