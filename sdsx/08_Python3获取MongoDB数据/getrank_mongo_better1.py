from pymongo import MongoClient

def get_rank(user_id):
    haha = MongoClient().shiyanlou

    s = haha.contests.aggregate([
        {'$group': {
            '_id': "$user_id",
            'sum_score': {'$sum': '$score'},
            'sum_time': {'$sum': '$submit_time'}}
        },
        {'$sort': 
            {'sum_score': -1, 'sum_time': 1}
        }
    ])

    for i, j in enumerate(s):
        if user_id == j['_id']:
            return i+1, j['sum_score'], j['sum_time']

