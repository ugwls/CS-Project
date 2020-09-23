from db import db_oven as oven
from db import db_washing as washing
from db import db_juicer as juicer
from db import db_dishwasher as dishwasher
from db import db_led as led
from db import db_laptops as laptops
from os import system, name
import mysql.connector
from time import sleep

def clear():
    sleep(1)
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
    sleep(1)

def mysql_connt():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="Ujjw@l.16",
        database="electronics")
    cur = mydb.cursor()
    cur.execute('create database if not exists electronics')
    mydb.commit()

mysql_connt()

while True:
    print('\t\t\t\tMenu', end='')
    print('''
1.Add record in tables
2.Update a table
3.Delete a Item
4.See Details
5.Exit
        ''')
    menu = int(input('Enter your option: '))
    if 1 == menu:
        clear()
        print('\t\t\t\tSelect a Table')
        print('''
1.Oven
2.Washing Machines
3.Juicer
4.Dish Washer
5.LED TV
6.Laptops
7.Go To Main Menu 
                ''')
        submenu = int(input('Enter your option: '))
        if 1 == submenu:
            clear()
            oven.add_oven()
            clear()
            continue
        if 2 == submenu:
            clear()
            washing.add_washing()
            clear()
            continue
        if 3 == submenu:
            clear()
            juicer.add_juicer()
            clear()
            continue
        if 4 == submenu:
            clear()
            dishwasher.add_dishwasher()
            clear()
            continue
        if 5 == submenu:
            clear()
            led.add_led()
            clear()
            continue
        if 6 == submenu:
            clear()
            laptops.add_laptop()
            clear()
            continue
        if 7 == submenu:
            exit()
        continue
    if 2 == menu:
        print('\t\t\t\tSelect a Table')
        print('''
1.Oven
2.Washing Machines
3.Juicer
4.Dish Washer
5.LED TV
6.Laptops
7.Go To Main Menu 
                ''')
        submenu = int(input('Enter your option: '))
        if 1 == submenu:
            clear()
            oven.update()
            clear()
            continue
        if 2 == submenu:
            clear()
            washing.update()
            clear()
            continue
        if 3 == submenu:
            clear()
            juicer.update()
            clear()
            continue
        if 4 == submenu:
            clear()
            dishwasher.update()
            clear()
            continue
        if 5 == submenu:
            clear()
            led.update()
            clear()
            continue
        if 6 == submenu:
            clear()
            laptops.update()
            clear()
            continue
        if 7 == submenu:
            exit()
        continue
    if 3 == menu:
        print('\t\t\t\tSelect a Table')
        print('''
1.Oven
2.Washing Machines
3.Juicer
4.Dish Washer
5.LED TV
6.Laptops
7.Go To Main Menu 
                ''')
        submenu = int(input('Enter your option: '))
        if 1 == submenu:
            clear()
            oven.delete()
            clear()
            continue
        if 2 == submenu:
            clear()
            washing.delete()
            clear()
            continue
        if 3 == submenu:
            clear()
            juicer.delete()
            clear()
            continue
        if 4 == submenu:
            clear()
            dishwasher.delete()
            clear()
            continue
        if 5 == submenu:
            clear()
            led.delete()
            clear()
            continue
        if 6 == submenu:
            clear()
            laptops.delete()
            clear()
            continue
        if 7 == submenu:
            exit()
        continue
    if 4 == menu:
        print('\t\t\t\tSelect a Table')
        print('''
1.Oven
2.Washing Machines
3.Juicer
4.Dish Washer
5.LED TV
6.Laptops
7.Go To Main Menu 
                ''')
        submenu = int(input('Enter your option: '))
        if 1 == submenu:
            clear()
            oven.see_details()
            clear()
            continue
        if 2 == submenu:
            clear()
            washing.see_details()
            clear()
            continue
        if 3 == submenu:
            clear()
            juicer.see_details()
            clear()
            continue
        if 4 == submenu:
            clear()
            dishwasher.see_details()
            clear()
            continue
        if 5 == submenu:
            clear()
            led.see_details()
            clear()
            continue
        if 6 == submenu:
            clear()
            laptops.see_details()
            clear()
            continue
        if 7 == submenu:
            exit()
        continue
    if 5 == menu:
        exit()
    print('Wrong Option!!')
    continue
