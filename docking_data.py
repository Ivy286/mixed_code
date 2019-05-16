import os
import logging
import gzip
from collections import defaultdict


_FLOATX = 'float32'
_INTX = 'int32'
_UID_PREFIXES = defaultdict(int)
_GRAPH_DICT = {}
_EPSILON = 1e-6
LOSS = 'total_loss'


def get_uid(prefix=''):
    _UID_PREFIXES[prefix] += 1
    return _UID_PREFIXES[prefix]



def split_blocks_by_starts(filename, start_string):
    """
    usefull for read .fasta, .mol2 files

    >>> blocks = [['start line\n', 'middel 11\n', 'middel 12\n', 'middel 13\n'], ['start line\n', 'middel 21\n', 'middel 22\n', 'middel 23\n']]

    >>> filename = '/tmp/split_blocks_test.txt'
    >>> with open(filename, 'wb') as f:
            for block in blocks:
                f.write(''.join(block))

    >>> blocks_new = split_blocks_by_starts(temp_file, start_string='start line')
    >>> print(blocks_new == blocks)
    True
    """
    blocks = []
    if filename.endswith('.gz'):
        open_fn = gzip.open
    else:
        open_fn = open

    with open_fn(filename, mode='r') as f:
        count = 0
        lines = []
        for l in f.readlines():
            try:
                flag_start = l.startswith(start_string)
            except:
                flag_start = l.startswith(bytes(start_string, encoding='utf-8'))

            if flag_start:
                if len(lines) > 0:
                    blocks.append(lines)
                    lines = [l]
                else:
                    lines.append(l)
            else:
                lines.append(l)
        if len(lines) > 0:
            blocks.append(lines)
            
    return blocks


def split_blocks_by_ends(filename, end_string):
    blocks = []
    if filename.endswith('.gz'):
        open_fn = gzip.open
    else:
        open_fn = open

    with open_fn(filename, 'r') as f:
        lines = []
        for l in f:
            lines.append(l)
            if l.startswith(end_string):
                blocks.append(lines)
                lines = []

        assert l.startswith(end_string), (
                'last line: "{0}" does not start with "{1}"'.format(l, end_string))
        return blocks

    
def write_block(blocks, dir_path, filenames):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    def write_one(string_list, mol2file):
        with open(mol2file, 'w') as f:
            for s in string_list:
                f.write(s)

    for b, n in zip(blocks, filenames):
        output_file = os.path.join(dir_path, n)
        write_one(b, output_file)

def exact_mol2(): 

