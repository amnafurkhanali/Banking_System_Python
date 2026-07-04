from tkinter import *
from tkinter import messagebox
from datetime import date
import random
import mysql.connector as mys
###############################################
mycon = mys.connect(host='localhost', user='root', passwd='password', database='Banking_System')


######################################
def login():
  username = usernm.get()
  password = passwd.get()
  lc, uc, sp, nm = 0, 0, 0, 0
  uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  lowercase = "abcdefghijklmnopqrstuvwxyz"
  special = "!@#$%^&~*_"
  number = "0123456789"
  if (len(password) >= 8):
    for i in password:
      # counting lowercase alphabets
      if (i in lowercase):
        lc += 1
      # counting uppercase alphabets
      if (i in uppercase):
        uc += 1
      # counting digits
      if (i in number):
        nm += 1
      # counting the mentioned special characters
      if (i in special):
        sp += 1
  #Checking Validity of Username and Password
  if len(username) >= 8 and (lc >= 1 and uc >= 1 and sp >= 1 and
                             nm >= 1) and (lc + sp + uc + nm == len(password)):
    Main_Window()
  elif len(username) < 8 and (lc < 1 and uc < 1 and sp < 1 and
                              nm < 1) and lc + sp + uc + nm != len(password):
    messagebox.showerror("Login Unsucessful", "Invalid Username and Password")
  elif len(username) < 8:
    messagebox.showerror("Login Unsucessful", "Invalid Username")
  elif (lc < 1 and uc < 1 and sp < 1
        and nm < 1) and lc + sp + uc + nm != len(password):
    messagebox.showerror("Login Unsucessful", "Invalid Password")


