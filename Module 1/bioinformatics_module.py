"""
Functions for Bioinformatics course
"""


def space_join(array):
    """
    Convert an array into a string with a space
    in between each item.
    """
    return " ".join([str(i) for i in array])


def pattern_count(text, pattern):
    """
    Returns the number occurrences of a pattern in the text.

    Args:
        text (str): the text.
        pattern (str): the pattern.

    Returns:
        count (int): the number of occurrences
    """
    count = 0
    for i in range(0, len(text)-len(pattern)+1):
        if text[i:i+len(pattern)] == pattern:
            count += 1
    return count


def frequency_table(text, k):
    """
    Returns a frequency table of k-mers in a text.

    Args:
        text (str): The text.
        k (int): the length of the k-mers.

    Returns:
        freq_map (dict): The map of each k-mer to its frequency.
    """
    freq_map = {}
    n = len(text)
    # indexing excludes end of range so must add +1 to n-k
    for i in range(0, n-k+1):
        pattern = text[i:i+k]
        if pattern not in freq_map:
            freq_map[pattern] = 1
        else:
            freq_map[pattern] += 1
    return freq_map


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


def frequent_words(text, k):
    """
    Returns the most frequent k-mers from a text.

    Args:
        text (str): the text.
        k (int): the length of the k-mers.

    Returns:
        frequent_patterns (list): the most frequent k-mers.
    """
    frequent_patterns = []
    freq_map = frequency_table(text, k)
    max_num = maxmap(freq_map)
    for pattern, freq in freq_map.items():
        if freq == max_num:
            frequent_patterns.append(pattern)
    return frequent_patterns


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


def pattern_match(genome, pattern):
    """
    Returns all starting positions in genome
    where pattern appears as a substring.

    Args:
        genome (str): the genome.
        pattern (str): the pattern.

    Returns:
        staring_positions (list): a list of indices
        where the pattern starts in the genome.
    """
    starting_positions = []
    for i in range(0, len(genome)-len(pattern)+1):
        if genome[i:i+len(pattern)] == pattern:
            starting_positions.append(i)
    return starting_positions


def find_clumps(text, k, L, t):
    """
    Return k-mer patterns found in clumps
    of size t within a window of length L.

    It was challenging to create an O(n) algorithm
    but it is leagues faster than an O(c^n) algorithm!

    Args:
        text (str): the text.
        k (int): the k-mer length.
        L (int): the length of the window.
        t (int): the base clump size.

    Returns:
        patterns (list): a list of patterns found in clumps.
    """
    patterns = []

    # Loop 0
    window = text[0:L]  # NOT text[0:L+1]
    freq_map = frequency_table(window, k)

    # Run this only in Loop 0 for O(n) algorithm
    for pattern, freq in freq_map.items():
        if freq >= t:
            patterns.append(pattern)

    # Loop 1 and on
    for i in range(1, len(text)-L+1):
        previous_first_k_mer = text[i-1:i+k-1]
        window = text[i:i+L]
        last_k_mer = window[-k:]

        # Decrement frequency of PREVIOUS first k-mer
        freq_map[previous_first_k_mer] -= 1

        # CURRENT first k-mer was counted in
        # previous loop, so no increment!

        # Increment frequency of last k-mer
        if last_k_mer not in freq_map:
            freq_map[last_k_mer] = 1
        else:
            freq_map[last_k_mer] += 1

        if freq_map[last_k_mer] >= t:
            patterns.append(last_k_mer)

    patterns = list(set(patterns))
    return patterns
