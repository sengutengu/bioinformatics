from bioinformatics_module import pattern_count

text = "TACGTACCGTCGTTTCCGTCAAACCACCCCGGCGTACCGCGCATGCCTCGTACCGTCCGTACCGGCGCGTACCGCGTACCGGAACTCTCTCGTACCGACGTACCGATCGTACCGTCGTACCGGGGTCGGGTCTTAGCGTACCGCGTACCGGAAACCGTACCGGGATTCGTACCGTCTGGTAGACACGGACGTACCGCCGTACCGACGTACCGTGACGTACCGACCCGTACCGCGTACCGTTCGTACCGTGCAAGATCGTACCGTCGTACCGAGCACGTACCGCGTACCGCCGTACCGGGCGTACCGACGTACCGACGTACCGCCCCGTACCGCGTACCGCGTACCGCGTACCGTACGAGTCGTACCGAGGTTGCGTACCGCTCCGTACCGCGAGATGCCCGTACCGCCGTACCGATACTATGACCGTACCGCGTACCGCGTACCGATACGTACCGAGAACGTACCGCCGTACCGTTAACGTACCGCGTACCGGCCGTACCGTCCCGTACCGGCGTACCGACGTACCGCCGTACCGACCGTACCGCGTACCGTCCGTACCGGCGTACCGCGTACCGCGTACCGGTACCGTACCGGCGTACCGAGGACGTACCGGTCTCGTACCGTCGTACCGAGGCCGTACCGTTTCGTACCGCGTACCGAACGTACCGCGTACCGGTCGTACCGGGGCGTACCGCTCCGTACCGAGGGGAATGATCCGTACCGCGTACCGGTGGCCCTATACGTACCGCGTACCGCGTACCGGCGTACCGCCGTACCGCGTACCGCACGTACCGCGTACCGCGTACCGACGCGTACCGGTCCCCGTACCGGCCCCGTACCGCGTACCGCCGTACCGCCTACGTACCGTCCGTACCGTCGTACCGCGTACCGGACCGTACCGACACGTACCGCGTACCGGTCCGTACCGTAGGCGTACCGGGAGGATCTCGCTACGTACCGTCTCGTACCGCACGTACCGATACGTACCGTTTGCTTACCCGTACCGCGTACCG"
pattern = "CGTACCGCG"

print(pattern_count(text, pattern))