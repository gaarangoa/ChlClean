
def parse_sam(fi='', identity=80, coverage=25, fox=''):
    BH={}
    for line in open(fi):
        values=line.replace("\n","").split("\t")
        matchedbp=sum([int(x.strip('M')) for x in re.findall(r'(\d*M)', values[5])])
        if  matchedbp<coverage: continue
        try:
            current_best_hit=int(line.split("NM:i:")[1].split()[0])
            prev_best_hit=int(BH[values[0]].split("NM:i:")[1].split()[0])
            if current_best_hit<prev_best_hit:
                BH[values[0]]=line
        except:
            BH[values[0]]=line

    fo = open(fox)
    for i in BH:
        line = BH[i]
        values=line.replace("\n","").split("\t")
        matchedbp=sum([int(x.strip('M')) for x in re.findall(r'(\d*M)', values[5])])
        alignlen=float(len(values[9]))
        read_identity = alignlen/matchedbp
        if read_identity < identity: continue
        if matchedbp < coverage: continue
        fo.write(values[0]+"\n")
    
    fo.close()
        

