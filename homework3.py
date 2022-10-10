#Игра против бота
from random import randint
n = int(100)
player1 = 0
player2 = 0
turn = randint(1, 2) 
limit = 28

while n > 0 :
  a = 0
  if turn ==1:
    if n > limit :
        a = randint (1, 28)
    else :
        a = n  
    print(f'бот взял {a} конфет')      
  else:    
        while not (a > 0 and a <= n and a <= limit):
            a = int(input(f'игрок введите количество конфет '))
            if a > limit :
               print('можно взять не больше 28 конфет')  
            if a > n :  
               print(f'нельзя взять больше конфет,чем {n}')   
  n = n - a
  print(f'осталось {n} конфет')

  if turn == 1 :
    player1 = player1 + a
    
    turn = 2
  else :
    player2 = player2 + a
    turn = 1

if turn == 1:
    
    print(f'победил игрок')
else:
       
    print(f'победил бот')




