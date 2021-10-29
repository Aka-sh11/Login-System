import tkinter as tk
from tkinter.messagebox import *


class Login:
    def __init__(self, root):

        # 2D list of users
        self.users = [['user', 'pass']]

        # Tkinter FrontEnd
        self.root = root
        self.root.title('Login System')
        self.root.geometry('1199x600+100+50')
        # self.root.resizable(False,False)

        # Loading Image
        self.bg = tk.PhotoImage(file='bg.png')

        # Label to put the image on
        self.bg_image = tk.Label(root, image=self.bg)
        self.bg_image.place(x=0, y=0, relwidth=1, relheight=1)

        # Login Frame
        frame_login = tk.Frame(self.root, bg='white')
        frame_login.place(x=150, y=150, height=340, width=500)

        # Top Title Area
        title_label = tk.Label(frame_login, text='Login Here', font=('Helvetica', 35, 'bold'), bg='White', fg='#005B96')
        title_label.place(x=120, y=20)

        message_label = tk.Label(frame_login, text='Customer Login Area', font=('Gouly old style', 15, 'bold'),
                                 bg='White', fg='#005B96')
        message_label.place(x=140, y=80)

        # Username
        username_label = tk.Label(frame_login, text='Username', font=('Gouly old style', 12), bg='White', fg='Black')
        username_label.place(x=60, y=120)

        self.username_entry = tk.Entry(frame_login, font=('times new roman', 15), bg='#005B96', fg='White')
        self.username_entry.place(x=60, y=150, width=350, height=35)

        # password
        password_label = tk.Label(frame_login, text='Password', font=('Gouly old style', 12), bg='White', fg='Black')
        password_label.place(x=60, y=200)

        self.password_entry = tk.Entry(frame_login, font=('times new roman', 15), bg='#005B96', fg='White')
        self.password_entry.place(x=60, y=230, width=350, height=35)

        # forgot password button
        forget_button = tk.Button(frame_login, text='Forget Password?', font=('times new roman', 10), borderwidth=0,
                                  bg='White', fg='#005B96')
        forget_button.place(x=60, y=270)

        # submit button
        submit_button = tk.Button(self.root, text='Login', font=('times new roman', 20, 'bold'), bg='#005B96',
                                  fg='White', relief='raised', command=self.login)
        submit_button.place(x=300, y=470, width=180, height=40)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == '' or password == '':
            showerror('Empty', 'Entry is Empty! Please Enter Username and Password')
        else:
            for user in self.users:
                if username == user[0] and password == user[1]:
                    showinfo('Correct', f'Welcome {username}\nSigning you in...')
                    self.username_entry.delete(0, tk.END)
                    self.password_entry.delete(0, tk.END)
                    break
                elif username == user[0] and password != user[1]:
                    showerror('Wrong password', 'Wrong password Entered, Please try again')
                    self.password_entry.delete(0, tk.END)
                    break
            else:
                showerror('User Not Found', 'This Account Doesnt exist. Please Sign Up')


root = tk.Tk()
root_obj = Login(root)
root.mainloop()
