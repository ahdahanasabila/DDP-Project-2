from tkinter import *
from tkinter import messagebox
import random,os, tempfile, smtplib
#functionality part


    

def print_bill():
    if textarea.get(1.0, END)=='\n':
        messagebox.showerror('Error','Bill is empty')
    else:
        file=tempfile.mktemp('.txt')
        open(file,'w').write(textarea.get(1.0, END))
        os.startfile(file,'print')

def search_bill():
    for i in os.listdir('bills/'):
        if i.split('.')[0]==billnumberEntry.get():
            f=open(f'bills/{i}','r')
            textarea.delete(1.0, END)
            for data in f:
                textarea.insert(END, data)
            f.close()
            break
        else:
            messagebox.showerror('Error','invalid bill number')

if not os.path.exists('bills'):
    os.mkdir('bills')

def save_bill():
    global billnumber
    result=messagebox.askyesno('Confirm','Do You Want to Save the Bill?')
    if result:
        bill_content=textarea.get(1.0, END)
        file=open(f'bills/ {billnumber}.txt','w')
        file.write(bill_content)
        file.close()
        messagebox.showinfo('Succes',f'bill number{billnumber} is saved succesfully')
        billnumber=random.randint(500, 1000)

billnumber=random.randint(500, 1000)

def bill_area():
    if nameEntry.get()=='' or phoneEntry.get()=='':
        messagebox.showerror('Error', 'Customers Details Are Required')
    elif cosmeticpriceEntry.get()=='' or grocerypriceEntry.get()=='' or drinkspriceEntry.get()=='':
        messagebox.showerror('Error', 'No Products Are Selected')
    elif cosmeticpriceEntry.get()=='0 Rp' and grocerypriceEntry.get()=='0 Rp' and drinkspriceEntry.get()=='0 Rp':
        messagebox.showerror('Error', 'No Products are Selected')
    textarea.delete(1.0, END)

    textarea.insert(END,'\t\t**Welcome Customer**\n')
    textarea.insert(END, f'\nBill Number: {billnumber}\n')
    textarea.insert(END, f'\nCustomer Name: {nameEntry.get()}\n')
    textarea.insert(END, f'\nCustomer Number Phone: {phoneEntry.get()}\n')
    textarea.insert(END, '\n=======================================================')
    textarea.insert(END, 'Product\t\t\tQuantity\t\t\tPrice')
    textarea.insert(END, '\n=======================================================')
    if bathsoapEntry.get()!='0':
        textarea.insert(END, f'\nMie\t\t\t{bathsoapEntry.get()}\t\t\t{soapprice} Rp')
    if kerupukEntry.get()!='0':
        textarea.insert(END, f'\nSosis\t\t\t{kerupukEntry.get()}\t\t\t{kerupukprice} Rp')
    if fishrollEntry.get()!='0':
        textarea.insert(END, f'\nBakso\t\t\t{fishrollEntry.get()}\t\t\t{fishrollprice} Rp')
    if  sosisEntry.get()!='0':
        textarea.insert(END, f'\nKerupuk\t\t\t{sosisEntry.get()}\t\t\t{sosisprice} Rp')
    if baksoEntry.get()!='0':
        textarea.insert(END, f'\nfish Roll\t\t\t{baksoEntry.get()}\t\t\t{baksoprice} Rp')
    if dumplingEntry.get()!='0':
        textarea.insert(END, f'\nDumpling\t\t\t{dumplingEntry.get()}\t\t\t{dumplingprice} Rp')

    if riceEntry.get()!='0':
        textarea.insert(END, f'\nRice\t\t\t{riceEntry.get()}\t\t\t{riceprice} Rp')
    if daalEntry.get()!='0':
        textarea.insert(END, f'\nDaal\t\t\t{daalEntry.get()}\t\t\t{daalprice} Rp')
    if oilEntry.get()!='0':
        textarea.insert(END, f'\nOil\t\t\t{oilEntry.get()}\t\t\t{oilprice} Rp')
    if sugarEntry.get()!='0':
        textarea.insert(END, f'\nSugar\t\t\t{sugarEntry.get()}\t\t\t{sugarprice} Rp')
    if wheatEntry.get()!='0':
        textarea.insert(END, f'\nWheat\t\t\t{wheatEntry.get()}\t\t\t{wheatprice} Rp')
    if teaEntry.get()!='0':
        textarea.insert(END, f'\nTea\t\t\t{teaEntry.get()}\t\t\t{teaprice} Rp')

    if maazaEntry.get()!='0':
        textarea.insert(END, f'\nMaaza\t\t\t{maazaEntry.get()}\t\t\t{maazaprice} Rp')
    if frootiEntry.get()!='0':
        textarea.insert(END, f'\nFrooti\t\t\t{frootiEntry.get()}\t\t\t{frootiprice} Rp')
    if pepsiEntry.get()!='0':
        textarea.insert(END, f'\nPepsi\t\t\t{pepsiEntry.get()}\t\t\t{pepsiprice} Rp')
    if cocacolaEntry.get()!='0':
        textarea.insert(END, f'\nCoca Cola\t\t\t{cocacolaEntry.get()}\t\t\t{cocacolaprice} Rp')
    if dewEntry.get()!='0':
        textarea.insert(END, f'\nDew\t\t\t{dewEntry.get()}\t\t\t{dewprice} Rp')
    if spriteEntry.get()!='0':
        textarea.insert(END, f'\nSprite\t\t\t{spriteEntry.get()}\t\t\t{spriteprice} Rp')
    textarea.insert(END, '\n-------------------------------------------------------')

    if cosmetictaxEntry.get()!='0,0 Rp':
        textarea.insert(END, f'\nCosmetic Tax\t\t\t\t{cosmeticpriceEntry.get()}')
    if grocerytaxEntry.get()!='0,0 Rp':
        textarea.insert(END, f'\nGrocery Tax\t\t\t\t{grocerypriceEntry.get()}')
    if drinkstaxEntry.get()!='0,0 Rp':
        textarea.insert(END, f'\nDrinks Tax\t\t\t\t{drinkstaxEntry.get()}')
    textarea.insert(END, f'\n\nTotal Bill \t\t\t\t{totalbill}')
    textarea.insert(END, '\n-------------------------------------------------------')
    save_bill()

