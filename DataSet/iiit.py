import nltk
from nltk.tokenize import WordPunctTokenizer
import re
import csv
colleges = []
university_s = ["University", "university", "school", "School", "UNIVERSITY", "SCHOOL" ]
university_p = ["universities","UNIVERSITIES", "Universities", "schools", "Schools", "SCHOOLS"]
current_country = ["USA", "usa", "United States", "united states", "america", "America", "The USA", "the usa", "The US", "the us", "The United States of America", "United States of America",
    "the united states", "the United States", "AMERICA", "UNITED STATES"]
  
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
        myregex = r"\b" + re.escape(str(j)) + r"\b"
        sent = re.sub(myregex, "iiit", sent)
        myregex = r"#" + re.escape(str(j)) + r"*"
        sent = re.sub(myregex, "#iiit", sent)
    for j in university_p:
        myregex = r"\b" + re.escape(str(j)) + r"\b"
        sent = re.sub(myregex, "colleges", sent)
    for j in university_s:
        myregex = r"\b" + re.escape(str(j)) + r"\b"
        sent = re.sub(myregex, "college", sent)
    for j in current_country:
        myregex = r"\b" + re.escape(str(j)) + r"\b"
        sent = re.sub(myregex, "india", sent)
    sent = re.sub(r"\bFreshman\b", "first year", sent)
    sent = re.sub(r"\bfreshmen\b", "first years", sent)
    sent = re.sub(r"\bSophomore\b", "second year", sent)
    sent = re.sub(r"\bsophomores\b", "second years", sent)
    sent = re.sub(r"\btution", "fees", sent)
    file1.write(sent)

