#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""nucl_counter_seqloop(seq)
Created on Mon Apr 24 11:49:07 2023

Script that calls rosalind sequence analysis functions

@author: yin
"""
import rosalind_utils as r_utils
# from rosalind_utils import nucl_counter_seqloop, ...

seq = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'

# see the functions
#print(dir(r_utils))

nucl_counts = r_utils.nucl_counter_seqloop(seq)
transcribed = r_utils.dna_to_rna_long(seq)
rev_comp = r_utils.reverse_complement(seq)