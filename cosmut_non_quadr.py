#mutation density (COSMIC) for space between quadruplexes
import subprocess
w = open("mutdensgene_non_quadr2.txt","a")
for i in range(1,25,1):
    d5 = subprocess.check_output("wc -l gccoords_{}_un.bed".format(i),shell = True)   
    d1 = subprocess.check_output('wc -l mutcos{}.bed'.format(i),shell = True)#number of mutations
    d55 = d5.decode().split()[0]
    d11 = d1.decode().split()[0]
    sum1 = int(d55)*52#multiplying by interval length
    w.write("chr{}".format(i)+"\t"+str(float(int(d11)/int(sum1)))+"\n")#mutation density
w.close()
