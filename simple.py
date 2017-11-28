import time
import datetime
from Tkinter import*
import tkMessageBox
import os

root = Tk()
root.title("Welcome to the Nestor Analytics")
root.geometry("1350x650")



Tops = Frame(root, width = 1350, height = 10, bd = 5, relief = 'raise')
Tops.pack(side = TOP, fill = BOTH)
f1 = Frame(root, width = 600, height = 600, bd = 5, relief = 'raise')
f1.pack(side = LEFT, expand = YES, fill = BOTH)
f2 = Frame(root, width = 300, height = 700, bd = 5, relief = 'raise')
f2.pack(side = RIGHT, expand = YES, fill = BOTH)

f1a = Frame(f1, width = 600, height = 200, bd = 5, relief = 'raise')
f1a.pack(side = TOP, expand = YES, fill = BOTH)
f1b = Frame(f1, width = 600, height = 600, bd = 5)
f1b.pack(side = TOP, expand = YES, fill = BOTH) 

f1a1 = Frame(f1a, width = 600, height = 100, bd = 5)
f1a1.pack(side = TOP, expand = YES, fill = BOTH)
f1a2 = Frame(f1a, width = 600, height = 100, bd = 5)
f1a2.pack(side = TOP, expand = YES, fill = BOTH) 



lblinfo = Label(Tops, font = ('arial', 20, 'bold'), text = "    Nestor Analytics    ", bd = 5, width = 40)
lblinfo.grid(row = 0, column = 0)
lblinfo.pack(expand = YES, fill = BOTH)

def iExit():
    qExit = tkMessageBox.askyesno("PayRoll System", "Do you want to exit the system")
    if qExit > 0:
        root.destroy()
        return


def Reset():
    Name.set("")
    Address.set("")
    PhoneNumber.set("")
    Pincode.set("")
    School Name.set("")
    Model.set("")
    Quantity.set("")
    Amount.set("")
    CGST.set("")
    SGST.set("")
    Total.set("")
    TotalAmount.set("")
    txtPaySlip.delete("1.0",END)

def EnterInfo():
    txtPaySlip.insert(END, "School Name : \t\t"+ School Name.get()+"\n\n")
    txtPaySlip.insert(END, "HSN/SAC Code : \t\t"+ Model.get()+"\n\n")
    txtPaySlip.insert(END, "Quantity : \t\t"+ Quantity.get()+"\n\n")
    txtPaySlip.insert(END, "Amount : \t\t"+ Amount.get()+"\n\n")
    txtPaySlip.insert(END, "CGST : \t\t"+ CGST.get()+"\n\n")
    txtPaySlip.insert(END, "SGST : \t\t"+ SGST.get()+"\n\n")
    txtPaySlip.insert(END, "Total : \t\t"+ Total.get()+"\n\n")
    txtPaySlip.insert(END, "Total Amount : \t\t"+ TotalAmount.get()+"\n\n")
    
def view():
    f = open('helloworld.txt','w')
    f.write('Name : '+Name.get()+"\nAddress : "+Address.get()+"\nPhone Number : "+PhoneNumber.get()+"    Pincode : "+Pincode.get()+"\n\nItem\t\t\t\tHSN/CSC Code\t\tQuantity\tAmount\t\tCGST\tSGST\tTotal\n\n"+Item.get()+"\t\t\t\t"+Model.get()+"\t\t"+Quantity.get()+"\t"+Amount.get()+"\t\t"+CGST.get()+"\t"+SGST.get()+"\t"+Total.get())
    f.close()
    os.startfile("helloworld.txt")

Name = StringVar()
Address = StringVar()
PhoneNumber = StringVar()
Pincode = StringVar()
Item = StringVar()
Model = StringVar()
Quantity = StringVar()
Amount = StringVar()
CGST = StringVar()
SGST = StringVar()
Total = StringVar()
TotalAmount = StringVar()
DateOfOrder = StringVar()

DateOfOrder.set(time.strftime("%d/%m/%Y"))



lblHead1 = Label(f1a1, text = 'Custumer Details : ', font = ('arial', 16, 'bold'), bd = 5).grid(row = 0, column = 0)
lblName = Label(f1a1, text = 'Name', font = ('arial', 16, 'bold'), bd = 5).grid(row = 1, column = 0)
lblAdress = Label(f1a1, text = 'Adress', font = ('arial', 16, 'bold'), bd = 5).grid(row = 2, column = 0)
lblPhoneNumber = Label(f1a1, text = 'Phone Number', font = ('arial', 16, 'bold'), bd = 5).grid(row = 1, column = 2)
lblPincode = Label(f1a1, text = 'Pincode', font = ('arial', 16, 'bold'), bd = 5).grid(row = 2, column = 2)

