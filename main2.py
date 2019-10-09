import matplotlib.pyplot as plt
import pandas as pd


data = {'names':  ['Nick', 'Adam', 'Chuy', 'Bob', 'Atla'],
        'jan_ir': [ 100, 102, 122, 154, 133],
        'feb_ir': [  22, 123, 234, 155, 175],
        'mar_ir': [ 117, 156, 125, 129, 167]}


df = pd.DataFrame(data, columns=['names', 'jan_ir', 'feb_ir', 'mar_ir'])

df['total_ir'] = df['jan_ir'] + df['feb_ir'] + df['mar_ir']

print(df)

colors = [(1, .5, .5), (1, .4, .3), (.7, .7, .7), (.6, .6, .6), (.5, .5, .5)]

plt.pie(df['total_ir'],
        labels=df['names'],
        colors=colors,
        autopct="%1.1f%%")

plt.show()