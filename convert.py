from datetime import datetime

def stringToDate(text):
    try: return datetime.strptime(text, "%d %B %Y %I:%M")
    except: 
        try: return datetime.strptime(text, "%d.%m.%Y %I:%M")
        except:
            try: return datetime.strptime(text, "%d.%m.%y %I:%M")
            except:
                try: return datetime.strptime(text, "%d %B %Y")
                except: 
                    try: return datetime.strptime(text, "%d.%m.%Y")
                    except: 
                        try: return datetime.strptime(text, "%d.%m.%y")
                        except: print("Неверный формат даты")

def dateToString(date):
    return date.strftime("%d %B %Y %I:%M")

def noteToString(note): 
    return "{}\n{}|{}\n{}\n{}\n".format("-"*20, note["id"], dateToString(note["date"]), note["header"], note["body"])

def notesToString(data):
    massage = ""
    for note in data:
        noteText = noteToString(note)
        massage +=  noteText
    return massage