import json

import sqlalchemy
from sqlalchemy.orm import sessionmaker
from module import create_table, Publisher, Shop, Book, Stock, Sale

DSN = 'postgresql://postgres@localhost:5432/alchemy'
engine = sqlalchemy.create_engine(DSN)
create_table(engine)

Session = sessionmaker(bind=engine)
session = Session()

with open('tests_data.json', 'r') as fd:
    data = json.load(fd)

for record in data:
    model = {
        'publisher': Publisher,
        'shop': Shop,
        'book': Book,
        'stock': Stock,
        'sale': Sale,
    }[record.get('model')]
    session.add(model(id=record.get('pk'), **record.get('fields')))
session.commit()


# название книги
# | название магазина, в котором была куплена эта книга
# | стоимость покупки
# | дата покупки



session.close()