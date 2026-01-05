from blackjack import Game
import numpy as np
import random
from collections import defaultdict

epsilon = 1
gamma = 0.1
alpha = 0.05

Q = defaultdict(lambda: [0,0])
td_total = list()

def decideAction(state):
    outcomes = ["Off Policy", "On Policy"]
    probabilities = [epsilon, 1-epsilon] 

    # Sample two outcomes with replacement
    decision = random.choices(outcomes, weights=probabilities, k=1)[0]
    if decision == "Off Policy":
        return random.sample([0,1], 1)[0]
    elif decision == "On Policy":
        return np.argmax(Q[state])

for i in range(1,1000):
    print("Game ", i)
    if i%10 == 0:
        epsilon -= 0.005
    game = Game()
    state, initial_reward = game.deal()
    didPlayerFinishTurn = False
    print("\tPlayer Hand: \t", game.player_hand)
    print("\tPlayer Value: \t", game.calc_value_of_hand(game.player_hand))
    print("\tDealer Hand: \t", game.dealer_hand)
    print("\tDealer Value: \t", game.calc_value_of_hand(game.dealer_hand))
    print('\tInitial State:\t', state)
    print('\tInitial Reward:\t', initial_reward)


    while game.is_game_over(didPlayerFinishTurn) is False:
        action = decideAction(state)
        if action == 0:
            print("\t\tAction: \t Stand")
            didPlayerFinishTurn = True
        elif action == 1:
            print("\t\tAction: \t Still HIT DOE!!!!")
        
        next_state, current_reward = game.make_action(action)
        print("\t\t\tPlayer Hand: \t", game.player_hand)
        print("\t\t\tPlayer Value: \t", game.calc_value_of_hand(game.player_hand))
        print("\t\t\tDealer Hand: \t", game.dealer_hand)
        print("\t\t\tDealer Value: \t", game.calc_value_of_hand(game.dealer_hand))
        print('\t\t\tState:\t', state)
        print('\t\t\tReward:\t', current_reward)

        if game.calc_value_of_hand(game.player_hand) > 21:
            didPlayerFinishTurn = True
        
        Q_old = Q[state][action]
        td = current_reward + gamma * max(Q[next_state]) - Q_old
        Q[state][action] = Q_old + alpha * td
        print('\tQ: \t', Q)
        state = next_state
        td_total.append(td)