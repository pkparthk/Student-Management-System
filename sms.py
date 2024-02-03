from tkinter import *
import time
import ttkthemes
from tkinter import ttk, messagebox,filedialog
import pymysql
import pandas

# functionality part
def exit():
    result=messagebox.askyesno('Confirm','Do you want to Exit?')
    if result:
        root.destroy()
    else:
        pass
def export_data():
    url=filedialog.asksaveasfilename(defaultextension='.csv')
    indexing = studentTable.get_children()
    newlist = []
    for index in indexing:
        content=studentTable.item(index)
        datalist = content['values']
        newlist.append(datalist)
    table=pandas.DataFrame(newlist,columns=['Id','Name','Father''s Name','Mother''s Name', 'Contact No', 'Email', 'D.O.B', 'Gender', 'Blood Group',
                                            'Address', 'Added Date', 'Added Time'])
    table.to_csv(url, index=False)
    messagebox.showinfo('Success', 'Data is Saved Successfully')

def toplevel_data(title,button_text,command):
    global idEntry,nameEntry, fatherEntry, motherEntry, contactEntry, emailEntry, dobEntry, genderEntry, bloodEntry, addressEntry, screen
    screen = Toplevel()
    screen.resizable(False, False)
    screen.grab_set()
    screen.title(title)
    idLabel = Label(screen, text='Id', font=('times new roman', 20, 'bold'))
    idLabel.grid(row=0, column=0, padx=30, pady=15, sticky=W)
    idEntry = Entry(screen, font=('roman', 15, 'bold'))
    idEntry.grid(row=0, column=1, padx=15, pady=15)
    nameLabel = Label(screen, text='Name', font=('times new roman', 20, 'bold'))
    nameLabel.grid(row=1, column=0, padx=30, pady=15, sticky=W)
    nameEntry = Entry(screen, font=('roman', 15, 'bold'))
    nameEntry.grid(row=1, column=1, padx=15, pady=15)
    fatherLabel = Label(screen, text='Father''s Name', font=('times new roman', 20, 'bold'))
    fatherLabel.grid(row=2, column=0, padx=30, pady=15, sticky=W)
    fatherEntry = Entry(screen, font=('roman', 15, 'bold'))
    fatherEntry.grid(row=2, column=1, padx=15, pady=15)
    motherLabel = Label(screen, text='Mother''s Name', font=('times new roman', 20, 'bold'))
    motherLabel.grid(row=3, column=0, padx=30, pady=15, sticky=W)
    motherEntry = Entry(screen, font=('roman', 15, 'bold'))
    motherEntry.grid(row=3, column=1, padx=15, pady=15)
    contactLabel = Label(screen, text='Contact No.', font=('times new roman', 20, 'bold'))
    contactLabel.grid(row=4, column=0, padx=30, pady=15, sticky=W)
    contactEntry = Entry(screen, font=('roman', 15, 'bold'))
    contactEntry.grid(row=4, column=1, padx=15, pady=15)
    emailLabel = Label(screen, text='Email', font=('times new roman', 20, 'bold'))
    emailLabel.grid(row=5, column=0, padx=30, pady=15, sticky=W)
    emailEntry = Entry(screen, font=('roman', 15, 'bold'))
    emailEntry.grid(row=5, column=1, padx=15, pady=15)
    dobLabel = Label(screen, text='D.O.B', font=('times new roman', 20, 'bold'))
    dobLabel.grid(row=6, column=0, padx=30, pady=15, sticky=W)
    dobEntry = Entry(screen, font=('roman', 15, 'bold'))
    dobEntry.grid(row=6, column=1, padx=15, pady=15)
    genderLabel = Label(screen, text='Gender', font=('times new roman', 20, 'bold'))
    genderLabel.grid(row=7, column=0, padx=30, pady=15, sticky=W)
    genderEntry = Entry(screen, font=('roman', 15, 'bold'))
    genderEntry.grid(row=7, column=1, padx=15, pady=15)
    bloodLabel = Label(screen, text='Blood Group', font=('times new roman', 20, 'bold'))
    bloodLabel.grid(row=8, column=0, padx=30, pady=15, sticky=W)
    bloodEntry = Entry(screen, font=('roman', 15, 'bold'))
    bloodEntry.grid(row=8, column=1, padx=15, pady=15)
    addressLabel = Label(screen, text='Address', font=('times new roman', 20, 'bold'))
    addressLabel.grid(row=9, column=0, padx=30, pady=15, sticky=W)
    addressEntry = Entry(screen, font=('roman', 15, 'bold'))
    addressEntry.grid(row=9, column=1, padx=15, pady=15)
    student_button = ttk.Button(screen, text=button_text, command=command)
    student_button.grid(row=10, columnspan=2, pady=15)
    if title=='Update Student':
        indexing = studentTable.focus()

        content = studentTable.item(indexing)
        listdata = content['values']
        idEntry.insert(0, listdata[0])
        nameEntry.insert(0, listdata[1])
        fatherEntry.insert(0,listdata[2])
        motherEntry.insert(0,listdata[3])
        contactEntry.insert(0, listdata[4])
        emailEntry.insert(0, listdata[5])
        dobEntry.insert(0, listdata[6])
        genderEntry.insert(0, listdata[7])
        bloodEntry.insert(0,listdata[8])
        addressEntry.insert(0, listdata[9])

