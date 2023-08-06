from .graph import graph

class BFS:
    @staticmethod
    def bfs(graph: graph, start_vertex: int):
        visited = [False] * graph.order             # Create a list to keep track of visited vertices
        queue = [start_vertex]                      # Initialize the queue with the start vertex

        visited[start_vertex] = True                # Mark the start vertex as visited

        while queue:                                # Iterate until the queue is empty
            vertex = queue.pop(0)                   # Pop the first vertex from the queue
            print(vertex, end=" ")                  # Print the visited vertex

            for neighbor, element in graph.graph_structure[vertex]:     # Iterate through the neighbors of the current vertex
                if not visited[neighbor]:                               # If the neighbor has not been visited, mark it as visited and add it to the queue
                    visited[neighbor] = True
                    queue.append(neighbor)