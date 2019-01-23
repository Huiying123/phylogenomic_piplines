#! /usr/bin/python
# coding:utf-8

import re
import gzip

infile=gzip.open("/media/uni/data/projects/Populus_phylogenomic/08.all_site_ML_tree/04.treemix/02.without_prot8714/treemix.gz","rb")

outfile=gzip.open("/media/uni/data/projects/Populus_phylogenomic/08.all_site_ML_tree/04.treemix/02.without_prot8714/treemix2.gz","wb")

for string in infile:
    string=string.rstrip()
    string_L=re.split("\s+",string)
    part1=" ".join(string_L[0:2])
    part2=" ".join(string_L[3:])
    #print part1,part2
    outfile.write(part1+" "+part2+"\n")
