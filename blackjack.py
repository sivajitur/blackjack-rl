import random
import itertools

class Game:
    def __init__(self):
        suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
        value = ["A"] + list(range(2,11)) + ["J"] + ["Q"] + ["K"]
        self.deck = list(itertools.product(value, suits))
        self.player_hand = None
        self.dealer_hand = None
    
    
    def is_game_over(self, didPlayerFinishTurn):
        player_value = self.calc_value_of_hand(self.player_hand)
        dealer_value = self.calc_value_of_hand(self.dealer_hand)

        # If player hits 21, game should end immediately
        if player_value == 21:
            return True

        # If player busts, game ends
        if player_value > 21:
            return True

        # If dealer busts, game ends
        if dealer_value > 21:
            return True

        # If both have 21, game ends
        if player_value == 21 and dealer_value == 21:
            return True

        # If player stands, check if dealer has finished
        if didPlayerFinishTurn:
            if dealer_value >= 17:
                return True

        return False

    def calc_value_of_hand(self, hand):
        total = 0
        aces = 0

        for value, suit in hand:
            if isinstance(value, int):
                total += value
            elif value in ["J", "Q", "K"]:
                total += 10
            elif value == "A":
                total += 11
                aces += 1

        # Adjust for multiple Aces if total > 21
        while total > 21 and aces:
            total -= 10
            aces -= 1

        return total

    """
    def calc_value_of_hand(self, hand):
        sum = 0
        if len(hand) > 1:                      # Player's Hand
            for card in hand:
                value, suit = card
                if value in ["J", "Q", "K"]:
                    sum += 10
                elif value == "A":
                    sum += 11
                else:
                    sum += value

            if any(card[0] == 'A' for card in hand) and sum > 21:
                sum -= 10


        elif len(hand) == 1:                    # Dealer's Hand that is shown to player
            for value, suits in hand:
                if value in ["J", "Q", "K"]:
                    sum += 10
                elif value == "A":
                    sum += 11
                    if sum > 21:
                        sum -= 10
                else:
                    sum += value
        
        return sum
    """
    def get_state(self) -> (int, int, bool):
        player_value = self.calc_value_of_hand(self.player_hand)
        dealer_value = self.calc_value_of_hand([self.dealer_hand[0]]) #only the shown card
        do_i_have_an_ace = any(card[0] == 'A' for card in self.player_hand)
        return player_value, dealer_value, do_i_have_an_ace

    
    def get_reward(self):
        if (self.calc_value_of_hand(self.player_hand) == 21 and self.calc_value_of_hand(self.dealer_hand) == 21):
            return 0
        elif (self.calc_value_of_hand(self.player_hand) == 21 or self.calc_value_of_hand(self.dealer_hand) > 21):
            return 1
        elif (self.calc_value_of_hand(self.dealer_hand) == 21 or self.calc_value_of_hand(self.player_hand) > 21):
            return -1
        else:
            return 0

    def get_deck(self):
        return self.deck

    def deal(self):
        random.shuffle(self.deck)
        self.player_hand = [self.deck[0], self.deck[1]]
        self.dealer_hand = [self.deck[2], self.deck[3]]
        for i in range(0,4):
            self.deck[i] = None
        if self.calc_value_of_hand(self.player_hand) == 21:
            return (self.get_state(), 1.5)
        return (self.get_state(), self.get_reward())

    def make_action(self, action):
        if action == 1: #your boy hit
            for i in range(len(self.deck)):
                if self.deck[i] is not None:
                    self.player_hand.append(self.deck[i])
                    self.deck[i] = None
                    break
            if self.calc_value_of_hand(self.player_hand) > 21:
                return self.get_state(), -1  # player busts
            return self.get_state(), self.get_reward()
        else:
            return self.dealer_hits()

    def dealer_hits(self):
        dealer_total = self.calc_value_of_hand(self.dealer_hand)

        # Dealer stands on 17 or higher
        if dealer_total >= 17:
            if dealer_total > self.calc_value_of_hand(self.player_hand):
                reward = -1
            elif dealer_total < self.calc_value_of_hand(self.player_hand):
                reward = 1
            else: 
                reward = self.get_reward()
            return self.get_state(), reward

        # Dealer hits until reaching 17 or higher
        while dealer_total < 17:
            # Find the next available card in the deck
            for i in range(len(self.deck)):
                if self.deck[i] is not None:
                    self.dealer_hand.append(self.deck[i])
                    self.deck[i] = None
                    break
            dealer_total = self.calc_value_of_hand(self.dealer_hand)
        if  self.calc_value_of_hand(self.player_hand) < 21 and self.calc_value_of_hand(self.dealer_hand) < 21:
            if self.calc_value_of_hand(self.dealer_hand) > self.calc_value_of_hand(self.player_hand):
                reward = -1
            elif self.calc_value_of_hand(self.dealer_hand) < self.calc_value_of_hand(self.player_hand):
                reward = 1
            else:
                reward = 0
        else: 
            reward = self.get_reward()
            
        return self.get_state(), reward
