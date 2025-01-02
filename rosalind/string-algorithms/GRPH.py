def find_adjacency_list(ss_dict, k):    
    """
    Given: A collection of DNA strings in FASTA format having total length at most 10 kbp.
    Return: The adjacency list corresponding to O_3. You may return edges in any order.
    """
    for key, value in ss_dict.items():
        new_value = (value[:k], value[-k:])
        ss_dict[key] = new_value

    # O(n^2). Not great
    adjacency_list = []
    for key, value in ss_dict.items():
        for i, j in ss_dict.items():
            if ss_dict[key][1] == ss_dict[i][0] and key != i:
                adjacency_list.append(f"{key} {i}")
    return adjacency_list


def find_adjacency_list_faster(ss_dict, k):
    """
    O(n*m) time implementation of solution
    """
    # Create a hash table
    suffix_to_keys = {}
    for key, value in ss_dict.items():
        suffix = value[-k:]
        if suffix not in suffix_to_keys:
            suffix_to_keys[suffix] = []
        suffix_to_keys[suffix].append(key)

    adjacency_list = []
    # n = len(ss_dict)
    for key, value in ss_dict.items():
        prefix = value[:k]
        if prefix in suffix_to_keys:
            # m = 4^k = at most 64 with k=3
            for candidate in suffix_to_keys[prefix]:
                if candidate != key:
                    adjacency_list.append(f"{candidate} {key}")
    return adjacency_list


def parse_FASTA(ss):
    # ss stands for SequenceS
    ss = ss.replace("\n", "").split(">")
    ss_dict = {}
    for s in ss[1:]:
        ss_dict[f'{s[:13]}'] = s[13:]

    return ss_dict


with open('rosalind_grph.txt', 'r') as file:
    rosalind_grph = file.read()

ls = find_adjacency_list_faster(parse_FASTA(rosalind_grph), 3)

for i in ls:
    print(i)
