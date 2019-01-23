#! /usr/bin/python
# coding:utf-8

import re
import os
import os.path
from os import walk

for (dirpath,dirnames,filenames) in os.walk("/media/uni/data/projects/Populus_phylogenomic/05.remove_duplicate/01.remove_duplicate_file/"):
    for file in filenames:
        if re.findall(r".bam$",file):
            print "samtools index /media/uni/data/projects/Populus_phylogenomic/05.remove_duplicate/01.remove_duplicate_file/"+file
            