lblHead2 = Label(f1a2, text = 'Product Description : ', font = ('arial', 16, 'bold'), bd = 5).grid(row = 0, column = 0)
lblItem = Label(f1a2, text = 'Item', font = ('arial', 16, 'bold'), bd = 5).grid(row = 1, column = 0)
lblModel = Label(f1a2, text = 'HSN/SAC Code', font = ('arial', 16, 'bold'), bd = 5).grid(row = 2, column = 0)
lblQuantity = Label(f1a2, text = 'Quantity', font = ('arial', 16, 'bold'), bd = 5).grid(row = 3, column = 0)
lblAmount = Label(f1a2, text = 'Amount', font = ('arial', 16, 'bold'), bd = 5).grid(row = 1, column = 2)
lblCGST = Label(f1a2, text = 'CGST', font = ('arial', 16, 'bold'), bd = 5).grid(row = 2, column = 2)
lblSGST = Label(f1a2, text = 'SGST', font = ('arial', 16, 'bold'), bd = 5).grid(row = 3, column = 2)
lblTotal = Label(f1a2, text = 'Total', font = ('arial', 16, 'bold'), bd = 5).grid(row = 4, column = 2)
lblTotalAmount = Label(f1a2, text = 'Total Amount', font = ('arial', 16, 'bold'), bd = 5).grid(row = 5, column = 2)



etxtName = Entry(f1a1, textvariable = Name, font = ('arial', 16, 'bold'), bd = 5, width = 22, justify = 'left')
etxtName.grid(row = 1, column = 1)
etxtAdress = Entry(f1a1, textvariable = Address, font = ('arial', 16, 'bold'), bd = 5, width = 22, justify = 'left')
etxtAdress.grid(row = 2, column = 1)
etxtPhoneNumber = Entry(f1a1, textvariable = PhoneNumber, font = ('arial', 16, 'bold'), bd = 5, width = 22, justify = 'left')
etxtPhoneNumber.grid(row = 1, column = 3)
etxtPincode = Entry(f1a1, textvariable = Pincode, font = ('arial', 16, 'bold'), bd = 5, width = 22, justify = 'left')
etxtPincode.grid(row = 2, column = 3)

etxtItem = Entry(f1a2, textvariable = Item, font = ('arial', 16, 'bold'), bd = 5, width = 22, justify = 'left')
etxtItem.grid(row = 1, column = 1)
etxtModel = Entry(f1a2, textvariable = Model, font = ('arial', 16, 'bold'), bd = 5, width = 22, justify = 'left')
etxtModel.grid(row = 2, column = 1)
etxtQuantity = Entry(f1a2, textvariable = Quantity, font = ('arial', 16, 'bold'), bd = 5, width = 22, justify = 'left')
etxtQuantity.grid(row = 3, column = 1)
etxtAmount = Entry(f1a2, textvariable = Amount, font = ('arial', 16, 'bold'), bd = 5, width = 22, justify = 'left')
etxtAmount.grid(row = 1, column = 3)
etxtCGST = Entry(f1a2, textvariable = CGST, font = ('arial', 16, 'bold'), bd = 5, width = 22, justify = 'left')
etxtCGST.grid(row = 2, column = 3)
etxtSGST = Entry(f1a2, textvariable = SGST, font = ('arial', 16, 'bold'), bd = 5, width = 22, justify = 'left')
etxtSGST.grid(row = 3, column = 3)
etxtTotal = Entry(f1a2, textvariable = Total, font = ('arial', 16, 'bold'), bd = 5, width = 22, justify = 'left')
etxtTotal.grid(row = 4, column = 3)
etxtTotalAmount = Entry(f1a2, textvariable = TotalAmount, font = ('arial', 16, 'bold'), bd = 5, width = 22, justify = 'left')
etxtTotalAmount.grid(row = 5, column = 3)
btnTotal = Button(f1a2, text = 'Add', command = EnterInfo, bd = 5, fg = 'black', font = ('arial', 16, 'bold'), width = 10, height = 1).grid(row = 5, column = 1)



lblpaySlip = Label(f2, textvariable = DateOfOrder, font = ('arial', 21, 'bold'), bd = 5).grid(row = 0, column = 0)
txtPaySlip = Text(f2, width = 34, height = 20, bd = 16, font = ('arial', 12, 'bold'))
txtPaySlip.grid(row = 1, column = 0)



btnReceipt = Button(f1b, text = 'View Receipt', command = view, padx = 5, pady = 5, bd = 5, fg = 'black', font = ('arial', 16, 'bold'), width = 16, height = 1).grid(row = 0, column = 0)
btnPrint = Button(f1b, text = 'Print Receipt', padx = 5, pady = 5, bd = 5, fg = 'black', font = ('arial', 16, 'bold'), width = 16, height = 1).grid(row = 0, column = 1)
btnReset = Button(f1b, text = 'Reset', command = Reset, padx = 5, pady = 5, bd = 5, fg = 'black', font = ('arial', 16, 'bold'), width = 16, height = 1).grid(row = 0, column = 2)
btnExit = Button(f1b, text = 'Exit', command = iExit, padx = 5, pady = 5, bd = 5, fg = 'black', font = ('arial', 16, 'bold'), width = 16, height = 1).grid(row = 0, column = 3)



root.mainloop()
