def hamming(s1, s2):
    """
    Find Hamming distance between two strings
    """
    dist = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            dist += 1
    return dist


def immediate_neighbors(pattern):
    # Challenging!
    neighborhood = []
    for i in range(len(pattern)):
        symbol = pattern[i]
        nts = ["A", "T", "G", "C"]
        nts.remove(symbol)
        for j in nts:
            neighbor = pattern[:i] + j + pattern[i+1:]
            neighborhood.append(neighbor)
    return neighborhood


def neighbors(pattern, d):
    # handle edge cases first
    if d == 0:
        return [pattern] # absolutely necessary to return list
    if len(pattern) == 1:
        return ["A", "T", "G", "C"]
    neighborhood = []
    suffix_neighbors = neighbors(pattern[1:], d)
    for text in suffix_neighbors:
        if hamming(pattern[1:], text) < d:
            for nt in ["A", "T", "G", "C"]:
                neighborhood.append(nt+text)
        else:
            neighborhood.append(pattern[0]+text)
    return neighborhood


def maxmap(input_map):
    """
    Returns the maximum value (not key) in a map.

    Args:
        input_map (dict): the map (type(value) == int)

    Returns:
        max_value (int): the maximum value.
    """
    max_value = max(input_map.values())
    return max_value


def reverse_complement(pattern):
    """
    Returns the reverse complement of a DNA pattern.

    Args:
        pattern (str): the DNA pattern.

    Returns:
        reversed_pattern (str): the reverse complement of the DNA pattern.
    """
    reversed_pattern = pattern[::-1]
    reverse_complement_pattern = ""
    complement_dict = {"A": "T", "T": "A", "G": "C", "C": "G"}
    for char in reversed_pattern:
        reverse_complement_pattern += complement_dict[char]
    return reverse_complement_pattern


def frequent_words_with_mismatches(text, k, d):
    """
    text == text
    k == length of k-mer
    d == allowed number of mismatches
    *** most frequent word does not have to be in the text itself
    """

    patterns = []
    freq_map = {}

    n = len(text)

    for i in range(n-k+1):
        pattern = text[i:i+k]
        neighborhood = neighbors(pattern, d)
        for j in range(len(neighborhood)):
            neighbor = neighborhood[j]
            if neighbor not in freq_map.keys():
                freq_map[neighbor] = 1
            else:
                freq_map[neighbor] += 1
    m = maxmap(freq_map)

    for pattern, value in freq_map.items():
        if value == m:
            patterns.append(pattern)

    return patterns

def frequent_words_with_mismatches_and_rc(text, k, d):
    """
    text == text
    k == length of k-mer
    d == allowed number of mismatches
    *** most frequent word does not have to be in the text itself
    """

    patterns = []
    freq_map = {}

    n = len(text)

    for i in range(n-k+1):
        pattern = text[i:i+k]
        neighborhood = neighbors(pattern, d)
        for j in range(len(neighborhood)):
            neighbor = neighborhood[j]
            rc = reverse_complement(neighbor)
            if neighbor not in freq_map.keys():
                freq_map[neighbor] = 1
            else:
                freq_map[neighbor] += 1
            if rc not in freq_map.keys():
                freq_map[rc] = 1
            else:
                freq_map[rc] += 1
    m = maxmap(freq_map)

    for pattern, value in freq_map.items():
        if value == m:
            patterns.append(pattern)

    return patterns

# For Salmonella enterica, 

f = open("salmonella_enterica.txt", "r")
genome = f.read().replace("\n", "")
f.close()

minskew = 3764856
window = genome[minskew-500:minskew+500]

print(" ".join([i for i in frequent_words_with_mismatches(window, 9, 1)]))