def total():
    global soapprice, kerupukprice, fishrollprice, sosisprice, baksoprice, dumplingprice
    global riceprice, daalprice, oilprice, sugarprice, wheatprice, teaprice
    global maazaprice, frootiprice, pepsiprice, cocacolaprice, dewprice, spriteprice
    global totalbill
    #cosmetic price calculation
    soapprice=int(bathsoapEntry.get())*3000
    sosisprice=int(sosisEntry.get())*2000
    baksoprice=int(baksoEntry.get())*5000
    fishrollprice=int(fishrollEntry.get())*3000
    kerupukprice=int(kerupukEntry.get())*3000
    dumplingprice=int(dumplingEntry.get())*3000

    totalcosmeticprice=soapprice+baksoprice+sosisprice+fishrollprice+kerupukprice+dumplingprice
    cosmeticpriceEntry.delete(0, END)
    cosmeticpriceEntry.insert(0, f'{totalcosmeticprice} Rp')
    cosmetictax=totalcosmeticprice*0.12
    cosmetictaxEntry.delete(0, END)
    cosmetictaxEntry.insert(0, str(cosmetictax)+ ' Rp')

    #grocery price calculation
    riceprice=int(riceEntry.get())*2000
    daalprice=int(daalEntry.get())*2000
    oilprice=int(oilEntry.get())*1500
    sugarprice=int(sugarEntry.get())*3000
    teaprice=int(teaEntry.get())*3000
    wheatprice=int(wheatEntry.get())*8000

    totalgroceryprice=riceprice+daalprice+oilprice+sugarprice+teaprice+wheatprice
    grocerypriceEntry.delete(0, END)
    grocerypriceEntry.insert(0, str(totalgroceryprice)+' Rp')
    grocerytax=totalgroceryprice*0.05
    grocerytaxEntry.delete(0, END)
    grocerytaxEntry.insert(0, str(grocerytax)+ ' Rp')


    maazaprice=int(maazaEntry.get())*3000
    frootiprice=int(frootiEntry.get())*4000
    dewprice=int(dewEntry.get())*5000
    pepsiprice=int(pepsiEntry.get())*7000
    spriteprice=int(spriteEntry.get())*10000
    cocacolaprice=int(cocacolaEntry.get())*5

    totaldrinksprice=maazaprice+frootiprice+dewprice+pepsiprice+spriteprice+cocacolaprice
    drinkspriceEntry.delete(0, END)
    drinkspriceEntry.insert(0, str(totaldrinksprice)+' Rp')
    drinkstax=totaldrinksprice*0.08
    drinkstaxEntry.delete(0, END)
    drinkstaxEntry.insert(0, str(drinkstax)+ ' Rp')


    totalbill=totalcosmeticprice+totalgroceryprice+totaldrinksprice+cosmetictax+grocerytax+drinkstax



