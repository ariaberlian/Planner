"""
PLANNER

Program Topological Sort untuk penyelesaian masalah pengambilan rencana kuliah
Asumsi : Kuliah dan pre-requisite nya berupa Directed Acyclic Graph (DAG)
"""

# sol   : array of solution
# graph : array of tuple (prec, succ)


def read_file():

    # data  : matriks of data
    # data_perline : array of data per line

    graph = []
    data = []
    fn = input("Masukkan nama file (lengkap dengan alamat, cth:'D:\coba.txt'): ")
    f = open(fn, "r")
    for line in f:
        data_perline = line.replace(".", "").rstrip()
        data_perline = data_perline.split(", ")
        data.append(data_perline)

    for i in range(len(data)):
        last = True
        for j in range(len(data)):
            if j == i:
                continue
            else:
                for k in range(len(data[j])):
                    if data[i][0] == data[j][k]:
                        graph.append((data[i][0], data[j][0]))
                        last = False
        if last:
            graph.append((data[i][0], None))

    f.close()
    return graph


def countInDegree(graph, el):
    count = 0
    for i in range(len(graph)):
        if graph[i][1] == el:
            count += 1
    return count


def deleteTuple(graph, el):
    i = 0
    while i < len(graph) and graph != []:
        if graph[i][0] == el:
            graph.pop(i)
            if len(graph) != 0:
                i -= 1
        else:
            i += 1
    return graph


def topo_sort(graph):
    sol = []
    j = 0
    need_to_delete = []
    while graph != []:
        i = 0
        sol.append(set())
        while i < len(graph):
            if countInDegree(graph, graph[i][0]) == 0:
                sol[j].add(graph[i][0])
            i += 1
        
        sol[j] = list(sol[j])
        for i in range(len(sol[j])):
            graph = deleteTuple(graph, sol[j][i])

        j += 1
    return sol

### Driver
g = read_file()
sol = topo_sort(g)

for i in range(len(sol)):
    print("Semester", i + 1, ":", end='')
    for j in range(len(sol[i])):
        if j != len(sol[i])-1:
            print(sol[i][j], ",", end='')
        else:
            print(sol[i][j])
    print('')
