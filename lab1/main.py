__author__ = "Gabriele Greco"

SEED = 42

import random
import logging

# Generator of sets
def problem(N, seed=None):
    random.seed(seed)
    return [
        list(set(random.randint(0, N - 1) for n in range(random.randint(N // 5, N // 2))))
        for n in range(random.randint(N, N * 5))
    ]
# Greedy Solution
def greedy(N):
    goal = set(range(N))
    covered = set()
    solution = list()
    all_lists = sorted(problem(N, seed=42), key=lambda l: len(l))
    while goal != covered:
        x = all_lists.pop(0)
        if not set(x) < covered:
            solution.append(x)
            covered |= set(x)

    logging.info(
        f"Greedy solution for N={N}: w={sum(len(_) for _ in solution)} nodes={len(solution)} (bloat={(sum(len(_) for _ in solution)-N)/N*100:.0f}%)"
    )
    logging.debug(f"{solution}")

# Algorithm
def My_Solution(N):
    goal = set(range(N)) # my goal, for N = 5 goal = 1, 2, 3, 4, 5
    covered = set() # elements covered
    solution = list() # my solution, list of sets
    all_lists = sorted(problem(N, SEED), key=lambda l: len(l)) # generate all subsets
    start_node = all_lists[-1] # starting node the one with most element
    all_lists.remove(start_node) # removing the node from the list
    solution.append(start_node) # add the node to the solution
    covered = set(start_node) # update covered set
    value = 0  # cost, this is like my h function
               # I want the node with the highest value computed like this
               # It is the difference between the number of same elements (useless elements) between covered and the analyze set
               # and the difference between the new set and covered (new elements)
    new_set = set()

    while goal != covered: # check goal and covered
        for x in all_lists: # start
            if(len(covered - set(x)) + len(set(x) - covered) > value and not all(a in covered for a in x)):
                value = len(covered - set(x)) + len(set(x) - covered)
                new_set = x
        all_lists.remove(new_set)
        solution.append(new_set)
        covered |= set(new_set)
        value = 0 # reset minimum for next round

    logging.info(
        f"My solution for N={N}: w={sum(len(_) for _ in solution)} nodes={len(solution)} (bloat={(sum(len(_) for _ in solution)-N)/N*100:.0f}%)"
    )
    logging.debug(f"{solution}")
    return

def main():
    logging.getLogger().setLevel(logging.INFO)
    for N in [5, 10, 20, 100, 500, 1000]:
        greedy(N)
    for N in [5, 10, 20, 100, 500, 1000]:
       My_Solution(N)

if __name__ == '__main__':
    main()
