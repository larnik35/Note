from datetime import datetime
from fileManager import *
from convert import noteToString, notesToString
from counter import Counter
def addNote(data, path):
    Counter.index += 1
    data.append({"id" : Counter.index, 
                 "header" : input("Введите заголовок: "), 
                 "body" : input("Введите текст заметки: "), 
                 "date" : datetime.now()})
    saveFile(data, path)

def findNote(data, param):
    if isinstance(param, int):
        for note in data:
            if note["id"] == param:
                return note
    if isinstance(param, str):
        for note in data:
            if note["header"] == param:
                return note 
    print("Нет такой записи!")
    return False

def showNotes(data):
    print(notesToString(data))

def showNotesInInterval(data, dateStart, dateEnd):
    print(notesToString(samplingNoteByDate(data, dateStart, dateEnd)))

def samplingNoteByDate(data, dateStart, dateEnd):
    selection = list()
    if dateStart == None and dateEnd != None:
        for note in data:
            if note["date"] <= dateEnd:
                selection.append(note)
        return selection
    if dateStart != None and dateEnd == None:
        for note in data:
            if dateStart <= note["date"]:
                selection.append(note)
        return selection
    for note in data:
        if dateStart <= note["date"] <= dateEnd:
            selection.append(note)
    return selection

def deleteNote(data, param, path):
    note = findNote(data, param)
    if not note: return
    print("Запись \"" + str(note["header"]) + "\" удалена")
    data.remove(note)            
    saveFile(data, path)

def editNote(data, param, path):
    note = findNote(data, param)
    if not note: return
    check = 0
    inputUser = input("Введите заголловок: ")
    if inputUser != "":
        note["header"] = inputUser
    else: check += 1
    inputUser = input("Введите текст заметки: ")
    if inputUser != "":
        note["body"] = inputUser
    else: check += 1
    if check < 2: 
        note["date"] = datetime.now()
        print("Запись \"" + str(note["header"]) + "\" измененна")            
        saveFile(data, path)