__author__ = "Gabriele Greco"

SEED = 42

import random
import logging

# generator of sets
def problem(N, seed=None):
    random.seed(seed)
    return [
        list(set(random.randint(0, N - 1) for n in range(random.randint(N // 5, N // 2))))
        for n in range(random.randint(N, N * 5))
    ]

# Algorithm
def Algorithm(N):
    goal = set(range(N))
    covered = set()
    solution = list()
    all_lists = sorted(problem(N, SEED), key=lambda l: len(l)) # generate all subsets
    start_node = all_lists[-1] # starting node the one with most element
    all_lists.remove(start_node)
    solution.append(start_node)
    covered = set(start_node)
    min = 0  # minimum cost
    new_set = set()

    while goal != covered:
        for x in all_lists:
            if(len(covered - set(x)) + len(set(x) - covered) > min and not all(a in covered for a in x)):
                min = len(covered - set(x)) + len(set(x) - covered)
                new_set = x
        all_lists.remove(new_set)
        solution.append(new_set)
        covered |= set(new_set)
        min = 0 # reset minimum

    logging.info(
        f"Solution for N={N}: w={sum(len(_) for _ in solution)} (bloat={(sum(len(_) for _ in solution)-N)/N*100:.0f}%)"
    )
    logging.debug(f"{solution}")
    return

def main():
    logging.getLogger().setLevel(logging.INFO)
    for N in [5, 10, 20, 100, 500, 1000]:
       Algorithm(N)

if __name__ == '__main__':
    main()
