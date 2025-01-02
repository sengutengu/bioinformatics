def compute_gc(ss_dict):
    """
    Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
    Return: The FASTA ID of the string having the highest GC-content, followed by the GC-content of that string.
    """
    highest_gc_key, highest_gc_value = "", 0
    for key, value in ss_dict.items():
        gc_only = value.count("G") + value.count("C") # count function is super handy
        gc_value = 100*gc_only/len(value)
        if gc_value > highest_gc_value:
            highest_gc_key, highest_gc_value = key, gc_value
    
    return highest_gc_key, highest_gc_value


def parse_FASTA(ss):
    # ss stands for SequenceS
    ss = ss.replace("\n", "").split(">")
    ss_dict = {}
    for s in ss[1:]:
        ss_dict[f'{s[:13]}'] = s[13:]

    return ss_dict

with open('rosalind_gc.txt', 'r') as file:
    rosalind_gc = file.read()

print(compute_gc(parse_FASTA(rosalind_gc)))