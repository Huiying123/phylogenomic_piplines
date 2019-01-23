#! /usr/bin/python
# coding:utf-8

import re
import os

for files in os.listdir("/media/uni/data/projects/Populus_phylogenomic/07.snp_structure_analysis/07.mpest/03.treefiles/"):
    if re.findall("phy$",files):
		files2=files
		files3=files
		print "raxmlHPC-AVX -s "+files2,"-n "+files3+".phb -f a -m GTRGAMMAI -k -x 71828 -N 100 -p 31415" 
    
