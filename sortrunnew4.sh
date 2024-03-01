#!/bin/bash
for i in {1..24}
do
    bedtools intersect -a comp${i}_gene.bed -b /data/nooroka/grant/punkt3/sort_sort_sort2/sort_sort_sort_sort2/bed/${i}_2_sorted.bed > mutcos${i}.bed
done
