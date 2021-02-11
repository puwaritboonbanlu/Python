'''import os
shop_list=[]
amount = [0,0,0,0]
name_list = ['รองเท้านันยาง','ถุงเท้านันยาง','หมวกนันยาง','เสื้อยืดนันยาง']
price_list = [400,50,100,300]
class market :
    def list_def(self):
        for x in range(0,len(name_list)):
            print(x+1,name_list[x],price_list[x],'บาท')
    def choose(self):
        print('+++++++++++++++ นันยางช็อป +++++++++++++++')
        print('\tแสดงรายการสินค้า[a]\n\tเพิ่มรายการสินค้า[s]\n\tออกจากระบบ[x]')
    def input_choise(self):
        global choise
        choise = input('กรุณาเลือกคำสั่ง : ')
    def Show_products():
        amounttt=amount[0]+amount[1]+amount[2]+amount[3]+amount[4]
        pricett=amount[0]*4000+amount[1]*1000+amount[2]*300+amount[3]*300+amount[4]*200
        print("")
        print('{0:_<10}{0:_<10}'.format("","สินค้าที่คุณหยิบมีดังนี้"))
        print('{0:.<6}{1}{0:.<6}{2}{0:.<6}{3}{0:.<7}'.format("","สินค้า","จำนวน","ราคา"))
        print("{0:_<38}".format(""))
        if amount[0]!=0:
            print('{0:.<6}{1}{0:.<6}{2}{0:.<9}{3}{0:.<10}'.format("","รองเท้านันยาง",str(amount[0]),str(amount[0]*400)))
        if amount[1]!=0:
            print('{0:.<6}{1}{0:.<6}{2}{0:.<9}{3}{0:.<10}'.format("","ถุงเท้านันยาง",str(amount[1]),str(amount[1]*50)))
        if amount[2]!=0:
            print('{0:.<6}{1}{0:.<6}{2}{0:.<9}{3}{0:.<10}'.format("","หมวกนันยาง",str(amount[2]),str(amount[2]*100)))
        if amount[3]!=0:
            print('{0:.<6}{1}{0:.<6}{2}{0:.<9}{3}{0:.<10}'.format("","้เสื้อยืดนันยาง",str(amount[3]),str(amount[3]*300)))
        print("{0:_<38}".format(""))
        print('{0:.<6}{1}{0:.<6}{2}{0:.<9}{3}{0:.<10}'.format("","รวม",str(amounttt),str(pricett)))
        print("")
    print("\tโปรมเเกรมร้านค้าอุปกรณ์บาสเกตบอลออนไลน์\n","\t-"*35)
    def pick_products():
        c=0
        while(True):
            print("  1.รองเท้านันยาง\n  2.ถุงเท้านันยาง\n  3.หมวกนันยาง\n  4.เสื้อยืดนันยาง\n  6.ออกจากฟังก์ชัน")
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
                elif int(c)==6 or c=="6":
                    break
                else:
                    print("กรุณากรอกหมายเลขให้ถูกต้อง")
                add = input ('ต้องการเพิ่มสินค้าอีกหรือไม่ [y/n] :')
                if add == 'n' :
                    break
                elif add == 'y' :
                    continue
    while True:
        x = market()
        x.choose()
        x.input_choise()
        if choise == 'a' :
            os.system('cls')
            print('กรุณาเลือกคำสั่ง : ',choise)
            x.list_def()
        if choise == 's' :
            print('กรุณาเลือกคำสั่ง : ',choise)
            x.add_list()
        if choise == 'x' :
            os.system('cls')
            print('กรุณาเลือกคำสั่ง : ',choise)
            close = input('ต้องการปิดโปรแกรมหรือไม่ [y/n] : ')
            if close == 'n' :
                os.system('cls')
            if close == 'y' :
                os.system('cls')
                print('ปิดโปรแกรม')
                break'''