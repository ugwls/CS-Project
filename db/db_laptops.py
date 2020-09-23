import mysql.connector
from db.db_info import *


def enter():
    input()
    if 32 == ord(' '):
        print(end='')


mydb = mysql.connector.connect(
    host=HOST,
    user=USER,
    passwd=PASSWORD,
    database=DATABASE)
cur = mydb.cursor()
cur.execute('create database if not exists electronics')
mydb.commit()

laptops = '''
create table if not exists laptop(
item_no int, 
item_id varchar(5), 
Brand varchar(30),
Model varchar(50),
Quantity int,
Price_per_unit varchar(30),
MRP varchar(30))
'''
cur.execute(laptops)
mydb.commit()


def add_laptop():
    try:
        print('Enter the details :')
        s = 'insert into laptop (item_no, item_id, brand, model, quantity, price_per_unit, MRP) values(%s,%s,%s,%s,' \
            '%s,%s,%s) '
        item_no = int(input('Enter Item no.: '))
        item_id = input('Enter Item id: ')
        brand = input('Enter Brand name: ')
        model = input('Enter Model name: ')
        quantity = int(input('Enter Quantity: '))
        price = input('Enter Price: ')
        mrp = input('Enter MRP: ')
        value = (item_no, item_id, brand, model, quantity, 'Rs.' + price, 'Rs.' + mrp)
        cur.execute(s, value)
        print('Successfully added')
        mydb.commit()
        print('Press ENTER to continue.....', end='')
        enter()
    except():
        print('Error... try it again!!!')


def delete():
    try:
        item_id = input('Enter item id you want to delete: ')
        s = 'DELETE FROM laptop WHERE item_id = %s'
        value = (item_id,)
        cur.execute(s, value)
        mydb.commit()
        print('Successfully deleted!!!!!!')
        print('Press ENTER to continue.....', end='')
        enter()
    except():
        print('Error... try it again!!!')


def update():
    try:
        s = 'update laptop set item_id= %s, brand= %s, model= %s, quantity= %s, price_per_unit= %s, MRP= %s where ' \
            'item_no= %s '
        item_no = int(input('Enter Item no.: '))
        item_id = input('Enter Item id: ')
        brand = input('Enter Brand name: ')
        model = input('Enter Model name: ')
        quantity = int(input('Enter Quantity: '))
        price = input('Enter Price: ')
        mrp = input('Enter MRP: ')
        value = (item_id, brand, model, quantity, 'Rs.' + price, 'Rs.' + mrp, item_no)
        cur.execute(s, value)
        mydb.commit()
        print("Successfully updated!!!!!!!!")
        print('Press ENTER to continue.....', end='')
        enter()
    except():
        print('Error... try it again!!!')


def see_details():
    s = 'select * from laptop'
    cur.execute(s)
    result = cur.fetchall()
    for rec in result:
        print(rec)
    print('Press ENTER to continue.....', end='')
    enter()
