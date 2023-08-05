from graphalgo.graph import Graph


def main():

    g = Graph(directed=False)
    g.add_edge('A', 'B', 3)
    g.add_edge('A', 'C', 1)
    g.add_edge('B', 'D', 5)
    g.add_edge('C', 'D', 2)
    g.add_edge('C', 'E', 4)
    g.add_edge('D', 'E', 1)


    print("Graph order:", g.order)
    print("Graph size:", g.size)
    print("DFS:")
    g.dfs('A')
    print("\nBFS:")
    g.bfs('A')
    print("\nDijkstra:")
    distances = g.dijkstra('A')
    for vertex, distance in distances.items():
        print(f"{vertex}: {distance}")


if __name__ == '__main__':
    main()