import gym
from nes_py.wrappers import JoypadSpace
from gym_super_mario_bros.actions import SIMPLE_MOVEMENT

# Setup game
env = gym.make('SuperMarioBros-v0')
env = JoypadSpace(env, SIMPLE_MOVEMENT)

# Reset the environment
state = env.reset()

for step in range(100000):
    action = env.action_space.sample()  # Random action
    state, reward, done, info = env.step(action)
    
    env.render()  # This will render the environment
    
    if done:
        state = env.reset()

env.close()