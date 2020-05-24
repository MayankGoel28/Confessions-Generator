import nltk
from nltk.tokenize import WordPunctTokenizer 
import csv
colleges = []
university = ["University", "university", "school", "School", "UNIVERSITY", "SCHOOL", "universities","UNIVERSITIES", "Universities", "schools", "Schools", "SCHOOLS" ]

  
tokenizer = WordPunctTokenizer() 
with open('college_list.csv', newline='') as f:
    reader_colleges = csv.reader(f)
    data_colleges = list(reader_colleges)

for i in data_colleges:
    if( i[0] == "School Name"):
        pass
    else:
        college_name = str(i[0])
        colleges.append(college_name)
        res = college_name.lower()
        colleges.append(res)

with open('test.csv', newline='') as f:
    reader_confession = csv.reader(f)
    data_confession = list(reader_confession)

file1 = open("iiit_source.txt","w+")
counter = 0
for i in data_confession:
    sent = str(i)
    for j in colleges:
        sent = sent.replace(str(j), "iiit" )
    for j in university:
        sent = sent.replace(str(j), "college")
    file1.write(sent)

