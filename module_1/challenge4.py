from bioinformatics_module import pattern_match, space_join

f = open("Vibrio_cholerae.txt", "r")
genome = f.read()
f.close()

pattern = "ATGATCAAG"

print(space_join(pattern_match(genome, pattern)))
