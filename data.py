from tkinter import *
from sqlite3 import *
from tkinter import messagebox
from tkinter.messagebox import *
conn=connect("aditya")
cur=conn.cursor()
def insert(rollno,name):
    print(rollno.get(),name.get())
    rollno=rollno.get()
    name=name.get()
    create="""create table if not exists aec(rollno varchar(20),name varchar(100))"""
    cur.execute(create)
    conn.commit()
    if(rollno!="" and name!=""):
        sel="select * from aec where rollno=?"
        values=[rollno,]
        cur.execute(sel,values)
        data1=cur.fetchall()
        if(len(data1)==0):
            insert="""insert into aec (rollno,name)values(?,?)"""
            values=[rollno,name]
            d=cur.execute(insert,values)
            conn.commit()
            if d:
                messagebox.showinfo("Notice","inserted")
            else:
                messagebox.showinfo("Warning","Not Inserted")
        else:
            messagebox.showinfo("warning","Already in db")
            confirm=messagebox.askokcancel("conformation","Are you want to update?")
            if confirm:
                update="update aec set rollno=?,where name=?"
                values=[rollno,name]
                conn.commit()
                messagebox.showinfo("info","Data is updated")
    else:
        messagebox.showinfo("warning","some fields are empty")
                    
                    
    
        t1.delete(0,END)
        t2.delete(0,END)
def view():
    select="select * from aec"
    cur.execute(select)
    data=cur.fetchall()
    for row in data:
        for r in row:
            print(r,end=" ")
def delete():
    confirm=messagebox.askokcancel("conformation","Are you sure to delete?")
    if confirm:
        delete="delete from aec"
        cur.execute(delete)
        messagebox.showinfo("Notice","Data is Deleted")
        conn.commit()
        
root=Tk()
root.title("my data")
root.geometry("600x600")
l1=Label(root,text="rollno")
l1.grid(row=0,column=0)
roll_txt=StringVar()
t1=Entry(root,textvariable=roll_txt)
t1.grid(row=0,column=1)




l2=Label(root,text="name")
l2.grid(row=1,column=0)
name_txt=StringVar()
t2=Entry(root,textvariable=name_txt)
t2.grid(row=1,column=1)
b1=Button(root,text="Register",command=lambda:insert(roll_txt,name_txt))
b1.grid(row=2,column=0,columnspan=4)
b2=Button(root,text="view data",command=view)
b2.grid(row=3,column=0,columnspan=4)
b3=Button(root,text="delete data",command=delete)
b3.grid(row=4,column=0,columnspan=4)



root.mainloop()
