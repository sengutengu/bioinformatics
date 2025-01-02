def reverse_complement(s):
    """
    Given: A DNA string s of length at most 1000 bp.
    Return: The reverse complement s^c of s.
    """
    reverse = s[::-1]
    
    rc = ""
    for i in reverse:
        if i == "A":
            rc += "T"
        if i == "T":
            rc += "A"
        if i == "G":
            rc += "C"
        if i == "C":
            rc += "G"
    return rc

def reverse_complement_better(s):
    complement_dict = {"A": "T", "T": "A", "G": "C", "C": "G"}
    return "".join(complement_dict[nt] for nt in s[::-1])

def reverse_complement_even_better(s):
    return s[::-1].translate(str.maketrans("ATGC", "TACG"))

with open("rosalind_revc.txt", "r") as file:
    rosalind_revc = file.read()

print(reverse_complement_even_better(rosalind_revc))
