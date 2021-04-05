import numpy as np

class Environment:
    cliff = -3
    road = -1
    goal = 1

    goal_position = [2, 2]

    reward_list = [[road, road, road], [road, road, road], [road, road, goal]]
    reward_list1=[["road", "road", "road"],["road","road","road"],["road","road","goal"]]

    def __init__(self):
        self.reward=np.array(self.reward_list)

    def move(self, agent, action):
        '''
            action=0,1,2,3
            agent.action=np.array([[-1,0],[0,1],[1,0],[0,-1]])
            위, 오른쪽, 아래, 왼쪽
        '''
        new_pos=agent.pos+agent.action[action]

