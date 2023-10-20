# Import gym stuff
import gym
from gym import Env
from gym.spaces import Discrete, Box, Dict, Tuple, MultiBinary, MultiDiscrete

# Import helpers
import numpy as np
import random
import os
from collections import Counter

# Import stable baselines stuff
from stable_baselines3.ppo.ppo import PPO
from stable_baselines3.common.vec_env.dummy_vec_env import DummyVecEnv
from stable_baselines3.common.evaluation import evaluate_policy
from stable_baselines3.common.env_checker import check_env
from stable_baselines3.common.monitor import Monitor


class Dice:
    def __init__(self, index=0, value=None, kept=False):
        self.index = index
        self.value = value
        if self.value == None:
            self.value = random.randrange(1, 7)
        self.kept = kept

    def roll(self):
        """Assign a new value to individual die."""
        if self.kept == False:
            self.value = random.randrange(1, 7)

    def keep(self):
        """Change kept-status of individual die."""
        self.kept = not self.kept
        
    def __eq__(self, other):
        return self.value == other.value
    
    def __lt__(self, other):
        return self.value < other.value
    
    def __gt__(self, other):
        return self.value > other.value


class Scoresheet:
    def __init__(self, standard=True):
        self.standard = standard
        if self.standard:
            self.maxrounds = 12
            
    @staticmethod
    def standard_scores():
        """Get a dictionary with formulas for each scoring option."""
        scores = {
            1: (
                lambda result: sum(
                    [x for x in result if x == 1 and result.count(1) > 0]
                )
            ),
            2: (
                lambda result: sum(
                    [x for x in result if x == 2 and result.count(2) > 0]
                )
            ),
            3: (
                lambda result: sum(
                    [x for x in result if x == 3 and result.count(3) > 0]
                )
            ),
            4: (
                lambda result: sum(
                    [x for x in result if x == 4 and result.count(4) > 0]
                )
            ),
            5: (
                lambda result: sum(
                    [x for x in result if x == 5 and result.count(5) > 0]
                )
            ),
            6: (
                lambda result: sum(
                    [x for x in result if x == 6 and result.count(6) > 0]
                )
            ),
            7: (
                lambda result: sum(result)
                if [x for x in result if result.count(x) >= 3] != []
                else 0
            ),
            8: (
                lambda result: sum(result)
                if [x for x in result if result.count(x) >= 4] != []
                else 0
            ),
            9: (
                lambda result: 25
                if (
                    result.count(sorted(result)[0]) >= 2
                    and result.count(sorted(result)[-1]) >= 2
                    and result.count(sorted(result)[0])
                    + result.count(sorted(result)[-1])
                    >= 5
                )
                else 0
            ),
            10: (
                lambda result: 30
                if [
                    x
                    for x in [1, 2, 3]
                    if x in result
                    and x + 1 in result
                    and x + 2 in result
                    and x + 3 in result
                ]
                != []
                else 0
            ),
            11: (
                lambda result: 40
                if [
                    x
                    for x in [1, 2]
                    if x in result
                    and x + 1 in result
                    and x + 2 in result
                    and x + 3 in result
                    and x + 4 in result
                ]
                != []
                else 0
            ),
            12: (lambda result: 50 if result.count(result[0]) == 5 else 0),
            13: (lambda result: sum(result))
        }
        return scores

