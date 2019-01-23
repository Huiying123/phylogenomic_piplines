#! /usr/bin/python
# coding: utf-8

import re
import os
from os import walk
import os.path

L_all=[]
for (dirpath, dirnames,filenames) in os.walk("/media/uni/data/projects/Populus_phylogenomic/05.remove_duplicate/01.remove_duplicate_file/"):
    for filename in filenames:
        if re.findall(r".bam$",filename):
            L_all.append(os.path.join(dirpath,filename))
L_all_sort=sorted(L_all)
#print L_all

L_all2=[]
for (dirpath, dirnames,filenames) in os.walk("/media/uni/data/projects/Populus_phylogenomic/06.indelrealign/03.recalibration/"):
    for filename in filenames:
        if re.findall(r".table$",filename):
            L_all2.append(os.path.join(dirpath,filename))
L_all2_sort=sorted(L_all2)
#print L_all2
name2=""

for (file,file2) in zip(L_all_sort,L_all2_sort):
    file3=file+" "+file2
    name=re.search("([^\/]+).table$",file2)
    name2=name.group(1)
   # print file3
    print  "java -Xmx12g -jar /home/uni/programme/GenomeAnalysisTK-3.6/GenomeAnalysisTK.jar -T PrintReads -R /media/uni/data/projects/Populus_phylogenomic/01.ref/PhytozomeV11/Ptrichocarpa/assembly/Ptrichocarpa_210_v3.0.fa -I",file,"-BQSR",file2,"-o /media/uni/data/projects/Populus_phylogenomic/06.indelrealign/04.printreads/"+name2+".bam --log_to_file /media/uni/data/projects/Populus_phylogenomic/06.indelrealign/04.printreads/"+name2+"_printreads.log"






