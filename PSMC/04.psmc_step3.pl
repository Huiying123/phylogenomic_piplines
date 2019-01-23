#! /usr/bin/env perl
use strict;
use warnings;

my $out="$0.sh";
my $outdir="/media/uni/data/projects/Populus_phylogenomic/07.snp_structure_analysis/09.psmc/real_psmc/pade";
`mkdir $outdir` if(!-e $outdir);
open(O,"> $out");
print O "/home/uni/programme/psmc/psmc-0.6.5/psmc -N25 -t15 -r5 -p \"4+25*2+4+6\" -o $outdir/pade.psmc pade.psmcfa\n";
for(my $i=1;$i<=100;$i++){
    print O "/home/uni/programme/psmc/psmc-0.6.5/psmc -N25 -t15 -r5 -b -p \"4+25*2+4+6\" -o $outdir/round-$i.psmc pade.split.fa\n";
}
close O;
