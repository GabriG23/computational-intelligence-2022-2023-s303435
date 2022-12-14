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
2. `Davide_strategy`: it finds all the possibles moves then selects a random row and takes always at least k objects. If there is no upperbound for that row, it takes all of the objects. If there are no rows with more then one object, it starts to take one object random from the remained rows.
3. `GabriG_strategy`: is the my_strategy use in task 1 (see above the description)
4. `longest_row`: take the longest row and select random matches if row elements > k otherwise close the row selecting all matches
5. `pure_random`: pick a random row and select random matches (matches < k)

##### We played against
- `pure_random`: pick a random row and select random matches (matches < k)
- `optimal_solution`: nim-sum solution used by professor in class that use brute force to compute the best move

##### Results against pure random and optimal_strategy
INFO:root:The best strategy is GabriG_strategy with 97.0% winrate (fitness)
INFO:root:The best strategy is shortest_row with 14.0% winrate (fitness)

## 3) MinMax
For this task I've created code starting from the minimax pseudocode on [wikipedia](https://en.wikipedia.org/wiki/Minimax).
- The setup is the same one used for the other tasks. The main algorithm is composed by 3 functions:
- `find_best_move`: starting from all the possible moves of that position I compute the best move evaluating it with minmax_min function, that return the value of the best move. If the value is greater than the current want, I swap the move
- `minmax_nim`: it first check the value returned by the evaluation function, the depth, the possible moves and return 0 if it these values are not satisfied. Then it procede going down with the tree checking if we need to do our move or opponents move and compute the value of the node
- `evaluation`: check the current position and return -1 if we lost, 1 if we won and 0 if we neither won or lost
- to reduce computational time I chose a `depth bound equal to 4`

##### I played against
- `pure_random`: pick a random row and select random matches (matches < k)
- `optimal_strategy`: nim-sum solution used by professor in class that use brute force to compute the best move
- `shortest_row`: take the shortest row and select random matches if row elements > k otherwise close the row selecting all matches

### Results
- I played 100 and 1000 games for each strategy as first and second player
##### vs optimal strategy
1. with rows = 3 and k = 1 I obtained 100% win rate if I start first and 0% if I starts second. This is the other way around with rows = 4 as I win 100% of time as second player and 0% as first player
2. with k = 2 and rows > 5 I obtained from 5% to 10% winrate as both first and second player
- Below there are the overall result with randoms rows (from 3 to 6) and random upper bound k (from 1 to 4)
- INFO:root:Game played = 100: Winrate 1° player = 12.0% 
- INFO:root:Game played = 1000: Winrate 1° player = 13.3% 
- INFO:root:Game played = 100: Winrate 2° player = 18.0% 
- INFO:root:Game played = 1000: Winrate 2° player = 13.0% 
##### vs pure_random
- INFO:root:Game played = 100: Winrate 1° player = 44.0% 
- INFO:root:Game played = 1000: Winrate 1° player = 44.2% 
- INFO:root:Game played = 100: Winrate 2° player = 45.0% 
- INFO:root:Game played = 1000: Winrate 2° player = 43.4% 
##### vs shortest_row
- INFO:root:Game played = 100: Winrate 1° player = 22.0% 
- INFO:root:Game played = 1000: Winrate 1° player = 23.5% 
- INFO:root:Game played = 100: Winrate 2° player = 32.0% 
- INFO:root:Game played = 1000: Winrate 2° player = 22.8% 

## 4) Reinforcement learning
- I started from the code of Maze uploaded by Andrea Calabrese and then made some changes for my solution.
- The `Nim Class` is the same as the solutions above, I just added a get reward function that return 1 if the game is won, -1 if lost or 0 if None of them.
- I played againt `simple_strategy` (take always 1 from a random row), `pure_random`, `shortest_row` and `optimal_solution`
- `Agent`:
1. `init`: initialize all the variable and the vector G, which is a vector containing all the possible moves that we can execute
2. `choose_action`: from all the possible action pick the one with highest value of G
3. `update_state_history`: update the story after every made move
4. `learn`: the agent learn at the end of a game going through all history
- Main Function: I played 1000 games vs each strategy, counting the number of win after 100 games. 

I did not have much time to work on this last task due to personal issue, but it seems like there's no "learning" after each block of games, but the results are always the same for each strategy. This is probably due to a bad choice of G, some others state could be the state of rows in the current games + all the available moves

- vs pure random
- INFO:root:Game played = 100: Winrate = 51.0% 
- INFO:root:Game played = 300: Winrate = 44.0% 
- INFO:root:Game played = 500: Winrate = 49.0% 
- INFO:root:Game played = 700: Winrate = 51.0% 
- INFO:root:Game played = 900: Winrate = 46.0% 
- vs shortest row
- INFO:root:Game played = 100: Winrate = 31.0% 
- INFO:root:Game played = 300: Winrate = 23.0% 
- INFO:root:Game played = 500: Winrate = 31.0% 
- INFO:root:Game played = 700: Winrate = 26.0% 
- INFO:root:Game played = 900: Winrate = 31.0% 
- vs optimal
- INFO:root:Game played = 100: Winrate = 6.0% 
- INFO:root:Game played = 300: Winrate = 2.0% 
- INFO:root:Game played = 500: Winrate = 3.0% 
- INFO:root:Game played = 700: Winrate = 3.0% 
- INFO:root:Game played = 900: Winrate = 2.0%
- vs simple strategy
- INFO:root:Game played = 100: Winrate = 60.0% 
- INFO:root:Game played = 300: Winrate = 49.0% 
- INFO:root:Game played = 500: Winrate = 51.0% 
- INFO:root:Game played = 700: Winrate = 59.0% 
- INFO:root:Game played = 900: Winrate = 63.0% 