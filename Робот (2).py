# coding : utf-8

# import os || модуль для взаимодействия с операционной системой
import os
import sys
# модуль с функцией копированя  
import shutil
# import psutill модуль для работы с процессами
import psutil

# def имя_функции(аргументы):
    #тело_функции
    #return результат

def copy_file(filename):
    if os.path.isfile(filename):
        newfile = filename + '.dupl'
        # копирование модуль shutil
        shutil.copy(filename, newfile)
        if os.path.exists(newfile):
            print("Файл", newfile, "успешно создан")
        else:
            print("При копировании возникли проблемы")

def sys_info():
    print("Вот что я знаю о системе: ")
    print("Количество процессоров: ", psutil.cpu_count())
    print("Платформа: ", sys.platform)
    print("Кодировка файловой системы: ", sys.getfilesystemencoding())
    print("Текущая директория: ", os.getcwd())
    print("Текущий пользователь: ", os.getlogin())


print("Робот помощник")
print("Привет Программист!")
name = input("Ваше имя: ")

print (name, ", добро пожаловать в мир Python")

# while условие_работы:
	#тело_цикла
answer = ''
while answer != 'Q' and answer != 'q': 
        answer = input("Давайте поработаем? (Y/N/Q)")
# конструкция ветвленеия
#if условия_истинности:
	#действия_при_истинности
#else:
	#действия_при_неистенности
        if answer == 'Y' or answer == 'y':
                print("Вот что я умею:")
                print("1) Я могу вывести список файлов текущей директории")
                print("2) Я могу вывести информацию о системе")
                print("3) Я могу вывести список ID запущенных процессов")
                print("4) Я могу продублировать файлы в текущей директории")
                print("5) Я могу продублировать указанный файл")
                print("6) Я могу удалить созданные ранеее дубликаты")
                print("Для выхода нажмите 9")

                try:
                        work = int(input("Укажите номер действия, пожалуйста :)"))
                        if work == 1:
                                print(os.listdir())
                        elif work == 2:
                                sys_info()
                        elif work == 3:
                                print(psutil.pids())
                        elif work == 4:
                                print("Дублирую файлы в текущей директории")
                                file_list = os.listdir()
                                i = 0
                                while i < len(file_list):
                                    copy_file(file_list[1])
                                    i += 1
                        elif work == 5:
                                filename = input("Введите имя файла в формате название.расширение: ")
                                print("Дублирую указанный файл")
                                copy_file(filename)
                        elif work == 6:
                                try:
                                        dirname = input("Укажите имя директории(если необходимо удаление в текущей директории нажмите .): ")
                                        print("Удаляю дубликаты")
                                        file_list = os.listdir(dirname)
                                # for переменная in список
                                        # тело цикла
                                        for f in file_list:
                                                fullname = os.path.join(dirname, f)
                                                if fullname.endswith('.dupl'):
                                                        os.remove(fullname)
                                                i += 1
                                except (FileNotFoundError):
                                        print("Нет такой директории :(")
                        elif work == 9:
                                print("До свидания!")
                                break
                        else:
                                print("Робот вас не понял :( Попробуем еще раз")

                except (TypeError, ValueError):
                        print("Робот вас не понял :( Попробуем еще раз :( ")

        elif answer == 'N' or answer == 'n':
                print("До свидания!")
                break
        elif answer == 'Q' or answer == 'q':
                print ("Работа не волк, в лес не уйдёт :)")
        else:
                print("Робот вас не понял :(")
                