def update_data():
    query = ('update student set name=%s, father=%s, mother=%s, contact=%s, email=%s, dob=%s, gender=%s, blood=%s, '
             'address=%s, date=%s,time=%s where id=%s')
    mycursor.execute(query,(nameEntry.get(),fatherEntry.get(),motherEntry.get(),contactEntry.get(),emailEntry.get(),dobEntry.get(),genderEntry.get(), bloodEntry.get(),
                            addressEntry.get(),date, currenttime, idEntry.get()))
    con.commit()
    messagebox.showinfo('Success', f'Id {idEntry.get()} is modified successfully',parent=screen)
    screen.destroy()
    show_student()

def delete_student():
    indexing=studentTable.focus()
    content=studentTable.item(indexing)
    content_id=content['values'][0]
    query='delete from student where id=%s'
    mycursor.execute(query,content_id)
    con.commit()
    messagebox.showinfo('DELETED',f'Id {content_id} is Deleted Successfully')
    query='select * from student'
    mycursor.execute(query)
    fetched_data=mycursor.fetchall()
    studentTable.delete(*studentTable.get_children())
    for data in fetched_data:
        studentTable.insert('',END,values=data)

def show_student():
    query = 'select * from student'
    mycursor.execute(query)
    fetched_data = mycursor.fetchall()
    studentTable.delete(*studentTable.get_children())
    for data in fetched_data:
        studentTable.insert('', END, values=data)

def search_data():
    query='select * from student where id=%s or name=%s or father=%s or mother=%s or contact=%s or email=%s or dob=%s or gender=%s or address=%s or blood=%s'
    mycursor.execute(query,(idEntry.get(),nameEntry.get(),fatherEntry.get(),motherEntry.get(),contactEntry.get(), emailEntry.get(),dobEntry.get(),genderEntry.get(),bloodEntry.get(),addressEntry.get()))
    studentTable.delete(*studentTable.get_children())
    fetched_data=mycursor.fetchall()
    for data in fetched_data:
        studentTable.insert('',END,values=data)

def add_data():
    if idEntry.get()=='' or nameEntry.get()=='' or fatherEntry.get()==''or motherEntry.get()=='' or contactEntry.get()=='' or emailEntry.get()=='' or dobEntry.get()=='' or addressEntry.get()=='' or genderEntry.get()=='' or bloodEntry.get()=='':
        messagebox.showerror('Error', 'All fields are required',parent=screen)

    else:
        try:
            query = 'insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(query,(idEntry.get(),nameEntry.get(),fatherEntry.get(),motherEntry.get(),contactEntry.get(),emailEntry.get(),dobEntry.get(),
                                    genderEntry.get(), bloodEntry.get(), addressEntry.get(),date,currenttime))
            con.commit()
            result = messagebox.askyesno('Confirm','Data added Successfully. Do you want to clean the form?',parent=screen)
            if result:
                idEntry.delete(0,END)
                nameEntry.delete(0,END)
                fatherEntry.delete(0,END)
                motherEntry.delete(0,END)
                contactEntry.delete(0,END)
                emailEntry.delete(0,END)
                dobEntry.delete(0,END)
                genderEntry.delete(0,END)
                bloodEntry.delete(0,END)
                addressEntry.delete(0,END)
                screen.destroy()
            else:
                pass
        except:
            messagebox.showerror('Error', 'Id cannot be repeated', parent=screen)
            return

        query = 'select *from student'
        mycursor.execute(query)
        fetched_data = mycursor.fetchall()
        studentTable.delete(*studentTable.get_children())
        for data in fetched_data:
            studentTable.insert('',END,values=data)


