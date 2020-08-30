# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами. 
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]
sp=[1, 2, 4, 0]
sp2=[]

for i in sp[:]:
  i=i**2
  sp2.append(i)
print(sp2)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.
#V1
fruit1 = ["apple", "banana", "watermelon", "orange"]
fruit2 = ["peach", "lemon", "apple", "pear" ,"melon", "banana"]
FRUIT= list(set(fruit1) & set(fruit2))
print(FRUIT)

#V2
fruit3=[]
for i in fruit1:
  for q in fruit2:
    if q==i:
      fruit3.append(i)
print(fruit3)

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4
s=[1, 2, 3, 4, 5, 6, 7, 8, 9 , 10, 11, 12, 13, 14, 15, -2, -3, -4, 0]
s1=[]
#V1
for i in s:
  if i%3==0:
    s1.append(i)
  elif i%4!=0:
    s1.append(i)
  elif i>0:
    s1.append(i)
print(s1)

#V2
s2=[]
for i in s:
  if i%3==0 and i%4!=0 and i>0:
    s2.append(i)
print(sp2)

#V3
s3=[i for i in range(-20,21) if i%3==0 and i%4!=0 and i>0]
print(s3)
