def hamming(s1, s2):
    """
    Find Hamming distance between two strings
    """
    dist = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            dist += 1
    return dist


def approx_pattern_match(pattern, text, d):
    """
    Find all approximate matches with Hamming distance <= d
    """
    approx_matches = []
    for i in range(len(text)-len(pattern)+1): # range is non-inclusive
        compared_text = text[i:i+len(pattern)]
        if hamming(pattern, compared_text) <= int(d):
            approx_matches.append(i)
    return approx_matches

def approx_pattern_count(pattern, text, d):
    """
    Find the number of approximate matches
    """
    return len(approx_pattern_match(pattern, text, d))

f = open("approx_count.txt", "r")
input = f.read().split("\n")
f.close()

p = input[0]
t = input[1]
d = input[2]

print(approx_pattern_count(p, t, d))