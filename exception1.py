"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

def ask_user():
  while True:
    try:
      user_says = input('Как дела?\n')
      if user_says == 'Хорошо':
        print('И у меня тоже :)')
        break
      else:
        print('Всё понятно. Лови обнимашки \:_:/')
    except KeyboardInterrupt:
      print('Пока')
      break
    
if __name__ == "__main__":
    ask_user()
