import tkinter as tk
import tkinter.messagebox
import pickle

window=tk.Tk()
window.title('Welcome to this livebroadcast')
window.geometry('450x300')
#welcome image
canvas=tk.Canvas(window,bg='green',height=150,
                 width=450)

image_file=tk.PhotoImage(file='timg.gif')
image=canvas.create_image(0,0,anchor='nw',image=image_file)#锚点
canvas.pack(side='top')

#label
tk.Label(window,text='User name:').place(x=50,y=160)
tk.Label(window,text='Password:').place(x=50,y=190)
#entry
var_user_name=tk.StringVar()
var_user_name.set('example@python.com')

var_user_pwd=tk.StringVar()

entry_user_name=tk.Entry(window,textvariable=var_user_name)
entry_user_name.place(x=160,y=150)
entry_user_pwd=tk.Entry(window,textvariable=var_user_pwd,show='*')
entry_user_pwd.place(x=160,y=190)

#button
def user_login():
    user_name=var_user_name.get()
    user_pwd=var_user_pwd.get()
    try:
        with open('usrs_info.pickle','rb') as user_file:
            usrs_info=pickle.load(user_file)
    except FileNotFoundError:
        with open('usrs_info.pickle','wb') as user_file:
            usrs_info={'admin':'admin'}
            pickle.dump(usrs_info,user_file)
            
    if user_name in usrs_info:
        if user_pwd==usrs_info[user_name]:
            tk.messagebox.showinfo(title='Welcome',message='How are you?'+user_name)
        else:
            tk.messagebox.showerror(title='Error',message='Error,your password is incorrect')
    else:
        is_sign_up=tk.messagebox.askyesno(title='Welcome',message=
                                          'But you have not signed up yet.\nSign up please!')
    if is_sign_up:
        user_sign_up()




def user_sign_up():
    #top layer
    window_sign_up=tk.Toplevel(window)
    window_sign_up.geometry('350x200')
    window_sign_up.title('Sign up')
    #label
    tk.Label(window_sign_up,text='User name:').place(x=10,y=10)
    tk.Label(window_sign_up,text='Password:').place(x=10,y=50)
    tk.Label(window_sign_up,text='Confirm:').place(x=10,y=100)
    #entry
    new_user_name=tk.StringVar()
    new_user_name.set('NAME')
    new_user_pwd=tk.StringVar()
    new_user_cpwd=tk.StringVar()
    
    entry_new_name=tk.Entry(window_sign_up,textvariable=new_user_name)
    entry_new_name.place(x=100,y=10)
    entry_new_pwd=tk.Entry(window_sign_up,textvariable=new_user_pwd)
    entry_new_pwd.place(x=100,y=50)
    entry_new_cpwd=tk.Entry(window_sign_up,textvariable=new_user_cpwd)
    entry_new_cpwd.place(x=100,y=100)
           
    #button
    def confirm_sign():
        np=new_user_pwd.get()
        npc=new_user_cpwd.get()
        nn=new_user_name.get()
        with open('usrs_info.pickle','rb') as usr_file:
            exist_usr_info=pickle.load(usr_file)
        if np!=npc:
            tk.messagebox.showerror(title='Error',message='Password and Confirm password must be same')
        elif nn in exist_usr_info:
            tk.messagebox.showerror(title='Error',message='The user name has already existed')
        else:
            exist_usr_info[nn]=np#字典
            with open('usrs_info.pickle','wb') as usr_file:
                pickle.dump(exist_usr_info,usr_file)
            tk.messagebox.showinfo(title='Welcome',message='You have successfully signed up')
            window_sign_up.destroy()
    sign_up_btn=tk.Button(window_sign_up,text='Sign in',command=confirm_sign)
    sign_up_btn.place(x=175,y=150)
    


btn_login=tk.Button(window,text='Login',command=user_login)
btn_login.place(x=170,y=230)
btn_sign_up=tk.Button(window,text='Sign up',command=user_sign_up)
btn_sign_up.place(x=220,y=230)

window.mainloop()
