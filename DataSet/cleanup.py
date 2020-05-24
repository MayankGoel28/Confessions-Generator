import nltk
import re
from nltk.tokenize import sent_tokenize, word_tokenize
# file (size) (read/write)

file_l_1 = open("all_database.txt", "r+")
raw_tex_l = file_l_1.read()

file_l_2 = open("Text_Database/largepp_output.txt", "a")
file_m_2 = open("Text_Database/mediumpp_output.txt", "a")
file_s_2 = open("Text_Database/smallpp_output.txt", "a")

make_string = False
confession = ""
list_of_confessions = []
for i in raw_tex_l:
    if(i == ']'):
        list_of_confessions.append(confession)
        make_string = False
    if(make_string):
        confession += i
    if(i == '['):
        make_string = True

c = 0

for i in list_of_confessions:
    sentences = sent_tokenize(i)
    conf = []
    for j in sentences:
        sent = []
        words = word_tokenize(j)
        for k in words:
            word_exists = True
            for l in sent:
                if(l == k):
                    word_exists = False
                    break
            if(word_exists):
                sent.append(k)
        exist = True
        for k in conf:
            if(k == sent):
                exist = False
                break
        if exist:
            conf.append(sent)
    
    f_conf = "[\""
    for j in conf:
        for k in j:
            if(k == ',' or k == '.' or k[0] == '\''):
                f_conf = f_conf + str(k)
            else:
                f_conf = f_conf + " " + str(k)
        f_conf = f_conf + "\n"
    f_conf = f_conf + "\"]\n"
    len_of_confession = len(f_conf)
    c += len_of_confession
    if(len_of_confession <= 20000):
        file_s_2.write(f_conf)
    elif(len_of_confession<= 50000):
        file_m_2.write(f_conf)
    else:
        file_l_2.write(f_conf)


# c = c/len(list_of_confessions)
# print(c)
file_l_2.close()
file_m_2.close()
file_s_2.close()