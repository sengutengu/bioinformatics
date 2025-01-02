def count_nucleotides(s):
    """
    Counting DNA Nucleotides

    Given: A DNA string s of length at most 1000 nt.
    Return: Four integers counting the respective number of times that the symbols A C G and T occur in s (as tuple).
    """

    a = 0
    c = 0
    g = 0
    t = 0

    for nt in s:
        if nt == "A":
            a += 1
        elif nt == "C":
            c += 1
        elif nt == "G":
            g += 1
        elif nt == "T":
            t += 1

    return (a, c, g, t)
    
def count_nucleotides_better(s):
    """
    Counting DNA Nucleotides

    Given: A DNA string s of length at most 1000 nt.
    Return: Four integers counting the respective number of times that the symbols A C G and T occur in s (as tuple).

    Cleaner implementation using Python native count() function, and faster too.
    """

    return (s.count("A"), s.count("C"), s.count("G"), s.count("T"))

with open('rosalind_dna.txt', 'r') as file:
    rosalind_dna = file.read()

print(" ".join(str(x) for x in count_nucleotides(rosalind_dna)))