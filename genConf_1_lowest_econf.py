#!/usr/bin/python2.7
# ----------------------------------------------------------
# Copyright (C) 2017 PHARAMACELERA S.L.
# All rights reserved.
# 
# WARRANTY DISCLAIMER
#
# THESE MATERIALS ARE PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL PHARMACELERA OR ITS
# CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
# PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY
# OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY OR TORT (INCLUDING
# NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THESE
# MATERIALS, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
# 
# File: genConf.py
#
# Created on 19/07/2017
# Editer by tianflame on 22/10/2018
# ----------------------------------------------------------
#
# Molecular conformer generator
# The script is only designed to generate the lowest energy conformation from n conformations.  
# 
# Example:
# 
# genConf.py -isdf file_input.sdf -osdf file_output.sdf
# -n number_of_conformers (optional, if not specified is based 
# on the nomber of rotable bonds) -rtpre rms_threshold_pre_opt(optional) 
# -rtpost rms_threshold_post_opt(optional) -e energy_window (optional, Kcal/mol) 
# -t number_of_threads (if not specify 1)
# ----------------------------------------------------------
# ----------------------------------------------------------
import sys
from rdkit import Chem
from rdkit.Chem import AllChem
from concurrent import futures
import progressbar
import os
import argparse
import operator

sys.path.insert(0, './support')
parser = argparse.ArgumentParser(description='Molecular conformer generator')
parser.add_argument('-isdf', required=True, help='sdf input file')
parser.add_argument('-osdf', required=True, help='sdf output file')
parser.add_argument('-n', type=int, required=False, help='number of conformers')
parser.add_argument('-rtpre', type=float, required=False, help='rms threshold pre optimization')
parser.add_argument('-rtpost', type=float, required=False, help='rms threshold post minimization')
parser.add_argument('-e', type=float, required=False, help='energy window')
parser.add_argument('-printproperty', action='store_true', help='Print molecule properties (energy and rotable bond number)')
parser.add_argument('-t', type=int, required=False, help='number of threads')
args = parser.parse_args()

inp = args.isdf
out = args.osdf
 

if args.rtpre == None:
	rmspre = -1
else:
	rmspre = args.rtpre
if args.rtpost == None:
	rmspost = False
else:
	rmspost = args.rtpost
if args.t == None:
	threads = 1
else:
	threads = args.t
if args.e == None:
	ent = "Y"
else:
	ent = args.e

print("=============================================================")
print("The script is only designed to generate the lowest")
print("energy conformation from n conformations!")
print("=============================================================")


writer = Chem.SDWriter(out)
suppl = Chem.SDMolSupplier(inp)    
def genConf(m, nc, rms, efilter, rmspost):
	"""
	diz: [(energy, conf_id)]
	"""		
	nr = int(AllChem.CalcNumRotatableBonds(m))
	m = Chem.AddHs(m)
	Chem.AssignAtomChiralTagsFromStructure(m, replaceExistingTags=True)
	if nc == "X":
		if nr < 3:
                    nc = 50
		elif nr > 6:
		    nc = 300
		else:
                    nc = nr**3
	ids=AllChem.EmbedMultipleConfs(m, numConfs=nc, pruneRmsThresh=rms, randomSeed=1, useExpTorsionAnglePrefs=True, useBasicKnowledge=True)
	diz = []
	diz2 = []
	diz3 = []
	for id in ids:
		try:		
			prop = AllChem.MMFFGetMoleculeProperties(m, mmffVariant="MMFF94s")
			ff = AllChem.MMFFGetMoleculeForceField(m, prop, confId=id)
			ff.Minimize()
			en = float(ff.CalcEnergy())
			econf = (en, id)
			diz.append(econf)
		except:
			diz.append((float(10000), id))		
	#if efilter == "Y":
		#n, diz2 = ecleaning(m, diz, efilter)
	n, diz2 = lowest_conf(m, diz, efilter)
	#print(n)
	#print(diz2)
	"""	
	else:
		n = m
		diz2 = diz	
	if rmspost != False and n.GetNumConformers() > 1:	
		o, diz3 = postrmsd(n, diz2, rmspost) 
	else:
		o = n
		diz3 = diz2
	"""
	
	return n, diz2, nr

def ecleaning(m, diz, efilter):
	#diz = [value for value in diz if not diz]
	diz.sort()
	mini = float(diz[0][0])
	sup = mini + efilter
	n = Chem.Mol(m)
	n.RemoveAllConformers()
	n.AddConformer(m.GetConformer(int(diz[0][1])))
	nid = []
	ener = []
	nid.append(int(diz[0][1]))
	ener.append(float(diz[0][0]))	
	del diz[0]	
	for x,y in diz:
		if x <= sup:
			n.AddConformer(m.GetConformer(int(y)))
			nid.append(int(y))
			ener.append(float(x))
		else:
                    break
	diz2 = zip(ener, nid)
	return n, diz2

	
def lowest_conf(m, diz, efilter):
	"""
	Return the mol_file of lowest energy conformation.
	n: mol_file
	diz: [(energy, conf_id)]
	"""
	diz.sort()
	n = Chem.Mol(m)
	n.RemoveAllConformers()
	n.AddConformer(m.GetConformer(int(diz[0][1])))
	nid = []
	ener = []
	nid.append(int(diz[0][1]))
	ener.append(float(diz[0][0]))
	diz2 = zip(ener, nid)	
	
	return n, diz2
	
	
def postrmsd(n, diz2, rmspost):
	diz2.sort()
	o = Chem.Mol(n)
	o.RemoveAllConformers()
	confidlist = [diz2[0][1]]	
	enval = [diz2[0][0]]
	nh = Chem.RemoveHs(n)
	del diz2[0]
	for z,w in diz2:
		confid = int(w)
		p=0
		for conf2id in confidlist:
			rmsd = AllChem.GetBestRMS(nh, nh, probeConfId=confid, refConfId=conf2id)
			if rmsd < rmspost:
				p=p+1
				break			
		if p == 0:
			confidlist.append(int(confid))
			enval.append(float(z))
	for id in confidlist:
		o.AddConformer(n.GetConformer(id))
	diz3 = zip(enval, confidlist)
	return o, diz3
kk = 0
with futures.ProcessPoolExecutor(max_workers=threads) as executor:
	jobs = []
	nm = []
	numMol=0
	for mol in suppl:
            numMol = numMol+1
            if mol is not None:
                nm.append(mol.GetProp('_Name'))
                #print(mol.GetProp('IDNUMBER'))
                if args.n==None:
                        nc = "X"	
                else:
                        nc = args.n
                job = executor.submit(genConf, mol, nc, rmspre, ent, rmspost)
                jobs.append(job)
            else:
                print( "ERROR: Impossible to generate conformers for molecule number " + str(numMol))
	widgets = ["Generating conformations; ", progressbar.Percentage(), " ", progressbar.ETA(), " ", progressbar.Bar()]
	pbar = progressbar.ProgressBar(widgets=widgets, maxval=len(jobs))
	for job in pbar(futures.as_completed(jobs)):		
		mol,ids,nr = job.result()
	for j in range(0, len(jobs)):
		mol,ids,nr = jobs[j].result()
		name = nm[j]
		for en,id in ids:
			mol.SetProp('_Name', name)
			if args.printproperty == True:
                                mol.SetProp('ConfId', str(id))
                                mol.SetProp('ConfEnergies', str(en)+ " Kcal/mol")
                                mol.SetProp('Rotatable Bonds Number', str(nr))	
                                mol.SetProp('name', 'mol_'+str(kk))
                                kk += 1
			writer.write(mol, confId=id)
writer.close()
