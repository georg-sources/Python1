import sys

try:
    datei=open("test.txt")
except IOError as e:
    for par in e.args:
        print(par)
else:
    print("Datei geoeffnet")
    datei.close