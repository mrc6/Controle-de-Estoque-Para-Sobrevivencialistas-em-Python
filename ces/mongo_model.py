from pymongo import MongoClient


def insert_one(product_data):
    client = MongoClient()
    db = client.stock
    product_id = db.products.insert_one(product_data).inserted_id
    print("Produto inserido como ID: ", product_id)
    client.close()


def delete_one(query):
    client = MongoClient()
    db = client.stock
    db.products.delete_one(query)
    client.close()


def find_all():
    client = MongoClient()
    db = client.stock
    return db.products.find()
    client.close()


def find_out_of_date(date):
    client = MongoClient()
    db = client.stock
    return db.products.find({"val": {"$lt": date}})
    client.close()


def delete_all_out_of_date(date):
    client = MongoClient()
    db = client.stock
    db.products.delete_many({"val": {"$lt": date}})
    client.close()
