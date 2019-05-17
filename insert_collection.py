# -*- coding: utf-8 -*-
"""
Created on Sat May  4 13:15:11 2019

@author: Neha Koushik
"""

import json
import random
import datetime

def insertCollection():
    json1 = {}
    json1['search'] = []
    with open('testdata.txt', 'r') as outfile:
         data1 = outfile.read()
         json1 = json.loads(data1)    
         outfile.close
    
    srch_id = random.randint(1, 1000000000)
    list1= ['seo','digital marketing','content marketing','marketing saas','best seo tools','marketing cloud' , 'how to rank high on google','what is seo','what is a serp','search volume vs modeled traffic']
    search_item = random.choice(list1)
    srch_time = datetime.datetime.now().timestamp() 

    json1['search'].append({
         'id': srch_id,
        'item': search_item,
        'time': srch_time
    })




    with open('testdata.txt', 'w') as outfile:  
        json.dump(json1, outfile)
    outfile.close




    with open('testdata.txt', 'r') as outfile:
     data1 = outfile.read()
     json1 = json.loads(data1)
    outfile.close

 






