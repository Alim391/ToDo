class ToDo:

    def __init__(self, text):
        self.filename = text


    def add_task(self, text):
        try:
            task_line = f'[ ] {text}\n'
            with open(self.filename, 'a', encoding='utf-8') as add:
                add.write(task_line)
                print('Задача добавлена!')


        except FileNotFoundError:
            print('File not Found')

    def show_task(self):
        print('Вы выбрали показ задач. \nСписок задач на текущий момент: ')
        try:
            with open(self.filename, 'r') as show:
                lines = show.readlines()
                if not lines:
                    print('Список задач пока пуст.')
                    return
                for index, line in enumerate(lines, start=1):
                    print(f'{index}. {line.capitalize().strip()}', end='')

        except FileNotFoundError:
            print('File not Found')    


    def status_task(self, index_task):
        try:
            with open(self.filename, 'r', encoding='utf-8') as status:
                lines = status.readlines()

            if index_task < 1 or index_task > len(lines):
                print('Ошибка!!!! Нет задачи с таким номером!')
                return

            line = lines[index_task - 1]

            if line.startswith([ ]):
                lines[index_task - 1] = line.replace('[ ]', '[x], 1')
                print(f'Задача #{index_task} отмечена как выпольненнное!')
            elif line.startswith('[x]'):
                lines[index_task - 1] = line.replace('[x]', '[ ]', 1)
                print(f'Задача №{index_task} снова возвращена в активные.')

            with open(self.filename, 'w', encoding='utf-8') as status:
                status.writelines(lines)

        except FileNotFoundError:
            print('File not found')


    def del_task(self, keyword):
         try:
            with open(self.filename, 'r', encoding='utf-8') as dell:
                   lines = dell.readlines() 

            with open(self.filename, 'w', encoding='utf-8') as dell:
                for line in lines:
                    if keyword.lower() not in line.lower():
                        dell.write(line)   
            print(f'Удаление строк с ключевым словом "{keyword}" завершено.')     

         except FileNotFoundError:
            print('File not Found')     



todo = ToDo('todo.txt')
print('Добро пожаловать в задач. Если хотите остановить добавление задач введите "стоп"')
print('Выбирите действие: \n1 - Добавить задачу, \n2 - Посмотреть задачи, \n3 - Удалении задач, \n4 - Изменить статусь задачи, \n5 - выйти')

while True:
    try:
        choice_num = int(input('Введите цифру: '))
    except ValueError:
        print('Ошибка при вводе цифры(только от 1 до 5)')
        continue

    if choice_num == 1:
        print('Вы выбрали добавление задачи')
        while True:
            text = input('Напишите задачу: ')
            if text.lower() == 'стоп':
                break

            todo.add_task(text)
        
        print('Задачи успешно добавлены! \n')
            
            

    elif choice_num == 2:
        todo.show_task()
        print()
        print('Показ задач завершено успешно!')

    elif choice_num == 3:
        todo.show_task()
        try:
            task_num = int(input('\nВведите номер задачи, чтобы изменить её статус: '))
            todo.status_task(task_num)
        except ValueError:
            print('Ошибка: введите корректный номер задачи.')

    elif choice_num == 4:
        print('Вы выбрали удаление задач')
        keyword = input('Введите ключевое слово для удалении строки: ')
        todo.del_task(keyword)
        print(f'Удаление строки с ключевой строкой {keyword} заверщено')

    elif choice_num == 5:
         print('До свидания!')
         break

    else:
        print('Неверный пункт. Выберите от 1 до 5')

    
