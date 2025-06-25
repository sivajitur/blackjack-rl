from blackjack import Game
import sys
game = Game()
state, reward = game.deal()

print("Player Hand: \t", game.player_hand)
print("Player Value: \t", game.calc_value_of_hand(game.player_hand))
print("Dealer Hand: \t", game.dealer_hand[0])
print("Dealer Value: \t", game.calc_value_of_hand([game.dealer_hand[0]]))
print('Initial State:\t', state)
print('Initial Reward:\t', reward)
if reward > 0:
    print('you win')
    sys.exit()
elif reward < 0:
    print('you lose')
    sys.exit()

action = "hit"
while reward == 0 or action == "hit":
    action = input("Enter hit or stand here:\t")
    if action != 'hit':
        break
    state, reward = game.make_action(action)
    print("Player Hand: \t", game.player_hand)
    print("Player Value: \t", game.calc_value_of_hand(game.player_hand))
    print("Dealer Hand: \t", game.dealer_hand[0])
    print("Dealer Value: \t", game.calc_value_of_hand([game.dealer_hand[0]]))
    print('State:\t', state)
    print('Reward:\t', reward)
    if reward < 0:
        print('you lose')
        sys.exit()

print("\n-------------------------\n")
print("Dealer Hand: \t", game.dealer_hand)
print("Dealer Value: \t", game.calc_value_of_hand(game.dealer_hand))
#while reward == 0:
#    state, reward = game.make_action("hit")
#    print(state)
#    print(reward)
state, reward = game.dealer_hits()
print("\n-------------------------\n")

print("Player Hand: \t", game.player_hand)
print("Player Value: \t", game.calc_value_of_hand(game.player_hand))
print("Dealer Hand: \t", game.dealer_hand)
print("Dealer Value: \t", game.calc_value_of_hand(game.dealer_hand))
print('Final State:\t', state)
print('Final Reward:\t', reward)

if reward > 0:
    print('you win')
    sys.exit()
elif reward < 0:
    print('you lose')
    sys.exit()

