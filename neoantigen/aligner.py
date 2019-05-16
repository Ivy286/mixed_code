import os
from Bio.Blast import NCBIXML
from Bio import pairwise2
from math import log, exp
from Bio.SubsMat import MatrixInfo as matlist

#
# def __init__(self):
#     # dictionary of computed Ri-values mapped to neoantigen identifiers
#     self.Ri = {}
#     # dictionary of IEDB epitope alignments mapped to neoantigen identifiers
#     self.alignments = {}
#     # dictionary of the highest scoring alignments mapped to neoantigen identifiers
#     self.maximum_alignment = {}
def align(seq1, seq2):
    '''
    Smith-Waterman alignment with default parameters.
    '''
    matrix = matlist.blosum62
    gap_open = -11
    gap_extend = -1
    aln = pairwise2.align.localds(seq1.upper(), seq2.upper(), matrix, gap_open, gap_extend)
    return aln


def readAllBlastAlignments(xmlpath):

    '''
    Read precomputed blastp alignments from xml files,
    compute alignment scores,
    find the highest scoring alignment for each neoantigen.
    '''
    f = open(xmlpath)
    blast_records = NCBIXML.parse(f)
    # print blast_records
    maxscore = {}
    alignments = {}
    maximum_alignment = {}

    try:
        for brecord in blast_records:
            tab = str(brecord.query).split("|")
            # print tab
            ptype = tab[1]
            nid = int(tab[2])
            if ptype == "MUT":
                if not nid in maxscore:
                    maxscore[nid] = 0
                    # print brecord.alignments
                    for alignment in brecord.alignments:
                        if not nid in alignments:
                            alignments[nid] = {}
                            maximum_alignment[nid] = None
                            maximum_alignment[nid] = 0
                            maxscore[nid] = 0
                        species = " ".join((str(alignment).split())[1:-3])
                        for hsp in alignment.hsps:
                            # print hsp
                            if not "-" in hsp.query and not "-" in hsp.sbjct:
                                al = align(hsp.query, hsp.sbjct)
                                print al
                                if len(al) > 0:
                                    al = al[0]
                                    print al[0]
                                    alignments[nid][species] = al
                                    if al[2] > maxscore[nid]:
                                        maximum_alignment[nid] = species
                                        maxscore[nid] = al[2]

    except ValueError:
        print "error"
        pass
    f.close()

if __name__ == '__main__':
    xmlpath = '/home/xh/temp/neoantigen_alignments_Rizvi/neoantigens_AL4602_iedb.xml'
    print os.path.exists(xmlpath)
    readAllBlastAlignments(xmlpath)
