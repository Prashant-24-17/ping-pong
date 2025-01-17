import random
import numpy as np
import matplotlib.pyplot as plt
from collections import deque
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam

from paddle import Paddle

env = Paddle()

class DQN():
    def __init__(self,action_space,state_space):
        self.actions = action_space
        self.states = state_space
        self.lr = 0.002
        self.gamma = 0.5
        self.decay = 0.995
        self.epsilon = 1
        self.epsilon_min = 0.01
        self.batch_size = 50
        self.memory = deque(maxlen=100000)
        self.model = self.build_model()
        
    def build_model(self):
        model = Sequential()
        model.add(Dense(64, input_shape=(self.states,),activation='relu'))
        model.add(Dense(64, activation='relu'))
        model.add(Dense(self.actions,activation='linear'))
        model.compile(loss='mse', optimizer=Adam(learning_rate=self.lr))
        return model
        
    def remember(self, state, action, reward , next_state , done):
        self.memory.append((state, action, reward, next_state, done))
        
    def act(self,state):
        if np.random.rand()<=self.epsilon:
            return random.randrange(self.actions)
        
        action_val  = self.model.predict(state)
        return np.argmax(action_val[0])
    
    def replay(self):
        if len(self.memory)<self.batch_size:
            return
        minibatch = random.sample(self.memory,self.batch_size)
        
        states = np.array([i[0] for i in minibatch])
        actions = np.array([i[1] for i in minibatch])
        rewards = np.array([i[2] for i in minibatch])
        next_states = np.array([i[3] for i in minibatch])
        dones = np.array([i[4] for i in minibatch])
        
        states = np.squeeze(states)
        next_states = np.squeeze(next_states)
        
        targets = rewards + self.gamma*(np.amax(self.model.predict_on_batch(next_states), axis=1))*(1-dones)
        targets_full = self.model.predict_on_batch(states)
        
        ind = np.array([i for i in range(self.batch_size)])
        targets_full[[ind],[actions]]= targets
        
        self.model.fit(states,targets_full,epochs=1, verbose=0)
        if self.epsilon>self.epsilon_min:
            self.epsilon *= self.decay
            

def train(episode):
    loss = []
    action_space = 3
    state_space = 5
    
    max_steps = 1000
    
    agent = DQN(action_space,state_space)
    
    for e in range(episode):
        state = env.reset()
        state = np.reshape(state,(1,state_space))
        score = 0
        
        for i in range(max_steps):
            action = agent.act(state)
            reward , next_state , done = env.step(action)
            score += reward
            next_state = np.reshape(next_state , (1,state_space))
            agent.remember(state,action,reward,next_state,done)
            
            state = next_state
            agent.replay()
            if done:
                print("episode: {}/{}, score: {}".format(e, episode, score))
                break
        loss.append(score)
    return loss
                
if __name__ == '__main__':
    
    ep = 100
    loss = train(ep)
    plt.plot([i for i in range(ep)], loss)
    plt.xlabel('episodes')
    plt.ylabel('reward')
    plt.show()