from tkinter import *
import pickle

#testy w testach

def close():
    o.destroy()

def test():
    global b
    b.config(highlightbackground = 'tomato')
    save()
    saved_button()

def save():
    global b
    x = b['width']
    y = b['text']
    z = b['highlightbackground']
    b_save = {'width': x, 'text': y, 'highlightbackground': z}
    pickling_on = open("b_save","wb")
    pickle.dump(b_save, pickling_on)
    pickling_on.close()
    
def saved_button():
    try: 
        pickle_off = open("b_save","rb")
        d = pickle.load(pickle_off)
        test_button = Button(o, width = d['width'], text = d['text'], command = close, highlightbackground = d['highlightbackground'])
        test_button.grid(column = 36, row = 16, rowspan = 15)
        print(d)
    except: pass

o = Tk()
o.title('testy')
o.focus_get()

b = Button(o, width = 10, text = 'test', command = test, highlightbackground = 'tomato')
b.grid(column = 36, row = 1, rowspan = 15)

buttons = []

for i in range(875):
    buttons.append(Button(o, width = 1, text = str(i), command = lambda i=i: planted(i)))
    buttons[i].grid(column = i%35, row = i//35)

#c = Button(o, width = 10, text = 'save', command = save, highlightbackground = 'green')
#c.pack()



o.mainloop()

