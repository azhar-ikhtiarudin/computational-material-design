from ase import Atoms
from ase.io.vasp import write_vasp, read_vasp
from ase.visualize import view
import os
from ase.neb import NEB

IS = read_vasp('POSCAR1')
FS = read_vasp('POSCAR2')

nimg = int(input("Number of images: "))
images = [IS]
images += [IS.copy() for i in range(nimg)]
images +=[FS]

idpp = input("IDPP[y] or linear[n]: ")
neb = NEB(images)
if idpp == 'y' or 'Y':
    neb.interpolate('idpp',mic=True)
else:
    neb.interpolate(mic=True)

for i in range (len(neb.images)):
    os.system("mkdir 0"+str(i))
    write_vasp('POSCAR',neb.images[i],direct=True,long_format=True,vasp5=True,ignore_constraints=False,wrap=False)
    os.system("mv POSCAR 0"+str(i)+"/.")
	
