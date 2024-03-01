#!/bin/bash
for i in {1..24}
do
    bedtools subtract -a comp${i}_gene.bed -b comp${i}_out_gene_quadr_all_sorted.bed  > comp${i}_gene_GC.bed
    bedtools getfasta -fi hg38_new.fna -bed comp${i}_gene_GC.bed > comp${i}_gene_GC.fasta
done
