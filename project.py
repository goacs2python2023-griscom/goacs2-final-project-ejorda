import numpy
from statistics import mean
from bokeh.plotting import figure, show

f = open("songsHappy.csv", "r")
CountryList = [
[],
[],
[],
[],
[],
[],
[],
[],
[],
[],
]

Finland = CountryList[0]
Denmark = CountryList[1]
Switzerland = CountryList[2]
Iceland = CountryList[3]
Netherlands = CountryList[4]
Sweden = CountryList[5]
Israel = CountryList[6]
Luxembourg = CountryList[7]
Australia = CountryList[8]
Norway = CountryList[9]

for line in f:
    data = line.split(",")
    valence = data[9]
    if data[0] == ("Finland"):
        Finland.append(int(valence))
    elif data[0] == ("Denmark"):
        Denmark.append(int(valence))
    elif data[0] == ("Switzerland"):
        Switzerland.append(int(valence))
    elif data[0] == ("Iceland"):
        Iceland.append(int(valence))
    elif data[0] == ("Netherlands"):
        Netherlands.append(int(valence))
    elif data[0] == ("Sweden"):
        Sweden.append(int(valence))
    elif data[0] == ("Luxembourg"):
        Luxembourg.append(int(valence))
    elif data[0] == ("Israel"):
        Israel.append(int(valence))
    elif data[0] == ("Australia"):
        Australia.append(int(valence))
    elif data[0] == ("Norway"):
        Norway.append(int(valence))

p = figure(width=800, height=800, title="Countries and Music Valence                                                                                         Blue = One Song, Red = Average", x_range = (0, 11), y_range = (0, 100))

x = 1
def average(con):
    avg = int(mean((con)))
    return avg

for country in CountryList:
    xvar = [x]*50
    p.circle(xvar, country, size=10, color="navy", alpha=0.5)
    p.circle(x, average(country), size=10, color="red", alpha=1)
    x += 1

p.xaxis.axis_label = "Countries Ranking"
p.yaxis.axis_label = "Valence Level"
show(p)
