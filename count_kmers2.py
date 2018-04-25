#!/usr/bin/env python3

import glob
import pandas
import matplotlib.pyplot as plt
import sys

def count_kmers(k,fastq,counter={}):
    if k > 0 and type(k) is int:
        for line_num,line in enumerate(fastq):
            if line_num%4 == 1:
                line = line.rstrip()
                for i,base in enumerate(line[:-k+1]):
                    kmer = line[i:i+k]
                    assert len(kmer) == k, \
                    "Trying to add incorrect kmer: " +\
                    kmer+ " from line " + str(line_num) +\
                    " position " + str(i)
                    if kmer in counter:
                        counter[kmer] += 1
                    else:
                        counter[kmer] = 1
    return(counter)

def plot_kmer_freq(counter):
    w = range(len(counter))
    values = counter.values()
    labels = counter.keys()

    plt.figure(figsize = (10,4))
    plt.bar(w, values, tick_label = labels);
    plt.savefig('kmer_freq.png')

if __name__ == "__main__":
    counter = {}
    k = int(sys.argv[1])
    if k > 0:
        for filename in glob.glob('*.fastq'):
            f = open(filename,'r')
            fastq = f.readlines()
            counter = count_kmers(k,fastq,counter)
        #print(counter)
        print('Number of kmers: ',len(counter))
        print('Number of possible kmers: ',4**k)
        
        plot_kmer_freq(counter)
    else:
        print('k should be > 0')
