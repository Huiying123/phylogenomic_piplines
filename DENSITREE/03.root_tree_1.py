#! /usr/bin/python
# coding:utf-8

import re
import os
from os import walk

print "cat",
for (dirpath,dirnames,filenames) in walk("/media/uni/data/projects/Populus_phylogenomic/08.all_site_ML_tree/06.densitytree/outfile4"):
    for files in filenames:
        if re.findall(r"RAxML_bestTree.align.phb",files):
            print dirpath+"/"+files,
print "> /media/uni/data/projects/Populus_phylogenomic/08.all_site_ML_tree/06.densitytree/rooted_tree4/genetree_raw4.tree "
                        
                       
