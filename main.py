#1
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(i)

#2

cem = 0

while True:
    n = int(input("Ədəd daxil et: "))
    if n < 0:
        break
    if n > 0 and n % 2 == 1:
        cem += n

print("Cəm:", cem)


#3

for i in range(1, 51):
    if i % 4 == 0 and i % 6 != 0:
        print(i)

#4

say = 0

while True:
    n = int(input("Ədəd daxil et: "))
    if n == 0:
        break
    if 10 < n < 100 and n % 2 == 0:
        say += 1

print("Cüt ədədlərin sayı:", say)

#5

cem = 0

for i in range(1, 101):
    if i % 3 == 0 and i % 10 != 3:
        print(i)
        cem += i
        if cem > 500:
            break

#6

say = 0
ardicil = 0

while True:
    n = int(input("Ədəd daxil et: "))

    if n % 5 == 0 and n % 7 == 0:
        say += 1
        ardicil += 1
    else:
        ardicil = 0

    if ardicil == 3:
        break

print("Belə ədədlərin sayı:", say)


#7

for i in range(1, 201):
    if "4" not in str(i):
        if (i % 2 == 0 and i % 3 == 0) or (i % 2 == 1 and i % 11 == 0):
            print(i)


#9

n = int(input("Neçə ədəd? "))
secilen = []

for _ in range(n):
    a = int(input("Ədəd daxil et: "))
    if a > 0 and (a % 2 == 0 or a % 3 == 0) and "0" not in str(a):
        secilen.append(a)

print("Uyğun ədədlər:", secilen)

#10

say = 0
son3 = []

while True:
    n = int(input("Ədəd: "))
    say += 1
    son3.append(n)

    if len(son3) > 3:
        son3.pop(0)

    if len(son3) == 3 and sum(son3) > 100:
        break

print("Daxil edilən ədədlərin sayı:", say)

#11

uygun = []
sira = 0

while True:
    n = int(input("Ədəd: "))
    if n > 0 and n % 2 == 1 and n % 3 == 0:
        uygun.append(n)
        sira = 0
    else:
        sira += 1
    
    if sira == 2:
        break

print("Uyğun ədədlər:", uygun)
