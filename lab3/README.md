# Description of the Game (Wikipedia)
Nim is a mathematical game of strategy in which two players take turns removing objects from a distinct heap or piles. On each turn, a player must remove at least one object, and may remove any number of objects provided they all come from the same heap or pile.
- `Goal: in order to win we need to take the last object`

# Solutions & Results
## 1) My Solution

- Game played: we play `10`, `100`, `1000` games vs differents opponents
- `Rows` number: a random value from `5 to 13`
- Upperbound `k` of matches taken each round: a random value from `2 to 7`
- The file of task 1 is `1_my_solution.ipynb`
- The games have been player starting as `first player` (starts with first move) or `second player` (starts with  second move)
- I Nim Class is the one used in by professor

Description

- `my_strategy`: is really simple strategy that select the shortest row and it does 3 different operations depending on the value of matches
1. if matches <= k: close the row selecting all the matches
2. if matches > k*2: select k matches
3. if matches between (k) and (k*2) it (select row elements - k) matches

##### I played against different strategies
- `pure_random`: pick a random row and select random matches (matches < k)
- `shortest_row`: take the shortest row and select random matches if row elements > k otherwise close the row selecting all matches
- `optimal_solution`: nim-sum solution used by professor in class that use brute force to compute the best move

##### Results vs shortest row
- INFO:root:Game played = 10: Winrate 1° player = 60.0% 
- INFO:root:Game played = 100: Winrate 1° player = 45.0% 
- INFO:root:Game played = 1000: Winrate 1° player = 42.6% 
- INFO:root:Game played = 10: Winrate 2° player = 30.0% 
- INFO:root:Game played = 100: Winrate 2° player = 45.0% 
- INFO:root:Game played = 1000: Winrate 2° player = 39.7% 

##### Results vs pure random
- INFO:root:Game played = 10: Winrate 1° player = 90.0% 
- INFO:root:Game played = 100: Winrate 1° player = 92.0% 
- INFO:root:Game played = 1000: Winrate 1° player = 84.1% 
- INFO:root:Game played = 10: Winrate 2° player = 80.0% 
- INFO:root:Game played = 100: Winrate 2° player = 83.0% 
- INFO:root:Game played = 1000: Winrate 2° player = 85.8% 

##### Results vs optimal strategy
- INFO:root:Game played = 10: Winrate 1° player = 10.0% 
- INFO:root:Game played = 100: Winrate 1° player = 5.0% 
- INFO:root:Game played = 1000: Winrate 1° player = 7.2% 
- INFO:root:Game played = 10: Winrate 2° player = 10.0% 
- INFO:root:Game played = 100: Winrate 2° player = 5.0% 
- INFO:root:Game played = 1000: Winrate 2° player = 5.4% 

## 2) Evolution Algorithm
- The file of task 2 is `2_GA.ipynb` 
- For this task I've been working with: [Davide Aiello - Github](https://github.com/davideaiello/CI22-23_s303296). He had the idea of using evolutionary algorithm in order to find the best strategy to play the game, and then we coded together the solution
- I Nim Class is the one used in by professor
- population_size = `20`, offspring_size = `10`, num_generations = `100`, tournament_size = `2`, genetic_operator_randomness for mutation = `0.7`
- `Number of games` played: `100`
- `Rows` number: `11`
- Upperbound `k` of matches taken each round: `6`

Description
- For our solution we used a genetic algorithm. The population individuals are compose by the fitness value and 5 genome values from 0 to 1, one for each strategy, the bigger the value is the more the system will converge to that strategy. The mutation selected randomically which strategy to mutate recalculating the genome weight (we used a weighted average). One of the important function of our program is `compute_fitness` that compute the fitness which is the number of games won vs our opponent. In the end we combine the genetic information we use `uniform_cross_over` that based of the value of i put information of parent1 or parent2.

##### Differents strategy used
1. `shortest_row`: take the shortest row and select random matches if row elements > k otherwise close the row selecting all matches
2. `Davide_strategy`: find all the possibles moves and then:
- if there are more than 1 moves, select a random row and select the maximum number of matches than he can take (elements < k)
- otherwise select random elements from the row (elements < k)
3. `GabriG_strategy`: is the my_strategy use in task 1 (see above the description)
4. `longest_row`: take the longest row and select random matches if row elements > k otherwise close the row selecting all matches
5. `pure_random`: pick a random row and select random matches (matches < k)

##### We played against
- `pure_random`: pick a random row and select random matches (matches < k)

##### Results against pure random
INFO:root:The best strategy is GabriG_strategy with 97.0% winrate (fitness)

## 3) MinMax
- Working in progress

## 4) Reinforcement learning
- Working in progress