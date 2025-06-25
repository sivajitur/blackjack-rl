from blackjack import Game
import random

state_quality = dict()

game = Game()
state, reward = game.deal() 
state_quality[state] = []
state, curr_reward = game.make_action(0)
new_state, future_reward = game.make_action(1)
state_quality[state] = [curr_reward, future_reward]

print(state_quality)




# dict
# Key = state
# Value = [q(state, stand), q(state, hit)]