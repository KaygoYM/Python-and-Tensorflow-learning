import tkinter as tk
top = tk.Tk()#对象
top.title('台湾南昌')#title
top.geometry('500x600')#长宽

var=tk.StringVar()#字符串变量

#entry
e=tk.Entry(top,show=None)#show='*'
e.pack()


l=tk.Label(top,bg='yellow',width=10,textvariable=var).pack()

def insert_point():
    #var=e.get()#索取entry值
    #t.insert('insert',var)#从鼠标指针所在处插入
    e.delete('0','end')
    temp=lb.get(lb.curselection())
    var.set(temp)
    
    e.insert(0,var.get())


b1=tk.Button(top,text='脖',width=15,height=2,
             command=insert_point).pack()#加入布局

def insert_end():
    var2=e.get()
    t.insert(2.1,var2)#特定位置插
    #'end'插到尾部

b2=tk.Button(top,text='摸',width=15,height=2,
             command=insert_end).pack()

#text
t=tk.Text(top,height=4)
t.pack()


#listbox
varlist=tk.StringVar()
varlist.set(('黑暗剑','香香鸡','还行','怕不是'))
lb=tk.Listbox(top,listvariable=varlist)
list_items=['惊了','爽到']
for item in list_items:
    lb.insert('end',item)#lb.insert(1,'first'),1是index
    #lb.delete(2),2是索引
lb.pack()


#checkbutton
vv1=tk.IntVar()
vv2=tk.IntVar()

lv=tk.Label(top,bg='blue',width=20)
lv.pack()
def print_point():
    if(vv1.get()==1)&(vv2.get()==1):
        lv.config(text='I love both')
    elif(vv1.get()==1)&(vv2.get()==0):
        lv.config(text='I love 小姐姐')
    elif(vv1.get()==0)&(vv2.get()==1):
        lv.config(text='I love 小妹妹')
    else:
        lv.config(text='I love neither')
       
    
cb1=tk.Checkbutton(top,text='小姐姐',variable=vv1,onvalue=1,
                  offvalue=0,
                  command=print_point).pack()
cb2=tk.Checkbutton(top,text='小妹妹',variable=vv2,onvalue=1,
                  offvalue=0,
                  command=print_point).pack()


# 进入消息循环
top.mainloop()
