S=abs(int(input("Введите кол-во элементов списка:")))
num=input("Введите числа через пробел:").split()
num=list(num)
for i in range(len(num)):
 num[i]=int(num[i])
print(list(num))
num1=len(list(num))
print(num1)
if num1!=S:
 print("Кол-во элементов не соответтвует заданным параметрам")
elif num1==S:
 print("Кол-во элементов соответтвует заданным параметрам")
 for i in range(len(num)):
  num[i]=int(num[i])
x=int(input("Введите число x:"))
min = abs(x - num[0])
index = 0
for i in range(1, S):
        count = abs(x - num[i])
        if count < min:
            min = count
            index = i
print(f'Число {num[index]} в списке S наиболее близко по величине к числу {x}, их разница составляет {abs(x - num[index])}')
