#! /usr/bin/env python
#---------------------------------------------------
# get-smearing-pdos.py: read one or a pair alpha,  
# beta spin files with the cp2k pdos format and
# return a file "smeared.dat" with the Smeared DOS
#---------------------------------------------------
# Usage: ./get-smearing-pdos.py ALPHA.pdos BETA.pdos
#        or
#        ./get-smearing-pdos.py file.pdos 
#
# Output: 
#         smeared.dat: smeared DOS
#---------------------------------------------------
# Todo:
# - Atomatic name generation of output file
# - Move the algorithm to the module pdos
# - Implement printing of d orbitals
# - ...
#---------------------------------------------------
# Author: Juan Garcia e-mail: jcgarcia [at] wpi.edu
# Date:   11-12-2012
#---------------------------------------------------

import sys
from pdos import *


if len(sys.argv) == 2:

    infilename = sys.argv[1]

    alpha = pdos(infilename)
    npts = len(alpha.e)
    alpha_smeared = alpha.smearing(npts,0.2)
    eigenvalues = np.linspace(min(alpha.e), max(alpha.e),npts)
    
    g = open('smeared.dat','w')
    for i,j in zip(eigenvalues, alpha_smeared):
        t = str(i).ljust(15) + '     ' + str(j).ljust(15) + '\n'
        g.write(t)

elif len(sys.argv) == 3:

    infilename1 = sys.argv[1]
    infilename2 = sys.argv[2]

    alpha = pdos(infilename1)
    beta = pdos(infilename2)
    npts = len(alpha.e)
    alpha_smeared = alpha.smearing(npts,0.2)
    beta_smeared = beta.smearing(npts,0.2)
    totalDOS = sum_tpdos(alpha_smeared, beta_smeared)
    
    eigenvalues = np.linspace(min(alpha.e), max(alpha.e),npts)

    g = open('smeared.dat','w')
    for i,j in zip(eigenvalues, totalDOS):
        t = str(i).ljust(15) + '     ' + str(j).ljust(15) + '\n'
        g.write(t)

else:
    print ('  Wrong number of arguments!')
    print ('  usage:')
    print ('  ./get-smearing-pdos.py ALPHA.pdos')
    print ('  ./get-smearing-pdos.py ALPHA.pdos BETA.pdos')





