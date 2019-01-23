#! /usr/bin/python
# coding:utf-8

import re
import os

for files in os.listdir("/media/uni/data/projects/Populus_phylogenomic/07.snp_structure_analysis/12.phybase/5species_genetree/01.phylip_file"):
    if re.findall("phy$",files):
		files2=files
		#files3=files
		print "raxmlHPC-AVX -s /media/uni/data/projects/Populus_phylogenomic/07.snp_structure_analysis/12.phybase/5species_genetree/01.phylip_file/"+files2,"-n /media/uni/data/projects/Populus_phylogenomic/07.snp_structure_analysis/12.phybase/5species_genetree/02.tree_file/"+files2+".phb -f a -m GTRGAMMAI -k -x 71828 -N 100 -p 31415" 
    
