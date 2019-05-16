# import Bio.PDB
# import urllib2
# import os
#
# file_path = '/home/xh/temp'
# print os.path.exists(file_path)
# n = 0
# for filename in os.listdir(file_path):
#     print filename, n
#     for model in Bio.PDB.PDBParser().get_structure(n, filename):
#         for chain in model:
#             poly = Bio.PDB.Polypeptide.Polypeptide(chain)
#             print "Model %s Chain %s" % (str(model.id), str(chain.id)),
#             print poly.get_phi_psi_list()
#     n += n


import math
import Bio.PDB
def degrees(rad_angle) :
    """Converts any angle in radians to degrees.

    If the input is None, the it returns None.
    For numerical input, the output is mapped to [-180,180]
    """
    if rad_angle is None :
        return None
    angle = rad_angle * 180 / math.pi
    while angle > 180 :
        angle = angle - 360
    while angle < -180 :
        angle = angle + 360
    return angle

def ramachandran_type(residue, next_residue) :
    """Expects Bio.PDB residues, returns ramachandran 'type'

    If this is the last residue in a polypeptide, use None
    for next_residue.

    Return value is a string: "General", "Glycine", "Proline"
    or "Pre-Pro".
    """
    if residue.resname.upper()=="GLY" :
        return "Glycine"
    elif residue.resname.upper()=="PRO" :
        return "Proline"
    elif next_residue is not None \
    and next_residue.resname.upper()=="PRO" :
        #exlcudes those that are Pro or Gly
        return "Pre-Pro"
    else :
        return "General"
import os
input_path = "/home/xh/temp/"
# output_path ="/home/xh/temp"
print os.path.exists(input_path)
list = []
for ele0 in os.listdir(input_path):
    ele1 = ele0[:4]
    ele = ele1.strip()
    # print pdb_code, str(pdb_code)
    print "About to load Bio.PDB and the PDB file..."
    # print "%s.pdb" % pdb_code
    list.append(ele)
print list
for pdb_code in list:
    structure = Bio.PDB.PDBParser().get_structure(pdb_code, "%s.pdb" % pdb_code)
    print "Done"
    print "About to save angles to file..."
    output_file = open("/home/xh/aa/%s_biopython.tsv" % pdb_code, "wb")
    for model in structure:
        for chain in model:
            print "Chain %s" % str(chain.id)
            polypeptides = Bio.PDB.CaPPBuilder().build_peptides(chain)
            for poly_index, poly in enumerate(polypeptides):
                phi_psi = poly.get_phi_psi_list()
                for res_index, residue in enumerate(poly):
                    phi, psi = phi_psi[res_index]
                    if phi and psi:
                        #Don't write output when missing an angle
                        output_file.write("%s:Chain%s:%s%i\t%f\t%f\t%s\n" \
                                          % (pdb_code, str(chain.id), residue.resname,
                                             residue.id[1], degrees(phi), degrees(psi),
                                             ramachandran_type(residue, poly[res_index+1])))
    output_file.close()
    print "Done"
print "tasks have finished!"