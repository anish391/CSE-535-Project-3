# -*- coding: utf-8 -*-


import json
# if you are using python 3, you should 
import urllib.request
from urllib.parse import quote
#import urllib2

IRModel='BM25' #change values of core to vsm and dfr as per requirement


# change the url according to your own corename and query
lines = [line.rstrip('\n') for line in open('testqueries.txt',encoding='utf-8')]
i=1
for line in lines:
    
    qid,query = line.split(maxsplit=1)
    query = query.replace(':','\:')
    query = quote(query)
    query = query.replace(' ','%20')

    # change query id, core name and IRModel name accordingly
    inurl = 'http://localhost:8983/solr/bm25/select?defType=dismax&fl=id,%20score&indent=on&q='+str(query)+'&qf=tweet_hashtags^3%20text_en^6%20text_ru^6%20text_de^6%20text_en_copy%20text_de_copy%20text_ru_copy&rows=20&wt=json'
    outfn = str(i)+'.txt'
    outf = open(outfn, 'w')
    #data = urllib2.urlopen(inurl)
    # if you're using python 3, you should use
    data = urllib.request.urlopen(inurl)
    docs = json.load(data)['response']['docs']
    
    # the ranking should start from 1 and increase
    rank = 1
    for doc in docs:
        #print(doc)
        outf.write(qid + ' ' + 'Q0' + ' ' + str(doc['id']) + ' ' + str(rank) + ' ' + str(doc['score']) + ' ' + IRModel + '\n')
        rank += 1
    outf.close()
    i+=1
