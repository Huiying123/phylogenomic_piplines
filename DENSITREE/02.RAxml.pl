#! /usr/bin/env perl

use strict;

use warnings;



my $indir="/media/uni/data/projects/Populus_phylogenomic/08.all_site_ML_tree/06.densitytree/outfile4";

my $clustalw2="/home/uni/programme/clustalw/clustalw-2.1-linux-x86_64-libcppstatic/clustalw2";

my $raxml="/home/uni/programme/Raxml/standard-RAxML-8.2.9/raxmlHPC-AVX";

my $now=$ENV{'PWD'};



my @dir=<$indir/*>;



open O,"> $0.sh";

foreach my $dir(@dir){

    if(-d "$dir"){

        # print O "cd $dir; $clustalw2 -INFILE=align.fa -CONVERT -OUTFILE=align.phy -OUTPUT=PHYLIP; $raxml -s align.phy -n align.phb -f a -m GTRGAMMAI -k -x 271828 -N 100 -p 31415 -o bbu01,buffalo001,buffalo002,buffalo003; cd $now\n";

        print O "cd $dir; $clustalw2 -INFILE=align.fa -CONVERT -OUTFILE=align.phy -OUTPUT=PHYLIP; $raxml -T 2 -s align.phy -n align.phb -m GTRGAMMAI -p 31415 -o pbal01,pbal02,ptri01,ptri02; cd $now\n";

    }

}

close O;
