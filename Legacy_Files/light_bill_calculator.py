from tkinter import *
import light_functions as light
from GUI_functions import raise_frame
from light_classes import tdu

########## ALL classes and functions need to be modular! ##########
# available TDU providers
ctp = tdu("Centerpoint", 4.39, 0.033)
onc = tdu("Oncor", 3.42,0.034)
aepcent = tdu("AEP Central", 4.79, 0.040)
aepnort = tdu("AEP North", 4.79, 0.036)
tnmp = tdu ("TNMP", 7.85, 0.0403)
tduArray = [ctp, onc, aepcent, aepnort, tnmp]

root = Tk()
root.title('Light bill estimator')


frame1 = Frame(root)
frame1.grid()
pickTDU = Label(frame1, text = "Please select utility provider:",pady=5, padx=5)
pickTDU.grid()
selected = Label(frame1, text = "",pady=5, padx=5)
selected.grid()



################# Frame2 holds TDU provider names ##############
frame2 = Frame(root)
frame2.grid()

b1 = Button(frame2, text=ctp.name)
b1.grid(row=1,column=0, sticky='news' , pady=5, padx=5)
b2=Button(frame2,text=onc.name)
b2.grid(row=1,column=1,sticky='news' , pady=5, padx=5)
b3=Button(frame2,text=aepcent.name)
b3.grid(row=1,column=2,sticky='news' , pady=5, padx=5)
b4=Button(frame2,text=aepnort.name)
b4.grid(row=1,column=3,sticky='news' , pady=5, padx=5)
b5=Button(frame2,text=tnmp.name)
b5.grid(row=1,column=4,sticky='news' , pady=5, padx=5)


############### Binding TDU buttons ##################


def click1(value):
    global t1
    t1 = value
    selected.config(text=t1.name,fg='red')
    print(t1.name,t1.e,t1.b)


b1.bind('<Button-1>', lambda event, *args: click1(ctp))
b2.bind('<Button-1>', lambda event, *args: click1(onc))
b3.bind('<Button-1>', lambda event, *args: click1(aepcent))
b4.bind('<Button-1>', lambda event, *args: click1(aepnort))
b5.bind('<Button-1>', lambda event, *args: click1(onc))


################## label to select plan type ################
frame3 = Frame(root)
frame3.grid()
plan_type = Label(frame3, text="Please select plan type:", pady=5, padx=5)
plan_type.grid()


#  Create two frames, one for normal bill and another for tiered bill
frameN = Frame(root)
frameT = Frame(root)

# use loop to apply settings to frames
for frame in (frameN, frameT):
    frame.grid(row=15, column=0, sticky='news')

# use buttons to switch between frames using raise_frame command
Button(frameN, text='Tiered plan', command=lambda:raise_frame(frameT),pady=5, padx=5).pack()
Label(frameN, text='Normal plan selected',pady=5, padx=5,fg = 'red').pack()


#################################### FRAME N (normal bill)####################################
frame3 = Frame(frameN)
frame3.pack(padx=0, pady=15)
base = Label(frame3, text="Please enter base charge:", pady=5, padx=10)
base.pack(side=LEFT)
entry1 = Entry(frame3)
entry1.pack(side=RIGHT)

frame4 = Frame(frameN)
frame4.pack(padx=0, pady=15)
energy = Label(frame4, text="Enter energy Charge in cents", pady=5, padx=5)
energy.pack(side=LEFT)
entry2 = Entry(frame4)
entry2.pack(side=RIGHT)

frame5 = Frame(frameN)
frame5.pack(padx=0, pady=15)
energy = Label(frame5, text="Please enter kilowatts used:")
energy.pack(side=LEFT)
entry3 = Entry(frame5)
entry3.pack(side=RIGHT)

# calculate button
frame6 = Frame(frameN)
frame6.pack()
button = Button(frame6, text="Calculate!", width=15, height=1, bg='green', fg='orange')
button.pack()
# result label
bill = Label(frameN, text='Estimated Bill:',pady=10,padx=0,font=20)
bill.pack()
billF = Label(frameN, text='',pady=10,padx=0,font=20)
billF.pack()


