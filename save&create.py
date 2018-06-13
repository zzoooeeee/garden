from tkinter import *
import pickle

def close():
    o.destroy()

def create_buttons():
    global buttons
    buttons = []
    pickle_off = open("buttons_save","rb")
    file = pickle.load(pickle_off)
    print (file)



    
    '''[line.rstrip('\n') for line in file]
    pickle_off = open("buttons_save_test","rb")
    file = pickle.load(pickle_off)
    print (file)
    buttons_from_file = [line.rstrip('\n') for line in file]
    for i in range(875):
        buttons.append(Button(o, width = buttons_from_file[i]['width'], text = buttons_from_file[i]['text'], highlightbackground = buttons_from_file[i][['highlightbackground'], command = lambda i=i: planted(i)))
        buttons[i].grid(column = i%35, row = i//35)'''
    
                       
def save_buttons():
    global buttons
    '''pickling_on = open("buttons_save","wb")
    pickle.dump(None, pickling_on)
    pickling_on.close()'''
    for i in range(len(buttons)):
        x = buttons[i]['width']
        y = buttons[i]['text']
        z = buttons[i]['highlightbackground']
        b_save = {'width': x, 'text': y, 'highlightbackground': z}
        pickling_on = open("buttons_save","ab")
        pickle.dump(b_save, pickling_on)
        pickling_on.close()
        

def planted(i):
    pass

o = Tk()
o.title('save & create')
o.focus_get()

c = Button(o, width = 10, text = 'save all buttons', command = save_buttons, highlightbackground = 'green')
c.grid(column = 36, row = 10)

d = Button(o, width = 10, text = 'create buttons', command = create_buttons, highlightbackground = 'green')
d.grid(column = 36, row = 15)


buttons = []
for i in range(875):
    buttons.append(Button(o, width = 1, text = str(i), command = lambda i=i: planted(i)))
    buttons[i].grid(column = i%35, row = i//35)

#buttons[0].config(highlightbackground='blue')
for i in range(34,78):
    buttons[i].config(highlightbackground='yellow')

for i in range(340,780):
    buttons[i].config(highlightbackground='red')


o.mainloop()

