#! /usr/bin/python
# coding:utf-8

import re
from os import walk

for (dirpath,dirnames,filenames) in walk("/media/uni/data/projects/Populus_phylogenomic/07.snp_structure_analysis/12.phybase/5species_genetree/out/"):
    file=dirpath+"/seq.fa"
    name=re.search("out/(.*)/seq.fa",file)
    name1=name.group(1)
    #print dirpath
    #print name1
    print "clustalw2 -INFILE="+file+" -CONVERT -OUTFILE=/media/uni/data/projects/Populus_phylogenomic/07.snp_structure_analysis/12.phybase/5species_genetree/01.phylip_file/"+name1+".phy -OUTPUT=PHYLIP"
