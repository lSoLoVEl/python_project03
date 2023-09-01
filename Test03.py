#ให้ทำโปรแกรมป้อนจำนวนเงิน และจำนวนคนทางแป้นพิมพ์ และแสดงผลออกมาว่า
#จำนวนเงิน ???? บาท จำนวนคน ???? คน ต้องหารกันคนล้ะ ???? บาท
#ให้แสดงผลโดยใช้ print ทั้ง5แบบ
money = (input('โปรดใส่จำนวนเงิน : '))
person = input('โปรดใส่จำนวนคน : ')
print('------------------------------')
print(f'จำนวนเงิน {float(money):.2f} บาท จำนวนคน {person} คน ต้องหารกันคนละ {float(money)/int(person):.2f}บาท')
print('จำนวนเงิน',f'{float(money):,.2f},'บาท จำนวนคน', person ,'คน ต้องหารกันคนละ',f'{float(money)/int(person):.2f},'บาท')
print('จำนวนเงิน'+' ' +str(round(float(money),2))+ 'บาท จำนวนคน'+person+ 'คน ต้องหารกันคนละ'+ (float(money)/int(person),)+'บาท')
print('จำนวนเงิน {:.2f} บาท จำนวนคน {} คน ต้องหารกันคนละ {:.2f} บาท'.format(float(money),person,(float(money)/int(person))))
print('จำนวนเงิน %.2f บาท จำนวนคน %s คน ต้องหารกันคนละ %.2f บาท'%(float(money),person,(float(money)/int(person))))

