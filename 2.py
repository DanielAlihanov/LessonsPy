# Задача-1: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользоваться данным ресурсом можно только с 18 лет"

vzrst = int(input())
vzrst = vzrst - 18
if vzrst > 0:
  print("Василий на " + str(vzrst) + " года/лет больше 18")
elif vzrst < 0:
  print("Василий на " + str(-vzrst) + " года/лет меньше 18")
else:
  print("Вам 18 лет")

# Задача-2: Напишите программу, которая спрашивает "Четные или нечетные?", в зависимости от ответа,
# используя цикл с предусловием while или for in
# вывести в одну строку через пробел соотвествующие числа от 0 до 20
# Пример работы:
# $ "Четные или нечетные?"
# четные
# 0 2 4 6 8 10 12 14 16 18 20
# $ "Четные или нечетные?"
# нечетные
# 1 3 5 7 9 11 13 15 17 19
# $ "Четные или нечетные?"
# qwerty (или любая другая строка)
# Я не понимаю, что вы от меня хотите...

num1 = "Нечетные"
num2 ="Четные"
vv=str(input(num2+" или "+num1+"?"))
l=list(range(0,21,2))
p=list(range(1,20,2))
every_0=""
a=0

while a==0 : 
 if vv.lower()==num1.lower():
  print(vv.lower()+' '+num1.lower())
  for every in p :
   every_0=every_0+str(every) + " "
  print(every_0)
  break
  #a=a+1
 elif vv.lower()==num2.lower() :
  for every in l :
   every_0=every_0+str(every) + " "
  print(every_0)
  break
 vv=str(input("Я не понимаю, что вы от меня хотите..." + "Рано или поздно вы должны ввести  "+'"'+num2+'"'+" или "+'"'+num1+'"'+"?"))

# Задача-3: Дано произвольное целое число, вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании и понимании решите задачу с применением цикла for.

num = int(input("Введите число"))
num=str(num)
big=0

for i in num :
 i=int(i)
 if i>big :
  big=i
print(str(big))