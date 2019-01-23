library("ggplot2")
a=read.table(file="/media/uni/data/projects/Populus_phylogenomic/07.snp_structure_analysis/01.PCA/04.without_prot8714_discardhalfmissing/03.populus_36_discardhalfmissing_changed2.eigenvec",header=T)
pdf(file="/media/uni/data/projects/Populus_phylogenomic/07.snp_structure_analysis/01.PCA/04.without_prot8714_discardhalfmissing/Populus_pca34.3spcies.pdf")
ggplot(a,aes(PC3,PC4,colour=Species))+geom_point(size=5)
dev.off()


