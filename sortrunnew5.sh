#!/bin/bash
for i in {1..24}
do
	bedtools intersect -a  comp${i}_out_gene_quadr_all_sorted.bed -b /data/nooroka/grant/punkt3/sort_sort_sort2/sort_sort_sort_sort2/bed/un/${i}_2_sorted_un.bed > mutcosquadr${i}.bed #coordinates in mutation quadruplex  file intersect with COSMIC mutation coordinates in all chromosomes
done
