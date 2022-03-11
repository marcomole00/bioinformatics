import re
import sys

nodes={}
nodes_degree={}


def euler_theorem():
    odd_degree_nodes =0
    for key in nodes_degree.keys():
        odd_degree_nodes += nodes_degree[key] % 2

    if odd_degree_nodes == 0:
        print("an eulerian CYCLE exists")
        return True
    elif odd_degree_nodes == 2:
        print("an eulerian PATH exists")
        return True
    else:
        print("this graph is not traversable")
        return False

def generate_dot_graph(filename):
    f = open(f"{filename}.dot", "w")
    f.write("digraph debruijn {\n")

    for key in nodes.keys():
        for el in nodes[key]:
            print(f"{key}, {el}")
            f.write(f"{key}{nodes_degree[key]}° -> {el}{nodes_degree[el]}° [label= {key+ el[-1]}];\n")

    f.write("}")
    f.close()



def hierholzer():
    
    tpath = [] #temporary stack
    epath = [] # where the eulerian path will be at the end
    





# for generating the image install graphwiz and run
# $ dot -Tsvg {filename} > {output_name.svg}
genome = input("enter the sequence: ")
genome = re.sub('[^ACGT]', '', genome)
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
    
    nodes_degree[genome[i:i+k_mer_size-1]]+=1
    
    nodes_degree[genome[i+1 : i+k_mer_size]]+=1



if len(sys.argv) == 2:
    generate_dot_graph(sys.argv[1])
else:
    generate_dot_graph("default_name_for_graph")

euler_theorem()
