'''
import os
choice = 0
filename = ''

def menu() :
    global choice
    print('menu\n 1.opencalculate \n 2.open notepad\n 3.exit')
    choice = input('select menu')


def opennotepad():
    filename = 'C:\\Windows\\SysWOW64\\notepad.exe'
    print('memorandum writing %s' %filename)
    os.system(filename)

def opencalculator() :
    filename = 'C:\\Windows\\SysWOW64\\calc.exe'
    print('Calculate Number %s' %filename)
    os.system(filename)

while True :
    menu()
    if choice == '1':
        opencalculator()
    elif choice == '2':
        opennotepad()
    else:
        break
'''
'''def Introduce(arg1, arg2 = 'com',arg3 = 'ed',arg4= 'kku'):
    print("Hello,I am "+arg1+","+arg2+" "+arg3+" "+arg4)

Introduce("Python")
Introduce(arg1 = "Python")
Introduce(arg1 = "Python" , arg3="Sci")
Introduce("Python",arg4="CMU")'''

'''
print("โปรมเเกรมร้านค้าอุปกรณ์บาสเกตบอลออนไลน์\n","-"*35)

product = ['1.รองเท้าLBJ','2.เสื้อLaker','3.ถุงเท้าAdidas','4.ปลอกเเขน','5.สายรัดข้อมือ']

def menu():
    global choice
    print("menu\n 1.แสดงรายการสินค้า\n 2.หยิบสินค้าเข้าตะกร้า\n 3.แสดงรายจำนวนและราคาของสินค้าที่หยิบ\n 4.หยิบสินค้าออกจากตะกร้า\n 5.ปิดโปรเเกรม")
    choice = input("select menu : ")

def Showproducts():
    print("แสดงรายการสินค้า\n","-"*20)
    print("  1.รองเท้าLBJ ราคา 4000 บาท\n  2.เสื้อLaker ราคา 1,000 บาท\n  3.ถุงเท้าAdidas ราคา 300 บาท\n  4.ปลอกเเขน ราคา 300 บาท\n  5.สายรัดข้อมือ ราคา 200 บาท")

def Select_a_product():
    print("หยิบสินค้าเข้าตะกร้า")

def Displays():
    print("แสดงรายจำนวนและราคาของสินค้าที่หยิบ")


while True :
    menu()
    if choice == '1':
        Showproducts()
    elif choice == '2':
        Select_a_product()
    elif choice == '3':
        Displays()
    else:
        break #โค้ดไม่เสร็จ
'''
'''
from os import system, name
shop_list=[]
amount=[0,0,0,0,0]
price=[4000,1000,300,300,200]
def clear():
    if name == 'nt': 
        _ = system('cls')
    else: 
        _ = system('clear')
def out_products():
    n=0
    while(True):
        print("\tเเสดงรายการสินค้า")
        for i in shop_list:
            n+=1
            print("\t"+str(n)+"."+i)
        n=0
        c=int(input("เลือกลำดับสินค้าที่จะหยิบออก หรือพิมพ์ 6 เพื่อออก"))
        try:
            if c==1:
               amount[0]-=1
            elif c==2:
               amount[1]-=1
            elif c==3:
               amount[2]-=1
            elif c==4:
               amount[3]-=1
            elif c==5:
               amount[4]-=1
            elif c==6:
                break
        except:
            print("กรุณากรอกสินค้าให้ถูกต้อง")
def List_products():
    print("\tรายการสินค้า")
    print("\t1.รองเท้าLBJ ราคา 4000 บาท\n\t2.เสื้อLaker ราคา 1,000 บาท\n\t3.ถุงเท้าAdidas ราคา 300 บาท\n\t4.ปลอกเเขน ราคา 300 บาท\n\t5.สายรัดข้อมือ ราคา 200 บาท")
def pick_products():
    c=0
    while(True):
        print("  1.รองเท้าLBJ\n  2.เสื้อLaker\n  3.ถุงเท้าAdidas\n  4.ปลอกเเขน\n  5.สายรัดข้อมือ\n  6.ออกจากฟังก์ชัน")
        c=(input("เลือกหยิบสินค้าตามหมายเลข : "))
        try:
            if int(c)==1 or c=="1":
                shop_list.append("รองเท้าLBJ")
                amount[0]+=1
            elif int(c)==2 or c=="2":
                shop_list.append("เสื้อLaker")
                amount[1]+=1
            elif int(c)==3 or c=="3":
                shop_list.append("ถุงเท้าAdidas")
                amount[2]+=1
            elif int(c)==4 or c=="4":
                shop_list.append("ปลอกเเขน")
                amount[3]+=1
            elif int(c)==5 or c=="5":
                shop_list.append("สายรัดข้อมือ")
                amount[4]+=1
            elif int(c)==6 or c=="6":
                break
            else:
                print("กรุณากรอกหมายเลขให้ถูกต้อง")
        except:
            print("กรุณากรอกหมายเลขให้ถูกต้อง")
            pass
def Show_products():
    amounttt=amount[0]+amount[1]+amount[2]+amount[3]+amount[4]
    pricett=amount[0]*4000+amount[1]*1000+amount[2]*300+amount[3]*300+amount[4]*200
    print("")
    print('{0:_<10}{0:_<10}'.format("","สินค้าที่คุณหยิบมีดังนี้"))
    print('{0:.<6}{1}{0:.<6}{2}{0:.<6}{3}{0:.<7}'.format("","สินค้า","จำนวน","ราคา"))
    print("{0:_<38}".format(""))
    if amount[0]!=0:
        print('{0:.<6}{1}{0:.<6}{2}{0:.<9}{3}{0:.<10}'.format("","รองเท้าLBJ",str(amount[0]),str(amount[0]*4000)))
    if amount[1]!=0:
        print('{0:.<6}{1}{0:.<6}{2}{0:.<9}{3}{0:.<10}'.format("","เสื้อLaker",str(amount[1]),str(amount[1]*1000)))
    if amount[2]!=0:
        print('{0:.<6}{1}{0:.<6}{2}{0:.<9}{3}{0:.<10}'.format("","ถุงเท้าAdidas",str(amount[2]),str(amount[2]*300)))
    if amount[3]!=0:
        print('{0:.<6}{1}{0:.<6}{2}{0:.<9}{3}{0:.<10}'.format("","ปลอกเเขน",str(amount[3]),str(amount[3]*300)))
    if amount[4]!=0:
        print('{0:.<6}{1}{0:.<6}{2}{0:.<9}{3}{0:.<10}'.format("","สายรัดข้อมือ",str(amount[4]),str(amount[4]*200)))
    print("{0:_<38}".format(""))
    print('{0:.<6}{1}{0:.<6}{2}{0:.<9}{3}{0:.<10}'.format("","รวม",str(amounttt),str(pricett)))
    print("")
print("\tโปรมเเกรมร้านค้าอุปกรณ์บาสเกตบอลออนไลน์\n","\t-"*35)
while(True):
    print(" 1.แสดงรายการสินค้า\n 2.หยิบสินค้าเข้าตะกร้า\n 3.แสดงรายจำนวนและราคาของสินค้าที่หยิบ\n 4.หยิบสินค้าออกจากตะกร้า\n 5.ปิดโปรเเกรม")
    print("")
    ch=input("กรุณาเลือกทำรายการ")
    if ch == "1":
        clear()
        List_products()
    elif ch == "2":
        clear()
        pick_products()
    elif ch == "3":
        clear()
        Show_products()
    elif ch == "4":
        clear()        
        out_products()
    elif ch == "5":
        ch=input("ต้องการออกจากโปรแกรม ใช่หรือไม่ y/n: ")
        if ch == 'y':
            print('ออกจากโปรแกรมเรียบร้อย')
            break
        elif ch == 'n':
            continue 
       '''

