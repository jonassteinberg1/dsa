import asyncio, random
from typing import Any, Dict, List, Optional

def dfs_topo_sort(graph):
    state = {node: 0 for node in graph}  # 0=unseen, 1=visiting, 2=done
    stack = []
    order = []

    # Loop over every node to handle disconnected components
    for node in graph:
        # Start DFS only for unseen nodes
        if state[node] == 0:
            # Push this node as an entering frame
            stack.append((node, True))

            # Continue while there are frames on the stack
            while stack:
                # Pop the top frame (current node and its entering/leaving status)
                current, entering = stack.pop()

                # Handle entering nodes
                if entering:
                    # If the node is already visiting, we found a cycle
                    if state[current] == 1:
                        raise ValueError(f"Cycle detected at {current}")

                    # If already done, skip it
                    if state[current] == 2:
                        continue

                    # Mark the node as visiting
                    state[current] = 1

                    # Push a leaving frame so we can mark it done later
                    stack.append((current, False))

                    # traverse adjacency list in reverse order
                    # since the stack is lifo
                    for dep in reversed(graph[current]):
                        if state[dep] == 0:
                            stack.append((dep, True))

                # Handle leaving nodes
                else:
                    # Mark node as done (fully processed)
                    state[current] = 2

                    # Add node to the topological order
                    order.append(current)

    # Reverse to get correct topological order
    return order[::-1]


#print(dfs_topo_sort({
#    "A": ["B", "C"],     # A depends on B and C
#    "B": ["D", "E"],     # B depends on D and E
#    "C": ["F", "G"],     # C depends on F and G
#    "D": ["H"],          # D depends on H
#    "E": ["H", "I"],     # E depends on H and I
#    "F": ["I"],          # F depends on I
#    "G": [],             # G has no dependencies
#    "H": ["J"],          # H depends on J
#    "I": ["J"],          # I depends on J
#    "J": []              # J has no dependencies
#}))

async def fetch_node(node: Dict[str, Any], retries=3, base=0.05, cap=0.25) -> Optional[Dict[str, Any]]:
    name = node.get("node", "<unknown>")
    attempt = 0
    while True:
        try:
            # simulate network latency
            await asyncio.sleep(random.uniform(0.03, 0.12))
            # raise RuntimeError("flaky")  # flip on to test retries
            return node  # in your case, you’d parse/validate this dict
        except Exception:
            attempt += 1
            if attempt > retries:
                return None
            # full-jitter backoff
            await asyncio.sleep(random.uniform(0, min(cap, base * (2 ** (attempt - 1)))))

async def collect_nodes_taskgroup(nodes: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    results: List[Optional[Dict[str, Any]]] = [None] * len(nodes)
    async with asyncio.TaskGroup() as tg:
        for i, n in enumerate(nodes):
            tg.create_task(_wrap_fetch(i, n, results))
    # all tasks are done when we exit the block
    return [r for r in results if r is not None]

async def _wrap_fetch(i: int, n: Dict[str, Any], results: List[Optional[Dict[str, Any]]]) -> None:
    try:
        results[i] = await fetch_node(n)
    except Exception:
        results[i] = None  # swallow to avoid cancelling siblings

nodes = [{'node': 'node-1',
  'gpus': [{'id': 0,
    'utilization': 65,
    'memory_used': 10240,
    'memory_total': 16384},
   {'id': 1, 'utilization': 20, 'memory_used': 4096, 'memory_total': 16384}]},
 {'node': 'node-2',
  'gpus': [{'id': 0,
    'utilization': 50,
    'memory_used': 8192,
    'memory_total': 16384},
   {'id': 1, 'utilization': 70, 'memory_used': 11264, 'memory_total': 16384}]},
 {'node': 'node-3',
  'gpus': [{'id': 0,
    'utilization': 15,
    'memory_used': 2048,
    'memory_total': 16384},
   {'id': 1, 'utilization': 40, 'memory_used': 6144, 'memory_total': 16384}]}]

print(asyncio.run(collect_nodes_taskgroup(nodes)))
