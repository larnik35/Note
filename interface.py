from methods import *

def mainMenu(notes, path):
    print("Чтобы посмотреть список команд введите help")
    inputUser = input("Введите команду: ")
    if inputUser.startswith("add"):
        addNote(notes, path)
        return True
    if inputUser.startswith("edit"):
        request = inputUser.partition(" ")
        if request[2] != "":
            editNote(notes, request[2], path)
            return True
        print("Повторите запрос")
        return True
    if inputUser.startswith("delete"):
        request = inputUser.partition(" ")
        if request[2] != "":
            deleteNote(notes, request[2], path)
            return True
        print("Повторите запрос")
        return True
    if inputUser.startswith("show"):
        request = inputUser.partition(" ")
        if request[2].startswith("-sel"):
                request2 = request[2].partition(" ")[2].strip().partition(" to ")                                
                showNotesInInterval(notes,
                                    stringToDate(request2[0]),
                                    stringToDate(request2[2]))
                return True
                
        if request[2] != "":            
            print(noteToString(findNote(notes, request[2])))
            return True
        else:
            showNotes(notes)
            return True
    if inputUser.startswith("save"):
        request = inputUser.partition(" ")
        if request[2] != "":
            Counter.path = request[2] + ".csv"
        saveFile(notes, path)
        return True
    if inputUser.startswith("load"):
        request = inputUser.partition(" ")
        if request[2] != "":
            Counter.path = request[2] + ".csv"
        loadFile(notes, path)
        return True
    if inputUser.startswith("exit"):
        return False
    
    if inputUser.startswith("help"):
        print(manual)
        return True
    
manual = ("add\t- добавление новой заметки и сохранение изменений.\n" + 
          "edit\t- редактирование заметкии и сохранение изменений. Необходимо добавлять через пробел id или заголовок редактируемой заметки.\n" +
          "delete\t- удаление заметки и сохранение изменений. Необходимо добавлять через пробел id или заголовок заметки, которую нужно удалить.\n" +
          "show\t- без параметра показывает все заметки. Чтобы посмотреть одну запись нужно добавить через пробел id или заголовок.\n" +
          "\t  параметр -sel <start> to <end> делает выборку по дате. <start> и <end> могут быть пустыми.\n"
          "save\t- без параметра обновляет текущий файл. Название файла без расширения после пробела меняет файл для текущей сессии\n" +
          "load\t- без параметра обновляет данные сессии. Название файла без расширения после пробела меняет файл для текущей сессии\n" +
          "exit\t- выход из программы\n")