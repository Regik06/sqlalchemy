import json

import sqlalchemy
from sqlalchemy.orm import sessionmaker
from module import create_table, Publisher, Shop, Book, Stock, Sale


def get_data(data_file):
    with open(data_file, 'r') as fd:
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


if __name__ == "__main__" :
    DSN = 'postgresql://postgres@localhost:5432/alchemy'
    engine = sqlalchemy.create_engine(DSN)
    create_table(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    data_file = 'tests_data.json'
    get_data(data_file)
    session.close()