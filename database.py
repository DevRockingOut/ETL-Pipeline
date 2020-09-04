from pymongo import MongoClient

def connectToDatabase():
    # connect to MongoDB
    client = MongoClient("mongodb+srv://admin:EaI54ZRAjFmyDvei@cluster0.a1la9.mongodb.net/optima_analytics?retryWrites=true&w=majority")
    db = client.optima_analytics
    return db

def storeProducts(products):
    db = connectToDatabase()

    for p in products:
        product = {
            'name': p[0],
            'total_available': p[1]
        }

        # add new json object to collection 
        result = db.critical_products.insert_one(product)
        print("\n Inserted Product =>  _id: " + str(result.inserted_id) + " ; name: " + product['name'] + " ; total available: " + product['total_available'])

def getProducts():
    db = connectToDatabase()
    # return a list containing all the products in the criticalProducts collection
    return list(db.critical_products.find({}))