import tkinter as tk
top = tk.Tk()#对象
top.title('The first window')#title
top.geometry('500x200')#长宽

var=tk.StringVar()#字符串变量

l=tk.Label(top,textvariable=var,bg='blue',
           font=('Arial',12),width=15,height=2)#2字符高度

l.pack()#布局方式

on_hit=False

def hit_me():
    global on_hit
    if on_hit==False:
        on_hit=True
        var.set('狗才摸鱼')
    else:
        on_hit=False
        var.set('')
b1=tk.Button(top,text='摸',width=15,height=2,
             command=hit_me)
b1.pack()#加入布局
# 进入消息循环
top.mainloop()
