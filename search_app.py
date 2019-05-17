# -*- coding: utf-8 -*-
"""
Created on Sat May 11 10:37:46 2019

@author: Neha Koushik
"""

from most_common import mostCommon
from insert_collection import insertCollection
from last_minute import lastPeriod

ans = 'Y'

while(ans == 'Y' or ans == 'y'):
    
    
    opt = input("Please select one from below option:\n 1) Search a term \n 2) Search Terms in last 1 minute \n 3) Search Terms in last defined time \n 4) Most common search term\n")
    
    
    
    if opt == '1' :
        insertCollection()
        print("Search Term Inserted")
    elif opt == '2':
        c = lastPeriod(60)
        print(c)
    elif opt == '3':
        time = input("enter time period in seconds")
        c = lastPeriod(int(time))
        print(c)
    elif opt == '4':
        b = mostCommon()
        print(b)
    else:
        print("invalid option!!")
    ans = input("Do you want to continue Y/N?")



