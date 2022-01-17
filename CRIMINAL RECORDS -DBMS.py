import mysql.connector as mycon
from tkinter import *
from functools import partial
import matplotlib.pyplot as plt
#select c.*,r.description from crimerecords c,crimes r where c.crimeid=r.crimeid;
def no_crimeinplace():
     mycursor.execute("select count(*),placeofarrest from crimerecords group by placeofarrest")
     data1=mycursor.fetchall()
     list2=[]
     list3=[]
     for i in data1:
          list2.append(i[0])
          list3.append(i[1])
 
     plt.bar(list3,list2,color = "#2D2D30")
     plt.xlabel("Place")
     plt.ylabel("Number of crimes")
     plt.show()
     
def updatepolice():
     def update1():
          sql="update police set salary=%s where pname=%s"
          val=(int(salary.get()),name.get())
          mycursor.execute(sql,val)
          ameLabel=Label(tkWindow,text=name.get()+" updated",fg="#FD6A02",bg="#212121",font="Consolas 12 bold italic").grid(row=4, column=0)
          mydb.commit()
          
          
          
          
     tkWindow =Toplevel()  
     tkWindow.geometry('450x160')  
     tkWindow.title('UPDATE SALARY OF POLICE')
     tkWindow.configure(bg="#212121")     
     nameLabel=Label(tkWindow,text="ENTER POLICE NAME",fg="#FD6A02",bg="#212121",font="Consolas 12 bold italic").grid(row=1, column=0)
     name=StringVar()
     nameEntry=Entry(tkWindow,textvariable=name).grid(row=1, column=1)
     salaryLabel=Label(tkWindow,text="ENTER NEW SALARY",fg="#FD6A02",bg="#212121",font="Consolas 12 bold italic").grid(row=2, column=0)
     salary=StringVar()
     salaryEntry=Entry(tkWindow,textvariable=salary).grid(row=2, column=1)
     ameLabel=Label(tkWindow,text="",fg="#FD6A02",bg="#212121",font="Consolas 12 bold italic").grid(row=3, column=0)
     displaybutton=Button(tkWindow,text="UPDATE",fg="#FD6A02",bg="#2D2D30",activebackground="#FD6A02",font="Helvetica 10 bold",command=update1).grid(row=4,column=1)
     
def crimerate():
     a=()
     dict1={}
     mycursor.execute("select count(*),monthname(dateofcrime) from crimerecords group by monthname(dateofcrime) order by month(dateofcrime)")
     data=mycursor.fetchall()
     date=["January","February","March","April","May","June","July","August","September","October","November","December"]
     for i in date:
          dict1[i]=0
     for i in data:
          dict1[i[1]]=i[0]
     for i in dict1.values():
          a=a+(i,)
     b=list(dict1.keys())
     num=[1,2,3,4,5,6,7,8,9,10]
     year = ["2000", "2004", "2008", "2010", "2012"]
     population = (120, 140, 130, 200, 150)
     plt.bar(b,a,color ="#2D2D30",label="Number of Crimes")
     plt.xlabel("Month")
     plt.ylabel("Number of crimes")
     plt.legend()
     plt.show()
     
def findcriminals():
     def displaybyid():
        list1=" "
        tkWin =Toplevel()  
        tkWin.geometry('600x450')  
        tkWin.title('DISPLAY CRIMINALS ID:'+name.get())
        tkWin.configure(bg="#212121")
        sql="select r.cname,c.*,a.description from crimes a,crimerecords c,criminals r where c.criminalid=r.cid and r.cid=%s and c.crimeid=a.crimeid;"
        mycursor.execute(sql,(int(name.get()),))
        data=mycursor.fetchall()
        f="          NAME     DATE OF CRIME         CRIMEID     CRIMINALID      POLICEID     PLACEOFARREST      DESCRIPTION"
        for i in data:
            list1 =list1 +  str(i[0])+"\t\t"+str(i[1])+"\t\t"+str(i[2]) +"\t\t"+ str(i[3]) +"\t\t"+ str(i[4])+"\t\t"+ str(i[5])+"\t\t"+ str(i[6])
            list1=list1+"\n"
        print(f,"\n" ,list1)
        meLabel=Label(tkWin,text=f,fg="#FD6A02",bg="#2D2D30",font="Consolas 12 bold italic").grid(row=1, column=0)
        nameLabel=Label(tkWin,text=list1,fg="#FD6A02",bg="#212121",font="Consolas 10 bold italic").grid(row=2, column=0)
     def displaybyname():
          list1=" "
          tkWin =Toplevel()  
          tkWin.geometry('700x450')  
          tkWin.title('DISPLAY CRIMINALS NAME:'+ name.get())
          tkWin.configure(bg="#212121")
          sql="select r.cname,c.*,a.description from crimes a,crimerecords c,criminals r where c.criminalid=r.cid and r.cname=%s and c.crimeid=a.crimeid;"
          mycursor.execute(sql,(str(name.get()),))
          data=mycursor.fetchall()

          f="         NAME     DATE OF CRIME         CRIMEID    CRIMINALID    POLICEID   PLACEOFARREST    DESCRIPTION"
          for i in data:
               list1 =list1 +  str(i[0])+"\t\t"+str(i[1])+"\t\t"+str(i[2]) +"\t\t"+ str(i[3]) +"\t\t"+ str(i[4])+"\t\t"+ str(i[5])+"\t\t"+ str(i[6])+"\n"
          print(f,"\n" ,list1)
          meLabel=Label(tkWin,text=f,fg="#FD6A02",bg="#212121",font="Consolas 12 bold italic").grid(row=1, column=0)
          nameLabel=Label(tkWin,text=list1,fg="#FD6A02",bg="#212121",font="Consolas 10 bold italic").grid(row=2, column=0)
     def displaybycrimes():
          list1=" "
          tkWin =Toplevel()  
          tkWin.geometry('750x450')  
          tkWin.title('DISPLAY CRIMINALS CRIME:'+ name.get())
          tkWin.configure(bg="#212121")
          sql="select r.cname,c.*,a.description from crimes a,crimerecords c,criminals r where c.criminalid=r.cid and a.description=%s and c.crimeid=a.crimeid;"
          mycursor.execute(sql,(name.get(),))
          data=mycursor.fetchall()
          f="      NAME     DATE OF CRIME        CRIMEID       CRIMINALID       POLICEID    PLACEOFARREST     DESCRIPTION"
          for i in data:
               list1 =list1 + str(i[0])+"\t\t"+str(i[1])+"\t\t"+str(i[2]) +"\t\t"+ str(i[3]) +"\t\t"+ str(i[4])+"\t\t"+ str(i[5])+"\t\t"+ str(i[6])
               list1=list1+"\n"
               print(i)
               print(f,"\n" ,list1)
        
          meLabel=Label(tkWin,text=f,fg="#FD6A02",bg="#212121",font="Consolas 12 bold italic").grid(row=1, column=0)
          nameLabel=Label(tkWin,text=list1,fg="#FD6A02",bg="#212121",font="Consolas 10 bold italic").grid(row=2, column=0)
     tkWindow =Toplevel()  
     tkWindow.geometry('450x160')  
     tkWindow.title('FIND  CRIMINALS')
     tkWindow.configure(bg="#212121")
     nameLabel=Label(tkWindow,text="ENTER NAME/ID/CRIMES",fg="#FD6A02",bg="#212121",font="Consolas 12 bold italic").grid(row=2, column=0)
     name=StringVar()
     nameEntry=Entry(tkWindow,textvariable=name).grid(row=2, column=1)
     ameLabel=Label(tkWindow,text="",fg="#FD6A02",bg="#212121",font="Consolas 12 bold italic").grid(row=3, column=0)
     displaybutton=Button(tkWindow,text="DISPLAY CRIMINALS BY NAME",fg="#FD6A02",bg="#2D2D30",activebackground="#FD6A02",font="Helvetica 10 bold",command=displaybyname).grid(row=4,column=1)
     ameLabel=Label(tkWindow,text="",fg="#FD6A02",bg="#212121",font="Consolas 12 bold italic").grid(row=5, column=0)
     displaybutton1=Button(tkWindow,text="DISPLAY CRIMINAL BY ID",fg="#FD6A02",bg="#2D2D30",activebackground="#FD6A02",font="Helvetica 10 bold",command=displaybyid).grid(row=6,column=1)
     ameLabel=Label(tkWindow,text="",fg="#FD6A02",bg="#212121",font="Consolas 12 bold italic").grid(row=7, column=0)
     displaybutton2=Button(tkWindow,text="DISPLAY BY CRIME",fg="#FD6A02",bg="#2D2D30",activebackground="#FD6A02",font="Helvetica 10 bold",command=displaybycrimes).grid(row=8,column=1) 
def addcrimes():
    def addcrimes1():
        sql="insert into crimes(crimeid,description) values(%s,%s)"
        val=(int(date.get()),cid.get())
        mycursor.execute(sql,val)
        mydb.commit()
        passwordLabel = Label(tkWindow,text="Record inserted:"+ date.get(),fg="#ECF0F1",bg="#212121",font="Consolas 10 bold italic").grid(row=8, column=2)  
        
    tkWindow =Toplevel()  
    tkWindow.geometry('400x350')  
    tkWindow.title('ADD CRIMES')
    tkWindow.configure(bg="#212121")
    usernameLabel = Label(tkWindow, text="\T CRIME ID\t\t",fg="#FD6A02",bg="#212121",font="Consolas 10 bold italic").grid(row=0, column=0)
    date = StringVar()
    usernameEntry = Entry(tkWindow, textvariable=date).grid(row=0, column=1)  

    #password label and password entry box
    passwordLabel = Label(tkWindow,text="\tDESCRIPTION\t\t",fg="#FD6A02",bg="#212121",font="Consolas 10 bold italic").grid(row=2, column=0)  
    cid= StringVar()
    passwordEntry = Entry(tkWindow, textvariable=cid, show='').grid(row=2, column=1)
    signupButton = Button(tkWindow, text="ADD RECORD",fg="#FD6A02",bg="#2D2D30",activebackground="#FD6A02",font="Helvetica 14 bold",command=addcrimes1).grid(row=5,column=0)

def displaycrimes():
    list1='"\t'
    crimewindow =Toplevel()  
    crimewindow.geometry('600x160')  
    crimewindow.title('Display Crimes')
    crimewindow.configure(bg="#212121")
    sql="select* from crimes"
    mycursor.execute(sql)
    data=mycursor.fetchall()
    f="      CRIME ID   DESCRIPTION"
    for i in data:
        list1 =list1 +"\t"+ str(i[0])+"\t\t"+str(i[1])
        list1=list1+"  \n "
    
    ameLabel=Label(crimewindow,text=list1,fg="#FD6A02",bg="#212121",font="Consolas 10 bold italic").grid(row=2, column=0)
    meLabel=Label(crimewindow,text=f,fg="#FD6A02",bg="#212121",font="Consolas 12 bold italic").grid(row=0, column=0)
       
def findcrimerecords():
    def displaybyname1():
        list1=" "
        tkWin =Toplevel()  
        tkWin.geometry('600x450')  
        tkWin.title('CRIMERECORDS PLACE: '+name.get())
        tkWin.configure(bg="#212121")
        sql="select c.*,r.description from crimerecords c,crimes r where c.crimeid=r.crimeid and placeofarrest=%s"
        mycursor.execute(sql,(name.get(),))
        data=mycursor.fetchall()
        f="DATE OF CRIME         CRIMEID    CRIMINALID    POLICEID   PLACEOFARREST    DESCRIPTION"
        for i in data:
            list1 =list1 +  str(i[0])+"\t\t"+str(i[1])+"\t\t"+str(i[2]) +"\t\t"+ str(i[3]) +"\t\t"+ str(i[4])+"\t\t"+ str(i[5])
            list1=list1+"\n"
        meLabel=Label(tkWin,text=f,fg="#FD6A02",bg="#212121",font="Consolas 12 bold italic").grid(row=1, column=0)
        nameLabel=Label(tkWin,text=list1,fg="#FD6A02",bg="#212121",font="Consolas 10 bold italic").grid(row=2, column=0)
    def displaybycrime():
        list1=" "
        tkWin =Toplevel()  
        tkWin.geometry('700x450')  
        tkWin.title('CRIMERECORDS CRIME:'+name.get())
        tkWin.configure(bg="#212121")
        sql="select c.*,r.description from crimerecords c,crimes r where c.crimeid=r.crimeid and description=%s"
        mycursor.execute(sql,(str(name.get()),))
        data=mycursor.fetchall()
       
        f="DATE OF CRIME         CRIMEID    CRIMINALID    POLICEID   PLACEOFARREST    DESCRIPTION"
        for i in data:
            list1 =list1 +  str(i[0])+"\t\t"+str(i[1])+"\t\t"+str(i[2]) +"\t\t"+ str(i[3]) +"\t\t"+ str(i[4])+"\t\t"+ str(i[5])
            list1=list1+"\n"
        meLabel=Label(tkWin,text=f,fg="#FD6A02",bg="#212121",font="Consolas 12 bold italic").grid(row=1, column=0)
        nameLabel=Label(tkWin,text=list1,fg="#FD6A02",bg="#212121",font="Consolas 10 bold italic").grid(row=2, column=0)
    def displaybymonth():
        list1=" "
        tkWin =Toplevel()  
        tkWin.geometry('750x450')  
        tkWin.title('CRIMERECORDS MONTH:'+name.get())
        tkWin.configure(bg="#212121")
        sql="select c.*,r.description from crimerecords c,crimes r where c.crimeid=r.crimeid and monthname(dateofcrime) like %s"
        mycursor.execute(sql,(name.get(),))
        data=mycursor.fetchall()
        f="DATE OF CRIME         CRIMEID    CRIMINALID    POLICEID   PLACEOFARREST    DESCRIPTION"
        for i in data:
            list1 =list1 +  str(i[0])+"\t\t"+str(i[1])+"\t\t"+str(i[2]) +"\t\t"+ str(i[3]) +"\t\t"+ str(i[4])+"\t\t"+ str(i[5])
            list1=list1+"\n"
        
        meLabel=Label(tkWin,text=f,fg="#FD6A02",bg="#212121",font="Consolas 12 bold italic").grid(row=1, column=0)
        nameLabel=Label(tkWin,text=list1,fg="#FD6A02",bg="#212121",font="Consolas 10 bold italic").grid(row=2, column=0)
    tkWindow =Toplevel()  
    tkWindow.geometry('450x160')  
    tkWindow.title('DISPLAYCRIMERECORDS')
    tkWindow.configure(bg="#212121")
    nameLabel=Label(tkWindow,text="ENTER PLACE/MONTH/CRIME",fg="#FD6A02",bg="#212121",font="Consolas 12 bold italic").grid(row=2, column=0)
    name=StringVar()
    nameEntry=Entry(tkWindow,textvariable=name).grid(row=2, column=1)
    ameLabel=Label(tkWindow,text="",fg="#FD6A02",bg="#212121",font="Consolas 12 bold italic").grid(row=3, column=0)
    displaybutton=Button(tkWindow,text="DISPLAY CRIMES OF A PLACE",fg="#FD6A02",bg="#2D2D30",activebackground="#FD6A02",font="Helvetica 10 bold",command=displaybyname1).grid(row=4,column=1)
    ameLabel=Label(tkWindow,text="",fg="#FD6A02",bg="#212121",font="Consolas 12 bold italic").grid(row=5, column=0)
    displaybutton1=Button(tkWindow,text="DISPLAY CRIMES OF A MONTH(ENTER MONTH)",fg="#FD6A02",bg="#2D2D30",activebackground="#FD6A02",font="Helvetica 10 bold",command=displaybymonth).grid(row=6,column=1)
    ameLabel=Label(tkWindow,text="",fg="#FD6A02",bg="#212121",font="Consolas 12 bold italic").grid(row=7, column=0)
    displaybutton2=Button(tkWindow,text="DISPLAY PARTICULAR CRIMES",fg="#FD6A02",bg="#2D2D30",activebackground="#FD6A02",font="Helvetica 10 bold",command=displaybycrime).grid(row=8,column=1)


    

def addcriminals():
    def insert(name,cid,age):
        sql="insert into criminals(cname,cid,age ) values(%s,%s,%s)"
        val=(name.get(),int(cid.get()),int(age.get()))
        mycursor.execute(sql,val)
        mydb.commit()
        passwordLabel = Label(crimewindow,text="Record inserted:"+ name.get(),fg="#ECF0F1",bg="#212121",font="Consolas 10 bold italic").grid(row=5, column=1)  
        
    crimewindow =Toplevel()  
    crimewindow.geometry('450x160')  
    crimewindow.title('Add Criminal Record')
    crimewindow.configure(bg="#212121")

        #username label and text entry box
    usernameLabel = Label(crimewindow, text="\tName of Criminal\t\t",fg="#FD6A02",bg="#212121",font="Consolas 10 bold italic").grid(row=0, column=0)
    name = StringVar()
    usernameEntry = Entry(crimewindow, textvariable=name).grid(row=0, column=1)  

    #password label and password entry box
    passwordLabel = Label(crimewindow,text="\tCriminal ID\t\t",fg="#FD6A02",bg="#212121",font="Consolas 10 bold italic").grid(row=1, column=0)  
    cid= StringVar()
    passwordEntry = Entry(crimewindow, textvariable=cid, show='').grid(row=1, column=1)
    Jerseylabel = Label(crimewindow, text="\tAge\t\t",fg="#FD6A02",bg="#212121",font="Consolas 10 bold italic").grid(row=4, column=0)
    age = StringVar()
    JerseyEntry = Entry(crimewindow, textvariable=age).grid(row=4, column=1)
    
    signupButton = Button(crimewindow, text="ADD RECORD",fg="#FD6A02",bg="#2D2D30",activebackground="#FD6A02",font="Helvetica 12 bold",command=lambda:insert(name,cid,age)).grid(row=5,column=0)
def displayallcrimes():
    list1='\t'
    crimewindow =Toplevel()  
    crimewindow.geometry('600x160')  
    crimewindow.title('Display Crimes')
    crimewindow.configure(bg="#212121")
    sql="select* from crimerecords"
    mycursor.execute(sql)
    data=mycursor.fetchall()
    f="DATE OF CRIME       CRIME ID      CRIMINAL ID     POLICEID     PLACE"
    for i in data:
        list1 =list1 + str(i[0])+"\t\t"+str(i[1])+"\t\t"+str(i[2]) +"\t\t"+ str(i[3]) +"\t\t"+ str(i[4])
        list1=list1+"\n"
    
    ameLabel=Label(crimewindow,text=list1,fg="#FD6A02",bg="#212121",font="Consolas 10 bold italic").grid(row=2, column=0)
    meLabel=Label(crimewindow,text=f,fg="#FD6A02",bg="#212121",font="Consolas 10 bold italic").grid(row=0, column=0)
    
    
