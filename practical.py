
def get_powerset(V):
    P = [[]]
    for i in V:
        E_1 = [i]
        P.append(E_1)
    for i in V:
        for j in range(i + 1, len(V) + 1):
            E_2 = [i, j]
            P.append(E_2)
    for i in V:
        for j in range(i + 1, len(V) + 1):
            for k in range(j + 1, len(V) + 1):
                E_3 = [i, j, k]
                P.append(E_3)
    for i in V:
        for j in range(i + 1, len(V) + 1):
            for k in range(j + 1, len(V) + 1):
                for l in range(k + 1, len(V) + 1):
                    E_4 = [i, j, k, l]
                    P.append(E_4)
    for i in V:
        for j in range(i + 1, len(V) + 1):
            for k in range(j + 1, len(V) + 1):
                for l in range(k + 1, len(V) + 1):
                    for m in range(l + 1, len(V) + 1):
                        E_5 = [i, j, k, l, m]  
                        P.append(E_5)
    return P


def verify_solution(G, S):
    for v in S:
        ...
    return False


def find_vertex_cover(G):
    vertices = list(G.keys())
    powerset = get_powerset(vertices)
    print(powerset)
    for subset in powerset:
        is_valid = verify_solution(G, subset)
        if is_valid:
            return subset
    return vertices


if __name__ == "__main__":
    # Sample graph with vertices n = 5 and edges m = 5
    graph = {1: [2, 5],
             2: [3, 4],
             3: [4],
             4: [],
             5: []}
    print(find_vertex_cover(graph))