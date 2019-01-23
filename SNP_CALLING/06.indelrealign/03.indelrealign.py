#! /usr/bin/python
# coding: utf-8

import re
import os
import os.path
from os import walk

L_all=[]
for (dirpath,dirnames,filenames) in os.walk("/media/uni/data/projects/Populus_phylogenomic/05.remove_duplicate/01.remove_duplicate_file/"):
    for files in filenames:
        L_all.append(files)

for bamfile in L_all:
    if re.findall(r".bam$",bamfile):
        names=re.search("([a-z]{4}.*).bam$",bamfile)
        name=names.group(1)
       # print name
        print "java -Xmx12g -jar /home/uni/programme/GenomeAnalysisTK-3.6/GenomeAnalysisTK.jar -T IndelRealigner -R /media/uni/data/projects/Populus_phylogenomic/01.ref/PhytozomeV11/Ptrichocarpa/assembly/Ptrichocarpa_210_v3.0.fa -I /media/uni/data/projects/Populus_phylogenomic/05.remove_duplicate/01.remove_duplicate_file/"+name+".bam -targetIntervals /media/uni/data/projects/Populus_phylogenomic/06.indelrealign/01.indelrealignfile/01.forIndelRealigner.intervals -o /media/uni/data/projects/Populus_phylogenomic/06.indelrealign/01.indelrealignfile/"+name+"_realignedbam.bam"
