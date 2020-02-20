"""

Домашнее задание №1

Цикл while: ask_user

* Напишите функцию ask_user(), которая с помощью input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
   
"""


def ask_user():
  while True:
    user_says = input('Как дела?\n')
    if user_says == 'Хорошо':
      print('И у меня тоже :)')
      break
    else:
      print('Всё понятно. Лови обнимашки \:_:/') 

    
if __name__ == "__main__":
    ask_user()
