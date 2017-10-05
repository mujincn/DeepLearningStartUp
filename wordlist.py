# -*- coding: utf-8 -*-

from collections import Counter

with open('happiness_seg.txt') as file_link:
        file_content = file_link.read()

def str_filter(string):
    string = string.replace('，', ' ')
    string = string.replace('。', ' ')
    string = string.replace('“', ' ')
    string = string.replace('”', ' ')
    string = string.replace('?', ' ')
    string = string.replace('；', ' ')
    string = string.replace('：', ' ')
    string = string.replace('(', ' ')
    string = string.replace(')', ' ')
    string = string.replace('―', ' ')
    return string.replace('　', ' ')

# 输出去掉标点的字符串
def word_filter():
    word_string = str_filter(file_content).split()
    return word_string

# 构造二元词组
def double_list(str_list):
    for i  in range(len(str_list)-1):
        str_list[i]  = str_list[i] +' ' +  str_list[i+1]
    return str_list

# 统计二元词组
def result_list(str_list,n):
    word_counts = Counter(str_list)
    top_n = word_counts.most_common(n)
    print(top_n)


word_list = word_filter()
doule_word = double_list(word_list)
result_list(double_word,10)
