#! /usr/bin/env perl

use strict;

use warnings;



my $dir="/media/uni/data/projects/Populus_phylogenomic/08.all_site_ML_tree/06.densitytree/outfile4/"; # use RAxMLtree output

my $phyutility="/home/uni/programme/phyutility_roottree/phyutility/phyutility.jar";

my $outgroup="pbal01 pbal02 ptri01 ptri02";



open O,"> $0.sh";

print O "cat $dir/*/*.tre > $0.alltre\njava -jar $phyutility -rr -in $0.alltre -out $0.rrtre -names $outgroup\n";

close O;

/home/uni/programme/phyutility_roottree/phyutility/phyutility.jar -rr -in /media/uni/data/projects/Populus_phylogenomic/08.all_site_ML_tree/06.densitytree/rooted_tree4/genetree_raw4.tree -out /media/uni/data/projects/Populus_phylogenomic/08.all_site_ML_tree/06.densitytree/rooted_tree4/genetree_rooted4.tree -names pbal01 pbal02 ptri01 ptri02 -log /media/uni/data/projects/Populus_phylogenomic/08.all_site_ML_tree/06.densitree/rooted_tree4/genetree_rooted4.log
