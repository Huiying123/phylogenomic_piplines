my $pre="NA";
my $num=0;
while(<>){
chomp;
next if(/scaffold/);
my @a=split(/\s+/);
my $chr=$a[1];
if($chr ne $pre){
$num++;
}
$chr="chr$num";
$a[0]=$chr.":".$a[3];
$a[1]=$chr;
my $line=join "\t",@a;
print "$line\n";
$pre=$chr;
}
