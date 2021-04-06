import numpy as np


class Environment:
    cliff = -3
    road = -1
    goal = 1

    goal_position = [2, 2]

    reward_list = [[road, road, road], [road, road, road], [road, road, goal]]
    reward_list1 = [["road", "road", "road"], ["road", "road", "road"], ["road", "road", "goal"]]

    def __init__(self):
        self.reward = np.array(self.reward_list)

    def move(self, agent, action):
        '''
            action=0,1,2,3
            agent.action=np.array([[-1,0],[0,1],[1,0],[0,-1]])
            위, 오른쪽, 아래, 왼쪽
        '''
        done = False
        #현재 위치가 goal일때
        if

        new_pos = agent.pos + agent.action[action]

        observation = 1  # 움직인 후 위치, 그리드 밖이거나 goal이면 안움직임.
        return observation, reward, done


class Agent:
    action = np.array([[-1, 0], [0, 1], [1, 0], [0, -1]])
    select_action_pr=np.array([0.25, 0.25, 0.25, 0.25])

    def __init__(self, initial_position):
        self.pos=initial_position

    def set_pos(self, position):
        self.pos=position
        return self.pos

    def get_pos(self):
        return self.pos