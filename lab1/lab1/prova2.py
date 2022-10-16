__author__ = "Gabriele Greco"

SEED = 42

from cmath import inf
import random
import logging
from gx_utils import *
from collections import deque

# generator of sets
def problem(N, seed=None):
    random.seed(seed)
    return [
        list(set(random.randint(0, N - 1) for n in range(random.randint(N // 5, N // 2))))
        for n in range(random.randint(N, N * 5))
    ]

# Greedy solution
def greedy(N):
    goal = set(range(N))
    covered = set()
    solution = list()
    all_lists = sorted(problem(N, SEED), key=lambda l: len(l))
    while goal != covered:
        x = all_lists.pop(0)
        if not set(x) < covered:
            solution.append(x)
            covered |= set(x)

    logging.info(
        f"Greedy solution for N={N}: w={sum(len(_) for _ in solution)} (bloat={(sum(len(_) for _ in solution)-N)/N*100:.0f}%)"
    )
    logging.debug(f"{solution}")


# A* solution

def reconstruct_path(cameFrom, current):
    total_path = {current}
    while current in cameFrom:
        current = cameFrom[current]
        total_path.remove(current)
    return total_path

def h(state):
    return len(state)

def A_star_algorithm(N):
    goal = set(range(N))
    covered = set()
    optimal_solution = list()
    all_lists = sorted(problem(N, SEED), key=lambda l: len(l))
    start = all_lists[-1] # starting node the one with most element
    # The set of discovered nodes that may need to be (re-)expanded.
    # Initially, only the start node is known.
    # This is usually implemented as a min-heap or priority queue rather than a hash-set.
    openSet = {tuple(start)}

    # For node n, cameFrom[n] is the node immediately preceding it on the cheapest path from start to n currently known.
    cameFrom = dict()

    # For node n, gScore[n] is the cost of the cheapest path from start to n currently known.
    g = dict() # map with default value of Infinity
    g[tuple(start)] = 0

    # For node n, fScore[n] := gScore[n] + h(n). fScore[n] represents our current best guess as to
    # how cheap a path could be from start to finish if it goes through n.
    f = dict() # map with default value of Infinity
    f[tuple(start)] = h(start)

    while openSet is not None:
        # This operation can occur in O(Log(N)) time if openSet is a min-heap or a priority queue
        # current = the node in openSet having the lowest fScore[] value
        
        current = None
        for v in openSet:
            if current == None or g[v] + h(v) < g[current] + h(current): # if n == None or cost[v] + self.h(v) < cost[n] + self.h(n):
                current = v 

        optimal_solution.append(current)
        covered |= set(current)

        if covered == goal:
            return reconstruct_path(cameFrom, current)

        openSet.remove(current)
        for neighbor in all_lists:
            # d(current,neighbor) is the weight of the edge from current to neighbor
            # tentative_gScore is the distance from start to the neighbor through current
            tentative_gScore = g[current] + 1
            if tentative_gScore < len(neighbor): #g[tuple(neighbor)]
                # This path to neighbor is better than any previous one. Record it!
                cameFrom[tuple(neighbor)] = current
                g[tuple(neighbor)] = tentative_gScore
                f[tuple(neighbor)] = tentative_gScore + h(neighbor)
                if tuple(neighbor) not in openSet:
                    openSet.add(tuple(neighbor))

    #Open set is empty but goal was never reached
    logging.info(
        f"A* solution for N={N}: w={sum(len(_) for _ in optimal_solution)} (bloat={(sum(len(_) for _ in optimal_solution)-N)/N*100:.0f}%)"
    )
    logging.debug(f"{optimal_solution}")



def main():
    logging.getLogger().setLevel(logging.INFO)
    # A* solution
    for N in [5, 10, 20, 100, 500, 1000]:
       A_star_algorithm(N)

if __name__ == '__main__':
    main()
