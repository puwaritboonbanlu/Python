'''a=input("input first number :")
b=input("input second number :")
print((a),"=",(b),":",a==b)
print((a),"<",(b),":",a<b)
print((a),">",(b),":",a>b)'''

'''print(bool("Hello"))
print(bool(""))'''

'''a = 60 #30=0011 1100
b = 13 #13=0000 1101
c = 0

c = a & b #12=0000 1100
print(c)

c = a | b #61=0011 1101
print(c)

c = a ^ b #49 =0011 0001
print(c)

c = ~ a #-61 = 1100 0011
print(c)

c = a << 2 # 240= 1111 0000
print(c)

c = a >> 2 
print(c)'''

'''x = input("number of Day-->")
print("Hour =",int(x)*24)
print("minutes =",int(x)*1440)
print("seconds =",int(x)*86400)'''

'''friend = ["jan","cream","phu","bam","aom","pee","bas","kong","da","james"]
friend.append("dome")
friend.append("poondang")
friend.insert(1,"csa")
friend.insert(8,"ped")
friend.remove("aom")
friend.pop(3)
del friend[7]
friend.clear()
print(friend)
del friend'''

'''animal={"cat","dog","rat","pig","ant"}
animal.add("monkey")
animal.update(["python","capibara","spider","wombat","penguin","crocodile"])
print(animal)'''

'''print("++++++++++++++++++++++++++++++\n     โปรแกรมหยิบสินค้าในตาราง \n++++++++++++++++++++++++++++++")
a=input("\nหยิบสินค้าชิ้นที่ 1-->")
b=input("หยิบสินค้าชิ้นที่ 2-->")
c=input("หยิบสินค้าชิ้นที่ 3-->")
d=input("หยิบสินค้าชิ้นที่ 4-->")
e=input("หยิบสินค้าชิ้นที่ 5-->")
product=[a,b,c,d,e]
print("++++++++++++++++++++++++++++++\n")  
print("สินค้าชิ้นที่ 1.",product[0])
print("สินค้าชิ้นที่ 2.",product[1])
print("สินค้าชิ้นที่ 3.",product[2])
print("สินค้าชิ้นที่ 4.",product[3])
print("สินค้าชิ้นที่ 5.",product[4])'''

'''print("      โปรเเกรมคำนาณค่าผ่านทางมอเตอร์เวย์       ")
print("---------------------------------------\n")
print("รถยนต์ 4 ล้อ กด 1")
print("รถยนต์ 6 ล้อ กด 2")
print("รถยนต์มากกว่า 6 ล้อ กด 3\n")
car1_list = ["ลาดกระบัง-->บางบ่อ : 25บาท","ลาดกระบัง-->บางประกง : 30บาท","ลาดกระบัง-->พนัสนิคม : 45บาท","ลาดกระบัง-->บ้านบึง : 55บาท","ลาดกระบัง-->บางพระ : 60บาท"]
car2_list = ["ลาดกระบัง-->บางบ่อ : 40บาท","ลาดกระบัง-->บางประกง : 45บาท","ลาดกระบัง-->พนัสนิคม : 75บาท","ลาดกระบัง-->บ้านบึง : 90บาท","ลาดกระบัง-->บางพระ : 100บาท"]
car3_list = ["ลาดกระบัง-->บางบ่อ : 70บาท","ลาดกระบัง-->บางประกง : 70บาท","ลาดกระบัง-->พนัสนิคม : 110บาท","ลาดกระบัง-->บ้านบึง : 130บาท","ลาดกระบัง-->บางพระ : 140บาท"]
car = int(input("เลือกประเภทยานพาหนะ :"))
if car == 1 :
    print("ค่าบริการรถยนต์ 4 ล้อ")
    for x in car1_list:
        print("\n",x)
elif car == 2 :
    print("ค่าบริการรถยนต์ 6 ล้อ")
    for x in car2_list:
        print("\n",x)
elif car == 3 :
    print("ค่าบริการรถยนต์มากกว่า 6 ล้อ")
    for x in car2_list:
        print("\n",x)'''