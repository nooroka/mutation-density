import sys
op = open("comp{}_out_gene.txt".format(sys.argv[1]),"r")
w = open("comp{}_out_gene_quadr.txt".format(sys.argv[1]),"w")
i = 0
for line in op:
    line = line.strip()
    line = line.split()
    if len(line)>0:
        if ":" in line[0]:
           # print(line)
            inter = line[0]
            line2 = line[0].split(":")
            line22 = line2[1].split("-")
           # print("ok "+str(line2[0])+" "+str(line22[0]))
            name = line2[0]
        if len(line) == 8 and "ID" not in line:
            coord1 = line22[0]
            a = int(coord1)+int(line[1])-10+1 #учитываем, что bed, переводим в txt
            b = int(coord1)+int(line[4])+10
            w.write(str(inter)+"\t"+str(name)+"\t"+str(a)+"-"+str(b)+"\n")
            i+=1
        #print(line)
w.close()
op.close()
