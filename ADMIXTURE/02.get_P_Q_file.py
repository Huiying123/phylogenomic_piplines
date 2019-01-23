#! /usr/bin/python
# -*- coding:utf-8 -*-

import string
for i in range(1,11):
    print "admixture --cv -j12 01.populus_36.bed",i,"| tee 01.populus_36.bed."+str(i)+".log"
    