def connect_database():
    def connect():
        global mycursor, con
        try:
            # con = pymysql.connect(host=hostEntry.get(),user=userEntry.get(),passwd=passwordEntry.get())
            con = pymysql.connect(host='localhost', user='root', passwd='1304')
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error','Invalid Details',parent=connectWindow)
            return
        try:
            query='create database studentManagementSystem'
            mycursor.execute(query)
            query='use studentManagementSystem'
            mycursor.execute(query)
            query=('create table student(id int not null primary key, name varchar(30), father varchar(40), '
                   'mother varchar(40), contact varchar(10),email varchar(30), dob varchar(20), gender varchar(20), '
                   'blood varchar(20), address varchar(100),date varchar(50), time varchar(50))')
            mycursor.execute(query)
        except:
            query='use studentManagementSystem'
            mycursor.execute(query)
        messagebox.showinfo('Success', 'Database Connection is Successful', parent=connectWindow)
        connectWindow.destroy()
        addStudentButton.config(state=NORMAL)
        searchStudentButton.config(state=NORMAL)
        updateStudentButton.config(state=NORMAL)
        showStudentButton.config(state=NORMAL)
        exportDataButton.config(state=NORMAL)
        deleteStudentButton.config(state=NORMAL)

    def toggle_password_visibility():
        if hide_password.get():
            passwordEntry.config(show='*')
            eyeButtonImage.config(image=hideImage)
        else:
            passwordEntry.config(show='')
            eyeButtonImage.config(image=showImage)
        hide_password.set(not hide_password.get())

    connectWindow = Toplevel()
    connectWindow.grab_set()
    connectWindow.geometry('520x270+730+230')
    connectWindow.title('Database Connection')
    connectWindow.resizable(False,False)

    hostnameLabel = Label(connectWindow, text='Host Name', font=('arial',20,'bold'))
    hostnameLabel.grid(row=0,column=0,padx=20,pady=20)

    hostEntry=Entry(connectWindow,font=('roman',15,'bold'),bd=2)
    hostEntry.grid(row=0,column=1,padx=40,pady=20)

    usernameLabel = Label(connectWindow, text='User Name', font=('arial', 20, 'bold'))
    usernameLabel.grid(row=1, column=0, padx=20)

    userEntry = Entry(connectWindow, font=('roman', 15, 'bold'), bd=2)
    userEntry.grid(row=1, column=1, padx=40, pady=20)

    passwordLabel = Label(connectWindow, text='Password', font=('arial', 20, 'bold'))
    passwordLabel.grid(row=2, column=0, padx=20)

    passwordEntry = Entry(connectWindow, font=('times new roman', 15, 'bold'), bd=2, show='*')
    passwordEntry.grid(row=2, column=1, padx=40, pady=20)

    showImage = PhotoImage(file='show.png')
    hideImage = PhotoImage(file='hide.png')
    hide_password = BooleanVar()
    hide_password.set(False)
    eyeButtonImage = Button(connectWindow, image=hideImage, bd=0, cursor='hand2',command=toggle_password_visibility)
    eyeButtonImage.grid(row=2, column=2)

    connectButton=ttk.Button(connectWindow,text='CONNECT', command=connect, cursor='hand2')
    connectButton.grid(row=3,columnspan=2)

count=0
text = ''
def slider():
    global text
    global count
    if count == len(s):
        count = 0
        text=''
    text=text+s[count]  # s
    count += 1
    sliderLabel.config(text=text)
    sliderLabel.after(300,slider)
def clock():
    global date, currenttime
    date = time.strftime('%d/%m/%Y')
    currenttime = time.strftime('%H:%M:%S')
    datetimeLabel.config(text=f'   Date: {date}\nTime: {currenttime}')
    datetimeLabel.after(1000, clock)

# GUI Part
root = ttkthemes.ThemedTk()

root.get_themes()

root.set_theme('radiance')

root.geometry('1174x680+0+0')
root.resizable(False, False)
root.title('Student Management System')

datetimeLabel=Label(root,font=('times new roman',18,'bold'))
datetimeLabel.place(x=5,y=5)
clock()
s='Student Management System'
sliderLabel=Label(root,text=s,font=('arial',28,'italic bold'), width=30)
sliderLabel.place(x=200, y=0)
slider()

connectButton = ttk.Button(root,text='Connect to Database', command=connect_database,cursor='hand2')
connectButton.place(x=980,y=0)

