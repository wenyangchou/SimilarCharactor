from pypinyin import pinyin,Style,lazy_pinyin
from quadrilateral_code_dictionary import quadrilateral_code_dictionary as qcd
from structure_code_dictionary import structure_code_dictionary as scd
from initial_code_dictionary import initial_code_dictionary as icd
from final_code_dictionary import final_code_dictionary as fcd
from  write_number_dictionary import write_number_dictionary as wnd
from character import symbol_lst
from code_directionary import code_directionary as cd
from char_number_directionary import char_number_directionary as cnd
from zhconv import convert

def extract_initial_and_final(pinyin_string):
    if pinyin_string[0:2] not in ['zh','ch','sh']:

        if pinyin_string[0] not in ['b','p','m','f','d','t','n','l','g','k','h','j','q','x','r','z','c','s','y','w']:
            final = '0'
            initial = pinyin_string
        else:
            final = pinyin_string[0]  # 此处四行为声母韵母抽取
            initial = pinyin_string[1:]
    else:
        final = pinyin_string[0:2]
        initial = pinyin_string[2:]
    return initial,final

#编码格式【韵母，声母，结构，四角编码，笔画数】 共8位
def string2code(string):
    code_string = ''
    for char in string:
        if char in ['1','2','3','4','5','6','7','8','9','0']:
            char = cnd[char]
        code_string = code_string + cd.get(char,'')
    return code_string

#计算每个汉字的音形码
def get_code():
    char_array = symbol_lst()
    file = open('C:/Users/fooww/Desktop/code.txt','w+')
    for char in char_array:
        pinyin_char = lazy_pinyin(char)[0]
        initial, final = extract_initial_and_final(pinyin_char)
        code_string = icd[initial] + fcd[final] + scd[char] + qcd[char] + wnd[char]
        file.writelines("'"+ char+"':'"+code_string+"',\n")
    file.close()

def traditional2simplified(string):
    return convert(string, 'zh-cn')

get_code()