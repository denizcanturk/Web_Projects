a = 3.3423423424234234242
print(9//6)
print(9 % 6)
print((9 % 6) % 2)
print(2**3**2)
print(2**9)

idx = 1
while idx < 9:
    print(idx*"*")
    idx+=1
    
print("+"+10*"-" + "+")
print("|" + " " *10 + "|")
print("+"+10*"-" + "+")

print(str(a) * 5)
print(range(1,4))
b= "_asdlfkjfl_"
c="_sdfsdfsf_"
print("Merhaba" + b + c)
print("Merhaba" + b)
print("Merhaba", a, b)
print(f"Merhaba {a} ve Merhaba {b}")
g = 81
d = 3
e = a / 3
f = g // 3
print(type(a))
print(type(d))
print(type(e))
print(type(f))
print(f)
h = g / d
print(type(h))
print(h)
print(a*d)

flt = 23.1415926
kInt = 11
bInt = 1234

bolmeSonucuF_I = flt / kInt

bolmeSonucu_kI = bInt / kInt

bolumb_kI = bInt // kInt


print(bolmeSonucuF_I, type(bolmeSonucuF_I))
print(bolmeSonucu_kI, type(bolmeSonucu_kI))
print(int(bolmeSonucu_kI), type(bolmeSonucu_kI))
print(bolumb_kI, type (bolumb_kI))

maas = float(input("Maas miktarınızı giriniz : "))
cocukSayisi = int(input("Kac Cocugunuz var : "))

if cocukSayisi == 1 :
	maas *= 1.05
elif cocukSayisi == 2 : 
	maas *= 1.1
else:
	maas *=1.15
	
print("Maasınız son miktarı : " + str(maas))

isim = "Deniz CANTÜRK"

uzunluk = len(isim)

for i in range(0,uzunluk):
    print(isim[i], end=".")

print()

print(isim[0])

for i in range(0,5):
    print(i)
    
a = "4.5"
print(type(a))
print(int(float(a)))

a = 13.949999999999999
#format(a, '.2f')
print(f"{a:.4f}")
print(a)

sequence = [1,2,8,100,200,'datacamp','tutorial']

for i in sequence:
    print(i)
    
for i in range(len(sequence)):
    print(sequence[i])
    
for i in range(4,100,5):
    print(i, end=" ")
print()

a = [1,2,3,4,5]
b = iter(a)
while True:
	    try:
	        k = next(b)
	    except StopIteration:
	       print("Sonuna Geldi")
	       break
	    print(k
     
isim = 45852

for i in isim:
    print(i)
    
data = [5, 6, 12, 104, 204, "Python", "Dersim"]

sayac = 0

for i in range(len(data)):
	if data[i] % 2 == 0:
		sayac +=1

print(sayac)

for I in "Python":
	print(I) 
 
 
data = [5, 6, 12, 104, 204, "Python", "Dersim"]
for i in data:
	print(i)