#GUI part

root=Tk()
root.title('Seblak Prasmanan')  
root.geometry('1270x658')
root.iconbitmap('icon.ico')
headingLabel=Label(root, text='Hitung Jumlah Pesanan Seblak Prasmanan', font=('times new roman', 30, 'bold'), bg='gray20', fg='white', bd=12, relief=GROOVE)
headingLabel.pack(fill=X)

customer_detail_frame=LabelFrame(root, text='Customer Details', font=('times new roman', 15, 'bold'), fg='white',bd=12, relief=GROOVE, bg='gray20')
customer_detail_frame.pack(fill=X)

nameLabel=Label(customer_detail_frame, text='Name', font=('times new roman', 15, 'bold'), bg='gray20', fg='white')
nameLabel.grid(row=0, column=0, padx=20)

nameEntry=Entry(customer_detail_frame, font=('arial', 15), bd=7, width=18)
nameEntry.grid(row=0, column=1, padx=8)

phoneLabel=Label(customer_detail_frame, text='Phone Number', font=('times new roman', 15, 'bold'), bg='gray20', fg='white')
phoneLabel.grid(row=0, column=2, padx=20, pady=2 )

phoneEntry=Entry(customer_detail_frame, font=('arial', 15), bd=7, width=18)
phoneEntry.grid(row=0, column=3, padx=8)

billnumberLabel=Label(customer_detail_frame, text='Bill Number', font=('times new roman', 15, 'bold'), bg='gray20', fg='white')
billnumberLabel.grid(row=0, column=4, padx=20, pady=2 )

billnumberEntry=Entry(customer_detail_frame, font=('arial', 15), bd=7, width=18)
billnumberEntry.grid(row=0, column=5, padx=8)

searchButton=Button(customer_detail_frame, text='SEARCH', font=('arial', 12, 'bold'), bd=7, width=10, command=search_bill)
searchButton.grid(row=0, column=6, padx=20, pady=8)

productsFrame=Frame(root)
productsFrame.pack()

cosmeticsFrame=LabelFrame(productsFrame, text='Seafood', font=('times new roman', 15, 'bold'), fg='white',bd=12, relief=GROOVE, bg='gray20')
cosmeticsFrame.grid(row=0, column=0)

bathsoapLabel=Label(cosmeticsFrame, text='Mie', font=('times new roman', 15, 'bold'), bg='gray20', fg='white')
bathsoapLabel.grid(row=0, column=0, pady=9, padx=10, sticky='w')

