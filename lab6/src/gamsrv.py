import heapq
from typing import List, Tuple, Set

def find_optimal_server_latency(
    num_nodes: int,
    clients: Set[int],
    edges: List[Tuple[int, int, int]]
) -> int:

    graph = {i: [] for i in range(1, num_nodes + 1)}
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))

    ans = float('inf')
    servers = [i for i in range(1, num_nodes + 1) if i not in clients]

    for s in servers:
        dist = {i: float('inf') for i in range(1, num_nodes + 1)}
        dist[s] = 0
        pq = [(0, s)]

        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[u]:
                continue
            for v, w in graph[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    heapq.heappush(pq, (dist[v], v))

        max_c_dist = max((dist[c] for c in clients), default=float('inf'))
        
        if max_c_dist < ans:
            ans = max_c_dist

    return int(ans) if ans != float('inf') else -1


def solve(input_file: str = "gamsrv.in", output_file: str = "gamsrv.out") -> None:
    with open(input_file, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]

    if not lines:
        return

    n, m = map(int, lines[0].split())
    clients = set(map(int, lines[1].split()))

    edges = []
    for line in lines[2:2 + m]:
        u, v, w = map(int, line.split())
        edges.append((u, v, w))

    optimal_latency = find_optimal_server_latency(n, clients, edges)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(f"{optimal_latency}\n")


if __name__ == "__main__":
    solve()