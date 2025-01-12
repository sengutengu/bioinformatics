def find_minimum_skew(string):
    index = 0
    skew = 0
    minimum = 0
    min_indices = []
    for i in string:
        if i == "G":
            skew += 1
        elif i == "C":
            skew -= 1
        index += 1
        
        if skew < minimum:
            min_indices = []
            min_indices.append(index)
            minimum = skew
        elif skew == minimum:
            min_indices.append(index)
    return min_indices 


f = open("salmonella_enterica.txt", "r")
genome = f.read()
f.close()


print(" ".join([str(i) for i in find_minimum_skew(genome)]))

# For S. enterica, the min skew seems to be at 3818639 and 3818641. 
# OK. So we expect ori to be somewhere around here.