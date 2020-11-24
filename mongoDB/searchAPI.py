import pymongo


def query(keyword):
    myquery = {'$or':[
        {"url": {"$regex": f'.*{keyword}.*', "$options": 'i'}},
        {"story": {"$regex": f'.*{keyword}.*', "$options": 'i'}},
        {"full_title": {"$regex": f'.*{keyword}.*', "$options": 'i'}},
        {"story_desc": {"$regex": f'.*{keyword}.*', "$options": 'i'}},
        {"author": {"$regex": f'.*{keyword}.*', "$options": 'i'}},
        {"tag": {"$regex": f'.*{keyword}.*', "$options": 'i'}},
        {"place": {"$regex": f'.*{keyword}.*', "$options": 'i'}},
        {"time": {"$regex": f'.*{keyword}.*', "$options": 'i'}}
    ]}
    mydoc = mycol.find(myquery)
    # if mydoc.count():

    for x in mydoc:
        print(x)

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["news"]
mycol = mydb["news_table"]

search = str(input('search::\t'))
query(search)