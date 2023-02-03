import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('IMDB-Movie-Data.csv')
df.fillna(-1, inplace = True)
df.dropna()
df.info()
    
films = []
 
# def johnny_films(row):
#     global films 
#     if row['Actors'].find('Johnny Depp') != -1:
#         films.append(row['Title'])
#         films.append(row['Metascore'])
#         # films.append(row['Genre'])
#     return False

# df.apply(johnny_films, axis = 1)
# for film in films:
#     print(film)

# def a(row):
#     if row["Title"].find('Iron') != -1:
#         films.append(row['Title'])
#     return False
# df.apply(a, axis = 1)
# for film in films:
#     print(film)

# def robbert_films(row):
#     global films 
#     if row['Actors'].find('Robert Downey Jr.') != -1:
#         # print('Робберт-дауни Мл.')
#         films.append(row['Title'])
#         films.append(row['Metascore'])
#         # films.append(row['Genre'])
#     return False

# df.apply(robbert_films, axis = 1)
# for film in films:
#     print(film)

# def leo_films(row):
#     global films 
#     if row['Actors'].find('Leonardo DiCaprio') != -1:
#         films.append(row['Title'])
#         films.append(row['Metascore'])
#         # films.append(row['Genre'])
#     return False

# df.apply(leo_films, axis = 1)
# for film in films:
#     print(film)

def den_films(row):
    global films 
    if row['Actors'].find('Denzel Washington') != -1:
        films.append(row['Title'])
        films.append(row['Metascore'])
        # films.append(row['Genre'])
    return False

df.apply(den_films, axis = 1)
for film in films:
    print(film)

print('Средняя оценка 6 фильмов Деппа: 63.67')
print('Средняя оценка 6 фильмов Робберта: 73')
print('Средняя оценка 6 фильмов Леонардо: 76.67')
print('Средняя оценка 6 фильмов Дензела: 68.34')

a = 63.67
b = 73
c = 76.67
d = 68.34

s = pd.Series(data = [a,b,c,d],
index = ['Джонни Депп', "Робберт-дауни Мл.", "Леонардо Ди Каприо", "Дензел Вашингтон"])
s.plot(kind = 'barh')
plt.show()

print('Вывод: фильмы Леонардо Ди Каприо имеют больший средний рейтинг на MetaScore')

# df = pd.read_csv('IMDB-Movie-Data.csv')
# df['Rating'].plot(kind = 'hist', bins = 7)
# plt.show()
# print(df['Rating'].value_counts())
# print(df['Rating'].max())
