"""
This module was written for Johns Hopkins University's
Python for Bioinformatics Course.
"""


def gc(dna):
    """Returns the GC percentage of a DNA sequence."""
    dna = dna.upper()
    nbases = dna.count("N")  # undefined bases.
    gcpercent = 100*float((dna.count('C')+dna.count('G'))/(len(dna)-nbases))
    return gcpercent


print(gc("AAAGTNNAGTCC"))
help(gc)