bathsoapEntry=Entry(cosmeticsFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
bathsoapEntry.grid(row=0, column=1, pady=9, padx=10)
bathsoapEntry.insert(0,0)

sosisLabel=Label(cosmeticsFrame, text='Sosis', font=('times new roman', 15, 'bold'), bg='gray20', fg='white')
sosisLabel.grid(row=1, column=0, pady=9, padx=10)

sosisEntry=Entry(cosmeticsFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
sosisEntry.grid(row=1, column=1, pady=9, padx=10)
sosisEntry.insert(0,0)

baksoLabel=Label(cosmeticsFrame, text='Bakso', font=('times new roman', 15, 'bold'), bg='gray20', fg='white')
baksoLabel.grid(row=2, column=0, pady=9, padx=10, sticky='w  ')

baksoEntry=Entry(cosmeticsFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
baksoEntry.grid(row=2, column=1, pady=9, padx=10)
baksoEntry.insert(0,0)

kerupukLabel=Label(cosmeticsFrame, text='Kerupuk', font=('times new roman', 15, 'bold'), bg='gray20', fg='white')
kerupukLabel.grid(row=3, column=0, pady=9, padx=10, sticky='w')

kerupukEntry=Entry(cosmeticsFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
kerupukEntry.grid(row=3, column=1, pady=9, padx=10)
kerupukEntry.insert(0,0)

fishrollLabel=Label(cosmeticsFrame, text='Fish Roll', font=('times new roman', 15, 'bold'), bg='gray20', fg='white')
fishrollLabel.grid(row=4, column=0, pady=9, padx=10, sticky='w')

fishrollEntry=Entry(cosmeticsFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
fishrollEntry.grid(row=4, column=1, pady=9, padx=10)
fishrollEntry.insert(0,0)

dumplingLabel=Label(cosmeticsFrame, text='Dumpling', font=('times new roman', 15, 'bold'), bg='gray20', fg='white')
dumplingLabel.grid(row=5, column=0, pady=9, padx=10, sticky='w')

dumplingEntry=Entry(cosmeticsFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
dumplingEntry.grid(row=5, column=1, pady=9, padx=10)
dumplingEntry.insert(0,0)

groceryFrame=LabelFrame(productsFrame, text='Sayuran', font=('times new roman', 15, 'bold'), fg='white',bd=12, relief=GROOVE, bg='gray20')
groceryFrame.grid(row=0, column=1)

riceLabel=Label(groceryFrame, text='Kol', font=('times new roman', 15, 'bold'), bg='gray20', fg='white')
riceLabel.grid(row=0, column=0, pady=9, padx=10, sticky='w')

riceEntry=Entry(groceryFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
riceEntry.grid(row=0, column=1, pady=9, padx=10)
riceEntry.insert(0,0)

oilLabel=Label(groceryFrame, text='Sawi Putih', font=('times new roman', 15, 'bold'), bg='gray20', fg='white')
oilLabel.grid(row=1, column=0, pady=9, padx=10, sticky='w')

oilEntry=Entry(groceryFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
oilEntry.grid(row=1, column=1, pady=9, padx=10)
oilEntry.insert(0,0)

daalLabel=Label(groceryFrame, text='Sawi Hijau', font=('times new roman', 15, 'bold'), bg='gray20', fg='white')
daalLabel.grid(row=2, column=0, pady=9, padx=10, sticky='w')

daalEntry=Entry(groceryFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
daalEntry.grid(row=2, column=1, pady=9, padx=10)
daalEntry.insert(0,0)

wheatLabel=Label(groceryFrame, text='Jamur Kuping', font=('times new roman', 15, 'bold'), bg='gray20', fg='white')
wheatLabel.grid(row=3, column=0, pady=9, padx=10, sticky='w')

wheatEntry=Entry(groceryFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
wheatEntry.grid(row=3, column=1, pady=9, padx=10)
wheatEntry.insert(0,0)

sugarLabel=Label(groceryFrame, text='Jamur Enoki', font=('times new roman', 15, 'bold'), bg='gray20', fg='white')
sugarLabel.grid(row=4, column=0, pady=9, padx=10, sticky='w')

sugarEntry=Entry(groceryFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
sugarEntry.grid(row=4, column=1, pady=9, padx=10)
sugarEntry.insert(0,0)

teaLabel=Label(groceryFrame, text='Kangkung', font=('times new roman', 15, 'bold'), bg='gray20', fg='white')
teaLabel.grid(row=5, column=0, pady=9, padx=10, sticky='w')

teaEntry=Entry(groceryFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
teaEntry.grid(row=5, column=1, pady=9, padx=10)
teaEntry.insert(0,0)

drinksFrame=LabelFrame(productsFrame, text='Minuman', font=('times new roman', 15, 'bold'), fg='white',bd=12, relief=GROOVE, bg='gray20')
drinksFrame.grid(row=0, column=2)

maazaLabel=Label(drinksFrame, text='Air Putih', font=('times new roman', 15, 'bold'), bg='gray20', fg='white')
maazaLabel.grid(row=0, column=0, pady=9, padx=10, sticky='w')

maazaEntry=Entry(drinksFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
maazaEntry.grid(row=0, column=1, pady=9, padx=10)
maazaEntry.insert(0,0)

pepsiLabel=Label(drinksFrame, text='Es Teh', font=('times new roman', 15, 'bold'), bg='gray20', fg='white')
pepsiLabel.grid(row=1, column=0, pady=9, padx=10, sticky='w')

pepsiEntry=Entry(drinksFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
pepsiEntry.grid(row=1, column=1, pady=9, padx=10)
pepsiEntry.insert(0,0)

spriteLabel=Label(drinksFrame, text='Es Kopi', font=('times new roman', 15, 'bold'), bg='gray20', fg='white')
spriteLabel.grid(row=2, column=0, pady=9, padx=10, sticky='w')

spriteEntry=Entry(drinksFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
spriteEntry.grid(row=2, column=1, pady=9, padx=10)
spriteEntry.insert(0,0)

dewLabel=Label(drinksFrame, text='Teh Tarik', font=('times new roman', 15, 'bold'), bg='gray20', fg='white')
dewLabel.grid(row=3, column=0, pady=9, padx=10, sticky='w')

dewEntry=Entry(drinksFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
dewEntry.grid(row=3, column=1, pady=9, padx=10)
dewEntry.insert(0,0)

frootiLabel=Label(drinksFrame, text='Thai Tea', font=('times new roman', 15, 'bold'), bg='gray20', fg='white')
frootiLabel.grid(row=4, column=0, pady=9, padx=10, sticky='w')

frootiEntry=Entry(drinksFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
frootiEntry.grid(row=4, column=1, pady=9, padx=10)
frootiEntry.insert(0,0)

cocacolaLabel=Label(drinksFrame, text='Es Jeruk', font=('times new roman', 15, 'bold'), bg='gray20', fg='white')
cocacolaLabel.grid(row=5, column=0, pady=9, padx=10, sticky='w')

cocacolaEntry=Entry(drinksFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
cocacolaEntry.grid(row=5, column=1, pady=9, padx=10)
cocacolaEntry.insert(0,0)

billFrame=Frame(productsFrame, bd=8, relief=GROOVE)
billFrame.grid(row=0, column=3, padx=10)

billareaLabel=Label(billFrame, text='Label Area', font=('times new roma', 15, 'bold'), bd=7, relief=GROOVE)
billareaLabel.pack()

scrollbar=Scrollbar(billFrame, orient=VERTICAL)
scrollbar.pack(side=RIGHT, fill=Y)
textarea=Text(billFrame, height=18, width=55, yscrollcommand=scrollbar.set)
textarea.pack()
scrollbar.config(command=textarea.yview)

billmenuFrame=LabelFrame(root, text='Bill Menu', font=('times new roman', 15, 'bold'), fg='white',bd=12, relief=GROOVE, bg='gray20')
billmenuFrame.pack()

cosmeticpriceLabel=Label(billmenuFrame, text='Seafood', font=('times new roman', 14, 'bold'), bg='gray20', fg='white')
cosmeticpriceLabel.grid(row=0, column=0, pady=6, padx=10, sticky='w')

cosmeticpriceEntry=Entry(billmenuFrame, font=('times new roman', 14, 'bold'), width=10, bd=5)
cosmeticpriceEntry.grid(row=0, column=1, pady=6, padx=10)

grocerypriceLabel=Label(billmenuFrame, text='Sayuran', font=('times new roman', 14, 'bold'), bg='gray20', fg='white')
grocerypriceLabel.grid(row=1, column=0, pady=6, padx=10, sticky='w')

grocerypriceEntry=Entry(billmenuFrame, font=('times new roman', 14, 'bold'), width=10, bd=5)
grocerypriceEntry.grid(row=1, column=1, pady=6, padx=10)

drinkspriceLabel=Label(billmenuFrame, text='Minuman', font=('times new roman', 14, 'bold'), bg='gray20', fg='white')
drinkspriceLabel.grid(row=2, column=0, pady=6, padx=10, sticky='w')

drinkspriceEntry=Entry(billmenuFrame, font=('times new roman', 14, 'bold'), width=10, bd=5)
drinkspriceEntry.grid(row=2, column=1, pady=6, padx=10)

cosmetictaxLabel=Label(billmenuFrame, text='Seafood', font=('times new roman', 14, 'bold'), bg='gray20', fg='white')
cosmetictaxLabel.grid(row=0, column=2, pady=6, padx=10, sticky='w')

cosmetictaxEntry=Entry(billmenuFrame, font=('times new roman', 14, 'bold'), width=10, bd=5)
cosmetictaxEntry.grid(row=0, column=3, pady=6, padx=10)

grocerytaxLabel=Label(billmenuFrame, text='Sayuran', font=('times new roman', 14, 'bold'), bg='gray20', fg='white')
grocerytaxLabel.grid(row=1, column=2, pady=6, padx=10, sticky='w')

grocerytaxEntry=Entry(billmenuFrame, font=('times new roman', 14, 'bold'), width=10, bd=5)
grocerytaxEntry.grid(row=1, column=3, pady=6, padx=10)

drinkstaxLabel=Label(billmenuFrame, text='Minuman', font=('times new roman', 14, 'bold'), bg='gray20', fg='white')
drinkstaxLabel.grid(row=2, column=2, pady=6, padx=10, sticky='w')

drinkstaxEntry=Entry(billmenuFrame, font=('times new roman', 14, 'bold'), width=10, bd=5)
drinkstaxEntry.grid(row=2, column=3, pady=6, padx=10)

buttonFrame=Frame(billmenuFrame, bd=8, relief=GROOVE)
buttonFrame.grid(row=0, column=4, rowspan=3)

totalButton=Button(buttonFrame, text='Total', font=('arial', 16, 'bold'), bg='gray20', fg='white', bd=5, width=14, pady=10, command=total)
totalButton.grid(row=0, column=0, pady=20,)

billButton=Button(buttonFrame, text='Bill', font=('arial', 16, 'bold'), bg='gray20', fg='white', bd=5, width=14, pady=10, command=bill_area)
billButton.grid(row=0, column=1, pady=20)

printButton=Button(buttonFrame, text='Print', font=('arial', 16, 'bold'), bg='gray20', fg='white', bd=5, width=14, pady=10, command=print_bill)
printButton.grid(row=0, column=3, pady=20)

clearButton=Button(buttonFrame, text='Clear', font=('arial', 16, 'bold'), bg='gray20', fg='white', bd=5, width=15, pady=10)
clearButton.grid(row=0, column=4, pady=20)

root.mainloop()     