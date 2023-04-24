#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 11:49:09 2023

Rosalind utilities module

@author: yin
"""

print('You have imported rosalind_utils')
# count nucleotides

def nucl_counter_seqloop(sequence):
    """
    Counts the number of each nucleotide
    
    :param sequence: str, dna sequence
    
    :returns nucl_counts: dict, counts of each nucleotide
    """
    nucl_counts = {'A':0, 'T':0, 'C':0, 'G':0}
    
    for nucl in sequence:
        nucl_counts[nucl] = nucl_counts[nucl] + 1
        
    return nucl_counts

# transcribe

def dna_to_rna_long(sequence):
    """
    Transcribes DNA to RNA, replaces T with U
    
    :param sequence: str, dna sequence
    
    :return rnaseq: str, rna sequence
    """
    rnalist = []
    for nucl in sequence:
        if nucl == 'T':
            rnalist.append('U')
        else:
            rnalist.append(nucl)
    rnaseq = ''.join(rnalist)
    return rnaseq

# reverse complement

def reverse_complement(dnaseq):
    """
    Reverses your sequence and complements it based on
    the complements mapping (see complement_dict)
    
    :param dnaseq: str, dna sequence
    
    :return revcomp_dnaseq: str, dna sequence
    """
    complement_dict = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
    
    # reverse your dna
    rev_dna = dnaseq[::-1]
    # complement your dna
    comp_list = []
    for nucl in rev_dna:
        comp_list.append(complement_dict[nucl])
    
    revcomp_dnaseq = ''.join(comp_list)
    
    return revcomp_dnaseq

if __name__ == '__main__': # if script is run as a standalone program

    seq = 'TCATTCTGACTGCAACGGGCAATATGTCTCT'
    nucl_counts = nucl_counter_seqloop(seq)
    print(nucl_counts)
    transcribed = dna_to_rna_long(seq)
    print(transcribed)
    rev_comp = reverse_complement(seq)
    print(rev_comp)


print('end of script')