################### binding for normal bill calculation #########################
def handle_click(event):
    print("normal bill calculation in process")

    try:

        b = float(entry1.get())
        c = float(entry2.get())
        k = float(entry3.get())
        c = c / 100
        lb = (light.getbill(c, k, t1.e, b, t1.b))

        billF["text"] = "{lb:.2f}"

    except ValueError:
        billF.config(text="Values are invalid, try again...")


    print(lb)

button.bind('<Button-1>', handle_click)


############################# frame T (tiered plan) ##################################

Label(frameT, text='Tiered plan selected',pady=5, padx=5, fg= 'red').pack()
Button(frameT, text='Normal plan', command=lambda:raise_frame(frameN),pady=5, padx=5).pack()
y=10
x=0
frame7 = Frame(frameT)
frame7.pack()
base = Label(frame7, text="Please enter base charge:", pady=y, padx=x)
base.pack(side=LEFT)
entryT1 = Entry(frame7)
entryT1.pack(side=RIGHT)

frame8 = Frame(frameT)
frame8.pack()
tier1 = Label(frame8, text="Enter first tier limit in kWh:", pady=y, padx=x)
tier1.pack(side=LEFT)
entryT2 = Entry(frame8)
entryT2.pack(side=RIGHT)

frame9 = Frame(frameT)
frame9.pack()
cpk1 = Label(frame9, text="Enter cents per kilowatt: ", pady=y, padx=x)
cpk1.pack(side=LEFT)
entryT3 = Entry(frame9)
entryT3.pack(side=RIGHT)

frame10 = Frame(frameT)
frame10.pack()
tier2 = Label(frame10, text="Enter 2nd tier limit in kWh:", pady=y ,padx=x)
tier2.pack(side=LEFT)
entryT4 = Entry(frame10)
entryT4.pack(side=RIGHT)

frame11 = Frame(frameT)
frame11.pack()
cpk2 = Label(frame11, text="Enter 2nd tier cents per kilowatt:", pady=y, padx=x)
cpk2.pack(side=LEFT)
entryT5 = Entry(frame11)
entryT5.pack(side=RIGHT)

frame12 = Frame(frameT)
frame12.pack()
cpk3 = Label(frame12, text="Enter final tier cents per kWh:", pady=y, padx=x)
cpk3.pack(side=LEFT)
entryT6 = Entry(frame12)
entryT6.pack(side=RIGHT)

frame13 = Frame(frameT)
frame13.pack()
kwh = Label(frame13, text="Enter total kWh used", pady=y, padx=x)
kwh.pack(side=LEFT)
entryT7 = Entry(frame13)
entryT7.pack(side=RIGHT)



frameB = Frame(frameT)
frameB.pack()
button2 = Button(frameB,text="Calculate!", width=15, height=1, bg='green', fg='black')
button2.pack()





billT = Label(frameT,text='Estimated Bill:',pady=10,padx=0,font=20)
billT.pack()
billFT = Label(frameT, text='',pady=10,padx=0,font=20,)
billFT.pack()



###################### binding for tierd plan calc button #####################
def handle_click2(event):
    try:
        b = float(entryT1.get())  # base charge
        l1 = float(entryT2.get())  # first tier limit in kWh
        c1 = float(entryT3.get())  # first tier cents per kilowatt
        l2 = float(entryT4.get())  # second tier limit
        c2 = float(entryT5.get())  # second tier cents per kilowatt
        c3 = float(entryT6.get())  # final cents per kilowatt
        kw = float(entryT7.get())  # total kilowatts used

        # convert cents per kilowatt to decimal
        c1 = c1 / 100
        c2 = c2 / 100
        c3 = c3 / 100

        lb = light.getTbill(b, l1, c1, l2, c2, c3, kw, t1.e, t1.b)

        billFT["text"] = "{lb:.2f}"
    except ValueError:
        billT.config(text='Values are invalid, try again.')





    #frameT.pack_forget()


button2.bind('<Button-1>', handle_click2)


raise_frame(frameN)



root.mainloop()