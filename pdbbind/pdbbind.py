import csv


class target(object):

	def __init__(self, name):
		self._name = name
		self._ids = []
		self._ligdir = {}
		self._errorflag = {}

	def name(self):
		if '/' in self._name: 
			self._name = self._name.replace('/', ' or ')
		return self._name

	def ids(self):
		if self._ids == []:
			print('no ids')
		else:
			return self._ids

	def editids(self, sign, id):
		if sign == '+':
			self._ids.append(id)
			self._errorflag[id] = 0
			self._ligdir[id] = '/home/dongha/Desktop/v2015/' + id + '/' + id + '_ligand.mol2'
		elif sign == '-':
			self._ids.remove(id)
			self._errorflag.pop(id)
			self._ligdir.pop(id)
		else:
			print('sign error')

	def ligdir(self, id):
		return self._ligdir[id]

	def similarity(self, id):
		return similarityfrommol2(self.ligdir(self.ids()[0]), self.ligdir(id))

	def tanimoto(self, id):
		with open('/home/dongha/Desktop/ligs_merged/rpt/{}_1.rpt'.format(self.name()), 'r') as rpt:
			t = list(csv.DictReader(rpt, delimiter='\t'))
		for i in t:
			if id == i['Name'][:4]:
				return i['TanimotoCombo']
		raise ValueError('Can\'t get tanimotocombo!')

	def errorflag(self, id):
		return self._errorflag[id]

	def cherrorflag(self, id):
		self._errorflag[id] = 1
		return self._errorflag


import matplotlib.pyplot as mp
from rdkit import Chem
from rdkit import DataStructs
from rdkit.Chem import MolFromMol2File, MACCSkeys
from rdkit.Chem.EState.Fingerprinter import FingerprintMol


def MACCS_keys_similarity(mol_1, mol_2):
	fps_1 = MACCSkeys.GenMACCSKeys(mol_1)
	fps_2 = MACCSkeys.GenMACCSKeys(mol_2)
	similarity = DataStructs.FingerprintSimilarity(fps_1, fps_2)
	return similarity


def similarityfrommol2(mol2_file, mol1_file):
	mol_1 = Chem.MolFromMol2File(mol2_file, sanitize=False)
	mol_2 = Chem.MolFromMol2File(mol1_file, sanitize=False)
	return MACCS_keys_similarity(mol_1, mol_2)


def init():
	with open('/home/dongha/Desktop/v2015/INDEX_general_PL_name.2015', 'r') as f:
		cont = f.readlines()
		cont_ = []
	for i in cont[6:]:
		i_ = i.strip().split()
		newtarget = target(' '.join(i_[3:]))
		targetexistedflag = 0
		for c in cont_:
			if newtarget.name() == c.name():
				c.editids('+', i_[0])
				targetexistedflag = 1
		if not targetexistedflag:
				newtarget.editids('+', i_[0])
				cont_.append(newtarget)
	return cont_
'''
#take 1st lig
for t in cont_:
	if len(t.ids()) > 50:
		print('proceeding with {}'.format(t.name()))
		try:
			with open(t.ligdir(t.ids()[0]), 'r') as f:
				lig_1st = f.read()
		except IOError:
			with open(t.ligdir(t.ids()[1]), 'r') as f:
				lig_1st = f.read()
		with open('/home/dongha/Desktop/ligs_merged/{}_1st.mol2'.format(t.name()), 'w') as f:
			f.write(lig_1st)
print('fin')

'''

'''

#merge ligs of each target to one file
errornum = 0
for t in cont_:
	if len(t.ids()) > 50:
		print('proceeding with {}'.format(t.name()))
		errornum_ = 0
		merged = 0
		ligs = ''
		for i in t.ids():
			try:
				with open(t.ligdir(i), 'r') as f:
					ligs = ligs + f.read() + '\n'
				merged = merged + 1
			except IOError:
				errornum_ = errornum_ + 1
		errornum = errornum + errornum_
		with open('/home/dongha/Desktop/ligs_merged/{}.mol2'.format(t.name()), 'w') as f:
			f.write(ligs)
		print('total_ids: {}; merged_ids: {}; errornum: {}'.format(len(t.ids()), merged, errornum_))
print('total_errors:', errornum)
print('fin')
'''

'''
#cal similarity, tanimotocombo and save
for c in init():
	simi, tani = [], []
	if len(c.ids()) > 50:
		for id in c.ids():
			try:
				simi.append(str(c.similarity(id)))
			except:
				c.cherrorflag(id)
			if not c.errorflag(id):
				try:
					tani.append(str(c.tanimoto(id)))
				except ValueError:
					simi.pop()
		with open('/home/dongha/Desktop/tani_simi.txt', 'a') as f:
			f.write('Name: ' + c.name() + '\n')
			f.write('similarity,' + ','.join(simi) + '\n')
			f.write('tanimotocombo,' + ','.join(tani) + '\n')
'''

'''
#draw nubmer of ligands for each target
x = []
y = []
for index, c in enumerate(cont_):
	x.append(index)
	y.append(len(c.ids()))
	if len(c.ids()) > 50:
		print(len(c.ids()),c.name())
	if c.name() == 'EPIDERMAL GROWTH FACTOR RECEPTOR':
		print(len(c.ids()),c.name())
#mp.bar(x, y)
#mp.show()
'''


