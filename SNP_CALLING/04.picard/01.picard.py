#! /usr/bin/python
# coding:utf-8

import re
import os
from os import walk
L_all=[]
for (dirpath,dirnames,filenames)in os.walk("/media/uni/data/projects/Populus_phylogenomic/03.bwa_mapping/01.bamfile/"):
    for file in filenames:
        name=re.search("(^[a-z]{1,4}.*).bam$",file)
        file_name=name.group(1)
       # print file_name
        print "java -Xmx12g -jar /home/uni/programme/picard/picard-tools-2.5.0/picard.jar AddOrReplaceReadGroups INPUT=/media/uni/data/projects/Populus_phylogenomic/03.bwa_mapping/01.bamfile/"+file_name+".bam OUTPUT=/media/uni/data/projects/Populus_phylogenomic/04.picard/01.picard_files/"+file_name+"_RG.bam RGID=J00121_73_HCWWLBBXX_"+file_name,"RGLB="+file_name,"RGPL=illumina RGPU=J00121_73_HCWWLBBXX_"+file_name,"RGSM="+file_name,"SORT_ORDER=coordinate CREATE_INDEX=true VALIDATION_STRINGENCY=SILENT"
