"""
Functions for Bioinformatics course
"""


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


def better_frequent_words(text, k):
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
