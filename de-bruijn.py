from platform import node
import re
import sys

nodes={}
nodes_degree={}


def euler_theorem():
    odd_degree_nodes =0
    for key in nodes_degree.keys():
        odd_degree_nodes += abs(nodes_degree[key]) % 2

    if odd_degree_nodes == 0:
        print("an eulerian CYCLE exists")
        return 2
    elif odd_degree_nodes == 2:
        print("an eulerian PATH exists")
        return 1
    else:
        print("this graph is not traversable")
        return 0

def generate_dot_graph(filename):
    f = open(f"{filename}.dot", "w")
    f.write("digraph debruijn {\n")

    for key in nodes.keys():
        for el in nodes[key]:
            print(f"{key}, {el}")
            f.write(f'{key} [label="{key} °{nodes_degree[key]}"];\n')
   
    for key in nodes.keys():
        for el in nodes[key]:
            print(f"{key}, {el}")
            f.write(f"{key} -> {el} [label= {key+ el[-1]}];\n")

    f.write("}")
    f.close()



def hierholzer():
    if euler_theorem() == 0:
        return

    tpath = [] #temporary stack
    epath = [] # where the eulerian path will be at the end

    not_visited_edges = []
    for key in nodes.keys():
        for el in nodes[key]:
            not_visited_edges.append((key, el))
    
    #choose a suitable vertex -> start at the vertex with one more outgoing edge,
    #  end at the vertex with one more incoming edge!
    outgoing_edges = 0
    for key in nodes.keys():
        if len(nodes[key]) > outgoing_edges:
            outgoing_edges = len(nodes[key])
            v = key

    tpath.append(v)
    
    while(len(tpath)>0):
        u = tpath[-1]
        already_in_visited = 0
        # all outgoing edges from u have been visited?
        for edges in nodes[u]:
            if (u,edges) not in not_visited_edges: already_in_visited+=1
        
        # yes: pop u from tpath and push it to epath
        if already_in_visited == len(nodes[u]):
            epath.append(tpath.pop())
        
        # no: select a random edge (u,x), push x to tpath and mark (u,x) as visited       
        else:
            for x in nodes[u]:
                if (u,x)  in not_visited_edges: 
                    tpath.append(x)
                    not_visited_edges.remove((u,x))
                    break
    
    epath.reverse()
    print(epath)


            



# for generating the image install graphwiz and run
# $ dot -Tsvg {filename} > {output_name.svg}
genome = input("enter the sequence: ")
genome = re.sub('[^ACGT]', '', genome)
if len(genome) == 0: genome = 'TCATTCTTCAGGTCAAA'
print(f"here is the genome: {genome}")

k_mer_size = int(input("enter the k-mer size:"))
print(f"here is the k-mer size: {k_mer_size}")

while(k_mer_size>len(genome) or k_mer_size<=2):
    print("the k-mer size has to be less or equal to the length of the sequence and greater than two:")
    k_mer_size = int(input("enter the k-mer size:"))

for i in range(0,len(genome)-k_mer_size+1):
    print(f"kmer->{genome[i:i+k_mer_size]}")
    if genome[i:i+k_mer_size-1] not in nodes.keys():
        nodes[genome[i:i+k_mer_size-1]] = list()
        print(f"aggiungo il nodo {genome[i:i+k_mer_size-1]}")
    
    if genome[i+1 : i+k_mer_size] not in nodes_degree.keys():
      nodes_degree[genome[i+1:i+k_mer_size]] = 0

    if genome[i:i+k_mer_size-1] not in nodes_degree.keys():
     nodes_degree[genome[i:i+k_mer_size-1]] = 0


    nodes[genome[i:i+k_mer_size-1]].append(genome[i+1:i+k_mer_size])
    
    
    #degree is degree_in - degree_out 
    nodes_degree[genome[i:i+k_mer_size-1]]-=1
    nodes_degree[genome[i+1 : i+k_mer_size]]+=1



if len(sys.argv) == 2:
    generate_dot_graph(sys.argv[1])
else:
    generate_dot_graph("default_name_for_graph")

euler_theorem()
hierholzer()
