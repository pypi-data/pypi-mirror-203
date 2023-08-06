"""
Methods:
--------
- Reset 
- Step 
- Render 
- Close 

Attributes:
-----------
- observation_space 
- action_space 
"""


import gymnasium as gym 
from typing import Callable 
from rewards_envs import CarConfig, CarGame

class CarRaceEnv(gym.Env):
    def __init__(self, mode : str, track_num : int, reward_function : Callable, car_config : CarConfig) -> None:
        self.game = CarGame(
            mode = mode, track_num=track_num, 
            reward_function=reward_function, 
            car_config=car_config
        ) 
        
        self.reset() 
    
    def reset(self, seed = None, options = None):
        super().reset(seed=seed) 
        self.game.initialize() 
    
    def step():
        """"Performs the action"""
        
    
    def render():
        raise NotImplementedError
    
    def close():
        raise NotImplementedError