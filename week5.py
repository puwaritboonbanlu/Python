'''class nisit :
    def __init__(self,name,Student_code,sex,year,faculty,department,province) :
        self.name = name
        self.Student_code = Student_code
        self.sex = sex
        self.year = year
        self.faculty = faculty
        self.department = department
        self.province = province

    def shownisit(self) :
        print('{0:-<20}{1:-<20}'.format("","เเนะนำตัว"))
        print("สวัสดีครับ")
        print("ชื่อ-นามสกุล : ",self.name)
        print("รหัสนักศึกษา : ",self.Student_code)
        print("เพศ : ",self.sex)
        print("ชั้นปีการศึกษา : ",self.year)
        print("คณะ : ",self.faculty)
        print("สาขาวิชา : ",self.department)
        print("ภูมิลำเนา : ",self.province)

a = str(input("ชื่อ-นามสกุล : "))
b = str(input("รหัสนักศึกษา : ")) 
c = str(input("เพศ : ")) 
d = str(input("ชั้นปีการศึกษา : ")) 
e = str(input("คณะ : ")) 
f = str(input("สาขาวิชา : ")) 
g = str(input("ภูมิลำเนา : "))

x = nisit(a,b,c,d,e,f,g)
x.shownisit()'''

import os
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
    def add_list(self):
        while True:
            print('เพิ่มรายการสินค้า หากต้องการ กรอก exit')
            add_name = input('เพิ่มชื่อสินค้า : ')
            if add_name == 'exit':
                break
            else : 
                add_price = input('เพิ่มราคาสินค้า :')
                name_list.append(add_name)
                price_list.append(add_price)
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
            break