leftFrame=Frame(root)
leftFrame.place(x=50, y=80, width=300, height=600)

logo_image=PhotoImage(file='graduates.png')
logo_Label=Label(leftFrame,image=logo_image)
logo_Label.grid(row=0,column=0)

addStudentButton=ttk.Button(leftFrame,text='Add Student',width=25,cursor='hand2', state=DISABLED,command=lambda :toplevel_data('Add Student', 'ADD STUDENT',add_data))
addStudentButton.grid(row=1,column=0,pady=20)

searchStudentButton=ttk.Button(leftFrame,text='Search Student',width=25,cursor='hand2', state=DISABLED,command =lambda: toplevel_data('Search Student','SEARCH STUDENT', search_data))
searchStudentButton.grid(row=2,column=0,pady=20)

deleteStudentButton=ttk.Button(leftFrame,text='Delete Student',width=25,cursor='hand2', state=DISABLED,command = delete_student)
deleteStudentButton.grid(row=3,column=0,pady=20)

updateStudentButton=ttk.Button(leftFrame,text='Update Student',width=25,cursor='hand2', state=DISABLED,command = lambda: toplevel_data('Update Student','UPDATE STUDENT', update_data))
updateStudentButton.grid(row=4,column=0,pady=20)

showStudentButton=ttk.Button(leftFrame,text='Show Student',width=25,cursor='hand2', state=DISABLED,command=show_student)
showStudentButton.grid(row=5,column=0,pady=20)

exportDataButton=ttk.Button(leftFrame,text='Export Data',width=25,cursor='hand2', state=DISABLED, command=export_data)
exportDataButton.grid(row=6,column=0,pady=20)

exitButton=ttk.Button(leftFrame,text='Exit',width=25,cursor='hand2', command=exit)
exitButton.grid(row=7,column=0,pady=20)


rightFrame=Frame(root)
rightFrame.place(x=350, y=80, width=820, height=600)

scrollBarX=Scrollbar(rightFrame,orient=HORIZONTAL,cursor='hand2')
scrollBarY=Scrollbar(rightFrame,orient=VERTICAL,cursor='hand2')
studentTable = ttk.Treeview(rightFrame,columns=('Id', 'Name','Father''s Name','Mother''s Name', 'Mobile No.', 'Email',
                                                'D.O.B','Gender', 'Blood Group', 'Address', 'Added Date', 'Added Time'),
                            xscrollcommand=scrollBarX,yscrollcommand=scrollBarY)
scrollBarX.config(command=studentTable.xview)
scrollBarY.config(command=studentTable.yview)
scrollBarX.pack(side=BOTTOM, fill=X)
scrollBarY.pack(side=RIGHT, fill=Y)
studentTable.pack(fill=BOTH, expand=1)

studentTable.heading('Id', text='ID')
studentTable.heading('Name', text='NAME')
studentTable.heading('Father''s Name', text='FATHER''s NAME')
studentTable.heading('Mother''s Name', text='MOTHER''s NAME')
studentTable.heading('Mobile No.', text='Contact No.')
studentTable.heading('Email', text='E-Mail')
studentTable.heading('D.O.B', text='D.O.B')
studentTable.heading('Gender', text='GENDER')
studentTable.heading('Blood Group', text='BLOOD GROUP')
studentTable.heading('Address', text='ADDRESS')
studentTable.heading('Added Date', text='ADDED DATE')
studentTable.heading('Added Time', text='ADDED TIME')

studentTable.column('Id',width=50,anchor=CENTER)
studentTable.column('Name',width=250,anchor=CENTER)
studentTable.column('Father''s Name',width=250,anchor=CENTER)
studentTable.column('Mother''s Name',width=250,anchor=CENTER)
studentTable.column('Mobile No.',width=100,anchor=CENTER)
studentTable.column('Email',width=250,anchor=CENTER)
studentTable.column('D.O.B',width=100,anchor=CENTER)
studentTable.column('Gender',width=100,anchor=CENTER)
studentTable.column('Blood Group', width=140, anchor=CENTER)
studentTable.column('Address',width=300,anchor=CENTER)
studentTable.column('Added Date',width=150,anchor=CENTER)
studentTable.column('Added Time',width=150,anchor=CENTER)

style=ttk.Style()
style.configure('Treeview',rowheight=30,font=('ariel',11,'bold'),foregrounds='red4',background='white', fieldbackground='white' )
style.configure('Treeview',font=('ariel',13,'bold'),foreground='red')
studentTable.config(show='headings')

root.mainloop()