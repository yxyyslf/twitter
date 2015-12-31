__author__ = 'Yi'

from pymongo import MongoClient
import networkx as nx
import matplotlib.pyplot as plt

client = MongoClient()
db = client.twiiter
userRelationPicCol = db.userRelationPic
userRelationPicCursor = userRelationPicCol.find().limit(500)

TGraph = nx.DiGraph()
twitterGraph = []
idDic = []
idKey = {}
num = 1
for document in userRelationPicCursor:
    idDic.append((num,document['_id']))
    idKey[document['_id']] = num
    arrayLen = len(document['list'])
    for i in range(0,arrayLen-1):
        if (document['list'][i],document['list'][i+1]) not in twitterGraph:
            twitterGraph.append((document['list'][i],document['list'][i+1]))
    print(len(twitterGraph))
    num += 1

# f=open('node.txt','w')
# for i in idDic:
#     f.write(str(i[0])+' '+'"'+str(i[1])+'"'+"\n")
#     num+=1
# f.close()

f=open('edge.txt','w')
for i in twitterGraph:
    f.write(str(idKey[i[0]])+' '+str(idKey[i[1]])+"\n")
f.close()

# for edge in twitterGraph:
#     TGraph.add_edge(edge[0],edge[1])
#
# nx.draw(TGraph)
# plt.savefig("twitter.png")
