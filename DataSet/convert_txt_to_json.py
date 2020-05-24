import nltk
import re
from nltk.tokenize import word_tokenize
import json

pp_sizes = ["smallpp", "mediumpp", "largepp"]

for name in pp_sizes:
    file1 = open(f"./Text_Database/{name}_database.txt", "r+")
    raw_data = file1.read()

    list_of_sentences = []
    current_sent = ""
    isOpen = False
    final_sentences = []

    for i in raw_data:
        
        if ( i == ']'):
            isOpen = False
            list_of_sentences.append(current_sent)
            current_sent = ""
        if ( isOpen ):
            current_sent += i
        if ( i == '[' ):
            isOpen = True

    for i in range(0, len(list_of_sentences) -1 ):
        list_of_sentences[i] = str(list_of_sentences[i])


    for i in list_of_sentences:
        sent = word_tokenize(i)
        for j in range(0, len(sent)-1):
            word = str(sent[j])
            if(word[0] == '$'):
                next = str(sent[j+1])
                if(next[0].isdigit()):
                    if(next[len(next) - 1] == 'k'):
                        next = next[:len(next)-2]
                        next = float(next)*1000
                    else:
                        try:
                            next = float(next)
                        except:
                            continue
                    sent[j+1] = str((next*75))
                    sent[j] = "₹"
            if(word == "dollar" or word == "dollars" or word == "Dollar" or word == "Dollars"):
                prev = str(sent[j-1])
                if(prev[0].isdigit()):
                    prev = float(prev)
                    sent[j-1] = str((prev*75))
                    sent[j] = "rupees"
        
        string_reconstruction = ""
        for i in sent:
            string_reconstruction = string_reconstruction + " " + str(i)
        
        final_sentences.append(string_reconstruction)


    final_sentences_final = []

    for i in final_sentences:
        i = i[3:]
        i = i[:len(i) - 3]
        # i = "\"" + i + "\"\n"
        final_sentences_final.append(i)

    print(f"{name} has {len(final_sentences_final)} confessions")

    with open(f"./JSON_Database/{name}_database.json", 'w', encoding='utf-8') as f:
        json.dump({"content":final_sentences_final}, f, ensure_ascii=False)