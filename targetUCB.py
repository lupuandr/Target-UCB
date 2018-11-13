import numpy as np
import random

class TUCB():
    '''Simple class implementing the Target-UCB algorithm on a two-armed bandit.'''
    
    def __init__(self, nbr_neighbours):
        if(nbr_neighbours < 1):
            print("Error: at least one neighbour required")
            return -1
        
        #number of neighbours
        self.N = nbr_neighbours
        
        #number of own plays for arms 0 and 1
        self.n = [0,0]
        
        #number of target plays (averaged over neighbours)
        self.T = [0,0]
        
        #average reward
        self.avg_r = [0,0]
        
        #step (play) number
        self.t = 0
        
        #cumulative regret
        self.cumul_regret = []
        
        #np.random.seed(1)
    
    def getNextAction(self, nbr_actions = []):
        '''Takes list of previous play actions from neighbours and outputs a new action'''
        
        self.t += 1
        
        if(len(nbr_actions) != self.N):
            print("Error: Number of neighbours and number of neighbour actions does not match")
            return -1
        #update target plays
        if(self.t > 1):
            for a in nbr_actions:
                if(a == 0):
                    self.T[0] += 1/self.N
                elif(a == 1):
                    self.T[1] += 1/self.N
        
        if(self.n[0] == 0):
            #play arm 0 for the first time
            action = 0
        elif(self.n[1] == 0):
            #play arm 1 for the first time
            action = 1
        else:            
            #get estimation optimism:
            est_opt = [0,0]
            est_opt[0] = np.sqrt(2*np.log(self.t)/self.n[0])
            est_opt[1] = np.sqrt(2*np.log(self.t)/self.n[1])
            
            #get target optimism
            target_opt = [0,0]
            target_opt[0] = np.sqrt((self.T[0]-self.n[0])/self.T[0]) if ((self.T[0]-self.n[0]) > 0) else 0
            target_opt[1] = np.sqrt((self.T[1]-self.n[1])/self.T[1]) if ((self.T[1]-self.n[1]) > 0) else 0
            
            #get action values
            Q = [0,0]
            Q[0] = self.avg_r[0] + est_opt[0]*target_opt[0]
            Q[1] = self.avg_r[1] + est_opt[1]*target_opt[1]
            
            #get action
            if (Q[0] != Q[1]):
                action = np.argmax(Q)
            else:
                #tie breaker
                action = random.choice([0,1])
        
        step_reward = self.getReward(action)
        
        #update values
        if(action == 0):
            self.n[0] += 1
            self.avg_r[0] += (step_reward - self.avg_r[0])/self.n[0]
            
            #no added regret since arm 0 is optimal
            step_regret = 0
        elif(action == 1):
            self.n[1] += 1
            self.avg_r[1] += (step_reward - self.avg_r[1])/self.n[1]
            
            #add regret, where 0.2 is the gap between arms
            step_regret = 0.2
        
        if(self.t > 1):
            self.cumul_regret.append(self.cumul_regret[-1] + step_regret)
        else:
            self.cumul_regret.append(step_regret)
        
        return action
        
    def getReward(self, arm_played):
        '''Returns a reward from a Bernoulli distribution associated with the arm'''
        
        #determines arm win rate. Arm 0 is optimal.
        win_rate = [0.6, 0.4]
        
        pull = np.random.rand()
        
        if(arm_played == 0 and pull < win_rate[0]):
            #win
            return 1
        elif(arm_played == 1 and pull < win_rate[1]):
            #win
            return 1
        else:
            #loss
            return 0        

def main():
    import matplotlib.pyplot as plt
    
    '''Runs a fully-connected graph of 4 TUCB agents for 100 plays'''
    agents = []
    actions = []
    
    for i in range(0,4):
        agents.append(TUCB(3))
        actions.append(0)
    #get 100 runs
    for t in range(0,100):
        #copy list of previous action
        prev_act = list(actions)

        for i in range(0,len(agents)):
            actions[i] = agents[i].getNextAction(prev_act[0:i]+prev_act[(i+1):])
     
    plt.figure(figsize=(12,8))
    i=1
    for a in agents:
        plt.plot(a.cumul_regret, label = "Agent " + str(i))
        i += 1
    plt.xlabel("Plays", fontsize = 14)
    plt.ylabel("Cumulative regret", fontsize = 14)
    plt.xticks(fontsize = 14)
    plt.yticks(fontsize = 14)
    plt.legend(fontsize = 14)
    plt.title("Cumulative Regret of 4 TUCB Agents in a Fully Connected Graph", fontsize = 20)
    plt.show()
    

if __name__ == "__main__":
    main()



