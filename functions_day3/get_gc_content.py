"""
Calculate the GC content of the following sequences:
"""

sequence1 = 'GCGATACGTCGCGCTAGGGCCCATATTATAACGCGCTAGGCTATCGATTTATATATCGCGCGCGGGGGGCCAATATAAAAATCCCATTCCGGGG'
sequence2 = 'ATATAAAACCCGGGGAACGATTATCGACGCCGACTACACTACGATCGAGCGATCATTATATCGCAACACACAATATAAAAAAATTTCGCGC'
sequence3 = 'ATATATATTTTATTATATTTATATATTATATATATTATAAAAAAAAAAATTTATATATATAT'
sequence4 = 'GGGGGGGGGGCCGCCCCCCCCCGCGGCCCCCCCCCCCCCCGCGCGCGGGGGCGGCGCGGGGGGCCC'

yourseq = sequence2
GC_count = 0

#### with for-loop
# counts our occurrences of G or C
for nucl in yourseq:
    if nucl == 'C' or nucl =='G':
        GC_count += 1
    
print(f'You counted {GC_count} Gs and Cs')

GC_percent = 100 * (GC_count/len(yourseq))

print(f'Your GC percentage is: {GC_percent:.5f}!')

#### with str.count() method
GC_count_new = yourseq.count('G') + yourseq.count('C')
GC_percent_new = 100 * (GC_count_new/len(yourseq))
print(GC_percent_new)


              
