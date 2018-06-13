from tkinter import *
import pickle

#testy z gitem

def create_buttons(o):
    global buttons
    buttons = []
    #zrobić try except - z pliku
    for i in range(875):
        buttons.append(Button(o, width = 1, text = str(i), command = lambda i=i: item(i)))
        buttons[i].grid(column = i%35, row = i//35)
        buttons[i].content = None
        
def item(i):
    pass

def save_buttons():
    global buttons
    open("buttons_save", 'w').close()
    for i in range(len(buttons)):
        button_content = buttons[i].content
        button_text = buttons[i]['text']
        button_color = buttons[i]['highlightbackground']
        button_state = buttons[i]['state']
        button_save = {'content': button_content, 'text': button_text, 'highlightbackground': button_color, 'state': button_state}
        pickling_on = open("buttons_save","ab")
        pickle.dump(button_save, pickling_on)
        pickling_on.close()

def close():
    o.destroy()
    #dopisać zapytanie o save


class Perm():
    def __init__(self, name, color):
        self.name = name
        self.color = color

class Plant():
    def __init__(self, name, latin_name, annual, planting_date, description):
        self.name = name
        self.latin_name
        self.annual = annual
        self.planting_date = planting_date
        self.description = description

class Buttons():
    def __init__(self, button_text, button_command, button_highlightbackground, content):
        self.instance = Button(o, width = 1, state = normal, text = button_text, command = button_command, highlightbackground = button_highlightbackground)
        self.content = content

class Map():
    def __init__(self, o):
        create_buttons(o)
        save_button = Button(o, width = 10, text = 'save', command = save_buttons, highlightbackground = 'blue')
        save_button.grid(column = 36, row = 22)
        quit_button = Button(o, width = 10, text = 'quit', command = close, highlightbackground = 'blue')
        quit_button.grid(column = 36, row = 23)

o = Tk()
o.title('ogród Mamy')
o.focus_get()
mamas_garden = Map(o)
o.mainloop()

