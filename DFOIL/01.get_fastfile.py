#! /usr/bin/python
# coding:utf-8

import re
import os
from os import walk

print "python /home/uni/programme/dfoil/dfoil-master/fasta2dfoil.py",

for (dirpath,dirname,filename)in os.walk("/media/uni/data/projects/Populus_phylogenomic/07.snp_structure_analysis/14.dfoil_5_taxon/10kb/fasta_files/chr19"):

    for files in filename:
    
        if re.findall(r"align.fa",files):
            
            print  dirpath+"/"+files,
print"-o dfoil_outfile_chr19 -n pade0121 pqioT0103 palb01 ptma02 ptri01"
