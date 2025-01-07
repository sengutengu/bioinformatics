def find_rev_c(s):
    return s[::-1].translate(str.maketrans("ATGC", "TACG"))

def find_rev_p(s):
    rev_p_list = []
    for length in range(4, 12+1):
        for i in range(len(s)-length+1):
            fragment = s[i:i+length]
            if fragment == find_rev_c(fragment):
                rev_p_list.append((i+1, fragment))
    return rev_p_list

with open("rosalind_revp.txt", "r") as file:
    ss = file.read()

s = ss.replace("\n","")[14:]
print(s)

#s = "TCAATGCATGCGGGTCTATATGCAT"

for i in find_rev_p(s):
   print(f'{i[0]} {len(i[1])}')
