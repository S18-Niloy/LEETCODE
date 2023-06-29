class Solution:
    def criticalConnections(self, n, connections):
        graph = [[] for _ in range(n)]  # Adjacency list representation of the graph
        for conn in connections:
            u, v = conn
            graph[u].append(v)
            graph[v].append(u)

        low = [-1] * n  # Lowest depth of each node
        ids = [-1] * n  # Depth of each node
        parent = [-1] * n  # Parent of each node
        bridges = []  # List to store the critical connections

        def dfs(node, curr_id):
            ids[node] = curr_id
            low[node] = curr_id
            curr_id += 1

            for neighbor in graph[node]:
                if ids[neighbor] == -1:
                    parent[neighbor] = node
                    dfs(neighbor, curr_id)
                    low[node] = min(low[node], low[neighbor])

                    if low[neighbor] > ids[node]:
                        bridges.append([node, neighbor])
                elif neighbor != parent[node]:
                    low[node] = min(low[node], ids[neighbor])

        dfs(0, 0)
        return bridges


# Test case
n = 4
connections = [[0, 1], [1, 2], [2, 0], [1, 3]]
solver = Solution()
print(solver.criticalConnections(n, connections))  # Output: [[1, 3]]
