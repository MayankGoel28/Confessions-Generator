import pandas as pd

df = pd.read_csv('test.csv')

f = open('text_data.txt', 'w')

for i in range(len(df)):
    data = df.iloc[i]['Content']
    f.write(data[1:-1])
    f.write(".\n")

f.close()
