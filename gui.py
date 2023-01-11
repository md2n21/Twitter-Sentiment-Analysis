from tkinter import *
import tkinter as tk
from predict import *



def leftClick(evvnt):
    s.set('')
    enstr = Entry1.get() #get input text
    print('input text:',enstr )
    vText = predict(vectoriser, LRmodel, [enstr]) # predict
    print("result:",vText)
    Entry2.insert(tk.INSERT,vText['sentiment'].values[0])

def leftClick2(evvnt):
    s.set('')
    Entry2.insert(tk.INSERT,' ') 

if __name__ == "__main__":
    #load model
    vectoriser, LRmodel = load_models()
    root = Tk()
    root.geometry("700x500")
    root.title('Predict Tweet Sentiment ')
    
    Label(root,text='Please Enter a Tweet:',width=20).place(x=1,y=100)
    Entry1 = Entry(root)
    Entry1.place(x=200,y=1,width=200, height=150)
    Label(root,text='Critical Result:',width=20).place(x=1,y=300)
    s = StringVar()
    s.set('')
    Entry2 = Entry(root,textvariable=s)
    Entry2.place(x=200,y=200,width=200, height=150)
    Button1 = Button(root,text='Critical',width=8)
    Button1.place(x=40,y=400)
    Button2 = Button(root, text='Refresh', width=8)
    Button2.place(x=130, y=400)
    Button1.bind("<Button-1>",leftClick)
    Button2.bind("<Button-2>",leftClick2) 
    root.mainloop()



