# -*- coding: utf-8 -*-
"""
Created on Sun May  5 14:05:22 2019

@author: Neha Koushik
"""
import json
import datetime


def lastPeriod(time):
    with open('testdata.txt', 'r') as outfile:
         data1 = outfile.read()
         json1 = json.loads(data1)
    outfile.close

    count =0

    t1 = datetime.datetime.now().timestamp()
 
    for search in json1['search']:
        if (( t1 - search['time']) <= time) :
            count = count+1
    return count


    

    