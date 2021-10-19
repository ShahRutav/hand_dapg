import mj_envs
import click 
import os
import gym
import numpy as np
import pickle
from mjrl.utils.gym_env import GymEnv

DESC = '''
Helper script to visualize demonstrations.\n
USAGE:\n
    Visualizes demonstrations on the env\n
    $ python utils/visualize_demos --env_name relocate-v0\n
'''

# MAIN =========================================================
@click.command(help=DESC)
@click.option('--env_name', type=str, help='environment to load', required= True)
@click.option('--demos', type=str, help='Demonstrations', required=False, default=None)
def main(env_name, demos):
    if env_name is "":
        print("Unknown env.")
        return
    if demos == None:  
        demos = pickle.load(open('./demonstrations/'+env_name+'_demos.pickle', 'rb'))
    else : 
        demos = pickle.load(open(demos, 'rb'))
    # render demonstrations
    demo_playback(env_name, demos)

def demo_playback(env_name, demo_paths):
    e = GymEnv(env_name)
    e.reset()
    for path in demo_paths:
        e.set_env_state(path['init_state_dict'])
        actions = path['actions']
        ep_r = 0.0
        for t in range(actions.shape[0]):
            o, r, d,_ = e.step(actions[t])
            ep_r += r
            #e.env.mj_render()
        print("Episode Reward : ", ep_r)

if __name__ == '__main__':
    main()