def displayallpolice():
    def displayall():
        list1=' '
        sql="select* from police"
        mycursor.execute(sql)
        data=mycursor.fetchall()
        f="                NAME                   ID            PRECINCT              AGE                  DEPT                 SALARY"
        for i in data:
            list1 =list1 + "\t\t"+ str(i[0])+"\t\t"+str(i[1])+"\t\t"+str(i[2]) +"\t\t"+ str(i[3]) +"\t\t"+ str(i[4])+"\t\t"+ str(i[5])
            list1=list1+"\n"
        print(f,"\n",list1)
        tkWin =Toplevel()  
        tkWin.geometry('700x450')  
        tkWin.title('DISPLAY POLICE')
        tkWin.configure(bg="#212121")
        meLabel=Label(tkWin,text=f,fg="#FD6A02",bg="#212121",font="Consolas 10 bold italic").grid(row=1, column=0)
        nameLabel=Label(tkWin,text=list1,fg="#FD6A02",bg="#212121",font="Consolas 10 bold italic").grid(row=2, column=0)
         
    def displaybyname():
        list1=" "
        tkWin =Toplevel()  
        tkWin.geometry('700x450')  
        tkWin.title('DISPLAY POLICE')
        tkWin.configure(bg="#212121")
        sql="select* from police where pname=%s"
        mycursor.execute(sql,(name.get(),))
        data=mycursor.fetchall()
        f="                NAME                   ID            PRECINCT              AGE                  DEPT                 SALARY"
        for i in data:
            list1 =list1 +"\t\t"+ str(i[0])+"\t\t"+str(i[1])+"\t\t"+str(i[2]) +"\t\t"+ str(i[3]) +"\t\t"+ str(i[4])+"\t\t"+ str(i[5])
            list1=list1+"\n"
        print(f,"\n",list1)
        meLabel=Label(tkWin,text=f,fg="#FD6A02",bg="#212121",font="Consolas 10 bold italic").grid(row=1, column=0)
        nameLabel=Label(tkWin,text=list1,fg="#FD6A02",bg="#212121",font="Consolas 10 bold italic").grid(row=2, column=0)

    def displaybyid():
        list1=" "
        tkWin =Toplevel()  
        tkWin.geometry('700x450')  
        tkWin.title('DISPLAY POLICE')
        tkWin.configure(bg="#212121")
        sql="select* from police where pid=%s"
        mycursor.execute(sql,(int(name.get()),))
        data=mycursor.fetchall()
        f="                NAME                   ID            PRECINCT              AGE                  DEPT                 SALARY"
        for i in data:
            list1 =list1 +  str(i[0])+"\t\t"+str(i[1])+"\t\t"+str(i[2]) +"\t\t"+ str(i[3]) +"\t\t"+ str(i[4])+"\t\t"+ str(i[5])
            list1=list1+"\n"
        print(f,"\n",list1)
        meLabel=Label(tkWin,text=f,fg="#FD6A02",bg="#212121",font="Consolas 10 bold italic").grid(row=1, column=0)
        nameLabel=Label(tkWin,text=list1,fg="#FD6A02",bg="#212121",font="Consolas 10 bold italic").grid(row=2, column=0)
        
        
        
    tkWindow =Toplevel()  
    tkWindow.geometry('450x160')  
    tkWindow.title('DISPLAY POLICE RECORDS')
    tkWindow.configure(bg="#212121")
    nameLabel=Label(tkWindow,text="ENTER NAME/ID OF POLICE",fg="#FD6A02",bg="#212121",font="Consolas 10 bold italic").grid(row=2, column=0)
    name=StringVar()
    nameEntry=Entry(tkWindow,textvariable=name).grid(row=2, column=1)
    displaybutton=Button(tkWindow,text="DISPLAY BY NAME",fg="#FD6A02",bg="#2D2D30",activebackground="#FD6A02",font="Helvetica 10 bold",command=displaybyname).grid(row=4,column=0)
    displaybutton1=Button(tkWindow,text="DISPLAY BY ID",fg="#FD6A02",bg="#2D2D30",activebackground="#FD6A02",font="Helvetica 10 bold",command=displaybyid).grid(row=4,column=1)
    displaybutton2=Button(tkWindow,text="DISPLAY ALL POLICE RECORDS",fg="#FD6A02",bg="#2D2D30",activebackground="#FD6A02",font="Helvetica 12 bold",command=displayall).grid(row=6,column=1)
    
def addcrimerecord():
    def insert(date,cid,crid,policeid,place):
        sql="insert into crimerecords(dateofcrime,crimeid,criminalid,policeid,placeofarrest) values(%s,%s,%s,%s,%s)"
        val=(date.get(),int(crid.get()),int(cid.get()),int(policeid.get()),place.get())
        mycursor.execute(sql,val)
        mydb.commit()
        passwordLabel = Label(tkWindow,text="Record inserted:",fg="#ECF0F1",bg="#212121",font="Consolas 10 bold italic").grid(row=8, column=2)  
        
    tkWindow =Toplevel()  
    tkWindow.geometry('450x160')  
    tkWindow.title('Add Record')
    tkWindow.configure(bg="#212121")

        #username label and text entry box
    usernameLabel = Label(tkWindow, text="\tDate of crime\t\t",fg="#FD6A02",bg="#212121",font="Consolas 10 bold italic").grid(row=0, column=2)
    date = StringVar()
    usernameEntry = Entry(tkWindow, textvariable=date).grid(row=0, column=5)  

    #password label and password entry box
    passwordLabel = Label(tkWindow,text="\tCriminal ID\t\t",fg="#FD6A02",bg="#212121",font="Consolas 10 bold italic").grid(row=2, column=2)  
    cid= StringVar()
    passwordEntry = Entry(tkWindow, textvariable=cid, show='').grid(row=2, column=5)
    crimelabel = Label(tkWindow, text="     CrimeID\t\t",fg="#FD6A02",bg="#212121",font="Consolas 10 bold italic").grid(row=3, column=2)
    crid = StringVar()
    crimeyEntry = Entry(tkWindow, textvariable=crid).grid(row=3, column=5)
    Policelabel = Label(tkWindow, text="\tPOLICE ID\t\t",fg="#FD6A02",bg="#212121",font="Consolas 10 bold italic").grid(row=4, column=2)
    policeid= StringVar()
    policeidEntry = Entry(tkWindow, textvariable=policeid).grid(row=4, column=5)
    placelabel = Label(tkWindow, text="\tPLACE OF CRIME\t\t",fg="#FD6A02",bg="#212121",font="Consolas 10 bold italic").grid(row=5, column=2)
    place= StringVar()
    poidEntry = Entry(tkWindow, textvariable=place).grid(row=5, column=5)
    
             
            
    signupButton = Button(tkWindow, text="ADD RECORD",fg="#FD6A02",bg="#2D2D30",font="Consolas 14 bold ",command=lambda:insert(date,cid,crid,policeid,place)).grid(row=6, column=4)