'''
Dictionaly = {}
i=0
def menu():
    global choice
    print('\nพจนานุกรม\n1) เพิ่มคำศัพท์\n2) แสดงคำศัพท์\n3) ลบคำศัพท์\n4) ออกจากโปรแกรม')
    choice = input('input choice : ')
def addword():
    word = input('พิมพ์คำศัพท์   : ')
    types = input('ชนิดของคำศัพท์(n.,v.,adj.,adv.): ')
    mean = input('ความหมาย  : ')
    Dictionaly[word] = '{0:<15}{1:<15}'.format(types,mean)
    print('เพิ่มคำศัพท์เรียบร้อย')
def showwords():
    print('-'*43,'\n\tมีคำศัพท์ทั้งหมด',i,'คำ\n'+'-'*43)
    print('{0:<15}{1:<15}{2:<15}'.format('คำศัพท์','ประเภท','ความหมาย'))
    for k,v in Dictionaly.items():
        print('{0:<15}{1:<15}'.format(k,v))
def deleteword():
    remove = input('พิมพ์คำศัพท์ที่ต้องการลบ : ')
    x = input('ต้องการลบ '+remove+' ใช่หรือไม่ (y/n) : ')
    if x == 'y':
        Dictionaly.pop(remove)
        print('ลบ',remove,'เรียบร้อยเเล้ว')
    elif x == 'n':
        print('')
while True:
    menu()
    if choice == '1':
        addword()
        i+=1
    elif choice == '2':
        showwords()
    elif choice == '3':
        deleteword()
        i-=1
    else:
        exitt = input('ต้องการออกจากโปรเเกรมใช่หรือไม่ y/n : ')
        if exitt == 'y':
            print('ออกจากโปรแกรมเรียบร้อยแล้ว')
            break
'''
