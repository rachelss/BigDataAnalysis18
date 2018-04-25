#!/usr/bin/env python3

from count_kmers import count_kmers
import pytest

#avoid repetition by loading data in advance
@pytest.fixture
def fastq():
    f = open('sample.fastq','r')
    fastq = f.readlines()
    return fastq

#test k = 2 produces 16 kmers
def test_count_kmers(fastq):
#    f = open('sample.fastq','r')
#    fastq = f.readlines()
    counter = count_kmers(2,fastq,{})
    assert len(counter) == 16

#test k = 0 produces 0 kmers
def test_count_kmers0(fastq):
#    f = open('sample.fastq','r')
#    fastq = f.readlines()
    counter = count_kmers(0,fastq,{})
    assert len(counter) == 0
    
#test k = 1000 produces 0
def test_count_kmers1000(fastq):
#    f = open('sample.fastq','r')
#    fastq = f.readlines()
    counter = count_kmers(1000,fastq,{})
    assert len(counter) == 0
    
#test k = -2 produces 0
def test_count_kmers_neg(fastq):
#    f = open('sample.fastq','r')
#    fastq = f.readlines()
    counter = count_kmers(-2,fastq,{})
    assert len(counter) == 0
    
#test k = .3 produces 0
def test_count_kmers_dec(fastq):
#    f = open('sample.fastq','r')
#    fastq = f.readlines()
    counter = count_kmers(.3,fastq,{})
    assert len(counter) == 0