def addpolicerecord():
    def clicked(pname,pid,precinct,yearsexp,dept,salary):
        sql="insert into police(pname,pid,precinct,age,dept,salary) values(%s, %s,%s, %s,%s,%s)"
        val=(pname.get(),int(pid.get()),precinct.get(),int(yearsexp.get()),dept.get(),int(salary.get()))
        mycursor.execute(sql,val)
        passwordLabel = Label(tkWindow,text="Record inserted:"+ pname.get(),fg="#ECF0F1",bg="#212121",font="Consolas 10 bold italic").grid(row=8, column=2)  
        
        mydb.commit()
    tkWindow =Toplevel()  
    tkWindow.geometry('450x160')  
    tkWindow.title('Add Police Record')
    tkWindow.configure(bg="#212121")
#    mycursor.execute("SELECT* FROM POLICE")
#    data=mycursor.fetchall()
#    for i in data:
#        print(i)
        #username label and text entry box
    usernameLabel = Label(tkWindow, text="\tNAME\t\t",fg="#FD6A02",bg="#212121",font="Consolas 10 bold italic").grid(row=0, column=2)
    pname = StringVar()
    usernameEntry = Entry(tkWindow, textvariable=pname).grid(row=0, column=5)  

    #password label and password entry box
    passwordLabel = Label(tkWindow,text="\tPolice ID\t\t",fg="#FD6A02",bg="#212121",font="Consolas 10 bold italic").grid(row=1, column=2)  
    pid= StringVar()
    passwordEntry = Entry(tkWindow, textvariable=pid).grid(row=1, column=5)
    Jerseylabel = Label(tkWindow, text="\tPrecinct\t\t",fg="#FD6A02",bg="#212121",font="Consolas 10 bold italic").grid(row=4, column=2)
    precinct = StringVar()
    JerseyEntry = Entry(tkWindow, textvariable=precinct).grid(row=4, column=5)
    Teamlabel=Label(tkWindow, text="\tYears in Field\t\t",fg="#FD6A02",bg="#212121",font="Consolas 10 bold italic").grid(row=5, column=2)
    yearsexp=StringVar()
    TeamEntry=Entry(tkWindow,textvariable=yearsexp).grid(row=5, column=5)
    Deptlabel=Label(tkWindow, text="\tDepartment\t\t",fg="#FD6A02",bg="#212121",font="Consolas 10 bold italic").grid(row=6, column=2)
    dept=StringVar()
    deptEntry=Entry(tkWindow,textvariable=dept).grid(row=6, column=5)
    SALARYlabel = Label(tkWindow, text="\tSALARY \t\t",fg="#FD6A02",bg="#212121",font="Consolas 10 bold italic").grid(row=7, column=2)
    salary = StringVar()
    SALARYEntry = Entry(tkWindow, textvariable=salary).grid(row=7, column=5)

    #login button
    signupButton = Button(tkWindow, text="ADD RECORD",fg="#FD6A02",bg="#2D2D30",font="Consolas 14 bold ",command=lambda:clicked(pname,pid,precinct,yearsexp,dept,salary)).grid(row=10, column=4)
    tkWindow.mainloop()   
