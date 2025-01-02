def find_substring_positions(s, t):
    """
    Given: Two DNA strings s and t (each of length at most 1 kbp).
    Return: All locations of t as a substring of s.
    """
    indices = []
    for i in range(0, len(s)):
        if s[i:i+len(t)] == t:
            indices.append(str(i+1))
    return " ".join(indices)

with open('rosalind_subs.txt', 'r') as file:
    rosalind_subs = file.read().split("\n")

s = rosalind_subs[0].rstrip()
t = rosalind_subs[1].rstrip()

print(find_substring_positions(s, t))