# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()
name=0
sp=['яблоко',"банан", "киви", "арбуз"]
for i in sp :
  name+=1
  print("{0}. {1} !".format(str(name), i))

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

sp2=['яблоко',"2", "3", "4"]
for q in sp.copy() :
  print(q)
  for w in sp2.copy():
    if w==q :
      sp.remove(q)      
print(sp)

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

sp4=[]
sp3=[1,2,3,4,5,6,7,8,9,10,11,12,13,14]
for u in sp3 :
  if (u%2)==0 :
    u=u/4
    sp4.append(u)
  else :
    u=u*2
    sp4.append(u)
print(sp4)
