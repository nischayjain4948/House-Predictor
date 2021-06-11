import pandas as pd

import warnings
warnings.filterwarnings('ignore') 
import tkinter as tk

from tkinter import *
model = pd.read_pickle('HousePricePredictor')
import math

app=tk.Tk()
app.config(bg="blue")
app.geometry('400x400')
app.title("H_pred")
app.iconbitmap(r'D:\House predictor\logo.ico')
Photo = PhotoImage(file='D:\House predictor\housepic.png')
photo_Label = Label(image=Photo)
photo_Label.pack()





tk.Label(app,width=15,text="Area Income",bg="white",fg="black").place(x=20,y=30)
tk.Label(app,width=15,text="Area House Age",bg="white",fg="black").place(x=20,y=60)
tk.Label(app,width=15,text="Number of Rooms",bg="white",fg="black").place(x=20,y=90)
tk.Label(app,width=15,text="Area Population",bg="white",fg="black").place(x=20,y=120)
tk.Label(app,width=15,text="House Price :",fg="white",bg="black",font=("Helvetica", 15,"bold")).place(x=20,y=210)


area_income=tk.Variable(app)
house_age=tk.Variable(app)
rooms=tk.Variable(app)
population=tk.Variable(app)

tk.Entry(app,width=25,textvariable=area_income,bg='#ffffff').place(x=230,y=30)
tk.Entry(app,width=25,textvariable=house_age,bg='#ffffff').place(x=230,y=60)
tk.Entry(app,width=25,textvariable=rooms,bg='#ffffff').place(x=230,y=90)
tk.Entry(app,width=25,textvariable=population,bg='#ffffff').place(x=230,y=120)
predict_var = tk.Variable(app)
tk.Label(app,textvariable=predict_var,fg="midnightblue",bg="azure3",font=("Helvetica", 15,"bold")).place(x=230,y=210)
def register():
    a=area_income.get()
    b=house_age.get()
    c=rooms.get()
    d=population.get()
    query = pd.DataFrame({'Avg. Area Income':[a],'Avg. Area House Age':[b],
                      'Avg. Area Number of Rooms':[c],'Area Population':[d]})
    #n="%.1f$'%(model.predict(query)[0])"
    e=model.predict(query)[0]
    predict_var.set("{0:.1f}$".format(e))
    area_income.set('')
    house_age.set('')
    rooms.set('')
    population.set('')
    
    
    
    
tk.Button(app,text="Predict",command=register,bg="midnightblue",fg="white",font='arial 15 underline').place(x=150,y=150) 











    
    

app.mainloop()
