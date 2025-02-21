def find_unbalanced(graph):
    '''
    Find unbalanced nodes in a nearly balanced graph with a Eulerian path.
    '''
    sources = graph.keys()
    dests = sum(list(graph.values()), []) # list of arrow destinations
    all_nodes = set(list(sources) + list(dests))
    odds_dict = {}
    for node in all_nodes:
        if node in sources:
            n = len(graph[node]) # number of outdegrees
        else:
            n = 0
        for node2 in dests:
            if node == node2:
                n -= 1
        if n % 2 != 0:
            odds_dict[n] = node

    return odds_dict[1], odds_dict[-1]
    
def eulerian_cycle(graph):
    
    def random_walk(graph, current_node):
        '''
        Complete a cycle by walking through an Eulerian graph randomly.
        '''
        cycle = [current_node]
        while True:
            if current_node in graph.keys(): # if we're not stuck
                next_node = random.choice(graph[current_node])
                cycle.append(next_node)
    
                # remove new edge to be traversed from future consideration
                if len(graph[current_node]) > 1:
                    graph[current_node].remove(next_node)
                else:
                    graph.pop(current_node)
                    
                current_node = next_node
            else:
                break
        return cycle, graph

    def prev_cycle(cycle, new_start):
        '''
        Once new start node is selected, shift previous cycle to begin
        with new start node. 
        '''
        new_start_index = cycle.index(new_start) # all nodes are unique so this is fine
        return cycle[new_start_index:] + cycle[1:new_start_index+1]
    
    current_node = random.choice(list(graph.keys()))    
    cycle, graph = random_walk(graph, current_node)

    while len(graph) > 0:
        # choose new node to start from, given the previous iteration's cycle. 
        # if node is **left** in graph.keys(), i.e. still has unused outgoing edge(s)
        new_start = random.choice([node for node in cycle if node in graph.keys()])
        
        prev = prev_cycle(cycle, new_start)
        new, graph = random_walk(graph, new_start)
        cycle = prev + new[1:]
    
    return cycle

def eulerian_path(graph):
    orig, term = find_unbalanced(graph)
    graph.setdefault(term, []).append(orig) # add temporary edge to graph

    path = eulerian_cycle(graph)[:-1]

    # slice Eulerian cycle at temporary edge
    for i in range(len(path)-1):
        if path[0] == orig and path[len(path)-1] == term:
            return path
        if [path[i], path[i+1]] == [term, orig]:
            return path[i+1:] + path[0:i+1]
    
    return path


def read_pairs(k, d, text):
    pairs = []
    for i in range(len(text)-2*k-d+1):
        pairs.append([text[i:i+k], text[i+k+d:i+2*k+d]])
    pairs.sort()
    return pairs

def string_from_gapped_patterns(gapped_patterns, k, d):
    first_patterns = [p.split("|")[0] for p in gapped_patterns]
    second_patterns = [p.split("|")[1] for p in gapped_patterns]
    prefix_string = path_to_genome(first_patterns)
    suffix_string = path_to_genome(second_patterns)
    print(k)
    print(d)
    print(prefix_string)
    print(prefix_string[:k+d])
    print(suffix_string)
    for i in range(k+d+1, len(prefix_string)):
        if prefix_string[i] != suffix_string[i-k-d]:
            return "No string spelled by gapped patterns"
    return prefix_string[:k+d] + suffix_string

def de_bruijn_from_paired_kmers(patterns):
    adjacency_list = {}
    for p in patterns:
        pair = p.split("|")
        pref = f'{prefix(pair[0])}|{prefix(pair[1])}'
        suff = f'{suffix(pair[0])}|{suffix(pair[1])}'
        adjacency_list.setdefault(pref, []).append(suff)
    return adjacency_list


def gapped_string_reconstruction(patterns, k, d):
    graph = de_bruijn_from_paired_kmers(patterns)
    print(graph)
    gapped_patterns = eulerian_path(graph)
    print(gapped_patterns)
    return string_from_gapped_patterns(gapped_patterns, k, d)


f = open("input_3.txt", "r")
readin = f.read().split("\n")
k = int(readin[0].split(" ")[0])
d = int(readin[0].split(" ")[1])
patterns = readin[1].split(" ")

print(k)
print(d)

gapped_string_reconstruction(patterns, k, d)