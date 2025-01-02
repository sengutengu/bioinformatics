def transcribe_RNA(s):
    """
    Given: A DNA string t having length at most 1000 nt.
    Return: The transcribed RNA string of t.
    """
    return s.replace("T", "U")

s = "GATGGAACTTGACTACGTAAATT"

with open('rosalind_rna.txt', 'r') as file:
    rosalind_rna = file.read()

print(transcribe_RNA(rosalind_rna))