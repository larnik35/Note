from counter import Counter
from datetime import datetime
from convert import stringToDate, dateToString

def saveFile(data, path):
    tmp = list()
    for note in data:
        tmp.append("{};{};{};{}".format(note["id"], 
                                        note["header"], 
                                        note["body"], 
                                        dateToString(note["date"])))
    text = "\n".join(tmp)
    with open(path, "w") as file:
        file.write(text)

def loadFile(data, path):
    tmp = list()
    with open(path, "r") as file:
        for line in file:
            tmp.append(line.replace("\n", "").split(";"))
    tmpM = list()
    for item in tmp:
        data.append({"id" : int(item[0]), 
                     "header" : item[1], 
                     "body" : item[2],
                     "date" : stringToDate(item[3])})
        tmpM.append(int(item[0]))
    if len(tmpM) > 0:
        currentIndex = max(tmpM)
        if currentIndex >= Counter.index:
            Counter.index = currentIndex
