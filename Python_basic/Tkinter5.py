# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 15:01:08 2017

@author: hamch
"""
import tkinter as tk
window=tk.Tk()
window.title('zaima，请问这里是秦智障的直播间吗')
window.geometry('500x250')

var=tk.StringVar()
var2=tk.StringVar()
lab1=tk.Label(window,bg='yellow',width=15,)
lab1.pack()

def print_selection():
    lab1.config(text=var.get())#改参数

#radiobutton
rb1=tk.Radiobutton(window,text='鸡脖',variable=var,
                   value='那是爽到',#对var赋值
                   command=print_selection)
rb2=tk.Radiobutton(window,text='摸鱼',variable=var,
                   value='狗才摸鱼',
                   command=print_selection)
rb3=tk.Radiobutton(window,text='惊了',variable=var,
                   value='堇业先锋',
                   command=print_selection)
rb1.pack()
rb2.pack()
rb3.pack()

#scale_bar
def print_selection2(v):
    lab2.config(text='摸鱼已达'+v+'%')#改参数
s=tk.Scale(window,label='摸鱼进度',from_=0,to=100,
           orient=tk.HORIZONTAL,length=300, 
           showvalue=True,variable=var2,
           tickinterval=20,resolution=0.1,
           command=print_selection2)#length像素宽度
#tickinterval刻度，resolution精度
lab2=tk.Label(window,bg='red',width=15,text='')
s.pack()

lab2.pack()



window.mainloop()
