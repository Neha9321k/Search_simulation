# -*- coding: utf-8 -*-
"""
Created on Sun May  5 17:56:00 2019

@author: Neha Koushik
"""

import collections
import json


def mostCommon():
    with open('testdata.txt', 'r') as outfile:
         data1 = outfile.read()
         json1 = json.loads(data1)
         outfile.close

    list1 = []

    for words in json1['search']:
        list1.append(words['item'])

    return collections.Counter(list1).most_common(1)