class ActionSpace:
    
    @staticmethod    
    def roll_all(game):
        game.roll_all()
       
    @staticmethod
    def keep_1(game):
        game.dicelist[0].keep()
        game.roll_all()
    
    @staticmethod   
    def keep_2(game):
        game.dicelist[1].keep()
        game.roll_all()
    
    @staticmethod    
    def keep_3(game):
        game.dicelist[2].keep()
        game.roll_all()
    
    @staticmethod    
    def keep_4(game):
        game.dicelist[3].keep()
        game.roll_all()
    
    @staticmethod    
    def keep_5(game):
        game.dicelist[4].keep()
        game.roll_all()
        
    @staticmethod    
    def keep_12(game):
        game.dicelist[0].keep()
        game.dicelist[1].keep()
        game.roll_all()
        
    @staticmethod    
    def keep_13(game):
        game.dicelist[0].keep()
        game.dicelist[2].keep()
        game.roll_all()
        
    @staticmethod    
    def keep_14(game):
        game.dicelist[0].keep()
        game.dicelist[3].keep()
        game.roll_all()
        
    @staticmethod    
    def keep_15(game):
        game.dicelist[0].keep()
        game.dicelist[4].keep()
        game.roll_all()
        
    @staticmethod    
    def keep_23(game):
        game.dicelist[1].keep()
        game.dicelist[2].keep()
        game.roll_all()
        
    @staticmethod    
    def keep_24(game):
        game.dicelist[1].keep()
        game.dicelist[3].keep()
        game.roll_all()
        
    @staticmethod    
    def keep_25(game):
        game.dicelist[1].keep()
        game.dicelist[4].keep()
        game.roll_all()
        
    @staticmethod    
    def keep_34(game):
        game.dicelist[2].keep()
        game.dicelist[3].keep()
        game.roll_all()
        
    @staticmethod    
    def keep_35(game):
        game.dicelist[2].keep()
        game.dicelist[4].keep()
        game.roll_all()
        
    @staticmethod    
    def keep_45(game):
        game.dicelist[3].keep()
        game.dicelist[4].keep()
        game.roll_all()
    
    @staticmethod
    def keep_123(game):
        game.dicelist[0].keep()
        game.dicelist[1].keep()
        game.dicelist[2].keep()
        game.roll_all()
            
    @staticmethod        
    def keep_124(game):
        game.dicelist[0].keep()
        game.dicelist[1].keep()
        game.dicelist[3].keep()
        game.roll_all()
        
    @staticmethod    
    def keep_125(game):
        game.dicelist[0].keep()
        game.dicelist[1].keep()
        game.dicelist[4].keep()
        game.roll_all()
        
    @staticmethod    
    def keep_134(game):
        game.dicelist[0].keep()
        game.dicelist[2].keep()
        game.dicelist[3].keep()
        game.roll_all()
        
    @staticmethod    
    def keep_135(game):
        game.dicelist[0].keep()
        game.dicelist[2].keep()
        game.dicelist[4].keep()
        game.roll_all()
        
    @staticmethod    
    def keep_145(game):
        game.dicelist[0].keep()
        game.dicelist[3].keep()
        game.dicelist[4].keep()
        game.roll_all()
        
    @staticmethod    
    def keep_234(game):
        game.dicelist[1].keep()
        game.dicelist[2].keep()
        game.dicelist[3].keep()
        game.roll_all()
        
    @staticmethod    
    def keep_235(game):
        game.dicelist[1].keep()
        game.dicelist[2].keep()
        game.dicelist[4].keep()
        game.roll_all()
        
    @staticmethod    
    def keep_245(game):
        game.dicelist[1].keep()
        game.dicelist[3].keep()
        game.dicelist[4].keep()
        game.roll_all()
        
    @staticmethod    
    def keep_345(game):
        game.dicelist[2].keep()
        game.dicelist[3].keep()
        game.dicelist[4].keep()
        game.roll_all()
        
    @staticmethod    
    def keep_1234(game):
        game.dicelist[0].keep()
        game.dicelist[1].keep()
        game.dicelist[2].keep()
        game.dicelist[3].keep()
        game.roll_all()
    
    @staticmethod    
    def keep_1235(game):
        game.dicelist[0].keep()
        game.dicelist[1].keep()
        game.dicelist[2].keep()
        game.dicelist[4].keep()
        game.roll_all()
    
    @staticmethod    
    def keep_1245(game):
        game.dicelist[0].keep()
        game.dicelist[1].keep()
        game.dicelist[3].keep()
        game.dicelist[4].keep()
        game.roll_all()
    
    @staticmethod    
    def keep_1345(game):
        game.dicelist[0].keep()
        game.dicelist[2].keep()
        game.dicelist[3].keep()
        game.dicelist[4].keep()
        game.roll_all()
    
    @staticmethod    
    def keep_2345(game):
        game.dicelist[1].keep()
        game.dicelist[2].keep()
        game.dicelist[3].keep()
        game.dicelist[4].keep()
        game.roll_all()
  
