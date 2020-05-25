import nltk
import re
from nltk.tokenize import sent_tokenize, word_tokenize

# file_(size)_(read/write)              1: read     2: write
file_l_1 = open("new_all_database.txt", "r+")
raw_tex_l = file_l_1.read()

file_l_2 = open("largepp_output.txt", "w+")
file_m_2 = open("mediumpp_output.txt", "w+")
file_s_2 = open("smallpp_output.txt", "w+")

# recreating confessions
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

# constants for differentiating
SMALL = 550
MEDIUM = 700

# constants for counting
c = 0
n = 0
s = 0
m = 0
la = 0

for i in list_of_confessions:
    sentences = sent_tokenize(i)
    conf = []

    # removing repeating sentences
    for j in sentences:
        sent = []
        words = word_tokenize(j)

        # removing repating words
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

    # recreating confessions
    f_conf = "[\""
    count = 0
    for j in conf:
        for k in j:
            if(k == ',' or k == '.' or (k[0] == '\'' and len(k) > 1) ):
                f_conf = f_conf + str(k)
            else:
                f_conf = f_conf + " " + str(k)
        f_conf = f_conf + "\n"
        count += 1

        # splitting each confession to 10 lines
        if(count == 10):
            f_conf = f_conf + "\"]\n"      
            len_of_confession = len(f_conf)
            c+= len_of_confession
            n+=1
            if(len_of_confession <= SMALL):
                file_s_2.write(f_conf)
                s+=1
            elif(len_of_confession<= MEDIUM):
                file_m_2.write(f_conf)
                m+=1
            else:
                file_l_2.write(f_conf)
                la+=1
            count = 0
            f_conf = "[\""
    f_conf = f_conf + "\"]\n"      
    len_of_confession = len(f_conf)
    c+=len_of_confession
    n+=1
    if(len_of_confession<=10):
        pass
    elif(len_of_confession <= SMALL):
        file_s_2.write(f_conf)
        s+=1
    elif(len_of_confession<= MEDIUM):
        file_m_2.write(f_conf)
        m+=1
    else:
        file_l_2.write(f_conf)
        la +=1
    count = 0
    f_conf = "[\""


c = c/n
#print(c)
print(s)
print(m)
print(la)
file_l_2.close()
file_m_2.close()
file_s_2.close()