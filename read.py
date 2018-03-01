from DataContainer import DataContainer
from Ride import Ride

def getRide(data: str):
    dta = list(map(int, data.split(' ')))
    start = {'i' : dta[0], 'j': dta[1]}
    final = {'i' : dta[2], 'j' : dta[3]}
    e = dta[4]
    l = dta[5]
    return Ride(start, final, e, l)

def getDataContainer(fileName):

    dataContainer: DataContainer

    with open(fileName) as file:
        core = list(map(int, file.readline().split(' ')))
        dataContainer = DataContainer(*core)

        while True:
            try:
                dataContainer.ridesLst.append(getRide(file.readline()))
            except:
                break
        return dataContainer
