#! /usr/bin/python
# coding:utf-8

import re

with open("06.get_simplt_trees1.location.txt",'r') as infile:
    for string in infile:
        string=string.strip()
        #print string
        string2=re.split("\s",string)
        b=int(string2[0])
        if b >= 75 :
            c= " ".join(string2[1:3])
            print c
        
