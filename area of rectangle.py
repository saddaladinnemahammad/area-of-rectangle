a=int(input())
b=int(input())
c=int(input())
s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**0.5
print('%.f'%area)


DECIMAL TO OCTAL

def decimal_to_octal(decimal):
    octal = ""
    while decimal > 0:
        remainder = decimal % 8  
        octal = str(remainder) + octal  
        decimal = decimal // 8
    return octal
decimal = int(input())
octal = decimal_to_octal(decimal)
print(octal)


GLOSSARY SALARY

t=int(input())
a=(40/100)*t
b=(20/100)*t
c=t+a+b
print("%.2f"%c)


BANK NODES

t=int(input())
h=t//100
print(f'100-{h}')
t=t-(h*100)
f=t//50
print(f'50-{f}')
t=t-(f*50)
twenty=t//20
print(f'20-{twenty}')
t=t-(twenty*20)
ten=t//10
print(f'10-{ten}')
t=t-(ten*10)
five=t//5
print(f'5-{five}')
t=t-(five*5)
two=t//2
print(f'2-{two}')
t=t-(two*2)
one=t//1
print(f'1-{one}')



SIMPLE INTREST


p=float(input())
r=float(input())
t=float(input())
simple=(p*r*t)/100
print('%.1f'%simple)
