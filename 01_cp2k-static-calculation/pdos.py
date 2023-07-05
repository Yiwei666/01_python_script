#! /usr/bin/env python

from math import pi, sqrt	
import numpy as np

class pdos:
    """ Projected electronic density of states from CP2K output files

        Attributes
        ----------
        atom: str 
            the name of the atom where the DoS is projected
        iterstep: int
            the iteration step from the CP2K job
        efermi: float
            the energy of the Fermi level [a.u]
        e: float
            (eigenvalue - efermi) in eV
        occupation: int
            1 for occupied state or 0 for unoccupied
        pdos: nested list of float
            projected density of states on each orbital for each eigenvalue
            [[s1, p1, d1,....], [s2, p2, d2,...],...]
            s: pdos in s orbitals
            p: pdos in p orbitals
            d: pdos in d orbitals
            .
            .
            .
        tpdos: list of float
            sum of all the orbitals PDOS
            
        Methods
        -------
        smearing(self,npts, width)
            return the smeared tpdos 
    """
    
    def __init__(self, infilename):
        """Read a CP2K .pdos file and build a pdos instance

        Parameters
        ----------
        infilename: str
            pdos output from CP2K. 

        """    
        input_file = open(infilename, 'r')

        firstline  = input_file.readline().strip().split()
        secondline = input_file.readline().strip().split()

        # Kind of atom
        self.atom = firstline[6]
        #iterationstep
        self.iterstep = int(firstline[12][:-1]) #[:-1] delete ","
        # Energy of the Fermi level
        self.efermi = float(firstline[15])

        # it keeps just the orbital names
        secondline[0:5] = []
        self.orbitals = secondline 

        lines = input_file.readlines()
   
        eigenvalue = []
        self.occupation = []
        data = []
        self.pdos = []
        for index, line in enumerate(lines):
            data.append(line.split())
            data[index].pop(0)
            eigenvalue.append(float(data[index].pop(0)))
            self.occupation.append(int(float(data[index].pop(0))))
            self.pdos.append([float(i) for i in data[index]])

        self.e = [(x-self.efermi)*27.211384523 for x in eigenvalue] 

        self.tpdos = []
        for i in self.pdos:
           self.tpdos.append(sum(i))

    def __add__(self, other):
        """Return the sum of two PDOS objects"""
        sumtpdos = [i+j for i,j in zip(self.tpdos,other.tpdos)]
        return sumtpdos

    def delta(self,emin,emax,npts,energy,width):
        """Return a delta-function centered at energy
        
        Parameters
        ----------
        emin: float
            minimun eigenvalue
        emax: float
            maximun eigenvalue
        npts: int
            Number of points in the smeared pdos
        energy: float
            energy where the gaussian is centered
        width: float
            dispersion parameter

        Return 
        ------
        delta: numpy array
            array of delta function values

        """
        
        energies = np.linspace(emin, emax, npts)
        x = -((energies - energy) / width)**2
        return np.exp(x) / (sqrt(pi) * width)

    def smearing(self,npts, width,):
        """Return a gaussian smeared DOS"""

        d = np.zeros(npts)
        emin = min(self.e)
        emax = max(self.e)
        for e, pd in zip(self.e,self.tpdos):
            d +=pd*self.delta(emin,emax,npts,e,width)

        return d
    
def sum_tpdos(tpdos1, tpdos2):
    """Return the sum of two PDOS"""
    return [i+j for i,j in zip(tpdos1,tpdos2)]
            