############################################################################
def Main_Window():
  root.destroy()
  #creating the window
  home = Tk()
  home.title('Customer Home Page')
  home.state('zoomed')
  home.configure(bg='#98BF64')
  #adding the image
  global img
  img = PhotoImage(file='home.png')
  Label(home, image=img, bg='#98BF64').place(x=100, y=100)
  #creating frame beside image
  frame = Frame(home, width=500, height=600, bg='#98BF64')
  frame.place(x=700, y=70)
  #adding the title
  heading = Label(frame,
                  text='Customer Home Page',
                  fg='#234F1E',
                  bg='#98BF64',
                  font=('Microsoft YaHei UI Light', 23, 'bold'))
  heading.place(x=90, y=1)
  choose = Label(frame,
                 text='Please choose the service you want to access',
                 fg='#234F1E',
                 bg='#98BF64',
                 font=('Microsoft YaHei UI Light', 10, 'bold'))
  choose.place(x=90, y=70)

  #############################################################################
  def DEA():
    home.destroy()

    def delete():
      mobile_no = mobile.get()
      account_no = account.get()
      mycursor = mycon.cursor()
      query = 'select * from Account_Details where Account_Number ={} and Mobile_Number={}'.format(
          account_no, mobile_no)
      mycursor.execute(query)
      data = mycursor.fetchone()
      if data != None:
        query1 = 'delete from Account_Details where Account_Number ={} and Mobile_Number={}'.format(
            account_no, mobile_no)
        mycursor.execute(query1)
        mycon.commit()
        del_account.destroy()
        message = 'Your Account ' + str(
            account_no) + ' was Successfully Deleted.'
        messagebox.showinfo("Account Successfully Deleted", message)
      else:
        messagebox.showerror("Error", "Account Doesn't Exsist")

    del_account = Tk()
    del_account.title('Delete Account')
    del_account.state('zoomed')
    del_account.configure(bg='#98BF64')
    mainframe = Frame(del_account, height=600, width=900, background='#98BF64')
    mainframe.place(relx=0.5, rely=0.5, anchor=CENTER)
    #adding the image
    imgs = PhotoImage(file='delete.png')
    Label(mainframe, image=imgs, bg='#98BF64').place(relx=0.5,
                                                     rely=0.5,
                                                     anchor=E)
    #creating textbox beside image
    frame = Frame(mainframe, width=350, height=450, bg='#98BF64')
    frame.place(x=550, y=100)
    #adding the title
    heading = Label(frame,
                    text='Delete Account',
                    fg='#234F1E',
                    bg='#98BF64',
                    font=('Microsoft YaHei UI Light', 23, 'bold'))
    heading.place(x=50, y=0)

    #customer name
    def on_enter(e):
      custnm.delete(0, 'end')

    def on_leave(e):
      name = custnm.get()
      if name == ' ':
        custnm.insert(0, 'Customer Name')

    custnm = Entry(frame,
                   width=25,
                   fg='#234F1E',
                   border=0,
                   bg='#98BF64',
                   font=('Microsoft YaHei UI Light', 11))
    custnm.place(x=30, y=80)
    custnm.insert(0, 'Customer Name')
    custnm.bind('<FocusIn>', on_enter)
    custnm.bind('<FocusOut>', on_leave)
    Frame(frame, width=295, height=2, bg='#234F1E').place(x=25, y=107)

    #mobile number
    def on_enter(e):
      mobile.delete(0, 'end')

    def on_leave(e):
      mobile = custnm.get()
      if mobile == ' ':
        mobile.insert(0, 'Mobile Number')

    mobile = Entry(frame,
                   width=25,
                   fg='#234F1E',
                   border=0,
                   bg='#98BF64',
                   font=('Microsoft YaHei UI Light', 11))
    mobile.place(x=30, y=150)
    mobile.insert(0, 'Mobile Number')
    mobile.bind('<FocusIn>', on_enter)
    mobile.bind('<FocusOut>', on_leave)
    Frame(frame, width=295, height=2, bg='#234F1E').place(x=25, y=177)

    #account_no
    def on_enter(e):
      account.delete(0, 'end')

    def on_leave(e):
      account = custnm.get()
      if account == ' ':
        account.insert(0, 'Account Number')

    account = Entry(frame,
                    width=25,
                    fg='#234F1E',
                    border=0,
                    bg='#98BF64',
                    font=('Microsoft YaHei UI Light', 11))
    account.place(x=30, y=220)
    account.insert(0, 'Account Number')
    account.bind('<FocusIn>', on_enter)
    account.bind('<FocusOut>', on_leave)
    Frame(frame, width=295, height=2, bg='#234F1E').place(x=25, y=247)

    #address
    def on_enter(e):
      email.delete(0, 'end')

    def on_leave(e):
      email = custnm.get()
      if email == ' ':
        email.insert(0, 'Email Address')

    email = Entry(frame,
                  width=25,
                  fg='#234F1E',
                  border=0,
                  bg='#98BF64',
                  font=('Microsoft YaHei UI Light', 11))
    email.place(x=30, y=290)
    email.insert(0, 'Email Address')
    email.bind('<FocusIn>', on_enter)
    email.bind('<FocusOut>', on_leave)
    Frame(frame, width=295, height=2, bg='#234F1E').place(x=25, y=317)
    Button(frame,
           width=39,
           pady=7,
           text='Delete',
           bg="#234F1E",
           fg='#98BF64',
           border=0,
           command=delete).place(x=35, y=370)
    del_account.mainloop()

  ########################################################################################
  def VCB():
    home.destroy()

    def ex_vcb():
      mobile_no = mobile.get()
      account_no = account.get()
      mycursor = mycon.cursor()
      query = 'select Current_Balance from Account_Details where Account_Number = {} and Mobile_Number ={}'.format(
          account_no, mobile_no)
      mycursor.execute(query)
      data = mycursor.fetchone()
      if data != None:
        vcb.destroy()
        message = 'Your Current Balance is ' + str(data) + " AED."
        messagebox.showinfo("View Current Balance", message)
      else:
        messagebox.showerror("Error", "Account Doesn't Exsist")

    vcb = Tk()
    vcb.title('View Current Balance')
    vcb.state('zoomed')
    vcb.configure(bg='#98BF64')
    mainframe = Frame(vcb, height=480, width=2000, background='#98BF64')
    mainframe.place(relx=0.5, rely=0.5, anchor=CENTER)
    #adding the image
    imgs = PhotoImage(file='current balance.png')
    Label(mainframe, image=imgs, bg='#98BF64').place(x=400, y=0)
    #creating textbox beside image
    frame = Frame(mainframe, width=500, height=500, bg='#98BF64')
    frame.place(x=1100, y=70)
    #adding the title
    heading = Label(frame,
                    text='View Current Balance',
                    fg='#234F1E',
                    bg='#98BF64',
                    font=('Microsoft YaHei UI Light', 23, 'bold'))
    heading.place(x=15, y=0)

    #mobile number
    def on_enter(e):
      mobile.delete(0, 'end')

    def on_leave(e):
      mob = mobile.get()
      if mob == ' ':
        mobile.insert(0, 'Mobile Number')

    mobile = Entry(frame,
                   width=25,
                   fg='#234F1E',
                   border=0,
                   bg='#98BF64',
                   font=('Microsoft YaHei UI Light', 11))
    mobile.place(x=30, y=80)
    mobile.insert(0, 'Mobile Number')
    mobile.bind('<FocusIn>', on_enter)
    mobile.bind('<FocusOut>', on_leave)
    Frame(frame, width=295, height=2, bg='#234F1E').place(x=25, y=110)

    #account_no
    def on_enter(e):
      account.delete(0, 'end')

    def on_leave(e):
      account = mobile.get()
      if account == ' ':
        account.insert(0, 'Account Number')

    account = Entry(frame,
                    width=25,
                    fg='#234F1E',
                    border=0,
                    bg='#98BF64',
                    font=('Microsoft YaHei UI Light', 11))
    account.place(x=30, y=180)
    account.insert(0, 'Account Number')
    account.bind('<FocusIn>', on_enter)
    account.bind('<FocusOut>', on_leave)
    Frame(frame, width=295, height=2, bg='#234F1E').place(x=25, y=210)
    Button(frame,
           width=39,
           pady=7,
           text='View Current Balance',
           bg="#234F1E",
           fg='#98BF64',
           border=0,
           command=ex_vcb).place(x=35, y=280)
    vcb.mainloop()

  ########################################################################################
  def VLW():
    home.destroy()

    def ex_vlw():
      mobile_no = mobile.get()
      account_no = account.get()
      mycursor = mycon.cursor()
      query = 'select Last_Withdrawal from Account_Details where Account_Number = {} and Mobile_Number ={}'.format(
          account_no, mobile_no)
      mycursor.execute(query)
      data = mycursor.fetchone()
      date = data[0]
      date_string = date.strftime('%Y-%m-%d')
      vlw.destroy()
      if data != None:
        message = 'Your Last Withdrawal was on ' + str(date_string) + " ."
        messagebox.showinfo("View Last Withdrawal", message)
      else:
        messagebox.showerror("Error", "Account Doesn't Exsist")

    vlw = Tk()
    vlw.title('View Last Withdrawal')
    vlw.state('zoomed')
    vlw.configure(bg='#98BF64')
    mainframe = Frame(vlw, height=1000, width=2000, background='#98BF64')
    mainframe.place(relx=0.5, rely=0.5, anchor=CENTER)
    #adding the image
    imgs = PhotoImage(file='last.png')
    Label(mainframe, image=imgs, bg='#98BF64').place(x=600, y=200)
    #creating textbox beside image
    frame = Frame(mainframe, width=500, height=500, bg='#98BF64')
    frame.place(x=1000, y=300)
    #adding the title
    heading = Label(frame,
                    text='View Last Withdrawal',
                    fg='#234F1E',
                    bg='#98BF64',
                    font=('Microsoft YaHei UI Light', 23, 'bold'))
    heading.place(x=15, y=0)

    #mobile number
    def on_enter(e):
      mobile.delete(0, 'end')

    def on_leave(e):
      mob = mobile.get()
      if mobile == ' ':
        mobile.insert(0, 'Mobile Number')

    mobile = Entry(frame,
                   width=25,
                   fg='#234F1E',
                   border=0,
                   bg='#98BF64',
                   font=('Microsoft YaHei UI Light', 11))
    mobile.place(x=30, y=80)
    mobile.insert(0, 'Mobile Number')
    mobile.bind('<FocusIn>', on_enter)
    mobile.bind('<FocusOut>', on_leave)
    Frame(frame, width=295, height=2, bg='#234F1E').place(x=25, y=110)

    #account_no
    def on_enter(e):
      account.delete(0, 'end')

    def on_leave(e):
      account = mobile.get()
      if account == ' ':
        account.insert(0, 'Account Number')

    account = Entry(frame,
                    width=25,
                    fg='#234F1E',
                    border=0,
                    bg='#98BF64',
                    font=('Microsoft YaHei UI Light', 11))
    account.place(x=30, y=180)
    account.insert(0, 'Account Number')
    account.bind('<FocusIn>', on_enter)
    account.bind('<FocusOut>', on_leave)
    Frame(frame, width=295, height=2, bg='#234F1E').place(x=25, y=210)

    Button(frame,
           width=39,
           pady=7,
           text='View Last Withdrawal',
           bg="#234F1E",
           fg='#98BF64',
           border=0,
           command=ex_vlw).place(x=35, y=270)
    vlw.mainloop()

  ########################################################################################
  def VLD():
    home.destroy()

    def ex_vld():
      mobile_no = mobile.get()
      account_no = account.get()
      mycursor = mycon.cursor()
      query = 'select Last_Deposit from Account_Details where Account_Number = {} and Mobile_Number ={}'.format(
          account_no, mobile_no)
      mycursor.execute(query)
      data = mycursor.fetchone()
      date = data[0]
      date_string = date.strftime('%Y-%m-%d')
      vld.destroy()
      if data != None:
        message = 'Your Last Deposit was on ' + str(date_string) + " ."
        messagebox.showinfo("View Last Deposit", message)
      else:
        messagebox.showerror("Error", "Account Doesn't Exsist")

    vld = Tk()
    vld.title('View Last Deposit')
    vld.state('zoomed')
    vld.configure(bg='#98BF64')
    mainframe = Frame(vld, height=1000, width=2000, background='#98BF64')
    mainframe.place(relx=0.5, rely=0.5, anchor=CENTER)
    #adding the image
    imgs = PhotoImage(file='last.png')
    Label(mainframe, image=imgs, bg='#98BF64').place(x=600, y=200)
    #creating textbox beside image
    frame = Frame(mainframe, width=500, height=500, bg='#98BF64')
    frame.place(x=1000, y=300)
    #adding the title
    heading = Label(frame,
                    text='View Last Deposit',
                    fg='#234F1E',
                    bg='#98BF64',
                    font=('Microsoft YaHei UI Light', 23, 'bold'))
    heading.place(x=20, y=0)

    #mobile number
    def on_enter(e):
      mobile.delete(0, 'end')

    def on_leave(e):
      mob = mobile.get()
      if mob == ' ':
        mobile.insert(0, 'Mobile Number')

    mobile = Entry(frame,
                   width=25,
                   fg='#234F1E',
                   border=0,
                   bg='#98BF64',
                   font=('Microsoft YaHei UI Light', 11))
    mobile.place(x=30, y=80)
    mobile.insert(0, 'Mobile Number')
    mobile.bind('<FocusIn>', on_enter)
    mobile.bind('<FocusOut>', on_leave)
    Frame(frame, width=295, height=2, bg='#234F1E').place(x=25, y=110)

    #account_no
    def on_enter(e):
      account.delete(0, 'end')

    def on_leave(e):
      account = mobile.get()
      if account == ' ':
        account.insert(0, 'Account Number')

    account = Entry(frame,
                    width=25,
                    fg='#234F1E',
                    border=0,
                    bg='#98BF64',
                    font=('Microsoft YaHei UI Light', 11))
    account.place(x=30, y=180)
    account.insert(0, 'Account Number')
    account.bind('<FocusIn>', on_enter)
    account.bind('<FocusOut>', on_leave)
    Frame(frame, width=295, height=2, bg='#234F1E').place(x=25, y=210)
    Button(frame,
           width=39,
           pady=7,
           text='View Last Deposit',
           bg="#234F1E",
           fg='#98BF64',
           border=0,
           command=ex_vld).place(x=35, y=270)
    vld.mainloop()

  ########################################################################################
  def WM():
    home.destroy()

    def ex_wm():
      mobile_no = mobile.get()
      account_no = account.get()
      amount_ = int(amount.get())
      message = 'You are about to withdraw ' + str(
          amount_) + " AED. Do you want to continue?"
      messagebox.askyesno("Confirm", message)
      while True:
        mycursor = mycon.cursor()
        query = 'select Current_Balance from Account_Details where Account_Number={} and Mobile_Number ={}'.format(
            account_no, mobile_no)
        mycursor.execute(query)
        data = mycursor.fetchone()
        data2 = int(data[0])
        current_balance = data2 - amount_
        query1 = 'update Account_Details set Current_Balance={} where Account_Number={} and Mobile_Number ={}'.format(
            current_balance, account_no, mobile_no)
        mycursor.execute(query1)
        mycon.commit()
        last_withdrawal = date.today()
        query2 = 'update Account_Details set Last_Withdrawal = "{}" where Account_Number ={} and Mobile_Number ={}'.format(
            last_withdrawal, account_no, mobile_no)
        mycursor.execute(query2)
        mycon.commit()
        query3 = 'select Current_Balance from Account_Details where Account_Number={} and Mobile_Number={}'.format(
            account_no, mobile_no)
        mycursor.execute(query3)
        data3 = mycursor.fetchone()
        wm.destroy()
        if data3[0] < data2:
          messagebox.showerror("Withdrawal Successful",
                               ('Current Balance is', data3[0], '.'))
          break
        else:
          messagebox.showerror("Withdrawal Unsuccessful",
                               ('Current Balance is', current_balance, '.'))
          break

    wm = Tk()
    wm.title('Withdraw')
    wm.state('zoomed')
    wm.configure(bg='#98BF64')
    mainframe = Frame(wm, height=480, width=2000, background='#98BF64')
    mainframe.place(relx=0.5, rely=0.5, anchor=CENTER)
    #adding the image
    imgs = PhotoImage(file='withdraw.png')
    Label(mainframe, image=imgs, bg='#98BF64').place(x=400, y=50)
    #creating textbox beside image
    frame = Frame(mainframe, width=500, height=500, bg='#98BF64')
    frame.place(x=1100, y=70)
    #adding the title
    heading = Label(frame,
                    text='Withdraw',
                    fg='#234F1E',
                    bg='#98BF64',
                    font=('Microsoft YaHei UI Light', 23, 'bold'))
    heading.place(x=100, y=0)

    #mobile number
    def on_enter(e):
      mobile.delete(0, 'end')

    def on_leave(e):
      mob = mobile.get()
      if mob == ' ':
        mobile.insert(0, 'Mobile Number')

    mobile = Entry(frame,
                   width=25,
                   fg='#234F1E',
                   border=0,
                   bg='#98BF64',
                   font=('Microsoft YaHei UI Light', 11))
    mobile.place(x=30, y=80)
    mobile.insert(0, 'Mobile Number')
    mobile.bind('<FocusIn>', on_enter)
    mobile.bind('<FocusOut>', on_leave)
    Frame(frame, width=295, height=2, bg='#234F1E').place(x=25, y=110)

    #account_no
    def on_enter(e):
      account.delete(0, 'end')

    def on_leave(e):
      account = mobile.get()
      if account == ' ':
        account.insert(0, 'Account Number')

    account = Entry(frame,
                    width=25,
                    fg='#234F1E',
                    border=0,
                    bg='#98BF64',
                    font=('Microsoft YaHei UI Light', 11))
    account.place(x=30, y=150)
    account.insert(0, 'Account Number')
    account.bind('<FocusIn>', on_enter)
    account.bind('<FocusOut>', on_leave)
    Frame(frame, width=295, height=2, bg='#234F1E').place(x=25, y=180)

    def on_enter(e):
      amount.delete(0, 'end')

    def on_leave(e):
      amount = mobile.get()
      if amount == ' ':
        amount.insert(0, 'Amount')

    amount = Entry(frame,
                   width=25,
                   fg='#234F1E',
                   border=0,
                   bg='#98BF64',
                   font=('Microsoft YaHei UI Light', 11))
    amount.place(x=30, y=220)
    amount.insert(0, 'Amount')
    amount.bind('<FocusIn>', on_enter)
    amount.bind('<FocusOut>', on_leave)
    Frame(frame, width=295, height=2, bg='#234F1E').place(x=25, y=250)
    Button(frame,
           width=39,
           pady=7,
           text='Withdraw',
           bg="#234F1E",
           fg='#98BF64',
           border=0,
           command=ex_wm).place(x=35, y=310)
    wm.mainloop()
    ########################################################################################
  def DM():
    home.destroy()

    def ex_dm():
      mobile_no = mobile.get()
      account_no = account.get()
      amount_ = int(amount.get())
      message = 'You are about to deposit ' + str(
          amount_) + " AED. Do you want to continue?"
      messagebox.askyesno("Confirm", message)
      while True:
        mycursor = mycon.cursor()
        query = 'select Current_Balance from Account_Details where Account_Number={} and Mobile_Number ={}'.format(
            account_no, mobile_no)
        mycursor.execute(query)
        data = mycursor.fetchone()
        data2 = int(data[0])
        current_balance = data2 + amount_
        query1 = 'update Account_Details set Current_Balance={} where Account_Number={} and Mobile_Number ={}'.format(
            current_balance, account_no, mobile_no)
        mycursor.execute(query1)
        mycon.commit()
        last_deposit = date.today()
        query2 = 'update Account_Details set Last_Deposit = "{}" where Account_Number ={} and Mobile_Number ={}'.format(
            last_deposit, account_no, mobile_no)
        mycursor.execute(query2)
        mycon.commit()
        query3 = 'select Current_Balance from Account_Details where Account_Number={} and Mobile_Number ={}'.format(
            account_no, mobile_no)
        mycursor.execute(query3)
        data3 = mycursor.fetchone()
        dm.destroy()
        if data3[0] > data2:
          messagebox.showerror("Deposit Successful",
                               ('Current Balance is', data3[0], '.'))
          break
        else:
          messagebox.showerror("Deposit Unsuccessful",
                               ('Current Balance is', current_balance, '.'))
          break

    dm = Tk()
    dm.title('Deposit')
    dm.state('zoomed')
    dm.configure(bg='#98BF64')
    mainframe = Frame(dm, height=480, width=2000, background='#98BF64')
    mainframe.place(relx=0.5, rely=0.5, anchor=CENTER)
    #adding the image
    imgs = PhotoImage(file='deposit.png')
    Label(mainframe, image=imgs, bg='#98BF64').place(x=400, y=50)
    #creating textbox beside image
    frame = Frame(mainframe, width=500, height=500, bg='#98BF64')
    frame.place(x=1100, y=70)
    #adding the title
    heading = Label(frame,
                    text='Deposit',
                    fg='#234F1E',
                    bg='#98BF64',
                    font=('Microsoft YaHei UI Light', 23, 'bold'))
    heading.place(x=100, y=0)

    #mobile number
    def on_enter(e):
      mobile.delete(0, 'end')

    def on_leave(e):
      mob = mobile.get()
      if mobile == ' ':
        mobile.insert(0, 'Mobile Number')

    mobile = Entry(frame,
                   width=25,
                   fg='#234F1E',
                   border=0,
                   bg='#98BF64',
                   font=('Microsoft YaHei UI Light', 11))
    mobile.place(x=30, y=80)
    mobile.insert(0, 'Mobile Number')
    mobile.bind('<FocusIn>', on_enter)
    mobile.bind('<FocusOut>', on_leave)
    Frame(frame, width=295, height=2, bg='#234F1E').place(x=25, y=110)

    #account_no
    def on_enter(e):
      account.delete(0, 'end')

    def on_leave(e):
      account = mobile.get()
      if account == ' ':
        account.insert(0, 'Account Number')

    account = Entry(frame,
                    width=25,
                    fg='#234F1E',
                    border=0,
                    bg='#98BF64',
                    font=('Microsoft YaHei UI Light', 11))
    account.place(x=30, y=150)
    account.insert(0, 'Account Number')
    account.bind('<FocusIn>', on_enter)
    account.bind('<FocusOut>', on_leave)
    Frame(frame, width=295, height=2, bg='#234F1E').place(x=25, y=180)

    def on_enter(e):
      amount.delete(0, 'end')

    def on_leave(e):
      amount = mobile.get()
      if amount == ' ':
        amount.insert(0, 'Amount')

    amount = Entry(frame,
                   width=25,
                   fg='#234F1E',
                   border=0,
                   bg='#98BF64',
                   font=('Microsoft YaHei UI Light', 11))
    amount.place(x=30, y=220)
    amount.insert(0, 'Amount')
    amount.bind('<FocusIn>', on_enter)
    amount.bind('<FocusOut>', on_leave)
    Frame(frame, width=295, height=2, bg='#234F1E').place(x=25, y=250)
    Button(frame,
           width=39,
           pady=7,
           text='Deposit',
           bg="#234F1E",
           fg='#98BF64',
           border=0,
           command=ex_dm).place(x=35, y=310)
    dm.mainloop()

  ########################################################################################
  def CNA():
    home.destroy()

    def add():
      custrnm = custnm.get()
      mobile_no = mobile.get()
      email_id = email.get()
      number = 'correct'
      while number == 'correct':
        mycursor = mycon.cursor()
        account_no = random.randint(100000001, 999999999)
        query = 'select * from Account_Details where Account_Number ={}'.format(
            account_no)
        mycursor.execute(query)
        data = mycursor.fetchone()
        if data == None:
          query1 = 'insert into Account_Details(Account_Number, Customer_Name, Mobile_Number, Email_ID)values({}, "{}", {}, "{}")'.format(
              account_no, custrnm, mobile_no, email_id)
          mycursor.execute(query1)
          mycon.commit()
          number = 'error'
        else:
          number = 'correct'
        new_account.destroy()
        messagebox.showinfo("New Account Created",
                            ('Your Account Number is ', account_no, '.'))

    new_account = Tk()
    new_account.title('Create New Account')
    new_account.state('zoomed')
    new_account.configure(bg='#98BF64')
    mainframe = Frame(new_account,
                      height=480,
                      width=2000,
                      background='#98BF64')
    mainframe.place(relx=0.5, rely=0.5, anchor=CENTER)
    #adding the image
    imgs = PhotoImage(file='new.png')
    Label(mainframe, image=imgs, bg='#98BF64').place(x=400, y=50)
    #creating textbox beside image
    frame = Frame(mainframe, width=500, height=500, bg='#98BF64')
    frame.place(x=1100, y=20)
    #adding the title
    heading = Label(frame,
                    text='Create New Account',
                    fg='#234F1E',
                    bg='#98BF64',
                    font=('Microsoft YaHei UI Light', 23, 'bold'))
    heading.place(x=30, y=0)

    #customer name
    def on_enter(e):
      custnm.delete(0, 'end')

    def on_leave(e):
      name = custnm.get()
      if name == ' ':
        custnm.insert(0, 'Customer Name')

    custnm = Entry(frame,
                   width=25,
                   fg='#234F1E',
                   border=0,
                   bg='#98BF64',
                   font=('Microsoft YaHei UI Light', 11))
    custnm.place(x=30, y=80)
    custnm.insert(0, 'Customer Name')
    custnm.bind('<FocusIn>', on_enter)
    custnm.bind('<FocusOut>', on_leave)
    Frame(frame, width=295, height=2, bg='#234F1E').place(x=25, y=107)

    #mobile number
    def on_enter(e):
      mobile.delete(0, 'end')

    def on_leave(e):
      mobile = custnm.get()
      if mobile == ' ':
        mobile.insert(0, 'Mobile Number')

    mobile = Entry(frame,
                   width=25,
                   fg='#234F1E',
                   border=0,
                   bg='#98BF64',
                   font=('Microsoft YaHei UI Light', 11))
    mobile.place(x=30, y=150)
    mobile.insert(0, 'Mobile Number')
    mobile.bind('<FocusIn>', on_enter)
    mobile.bind('<FocusOut>', on_leave)
    Frame(frame, width=295, height=2, bg='#234F1E').place(x=25, y=177)

    #email id
    def on_enter(e):
      email.delete(0, 'end')

    def on_leave(e):
      email = custnm.get()
      if email == ' ':
        email.insert(0, 'Email ID')

    email = Entry(frame,
                  width=25,
                  fg='#234F1E',
                  border=0,
                  bg='#98BF64',
                  font=('Microsoft YaHei UI Light', 11))
    email.place(x=30, y=220)
    email.insert(0, 'Email ID')
    email.bind('<FocusIn>', on_enter)
    email.bind('<FocusOut>', on_leave)
    Frame(frame, width=295, height=2, bg='#234F1E').place(x=25, y=247)

    #address
    def on_enter(e):
      address.delete(0, 'end')

    def on_leave(e):
      address = custnm.get()
      if address == ' ':
        address.insert(0, 'Address')

    address = Entry(frame,
                    width=25,
                    fg='#234F1E',
                    border=0,
                    bg='#98BF64',
                    font=('Microsoft YaHei UI Light', 11))
    address.place(x=30, y=290)
    address.insert(0, 'Address')
    address.bind('<FocusIn>', on_enter)
    address.bind('<FocusOut>', on_leave)
    Frame(frame, width=295, height=2, bg='#234F1E').place(x=25, y=317)
    Button(frame,
           width=39,
           pady=7,
           text='Create',
           bg="#234F1E",
           fg='#98BF64',
           border=0,
           command=add).place(x=35, y=385)
    new_account.mainloop()

