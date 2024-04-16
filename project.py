import numpy
from statistics import mean
from bokeh.plotting import figure, show

f = open("songsHappy.csv", "r")

Finland = []
Denmark = []
Switzerland = []
Iceland = []
Netherlands = []
Sweden = []
Israel = []
Luxembourg = []
Australia = []
Norway = []

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

p = figure(width=800, height=800, title="Countries and Music Valence", x_range = (0, 11), y_range = (0, 100))
One = [1] * 50
Two = [2] * 50
Three = [3] * 50
Four = [4] * 50
Five = [5] * 50
Six = [6] * 50
Seven = [7] * 50
Eight = [8] * 50
Nine = [9] * 50
Ten = [10] * 50

def average(country):
    avg = int(mean((country)))
    return avg

AvFin = [average(Finland)] * 50
AvDen = [average(Denmark)] * 50
AvIce = [average(Iceland)] * 50
AvSwe = [average(Sweden)]
AvIsr = [average(Israel)]
AvNet = [average(Netherlands)]
AvNor = [average(Norway)]
AvLux = [average(Luxembourg)]
AvSwi = [average(Switzerland)]
AvAus = [average(Australia)]


p.circle(One, Finland, size=10, color="navy", alpha=0.5)
p.circle(Two, Denmark, size=10, color="navy", alpha=0.5)
p.circle(Three, Iceland, size=10, color="navy", alpha=0.5)
p.circle(Four, Sweden, size=10, color="navy", alpha=0.5)
p.circle(Five, Israel, size=10, color="navy", alpha=0.5)
p.circle(Six, Netherlands, size=10, color="navy", alpha=0.5)
p.circle(Seven, Norway, size=10, color="navy", alpha=0.5)
p.circle(Eight, Luxembourg, size=10, color="navy", alpha=0.5)
p.circle(Nine, Switzerland, size=10, color="navy", alpha=0.5)
p.circle(Ten, Australia, size=10, color="navy", alpha=0.5)
# show the results


p.circle(One, AvFin, size=10, color="red", alpha=1)
p.circle(Two, AvDen, size=10, color="red", alpha=1)
p.circle(Three, AvIce, size=10, color="red", alpha=1)
p.circle(Four, AvSwe, size=10, color="red", alpha=1)
p.circle(Five, AvIsr, size=10, color="red", alpha=1)
p.circle(Six, AvNet, size=10, color="red", alpha=1)
p.circle(Seven, AvNor, size=10, color="red", alpha=1)
p.circle(Eight, AvLux, size=10, color="red", alpha=1)
p.circle(Nine, AvSwi, size=10, color="red", alpha=1)
p.circle(Ten, AvAus, size=10, color="red", alpha=1)

p.xaxis.axis_label = "Countries Ranking"
p.yaxis.axis_label = "Valence Level"
show(p)
