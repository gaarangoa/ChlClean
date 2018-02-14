from parse import parse_sam
from Bio import SeqIO

class Cleaner():

    def __init__(self, reference='', paired_1='', paired_2='', output_path="", cores=8):
        self.reference = reference
        self.paired_1 = paired_1
        self.paired_2 = paired_2
        self.output_path = output_path
        self.cores = cores
        self.bowtie_out_file = self.output_path+'/bowtie.gg.sam'
        self.best_hit_file = self.output_path+'/bowtie.gg.sam.bh'

    def call_bowtie(self):
        # assumes bowtie is installed in your machine
        cmd=" ".join([
            'bowtie2', 
            '--fast-local --no-discordant -p '+self.cores,
            ' --no-unal --no-hd --no-sq -x', self.reference, 
            '-1', self.paired_1, 
            '-2', self.paired_2, 
            '-S', self.bowtie_out_file'>>', self.bowtie_out_file+'.log', '2>&1'
        ])
        os.system(cmd)
        parse_sam(fi = self.bowtie_out_file, fo = self.bes)

    def retrive(self, fi='', listf=''):
        cmd = "filter_fasta.py -f "+self.paired_1+" "+self.paired_1.replace(".fastq","")+".no-chl.fastq -s "+listf+" -n"
        os.system(cmd)
        cmd = "filter_fasta.py -f "+self.paired_2+" "+self.paired_2.replace(".fastq","")+".no-chl.fastq -s "+listf+" -n"
        os.system(cmd)
        

