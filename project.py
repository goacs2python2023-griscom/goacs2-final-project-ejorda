
f = open("songsHappy - Sheet1.csv", "r")

Finland = []
Denmark = []
Sweden = []
Iceland = []
Netherlands = []

for line in f:
    data = line.split(",")

    valence = data[9]
    if data[0] == ("Finland"):
        Finland.append(valence)
        print (valence)
    elif data[0] == ("Denmark"):
        Denmark.append(valence)
    elif data[0] == ("Sweden"):
        Sweden.append(valence)
    elif data[0] == ("Iceland"):
        Iceland.append(valence)
    elif data[0] == ("Netherlands"):
        Netherlands.append(valence)
        f.close
print (Finland)
print (Denmark)
print (Sweden)
print (Iceland)
print (Netherlands)

