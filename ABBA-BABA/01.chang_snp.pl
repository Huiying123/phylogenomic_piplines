while(<>){
    s/Chr/chr/g;
    s/chr0/chr/g;
    print "$_";
}
