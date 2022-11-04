# Computational Intelligence 2022/2023 Repository
- Student: Gabriele Greco
- ID: s303435

# Lab 2: Set Covering with EA (Evolutionary Algorithm)

The code is in the directory lab2, name of the file `main.ipynb`.
- `Libraries`: list of packages used
- `Data initialization and functions`: constants used and algorithm functions (evaluate, tournament, cross_over and mutation
- `Initial Population`: function to create the population
- `Evolution`: main function of the program

I started working from the solution One Max made by professor in class and then I adapted to the Set Covering problem, creating my fitness evaluation function.

This is a list of major variables:
- `N` = number of elements
- `population` = number of sets 
- `population_size` = len(population) (N * 5)
- `mutation_rate` = 0.55, I started from
- `offspring_size` = population_size / 2 (int)
- `NUM_GENERATIONS` = equal to N * 2, it scale with N because form small number of N after some computation we reach the steady state, so further iterations are useless

I've tried differents values of mutation_rate and kept 0.55 which is the best one. With lower and higher value we don't obtain good results for higher N values.
INFO:root: Solution for N=5: w=5 (bloat=0%) Fitness calls=60
INFO:root: Solution for N=10: w=10 (bloat=0%) Fitness calls=462
INFO:root: Solution for N=20: w=27 (bloat=35%) Fitness calls=714
INFO:root: Solution for N=50: w=79 (bloat=58%) Fitness calls=10813
INFO:root: Solution for N=100: w=176 (bloat=76%) Fitness calls=43027
INFO:root: Solution for N=500: w=1314 (bloat=163%) Fitness calls=905809
