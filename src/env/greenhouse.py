import sys
sys.path.append('C:/Users/giaco/Desktop/repos/wonderful-salad/src')
import gymnasium as gym
from gymnasium import spaces
import numpy as np
from env.update_environment import _update_environment
from env.reward_function import reward_function

class SaladGreenHouse(gym.Env):
    def __init__(self):
        super().__init__()
        
        self.action_space = gym.spaces.Box(low = np.array([0, -10, 0]), high = np.array([10, 10, 100]), 
                                       dtype = np.float32)
        self.observation_space = gym.spaces.Dict({
            "time": gym.spaces.Discrete(1440),
            "solar_light": gym.spaces.Box(low = 0, high = 1, shape=(1,), dtype=np.float32),
            "artificial_light": gym.spaces.Box(low = 0, high = 1, shape=(1,), dtype=np.float32),
            "soil_moisture": gym.spaces.Box(low=0, high=1, shape=(1,), dtype=np.float32),
            "temperature": gym.spaces.Box(low=5, high=25, shape=(1,), dtype=np.float32)
        })
        
        self.reward_range = (-np.inf, np.inf)
        self.state = None
        self.reset()
        
    def reset(self):
        self.time = 0
        self.solar_light = 0
        self.artificial_light = 0
        self.soil_moisture = 0
        self.temperature = 15
        
        self.state = {
            "time": np.array([self.time], dtype= np.float32),  # Inizio del giorno
            "solar_light": np.array([self.solar_light], dtype= np.float32),
            "artificial_light": np.array([self.artificial_light], dtype= np.float32),
            "soil_moisture": np.array([self.soil_moisture], dtype= np.float32),  # Inizialmente il terreno è ben irrigato
            "temperature": np.array([self.temperature], dtype= np.float32)  # Temperatura iniziale della giornata
        }
        return self.state
    
    def step(self, action):
        time, solar_light, artificial_light, soil_moisture, temperature = _update_environment(self, action)
        
        self.state = {
            "time": np.array([time], dtype= np.float32),  # Inizio del giorno
            "solar_light": np.array([solar_light], dtype= np.float32),
            "artificial_light": np.array([artificial_light], dtype= np.float32),
            "soil_moisture": np.array([soil_moisture], dtype= np.float32),  # Inizialmente il terreno è ben irrigato
            "temperature": np.array([temperature], dtype= np.float32)  # Temperatura iniziale della giornata
        }

        reward = reward_function(self.state, action)
        
        terminated = time >= 1439
        truncated = False
        info={}
        
        return self.state, reward, truncated, terminated, info
        
    def render(self, mode="human", close=False):
        pass
    def close(self):
        pass
    def seed(self, seed=None):
        pass