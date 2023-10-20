# Import gym stuff
import gym
from gym.vector import VectorEnv
from gym.spaces import Discrete, Box, Dict, Tuple, MultiBinary, MultiDiscrete

# Import helpers
import numpy as np
import random
import os

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
            self.value = random.randint(1, 6)
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
            
    @staticmethod
    def standard_scores():
        """Get a dictionary with formulas for each scoring option."""
        scores = {
            1: (
                lambda result: result.count(1)
            ),
            2: (
                lambda result: result.count(2)*2
            ),
            3: (
                lambda result: result.count(3)*3
            ),
            4: (
                lambda result: result.count(4)*4
            ),
            5: (
                lambda result: result.count(5)*5
            ),
            6: (
                lambda result: result.count(6)*6
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
                    result.count(result[0]) >= 2
                    and result.count(result[-1]) >= 2
                    and result.count(result[0])
                    + result.count(result[-1])
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
        
    
class Kniffel(VectorEnv):
    
    def __init__(self, allrolls, num_envs=1):
        
        self.allrolls = allrolls
        self.num_envs = num_envs
        self.past_states = dict()
        self.action_space = Discrete(44)
        self.observation_space = Dict({"rolls":Discrete(252), "rollcount":Discrete(3), "taken_scores":MultiBinary(13), "bonus":Discrete(2)})
        self.rollactions = {0: ActionSpace.roll_all,
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
        self.rollcount = 0
        self.scored = dict()
        self.has_bonus = False
        self.dicelist = [Dice(), Dice(), Dice(), Dice(), Dice()]
        self.start_turn()
        
    def step(self, action, observation=None):
        #print(action)
        info = {}
        done = False
        self.options_take()
        if action <= 30:
            if self.rollcount == 2:
                return self.get_observation(), -100, True, info
            else:
                self.rollactions[action](self)
                self.rollcount += 1
                self.dicelist.sort()
                self.unkeep()
                self.options_take()
                obs = self.get_observation()
                return obs, 0.1, done, info
            
        elif 30 < action <= 43:
            if action-30 in self.scored:
                return self.get_observation(), -100, True, info
            elif action-30 in self.options:
                self.scored[action-30] = self.options[action-30]
                self.calc_top()
                self.calc_total()
                if len(self.scored) == 13:
                    #print(self.total)
                    return self.get_observation(), self.calc_reward_take(action-30) + self.total//150, True, info
                self.rollcount = 0
                self.start_turn()
                obs = self.get_observation()
                return obs, self.calc_reward_take(action-30), done, info
            else:
                self.scored[action-30] = 0
                self.calc_top()
                self.calc_total()
                if len(self.scored) == 13:
                    #print(self.total)
                    return self.get_observation(), -0.5 + self.total//150, True, info
                self.rollcount = 0
                self.start_turn()
                obs = self.get_observation()
                return obs, -0.5, done, info
                
      
    def calc_reward_take(self, taken_option):
        if taken_option <= 6:
            if self.scored[taken_option] >= taken_option * 3 or self.has_bonus:
                return 1
            else:
                return 0
        elif self.scored[taken_option] >= 18:
            return 1
        else:
            return 0
        
        
          
    def reset(self):
        self.scored = dict()
        self.rollcount = 0
        self.has_bonus = False
        self.start_turn()
        return self.get_observation()
        
    def render(self):
        pass
    
    def unkeep(self):
        for i in self.dicelist:
            i.kept = False

    def roll_all(self):
        for i in self.dicelist:
            i.roll()
        
    def start_turn(self):
        if self.rollcount == 0: # If start of round, there is no choice.
            self.unkeep()
            self.roll_all()
            self.dicelist.sort()
            self.dicevalues = [i.value for i in self.dicelist]
            self.options_take()
            
    def options_take(self):
        """Return scoring options depending on roll."""
        self.options = dict()
        for key, value in Scoresheet.standard_scores().items():
            if key not in self.scored:
                if value(self.dicevalues) != 0:
                    self.options[key] = value(self.dicevalues)
                    
    def calc_top(self):
        top = 0
        for i in range (1, 7):
            if i in self.scored.keys():
                top += self.scored[i]
        if top >= 63:
            self.has_bonus = True
        
    def calc_total(self):
        total = 0
        for i in self.scored.keys():
            total += self.scored[i]
        if self.has_bonus:
            total += 35
        self.total = total
        
    def get_observation(self):
        values = tuple([i.value for i in self.dicelist])
        scored = list()
        for i in range(1, 14):
            if i not in self.scored:
                scored.append(0)
            else:
                scored.append(1)
        observation = {"rolls":self.allrolls.index(values), "rollcount":self.rollcount, "taken_scores":np.array(scored), "bonus":int(self.has_bonus)}
        return observation
    

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

        
"""env = Kniffel(allrolls)
env = DummyVecEnv([lambda: env])
env = VecMonitor(env)"""
log_path = os.path.join("RL_Kniffel", "Kniffel_PPO", "LogsVectorized")
ppo_path = os.path.join("RL_Kniffel", "Kniffel_PPO", "Models", "PPO_Kniffel_v8_vectorized8_rewfunct_nowrongturns")

"""model = PPO("MultiInputPolicy", env, verbose=1, tensorboard_log=log_path)

model.learn(total_timesteps=20000)"""


#model.save(ppo_path)
"""while True:
    env = Kniffel(allrolls, num_envs=8)
    env = Monitor(env)
    model = PPO.load(ppo_path, env)
    model.learn(total_timesteps=200000)
    model.save(ppo_path)"""

env = Kniffel(allrolls, num_envs=8)
env = Monitor(env)
"""model = PPO("MultiInputPolicy", env, verbose=1, tensorboard_log=log_path)
model.learn(total_timesteps=200000)
model.save(ppo_path)"""
model = PPO.load(ppo_path, env)
model.learn(total_timesteps=12000000)
model.save(ppo_path)
"""    
while True:
    model = PPO.load(ppo_path, env)
    model.learn(total_timesteps=200000)
    model.save(ppo_path)"""