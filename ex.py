import pymysql
con = pymysql.connect(host=hostEntry.get(),user=userEntry.get(),passwd=passwordEntry.get())
mycursor=con.cursor()
query='create database timetable'
mycursor.execute(query)
query='use timetable'
mycursor.execute()

