# Target-UCB

targetUCB.py is a simple class implementing of the Target-UCB bandit algorithm, as introduced in the AAAI-19 technical paper _Leveraging observations in bandits: Between risks and benefits_.

To import the Target-UCB class, simply use the command "from targetUCB import TUCB".

An example of how to construct and test a clique of 4 Target-UCB agents is also provided. 
Executing the targetUCB.py file as a script will run this clique for 100 episodes on a two-armed bandit problem and display the cumulative regret of all 4 agents.


# Human bandit dataset

The folder contains human player data for a two-armed bandit setting. All runs are composed of 100 episodes (1 arm selection followed by 1 reward received).

1. The "single_humans" folder contains data for 4 individual human players on a two armed bandit setting with arms A and B and the following specifications:
	- Both arms have static Bernoulli distributions.
	- Arm A has a "win" probability of 0.4
	- Arm B has a "win" probability of 0.6 (optimal)

2. The "cliques" folder contains data for 2 cliques (clique_1 and clique_2) of 4 human players on a two armed bandit setting with arms A and B and the following specifications:
	- Both arms have static Bernoulli distributions.
	- Arm A has a "win" probability of 0.6 (optimal)
	- Arm B has a "win" probability of 0.4

   The experiment was run in the following way:
	- At each episode, players picked an arm and received a reward.
	- After all players chose an arm for that episode, the arm chosen by each player was displayed for all players.
	- Players were in the same room on different computers, but did not know which person was associated with which player number (e.g. nobody except Player 1 knew who was Player 1)
	- Players could never see the rewards obtained by other players. 
	- clique_1 and clique_2 are composed of entirely different people.

3. For each experiment, the data is provided both as a .xlsx file with two sheets and as two .csv files. 
	- The "Plays" sheets corresponds to the *_plays.csv files whereas the "Full Results" sheets correspond to the *_full_results.csv files.
	- Plays sheets/files contain only the action chosen by each player at each episode, organized in columns in sequential order.
	- Full Results sheets/files contain both the action chosen and the corresponding reward received by each player.


   All .csv files are composed of 102 records (rows).
	- The first record contains the player ID(s)
	- The second record contains descrition of each column: "Arm" represents the arm chosen by the player. "Reward" represents the reward corresponding to the arm played (only for *_full_results.csv files).
	- The other 100 records each correspond to one episode (arm selection and reward received), in sequential order. Each record is of the form:
		- [Arm] or [Arm, Reward] for single player runs
		- [Arm P1, ..., Arm P4] or [Arm P1, Reward P1, ..., Arm P4, Reward P4] for cliques with players P1 to P4.
