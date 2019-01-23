#! /usr/bin/env perl
use strict;
use warnings;

my $file="/media/uni/data/projects/Populus_phylogenomic/08.all_site_ML_tree/04.treemix/02.without_prot8714/treemix2.gz";
my $output_dir="/media/uni/data/projects/Populus_phylogenomic/08.all_site_ML_tree/04.treemix/02.without_prot8714/output_files";
my $root="ptri";
`mkdir $output_dir` if(!-e "$output_dir");

open(O1,"> run_treemix.sh");
open(O2,"> run_plot.Rscript");
for(my $i=0;$i<15;$i++){
    my $m_para="";
    if($i>0){
        $m_para=" -m $i";
    }
    print O1 "/home/uni/programme/treemix/treemix-1.12/src/treemix -i $file$m_para -root $root -o $output_dir/out_$i > $output_dir/out_$i.log\n";
    print O2 "source('/home/uni/programme/treemix/treemix-1.12/src/plotting_funcs.R')\n";
    print O2 "pdf(file='$output_dir/out_$i.pdf')
plot_tree('$output_dir/out_$i')
plot_resid('$output_dir/out_$i','/media/uni/data/projects/Populus_phylogenomic/08.all_site_ML_tree/04.treemix/02.without_prot8714/00.species_9_names.txt')
dev.off()
";
}
close O1;
close O2;

