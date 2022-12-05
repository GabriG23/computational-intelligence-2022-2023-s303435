# Description of the Game (Wikipedia)
Nim is a mathematical game of strategy in which two players take turns removing objects from a distinct heap or piles. On each turn, a player must remove at least one object, and may remove any number of objects provided they all come from the same heap or pile.
- `Goal: in order to win we need to take the last object`

# Solutions & Results
## 1) My Solution
The solution
- Game played: we play `10`, `100`, `1000` games vs differents opponents
- `Rows` number: a random value from `5 to 13`
- Upperbound `k` of matches taken each round: a random value from `2 to 7`
- The file of task 1 is `1_my_solution.ipynb`
- The games have been player starting as `first player` (starts with first move) or `second player` (starts with  second move)
- I Nim Class is the one used in by professor

##### Different strategies
- `my_strategy`: really simple strategy that select the shortest row and it does 3 different operations depending on the value of matches
1. if matches <= k: close the row selecting all the matches and win
2. if matches > k*2: select k matches
3. if matches between (k) and (k*2) it select (matches - k - 1) in order to always win in the turn after the opponent (the opponent cannot win in this case)
4. my_strategy lose 100% of time vs nim-sum if there isn't a upperbound k for matches
- `pure_random`: pick a random row and select random matches (matches < k)
- `shortest_row`: take the shortest row and select random matches if row elements > k otherwise close the row selecting all 
- `optimal_solution`: nim-sum solution used by professor in class that use brute forcethe row elements

##### Results vs shortest row
- INFO:root:Game played = 10: Winrate 1° player = 100.0% 
- INFO:root:Game played = 100: Winrate 1° player = 100.0% 
- INFO:root:Game played = 1000: Winrate 1° player = 100.0% 
- INFO:root:Game played = 10: Winrate 2° player = 100.0% 
- INFO:root:Game played = 100: Winrate 2° player = 100.0% 
- INFO:root:Game played = 1000: Winrate 2° player = 100.0% 

##### Results vs pure random
- INFO:root:Game played = 10: Winrate 1° player = 100.0% 
- INFO:root:Game played = 100: Winrate 1° player = 99.0% 
- INFO:root:Game played = 1000: Winrate 1° player = 99.7% 
- INFO:root:Game played = 10: Winrate 2° player = 100.0% 
- INFO:root:Game played = 100: Winrate 2° player = 100.0% 
- INFO:root:Game played = 1000: Winrate 2° player = 99.1%

##### Results vs optimal strategy
- INFO:root:Game played = 10: Winrate 1° player = 100.0% 
- INFO:root:Game played = 100: Winrate 1° player = 92.0% 
- INFO:root:Game played = 1000: Winrate 1° player = 95.7% 
- INFO:root:Game played = 10: Winrate 2° player = 100.0% 
- INFO:root:Game played = 100: Winrate 2° player = 98.0% 
- INFO:root:Game played = 1000: Winrate 2° player = 95.8% 

## 2) Evolution Algorithm
- The file of task 1 is `2_GA.ipynb` 
Collaborator for task 3.2: Davide Aiello - [Github](https://github.com/davideaiello/CI22-23_s303296)
- The

INFO:root:The best strategy is<function GabriG_strategy at 0x000002019C1B9FC0> with 100.0% winrate (fitness)
optimal strategy vs shortest row
INFO:root:The best strategy is<function GabriG_strategy at 0x000002019C1B9F30> with 100.0% winrate (fitness)

## 3) MinMax
- Working in progress

## 4) Reinforcement learning
- Working in progress