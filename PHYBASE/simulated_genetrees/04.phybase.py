#! /usr/bin/python
# coding:utf-8

for i in range(1,1001):
    print '''library("phybase")
mptree1 = "(ptri:16.430592,((pqio:9,pade:9):0.430592,(palb:9.098414,ptma:9.098414):0.332178):7.000000);"
spname <- species.name(mptree1)
nodematrix <- read.tree.nodes(str=mptree1, name=spname)$nodes
nodematrix[,5]<-2
nodematrix
genetrees=1:28966
for(i in 1:28966)
genetrees[i]<-sim.coaltree.sp(rootnode=9, nodematrix=nodematrix,nspecies=5,seq=rep(1,5), name=spname)$gt '''
    
    print "write(genetrees, 'populus_simulated_5species."+ str(i) + ".tre')"
