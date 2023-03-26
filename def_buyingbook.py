import json
from datetime import datetime
dt = datetime.now()

import sqlalchemy
from sqlalchemy.orm import sessionmaker
from module import create_table, Publisher, Shop, Book, Stock, Sale

DSN = 'postgresql://postgres@localhost:5432/alchemy'
engine = sqlalchemy.create_engine(DSN)


Session = sessionmaker(bind=engine)
session = Session()


def buying_books(publisher):
    q = session.query(Publisher, Book, Stock, Shop, Sale
    ).filter(
        Publisher.id == Book.id_publisher
    ).filter(
        Book.id == Stock.id_book
    ).filter(
        Shop.id == Stock.id_shop
    ).filter(
        Stock.id == Sale.id_stock
    ).filter(
        Publisher.name == publisher
    )
    result = set()

    for c in q.all():
        book_name = str(result.union({c.Book.title})).replace("{", "").replace("}", "").replace("'", "")
        name_shop = str(result.union({c.Shop.name})).replace("{", "").replace("}", "").replace("'","")
        price_book = str(result.union({c.Sale.price})).replace("{", "").replace("}", "").replace("'","")
        date_buy = str(result.union({c.Sale.date_sale})).replace("{", "").replace("}", "").replace("'","").replace('datetime', '').replace('.', '').replace('(', '')
        date_ = date_buy[:12]
        count = str(result.union({c.Sale.count})).replace("{", "").replace("}", "").replace("'","")

        return f'{book_name} | {name_shop} | {float(price_book) * int(count)} | {date_.replace(",", "-").replace(" ", "")}'


publisher = input('Введите имя издателя: ')

print(buying_books(publisher))


session.close()