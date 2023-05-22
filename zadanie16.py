S=abs(int(input("Введите кол-во элементов списка:")))
num=input("Введите числа:").split()
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
res=0
if list(num)[i]==x:
 res +=1
 print(f'Число {x} встречается в списке {res} раз.')
else:
   print("Такого числа нет в списке")