from Bio.SeqIO.QualityIO import FastqGeneralIterator
import sys

fi = 'EMinf.fq'

for _id,seq,qual in FastqGeneralIterator(open(fi)):
    header = _id.split(' ')[0] 
    read = '@%s\n%s\n+\n%s' %(_id,seq,qual)
    break
