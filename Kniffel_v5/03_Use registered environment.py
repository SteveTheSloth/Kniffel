import gym
from gym.envs.classic_control import KniffelEnv
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

gym.envs.register(
     id='Kniffel-v0',
     entry_point='gym.envs.classic_control:KniffelEnv',
     max_episode_steps=300,
     kwargs={'allrolls': allrolls},
)


"""env = Kniffel(allrolls)
env = DummyVecEnv([lambda: env])
env = VecMonitor(env)"""
log_path = os.path.join("RL_Kniffel", "Kniffel_PPO", "Logs")
ppo_path = os.path.join("RL_Kniffel", "Kniffel_PPO", "Models", "PPO_Kniffel")

"""model = PPO("MultiInputPolicy", env, verbose=1, tensorboard_log=log_path)

model.learn(total_timesteps=20000)"""


#model.save(ppo_path)
"""while True:
    env = Kniffel(allrolls)
    env = DummyVecEnv([lambda: env])
    env = VecMonitor(env)
    model = PPO.load(ppo_path, env)
    model.learn(total_timesteps=200000)
    model.save(ppo_path)"""

env = gym.make('Kniffel-v0')
env = DummyVecEnv([lambda: env])
model = PPO("MultiInputPolicy", env, verbose=1, tensorboard_log=log_path)
model.learn(total_timesteps=20000)


