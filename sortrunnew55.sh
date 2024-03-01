#!/bin/bash
for i in {1..24}
do
	bedtools intersect -a  gccoords_${i}_un.bed -b /data/nooroka/grant/punkt3/sort_sort_sort2/sort_sort_sort_sort2/bed/un/${i}_2_sorted_un.bed > mutcos_non_quadr${i}.bed #coordinates in mutation interquadruplex GC-rich file intersect with COSMIC mutation coordinates in all chromosomes
done
