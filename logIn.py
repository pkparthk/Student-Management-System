from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

def toggle_password_visibility():
    if hide_password.get():
        passwordEntry.config(show='*')
        eyeButtonImage.config(image=hideImage)
    else:
        passwordEntry.config(show='')
        eyeButtonImage.config(image=showImage)
    hide_password.set(not hide_password.get())
def login():
    if usernameEntry.get() == '' or passwordEntry.get() == '':
        messagebox.showerror('Error', 'Fields cannot be empty')
    elif usernameEntry.get() == 'Parth' and passwordEntry.get() == '1234':
        messagebox.showinfo('Success', 'Welcome')
        window.destroy()
        import sms

    else:
        messagebox.showerror('Error', 'Please enter correct credentials')

window = Tk()

window.geometry('1280x700+0+0')
window.title('LogIn System of Student Management System')

window.resizable(False, False)

backgroundImage = ImageTk.PhotoImage(file='bg.jpg')

bgLabel = Label(window, image=backgroundImage)
bgLabel.place(x=0, y=0)

loginFrame = Frame(window, bg='white')
loginFrame.place(x=400, y=150)

logoImage = PhotoImage(file='Student logo.png')

logoLabel = Label(loginFrame, image=logoImage, bg='white')
logoLabel.grid(row=0, column=0, columnspan=2, pady=10)

# username
usernameImage = PhotoImage(file='username.png')
usernameLabel = Label(loginFrame,image=usernameImage, text='Username', compound=LEFT,
                      font=('times new roman',20,'bold'), bg='white')
usernameLabel.grid(row=1,column=0, pady=10, padx=20)

usernameEntry = Entry(loginFrame, font=('times new roman',20,'bold'), bd=5, fg='royalblue')
usernameEntry.grid(row=1,column=1, pady=10, padx=20)

# password
passwordImage = PhotoImage(file='password.png')
passwordLabel = Label(loginFrame,image=passwordImage, text='Password', compound=LEFT,
                      font=('times new roman',20,'bold'), bg='white')
passwordLabel.grid(row=2,column=0, pady=10, padx=20)

passwordEntry = Entry(loginFrame, font=('times new roman',20,'bold'), bd=5, fg='royalblue',show='*')
passwordEntry.grid(row=2,column=1, pady=10, padx=20)

showImage=PhotoImage(file='show.png')
hideImage=PhotoImage(file='hide.png')
hide_password = BooleanVar()
hide_password.set(False)
eyeButtonImage=Button(loginFrame, image=hideImage,bd=0,bg='white',cursor='hand2',command=toggle_password_visibility)
eyeButtonImage.grid(row=2,column=2,padx=(0,20))

loginButtonImage = PhotoImage(file='login.png')
loginButton = Button(loginFrame, image=loginButtonImage, bd=0, bg='#ffffff', cursor='hand2', command=login)
loginButton.grid(row=3,column=1, pady=20)
window.mainloop()