##########################################################################################
############################################################################
#OPtions

  Button(frame,
         width=39,
         pady=7,
         text='Drop Existing Account',
         bg="#234F1E",
         fg='#98BF64',
         border=0,
         command=DEA).place(x=100, y=130)
  Button(frame,
         width=39,
         pady=7,
         text='View Current Balance',
         bg="#234F1E",
         fg='#98BF64',
         border=0,
         command=VCB).place(x=100, y=190)
  Button(frame,
         width=39,
         pady=7,
         text='View Last Withdrawal',
         bg="#234F1E",
         fg='#98BF64',
         border=0,
         command=VLW).place(x=100, y=250)
  Button(frame,
         width=39,
         pady=7,
         text='View Last Deposit',
         bg="#234F1E",
         fg='#98BF64',
         border=0,
         command=VLD).place(x=100, y=310)
  Button(frame,
         width=39,
         pady=7,
         text='Withdraw Money ',
         bg="#234F1E",
         fg='#98BF64',
         border=0,
         command=WM).place(x=100, y=370)
  Button(frame,
         width=39,
         pady=7,
         text='Deposit Money',
         bg="#234F1E",
         fg='#98BF64',
         border=0,
         command=DM).place(x=100, y=430)
  Button(frame,
         width=39,
         pady=7,
         text='Create New Account',
         bg='#234F1E',
         fg='#98BF64',
         border=0,
         command=CNA).place(x=100, y=490)
  home.mainloop()


