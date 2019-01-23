#! /usr/bin/python
# coding:utf-8

import re
import os
from os import walk

L_bamfile=[]
for (dirfile,pathfile,filename)in os.walk("/media/uni/data/projects/Populus_phylogenomic/04.picard/01.picard_files/"):
   # print filename
    for files in filename:
        if re.findall(r".bam$",files):
            name=re.search("(^p.*).bam",files)
            name_bamfile=name.group(1)
           # print name_bamfile
            print "java -Xmx12g -jar /home/uni/programme/picard/picard-tools-2.5.0/picard.jar MarkDuplicates INPUT=/media/uni/data/projects/Populus_phylogenomic/04.picard/01.picard_files/"+name_bamfile+".bam OUTPUT=/media/uni/data/projects/Populus_phylogenomic/05.remove_duplicate/01.remove_duplicate_file/"+name_bamfile+"_rmdup.bam METRICS_FILE=/media/uni/data/projects/Populus_phylogenomic/05.remove_duplicate/02.duplication_metrics/"+name_bamfile+"_dup.txt REMOVE_DUPLICATES=true"