class MaxBigStreet(Env):
    def __init__(self, allrolls,num_envs=1, rollcount=0):
        
        self.allrolls = allrolls
        self.num_envs = num_envs
        self.action_space = Discrete(31)
        self.observation_space = Dict({"rolls":Discrete(252)})
        self.dicelist = [Dice(), Dice(), Dice(), Dice(), Dice()]
        self.dicelist.sort()
        
        self.ACTIONS = {0: ActionSpace.roll_all,
                    1: ActionSpace.keep_1,
                    2: ActionSpace.keep_2,
                    3: ActionSpace.keep_3,
                    4: ActionSpace.keep_4,
                    5: ActionSpace.keep_5,
                    6: ActionSpace.keep_12,
                    7: ActionSpace.keep_13,
                    8: ActionSpace.keep_14,
                    9: ActionSpace.keep_15,
                    10: ActionSpace.keep_23,
                    11: ActionSpace.keep_24,
                    12: ActionSpace.keep_25,
                    13: ActionSpace.keep_34,
                    14: ActionSpace.keep_35,
                    15: ActionSpace.keep_45,
                    16: ActionSpace.keep_123,
                    17: ActionSpace.keep_124,
                    18: ActionSpace.keep_125,
                    19: ActionSpace.keep_134,
                    20: ActionSpace.keep_135,
                    21: ActionSpace.keep_145,
                    22: ActionSpace.keep_234,
                    23: ActionSpace.keep_235,
                    24: ActionSpace.keep_245,
                    25: ActionSpace.keep_345,
                    26: ActionSpace.keep_1234,
                    27: ActionSpace.keep_1235,
                    28: ActionSpace.keep_1245,
                    29: ActionSpace.keep_1345,
                    30: ActionSpace.keep_2345,
                    }
        
    def step(self, action):
        self.ACTIONS[action](self)
        self.dicevalues = [i.value for i in self.dicelist]
        observation = {"rolls":self.allrolls.index(tuple(self.dicevalues))}
        info = {}
        for x in [1, 2]:
            if x in self.dicevalues and x + 1 in self.dicevalues and x + 2 in self.dicevalues and x + 3 in self.dicevalues and x + 4 in self.dicevalues:
                
                
                return observation, 1, True, info
        
        return observation, -1, True, info
        

        
    def reset(self):
        
        self.dicelist = [Dice(), Dice(), Dice(), Dice(), Dice()]
        self.dicelist.sort()
        values = tuple([i.value for i in self.dicelist])
        observation = {"rolls":self.allrolls.index(values)}
        return observation
    
    def render(self):
        pass
        
    def unkeep(self):
        for i in self.dicelist:
            i.kept = False
                    
    def roll_all(self):
        for i in self.dicelist:
            i.roll()
        self.dicelist.sort()



def golearn(allrolls):
    log_path = os.path.join("RL_Kniffel", "Kniffel_PPO", "LogBigStreet")
    ppo_path = os.path.join("RL_Kniffel", "Kniffel_PPO", "Models", "PPO_MaxBigStreet")


    env = MaxBigStreet(allrolls)
    env = Monitor(env)
    model = PPO("MultiInputPolicy", env, verbose=1, tensorboard_log=log_path)
    model.learn(total_timesteps=4000000)
    model.save(ppo_path)
    


ppo_path = os.path.join("RL_Kniffel", "Kniffel_PPO", "Models", "PPO_MaxBigStreet")
model = PPO.load(ppo_path)

# Deploy the model 


allrolls = list()
for i in range(1, 7):
    for j in range (1, 7):
        for k in range ( 1, 7):
            for l in range (1, 7):
                for m in range (1, 7):
                    roll = [i, j, k, l, m]
                    allrolls.append(roll)
                    
for index, i in enumerate(allrolls):
    i.sort()
    allrolls[index] = tuple(i)
    
allrolls = list(dict.fromkeys(allrolls))

env = MaxBigStreet(allrolls)
episodes = 10

for episode in range(1, episodes+1):
    obs = env.reset()
    done = False
    score = 0

    while not done:
        env.render()
        print([i.value for i in env.dicelist])
        action, next_state = model.predict(obs)     # Now using model here. Predict method returns two values: aciton and next state
        print(action)
        
        obs, reward, done, info = env.step(action)
        print([i.value for i in env.dicelist])
        score += reward
    print("Episode:{} Score:{}".format(episode, score))