#############################################################################
#creating the Login window
root = Tk()
root.title('Login')
root.geometry('925x500+300+200')
root.configure(bg='#fff')
mainframe = Frame(root, height=480, width=900, background='white')
mainframe.place(relx=0.5, rely=0.5, anchor=CENTER)
#adding the image
imgs = PhotoImage(file='login.png')
Label(mainframe, image=imgs, bg='white').place(x=50, y=50)
#creating textbox beside image
frame = Frame(mainframe, width=350, height=350, bg='white')
frame.place(x=480, y=70)
#adding the title
heading = Label(frame,
                text='LOGIN',
                fg='#57a1f8',
                bg='white',
                font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=100, y=5)


#username
def on_enter(e):
  usernm.delete(0, 'end')


def on_leave(e):
  name = usernm.get()
  if name == ' ':
    usernm.insert(0, 'Username')


usernm = Entry(frame,
               width=25,
               fg='black',
               border=0,
               bg='white',
               font=('Microsoft YaHei UI Light', 11))
usernm.place(x=30, y=80)
usernm.insert(0, 'Username')
usernm.bind('<FocusIn>', on_enter)
usernm.bind('<FocusOut>', on_leave)
Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)


#password
def on_focus_in(event):
  passwd = event.widget
  if passwd.get() == 'Password':
    passwd.delete(0, 'end')
    passwd.config(show='▪')


def on_focus_out(event):
  passwd = event.widget
  if passwd.get() == ' ':
    passwd.insert(0, 'Password')
    passwd.config(show=' ')


passwd = Entry(frame,
               width=25,
               fg="black",
               border=0,
               bg="white",
               font=('Microsoft YaHei UI Light', 10))
passwd.place(x=30, y=150)
passwd.bind("<FocusIn>", on_focus_in)
passwd.bind("<FocusOut>", on_focus_out)
passwd.insert(0, 'Password')
Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)
#Sign in Button
Button(frame,
       width=39,
       pady=7,
       text='Login',
       bg="#57a1f8",
       fg='white',
       border=0,
       command=login).place(x=35, y=230)
root.mainloop()
