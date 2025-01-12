string = "GAGCCACCGCGATA"
def find_skew_list(string):
    skew_list = [0]
    skew = 0
    for i in string:
        if i == "G":
            skew += 1
        elif i == "C":
            skew -= 1
        skew_list.append(skew)
    return skew_list

print(" ".join([str(i) for i in find_skew_list(string)]))
