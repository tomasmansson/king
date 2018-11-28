#!/usr/bin/env python


import random
import mysql.connector as mariadb

mariadb_connection = mariadb.connect(user='root', password='Pa55w.rd', database='nioliv_toma')
cursor = mariadb_connection.cursor()

cursor.execute('SELECT ord FROM hemligaord');
rows=cursor.fetchall()

ordval_list=[]
for i in rows:
	ordval_list.append(i[0])
	ord=random.choice(ordval_list)

import string
liv = 9
hemligt_ord=random.choice(ordlista)
ledtråd=list('?????')
hjärtsymbol=u'\u2764'
gissade_rätt=False


username = input('Enter your username: ')
print('Greetings', username, '! Welcome to Nine Lives. Let\'s start')



def uppdatera_ledtråd (gissad_bokstav, hemligt_ord, ledtråd):
    index=0
    while index < len(hemligt_ord):
        if gissad_bokstav == hemligt_ord[index]:
            ledtråd[index] = gissad_bokstav
        index=index+1

while liv > 0:
    print(ledtråd)
    print('Liv kvar: ' + hjärtsymbol * liv)
    gissning=input('Guess a letter or the whole secret word: ')
    
    if gissning==hemligt_ord:
        gissade_rätt=True
        break

    if gissning in (hemligt_ord):
        uppdatera_ledtråd(gissning, hemligt_ord, ledtråd)

    if ledtråd == list(hemligt_ord):
        gissade_rätt = True
        break
        
    else:
        print('Wrong, you\'ve now lost a life.')
        liv-=1

if gissade_rätt:
    print('Congratulations! You have won! The secret word was ' + hemligt_ord)
else:
    print('Game Over! You have lost. The secret word was ' + hemligt_ord)
    
    
