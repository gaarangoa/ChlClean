## Chloroplast removal tool

This is a simple tool that removes all 16s rRNAs-like reads from a paired-end sample. By using Bowtie2 paired end reads are screened against the 16S-rRNAs from the greengenes database and removed from the samples. 

### Requirements

    Bowtie2
    BioPython

### Instalation

    python setup.py install
    pip install . --upgrade

### Usage

    clremove clear --paired-1 ./test/r1.fq --paired-2 ./test/r2.fq --out-dir ./test/

### output files
The files with filtered chloroplast reads are stored as 
    
    *.no-chl.fastq
