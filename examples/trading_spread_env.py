"""
The aim of this file is to give a standalone example of how an environment  runs.
"""
import os
import numpy as np
from tgym.core import DataGenerator
from tgym.envs.trading_spread import SpreadTrading
from tgym.gens.deterministic import WavySignal

generator = WavySignal(period_1=25, period_2=50, epsilon=-0.5)

episode_length = 200
trading_fee = 0.2
time_fee = 0
# history_length number of historical states in the observation vector.
history_length = 2

environment = SpreadTrading(spread_coefficients=[1],
                            data_generator=generator,
                            trading_fee=trading_fee,
                            time_fee=time_fee,
                            history_length=history_length,
                            episode_length=episode_length)

environment.render()
i = 0
while True:
    #action = input("Action: Buy (b) / Sell (s) / Hold (enter): ")
    
    # if action == 'b':
    #     action = [0, 1, 0]
    # elif action == 's':
    #     action = [0, 0, 1]
    # else:
    #     action = [1, 0, 0]
    action = [0, 1, 0] if i%7 == 0 else ([0, 0, 1] if i%13 == 0 else [1, 0, 0])
    
    environment.step(action)
    environment.render()
    i += 1