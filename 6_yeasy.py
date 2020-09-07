# Задача-1:
# Следующая программа написана верно, однако содержит места потенциальных ошибок.
# используя конструкцию try добавьте в код обработку соответствующих исключений.
# Пример.
# Исходная программа:
def avg(a, b):
    """Вернуть среднее геометрическое чисел 'a' и 'b'.

    Параметры:
        - a, b (int или float).

    Результат:
        - float.
    """
    return (a * b) ** 0.5


a = float(input("a = "))
b = float(input("b = "))
c = avg(a, b)
print("Среднее геометрическое = {:.2f}".format(c))

# Задача-2:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
path_dir =[('dir_' + str(i + 1)) for  i in range(9)]
 
def make_dir(paths):
  dir_path = os.path.join(os.getcwd(),paths)
  try:
    os.mkdir(dir_path)
  except:
    print(dir_path + ' - такая директория уже есть')

def delete_dir(paths):
  dir_path = os.path.join(os.getcwd(),paths)
  try:
    os.rmdir(dir_path)
  except:
    print(dir_path + ' - такой директории не существует')

what_do=input("\"make\" or \"delete\" directories\n")

if what_do=='make' or what_do=='delete':
  pass
else:
  raise Exception("нужно правильно ввести решение по созданию или удалению директории соответсвенно: make или delete")

for i in path_dir:
  if what_do=="make":
    make_dir(i)
  elif what_do=="delete":
    delete_dir(i)
# Задача-3:
# Напишите скрипт, отображающий папки текущей директории.

# Задача-4:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
def copy_file(first_file,backup_file):
  shutil.copy(first_file,backup_file)
 
first_file = sys.argv[0]
backup_file = first_file + '.backup'
copy_file(first_file,backup_file)
