a3 = int(input("Введите число сотен первого числа: "))
a2 = int(input("Введите число десятков первого числа: "))
a1 = int(input("Введите число едениц первого числа: "))
b2 = int(input("Введите число десятков второго числа: "))
b1 = int(input("Введите число едениц второго числа: "))

print(("Число сотен итогового числа: "),(a3 + (a2+b2)//10))
print (("Число десятков итогового числа: "),((a2 +b2)%10 + (a1+b1)//10))
print (("Число едениц итогового числа: "),((a1+b1)%10))



