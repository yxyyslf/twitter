__author__ = 'Yi'

from pymongo import MongoClient

client = MongoClient()
db = client.twiiter
userRelationshipCol = db.userRelationship
userFollowerIdCol = db.userfollowerid
userFollowerIdCursor = userFollowerIdCol.find()
userIdList = []
userRel = {}

for document in userFollowerIdCursor:
    userIdList.append(document['userid'])
    if len(userIdList) % 1000 == 0:
        print(len(userIdList))


minTime = 100000000000000000000
for id in userIdList[0:3000]:
    try:
        print(id)
        userRel['_id'] = id
        userRel['parent'] = []
        userFollowerIdCursor = userFollowerIdCol.find()
        for follower in userFollowerIdCursor:
            if id in follower['follower']:
                print('Find A Relation!')
                userRel['parent'].append([follower['userid'],follower['time']])
        userRelationshipCol.insert(userRel)
    except Exception as e:
        print(e)