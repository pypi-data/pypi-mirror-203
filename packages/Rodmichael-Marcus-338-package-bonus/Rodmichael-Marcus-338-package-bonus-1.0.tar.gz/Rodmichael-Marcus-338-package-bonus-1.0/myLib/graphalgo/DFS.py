from .graph import graph

class DFS:
    @staticmethod
    def dfs(graph: graph, vertex: int, visited):
        visited[vertex] = True                           # Mark the current vertex as visited
        print(vertex, end=" ")                           # Print the visited vertex

        for neighbor, _ in graph.graph_structure[vertex]:            # Iterate through the neighbors of the current vertex
            if not visited[neighbor]:                                # If the neighbor has not been visited, perform a DFS on the neighbor
                DFS.dfs(graph, neighbor, visited)


