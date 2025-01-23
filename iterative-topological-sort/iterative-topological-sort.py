from queue import deque

def deployment_order(graph: dict, in_degree: dict) -> list:
    q = deque()
    results = []
    for d in in_degree:
        if in_degree[d] == 0:
            q.append(d)
    while len(q) > 0:
        service = q.popleft()
        results.append(service)
        for g in graph[service]:
            in_degree[g] -= 1
            if in_degree[g] == 0:
                q.append(g)
    cycles = [service for service in in_degree if in_degree[service] != 0]
    if cycles:
        raise Exception(f"Cycle Exists After Ordering: {cycles}")
    else:
        return results

deployment_order({'db': ['app', 'cache'], 'app': ['proxy'], 'cache': [], 'proxy': []}, {'db': 0, 'app': 1, 'cache': 1, 'proxy': 1})
