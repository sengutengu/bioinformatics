import random

def cycle_to_graph(cycle):
    cycle_graph = {}
    for i in range(len(cycle)-1):
        cycle_graph[cycle[i]] = [cycle[i+1]]
        
    return cycle_graph


def random_path(current_graph, current_node):
    cycle = [current_node]
    while True:
        if current_node in current_graph.keys():
            next_node = random.choice(current_graph[current_node])
            cycle.append(next_node)
            if len(current_graph[current_node]) > 1:
                current_graph[current_node].remove(next_node)
            else:
                current_graph.pop(current_node)
            current_node = next_node
        else:
            break
    return cycle, current_graph
    
def eulerian_cycle(graph):
    current_graph = graph.copy()
    current_node = random.choice(list(current_graph.keys()))    

    cycle, current_graph = random_path(current_graph, current_node)
    cycle_graph = cycle_to_graph(cycle)
    while len(current_graph) > 0:
        new_start = random.choice([node for node in cycle if node in current_graph.keys()])
        print(new_start)
        
        cycle, current_graph = random_path(cycle_graph, new_start)
        cycle, current_graph = random_path(current_graph, cycle[-1]
    
    print(cycle)
    print(current_graph)
    #while len(current_graph) > 0: