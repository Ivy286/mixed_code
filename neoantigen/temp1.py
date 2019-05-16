from Bio.Blast import NCBIXML
from Bio.SubsMat import MatrixInfo as matlist
from Bio import pairwise2

# mulseq1 = '/home/xh/temp/neoantigen_alignments_Rizvi/neoantigens_AL4602.fasta'
# mulseq2 ='/home/xh/temp/iedb.fasta'
#
#
def align(seq1, seq2):
    '''
    Smith-Waterman alignment with default parameters.
    '''
    matrix = matlist.blosum62
    gap_open = -11
    gap_extend = -1
    aln = pairwise2.align.localds(seq1.upper(), seq2.upper(), matrix, gap_open, gap_extend)
    return aln
#
# if __name__ == '__main__':
#     align(mulseq1, mulseq2)
from Bio.pairwise2 import format_alignment
from math import log
# def gap_function(x, y):
#
#     if y == 0:
#         return 0
#     elif y == 1:
#         return -2
#     return - (2+y/4.0+log(y)/2.0)
# print pairwise2.align.globalmc("ACCCCCGT", "ACG", 5, -4, gap_function, gap_function)
# matrix = matlist.blosum62
# print pairwise2.align.localds("ACCCCCGT", "ACG", 5, -4, matrix)

# for a in pairwise2.align.globaldx('KEVLE', 'EVL', matrix):
#     print format_alignment(*a)
#
# for a in pairwise2.align.localxx('ACCGT', 'ACG'):
#     print format_alignment(*a)
xmlpath = '/home/xh/temp/neoantigen_alignments_Rizvi/neoantigens_AL4602_iedb.xml'
f = open(xmlpath)
blast_records = NCBIXML.parse(f)
for brecord in blast_records:
    # print brecord
    for alignment in brecord.alignments:
        # print alignment
        for hsp in alignment.hsps:
            print hsp.query, hsp.sbjct
            print align(hsp.query, hsp.sbjct)