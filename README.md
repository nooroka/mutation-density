<b>1.py, 2.py,2_rev.py</b> - calculating quadruplexes with QGRS Conserve <br>
<b>1_run.py, 2_run.py</b> - running 1.py, 2.py, 2_rev.py for chromosomes <br>
<b>windowcoords13.py. coordsgc13.py</b> - calculating GC-rich regions <br>
<b>windowrun13.py, windowrun13.sh</b> - running windowcoords13.py for all chromosomes (equivalent) <br>
<b>script3.py, script4.py, script6.py, script2.py</b> - calculating mutational dbSNP density in quadruplexes and interquadruplexes (script3.sh and script4.sh are equivalent to script3.py and script4.py, respectively) <br>
The order of running: 1.py--2.py--script6.py--script3.py--script4.py--windowcoords13.py--coordsgc13.py--script2.py<br>
<b>windowgene.py,coordsgcgene.py, script2gene.py</b> - mutational density in all the genome except genes<br>
<b>sortrunnew5.py, sortrunnew5.sh, sortrunnew55.sh</b> - intersection between mutation and quadruplexes/interquadruplexes (sortrunnew5.sh and sortrunnew55.sh are equivalent to sortrunnew5.py - change files in *py, if you want to calculate the intersection for quadruplexes/interquadruplexes) <br>
<b>cosmut.py, cosmut_non_quadr.py</b> - mutational density for COSMIC mutations <br>
<b>bedtoolsgetfasta.py</b> -- intergene.bed coordinates to fasta file
