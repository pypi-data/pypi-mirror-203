from .graph import graph
class Dijkstra:
    @staticmethod
    def dijkstra(graph: graph, start_vertex: int):
        distances = [float('inf')] * graph.order            # Initialize the distances list with infinity for all vertices except the start vertex
        distances[start_vertex] = 0
        visited = [False] * graph.order                     # Create a list to keep track of visited vertices
        priority_queue = [(0, start_vertex)]                # Initialize the priority queue with the start vertex and its distance (0)

        while priority_queue:
            priority_queue.sort(key=lambda x: x[0])          # Sort the priority queue based on the distance
            current_distance, current_vertex = priority_queue.pop(0)          # Pop the vertex with the smallest distance from the priority queue
            if visited[current_vertex]:                                       # If the current vertex has already been visited, skip it
                continue

            visited[current_vertex] = True                                    # Mark the current vertex as visited
            for neighbor, weight in graph.graph_structure[current_vertex]:    # Iterate through the neighbors of the current vertex
                new_distance = current_distance + weight                      # Calculate the new distance to the neighbor
                if new_distance < distances[neighbor]:                        # If the new distance is smaller than the current distance for the neighbor, update it
                    distances[neighbor] = new_distance                        
                    priority_queue.append((new_distance, neighbor))           # Add the updated distance and the neighbor to the priority queue

        return distances                                                      # Return the list of shortest distances from the start vertex to all other vertices
