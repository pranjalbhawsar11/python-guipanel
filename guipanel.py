from tkinter import *
import os
import csv
from tkinter import filedialog
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders

c,count=0,0
creds="C:/Users/pc/Desktop/Azure Skynet/mycsv.csv"
def logout():
     rs.destroy()
     r=Tk()
     r.title(':D')
     r.iconbitmap()
     r.geometry('150x100')
     rlab=Label(r,text='\n[+]LOGGED OUT')
     rlab.pack()
     r.mainloop()
     login()
     

def mail():
    def attach():
        global count
        count+=1
        root.filename=filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*"))) 
        file=Label(root,text=root.filename)
        file.grid(row=7,column=0,sticky=W)
    def Pass():
         pass
    def sendmail():
        global count
        global c
        msg=MIMEMultipart()
        msg['From']='pbhawsar724@gmail.com'
        msg['To']=Toe.get()
        msg['Subject']=Subjecte.get()
        body=texte.get("1.0","end-1c")
        msg.attach(MIMEText(body,'plain'))

        if count>0:
            filename= root.filename
            attachment=open(filename,'rb')
            part=MIMEBase('application','octet-stream')
            part.set_payload((attachment).read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition',"attachment;filename="+filename)
            msg.attach(part)
        else:
                pass

        text=msg.as_string()
        mail=smtplib.SMTP('smtp.gmail.com',587)
        mail.starttls()
        mail.login('pbhawsar724@gmail.com','*********')
        try:
            mail.sendmail('pbhawsar724@gmail.com',msg['To'],text)
            c+=1
            print("email sent")
        except:
            print("error occured")
        mail.quit()
        root.destroy()
        if c>=1:
                 r=Tk()
                 r.title(':D')
                 r.iconbitmap()
                 r.geometry('150x100')
                 rlab=Label(r,text='\n[+]EMAIL SENT')
                 rlab.pack()
                 r.mainloop()
        else:
                 r=Tk()
                 r.title(':D')
                 r.iconbitmap()
                 r.geometry('150x100')
                 rlab=Lbel(r,text='\n[!]ERROR EMAIL SENDING')
                 rlab.pack()
                 r.mainloop()
                 
    root=Tk()
    root.title('new message')
    root.iconbitmap()
    To=Label(root,text='To:\n')
    To.grid(row=1,column=1,sticky=W)
    Subject=Label(root,text='Subject :')
    Subject.grid(row=2,column=1,sticky=W)
    text=Label(root,text='Message : ')
    text.grid(row=3,column=1,sticky=W)

    Toe=Entry(root,width=70)
    Subjecte=Entry(root,width=70)
    texte=Text(root,width=70,height=10)

    Toe.grid(row=1,column=2,sticky=W)
    Subjecte.grid(row=2,column=2,sticky=W)
    texte.grid(row=3,column=2,sticky=W)

    attach=Button(root,text="Attach files",relief=GROOVE,command=attach)
    attach.grid(row=6,column=0,sticky=W)
    send=Button(root,text="Send",relief=GROOVE,command=sendmail)
    send.grid(row=6,column=1,sticky=W)

    root.geometry("500x200")
    root.mainloop()

def send():
    global rs
    rs=Tk()
    rs.title('send message')
    rs.iconbitmap()
    rs.geometry('200x100')
    new =Button(rs,text='compose',relief=GROOVE,command=mail)
    new.grid(row=1,column=0,sticky=W)
    new =Button(rs,text='logout',relief=GROOVE,command=logout)
    new.grid(row=1,column=2,sticky=W)
    rs.mainloop()

def checklogin():
    with open(creds) as f:
        data=csv.reader(f)
        for line in data:
            try:
                uname=line[0]
                pword=line[1]

                if nameE.get()==uname and pwordE.get()==pword:
                    root.destroy()
                    rm=Tk()
                    rm.title(':D')
                    rm.iconbitmap()
                    rm.geometry('150x100')
                    rlab=Label(rm,text='\n[+] LOGGED IN')
                    rlab.pack()
                    rm.mainloop()
                    send()
                else:
                    rm=Tk()
                    rm.title(':D')
                    rm.iconbitmap()
                    rm.geometry('150x100')
                    rlab=Label(rm,text='\n[!]INVALID LOGIN')
                    rlab.pack()
                    rm.mainloop()
                    login()
            except IndexError:
               pass
def FSSignup():
    with open(creds,'w') as fm:
        fm.write(name.get())
        fm.write(',')
        fm.write(pword.get())
        fm.write('\n')
        fm.close()
    roots.destroy()
    login()


def signup():
    global pword
    global name
    global roots
    root.destroy()
    roots=Tk()
    roots.title('sign up')
    roots.iconbitmap()
    
     
    instruction=Label(roots,text='please enter creadentials\n')
    instruction.grid(row=0,column=0,sticky=E)
    pwordl=Label(roots,text='New password:')
    namel=Label(roots,text='New username: ')
    pwordl.grid(row=2,column=0,sticky=W)
    namel.grid(row=1,column=0,sticky=W)

    name=Entry(roots)
    pword=Entry(roots,show='*')

    name.grid(row=1,column=1,sticky=W)
    pword.grid(row=2,column=1,sticky=W)

    signupbutton=Button(roots,text="Sign Up",relief=GROOVE,command=FSSignup)
    signupbutton.grid(row=6,column=0,sticky=W)
    roots.mainloop()

def DelUser():
    os.remove(creds)
    root.destroy()
    signup()
    if os.path.isfile(creds):
        login()
    else:
        signup()

    

def login():
    global root
    global nameE
    global pwordE
    #creating a window manager
    root=Tk()
    root.title('login')
    root.iconbitmap()
    lab=Label(root,text='please login\n')
    lab.grid(sticky=E)
    nameL=Label(root,text='Userename: ')
    pwordL=Label(root,text='Password: ')
    nameL.grid(row=1,sticky=W)
    pwordL.grid(row=2,sticky=W)

    #creating entry
    nameE=Entry(root)
    pwordE=Entry(root,show='*')
    nameE.grid(row=1,column=1)
    pwordE.grid(row=2,column=1)

    #creating button to login,sign up and delete user

    loginB=Button(root,text='Login',relief=GROOVE,command=checklogin)
    loginB.grid(columnspan=2,sticky=W)
    loginB=Button(root,text='Sign up',relief=GROOVE,command=signup)
    loginB.grid(columnspan=2,sticky=W)
    deluser=Button(root,text='Delete User',fg='red',relief=GROOVE,command=DelUser)
    deluser.grid(column=2,sticky=W)
    root.mainloop()


login()    


 

    
    
            
                
            



