import tkinter as tk

window=tk.Tk()
window.title('My Window')
window.geometry('400x400')
#canvas画布
canvas=tk.Canvas(window,bg='green',height=100,
                 width=200)

#image_file=tk.PhotoImage(file='cat.gif')
#image=canvas.create_image(0,0,anchor='nw',image=image_file)#锚点
x0,y0,x1,y1=50,50,80,80
line=canvas.create_line(x0,y0,x1,y1)
oval=canvas.create_oval(x0,y0,x1,y1,fill='red')
arc=canvas.create_arc(x0+30,y0+30,x1+30,y1+30,start=0,extent=180)
rect=canvas.create_rectangle(100,30,100+20,30+20)
canvas.pack()
def move():
    canvas.move(rect,0,2)

button=tk.Button(window,text='move',command=move).pack()
#menubar菜单
l=tk.Label(window,bg='yellow',text='')
l.pack()
counter=0
def new_file():
    global counter
    l.config(text='do'+str(counter))
    counter+=1
    
menubar=tk.Menu(window)
filem=tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label='File',menu=filem)
filem.add_command(label='New',command=new_file)
filem.add_command(label='Open',command=new_file)
filem.add_command(label='Save',command=new_file)

filem.add_separator()
filem.add_command(label='Exit',command=window.quit)

editm=tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label='Edit',menu=editm)
editm.add_command(label='Cut',command=new_file)
editm.add_command(label='Copy',command=new_file)
editm.add_command(label='Paste',command=new_file)

subm=tk.Menu(filem)
filem.add_cascade(label='Import',menu=subm,underline=0)
subm.add_command(label='Import from files',command=new_file)


window.config(menu=menubar)

#Frame
tk.Label(window,text='on the window').pack()
frm=tk.Frame(window).pack()#主frame
frm_l=tk.Frame(frm,)
frm_r=tk.Frame(frm,)
frm_l.pack(side='left')
frm_r.pack(side='right')
tk.Label(frm_l,text='Left').pack()
tk.Label(frm_r,text='Right').pack()

#messagebox弹窗
def hit():
    #pass
    #tk.messagebox.showinfo(title='dog',message='LOL')
    #tk.messagebox.showwarning(title='HI',message='NONONO')
    tk.messagebox.showerror(title='cat',message='GO die')


tk.Button(window,text='Hit',command=hit).pack()

#pack grid place
tk.Label(window,text=1).pack(side='top')
tk.Label(window,text=1).pack(side='bottom')
tk.Label(window,text=1).pack(side='left')
tk.Label(window,text=1).pack(side='right')


#for i in range(4):
#    for j in range(3):
#       tk.Label(window,bg='red',text=str(i)+str(j)).grid(row=i,column=j,ipadx=10,ipady=10)

tk.Label(window,text='kkk').place(x=1,y=10,anchor='sw')

window.mainloop()