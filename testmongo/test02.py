from pymongo import MongoClient

if __name__ == '__main__':
    import json
    config_file = "config.json"
    with open( config_file, "r") as fp:
        config_json = json.load( fp )
        mongo_conf = config_json["mongo_conf"]
        print(mongo_conf)
        host = mongo_conf['host']
        port = mongo_conf['port']
        dbname = mongo_conf['db']
        colname = mongo_conf['collection']
        client = MongoClient(host,int(port))
        # db = client[dbname]
        # collection = db[colname]
        db=client.get_database(dbname)
        col = db.get_collection(colname)
        count =col.find().count()

        print(count)
        col.update({'name': 'zhaowei'}, {'$set': {'age':18}},True)
        count = col.find().count()
        print(count)

        # col.insert_one({"name":'zhaowei','age':17})