mydb = mycon.connect(
  host="localhost",
  user="root",
  password="J0zef#21"
)
#mycursor.execute("create table police(pname varchar(255),pid int(5) primary key,precinct varchar(255) ,age int(2),dept varchar(255),salary int(8))"
#mycursor.execute("create table criminals(cname varchar(255) ,cid int(5) primary key,age int(2)")
#mycursor.execute("create table crimerecords(dateofcrime date,crimeid int(4) criminalid int(5) ,policeid int(5),placeofarrest varchar(25)")
#mycursor.execute("create table crimes(crimeid int(5) primary key,description varchar(255)")
mycursor=mydb.cursor()
mycursor.execute("USE CRIMINALRECORDS")
menu=Tk()
menu.configure(bg='#212121')
menu.title("MAIN MENU")
menu.geometry("600x500")
label=Label(menu,text="  MAIN MENU",fg="#FD6A02",bg="#212121",activebackground="#FD6A02",font="Ariel 16 bold underline").grid(row=0,column=0)
displaybutton=Button(menu,text="   ADD NEW POLICE RECORD ",fg="#FD6A02",bg="#2D2D30",activebackground="#FD6A02",font="Helvetica 13 bold",command=addpolicerecord).grid(row=2,column=0)
displaybutton1=Button(menu,text="    ADD NEW CRIME RECORD  ",fg="#FD6A02",bg="#2D2D30",activebackground="#FD6A02",font="Helvetica 13 bold",command=addcrimerecord).grid(row=2,column=1)
displaybutton2=Button(menu,text="DISPLAY ALL POLICE RECORDS  ",fg="#FD6A02",bg="#2D2D30",activebackground="#FD6A02",font="Helvetica 13 bold",command=displayallpolice).grid(row=3,column=0)
displaybutton3=Button(menu,text="DISPLAY ALL CRIMERECORDS   ",fg="#FD6A02",bg="#2D2D30",activebackground="#FD6A02",font="Helvetica 13 bold",command=displayallcrimes).grid(row=3,column=1)
displaybutton4=Button(menu,text="ADD NEW CRIMINAL RECORD   ",fg="#FD6A02",bg="#2D2D30",activebackground="#FD6A02",font="Helvetica 13 bold",command=addcriminals).grid(row=4,column=0)
displaybutton5=Button(menu,text="       FIND CRIMERECORDS     ",fg="#FD6A02",bg="#2D2D30",activebackground="#FD6A02",font="Helvetica 13 bold",command=findcrimerecords).grid(row=4,column=1)
displaybutton6=Button(menu,text="        ADD CRIMES            ",fg="#FD6A02",bg="#2D2D30",activebackground="#FD6A02",font="Helvetica 13 bold",command=addcrimes).grid(row=5,column=0)
displaybutton7 =Button(menu,text="      DISPLAY ALL CRIMES    ",fg="#FD6A02",bg="#2D2D30",activebackground="#FD6A02",font="Helvetica 13 bold",command=displaycrimes).grid(row=5,column=1)
displaybutton8 =Button(menu,text="       FIND CRIMINALS         ",fg="#FD6A02",bg="#2D2D30",activebackground="#FD6A02",font="Helvetica 13 bold",command=findcriminals).grid(row=6,column=1)
displaybutton8 =Button(menu,text="DISPLAY CRIMERATE(graph)   ",fg="#FD6A02",bg="#2D2D30",activebackground="#FD6A02",font="Helvetica 13 bold",command=crimerate).grid(row=6,column=0)
displaybutton9=Button(menu,text="         UPDATE SALARY       ",fg="#FD6A02",bg="#2D2D30",activebackground="#FD6A02",font="Helvetica 13 bold",command=updatepolice).grid(row=7,column=0)
displaybutton10=Button(menu,text="DISPLAY CRIMES PER PLACE(graph)",fg="#FD6A02",bg="#2D2D30",activebackground="#FD6A02",font="Helvetica 13 bold",command=no_crimeinplace).grid(row=7,column=1)
mainloop()
