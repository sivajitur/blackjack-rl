# Blackjack Reinforcement Learning

A reinforcement learning implementation for training an agent to play Blackjack using Q-learning with epsilon-greedy exploration.

## Overview

This project implements a classic card game (Blackjack) with a reinforcement learning agent that learns optimal playing strategies through trial and error. The agent uses Q-learning to discover the best actions (hit or stand) in different game states.

## Project Structure

- **[blackjack.py](blackjack.py)** - Core game engine implementing Blackjack rules
  - `Game` class handles deck management, card dealing, and game logic
  - Implements hand value calculation with Ace handling
  - Computes game state and rewards

- **[blackjack_rl.py](blackjack_rl.py)** - Reinforcement learning trainer
  - Uses Q-learning algorithm to train an agent
  - Epsilon-greedy exploration strategy
  - Runs 1000 training episodes to learn optimal play

- **[blackjack_ui.py](blackjack_ui.py)** - Interactive console interface
  - Play Blackjack against the dealer
  - Human player vs. computer dealer
  - Real-time game state display

- **[blackjack_rl.ipynb](blackjack_rl.ipynb)** - Jupyter notebook
  - Analysis and visualization of training results
  - Plotting agent performance over episodes

## Game Rules

- Players and dealer are dealt 2 cards initially
- Goal: Get a hand value closer to 21 than the dealer without going over
- Actions: **Hit** (take another card) or **Stand** (stop taking cards)
- Rewards:
  - `+1` for winning
  - `-1` for losing (bust or dealer wins)
  - `0` for tie
  - `+1.5` for blackjack (21 with 2 cards)

## Game State

The state representation consists of:
- Player's current hand value (2-21)
- Dealer's visible card value (2-11)
- Whether player has a usable Ace

## Reinforcement Learning Approach

**Algorithm**: Q-Learning with Epsilon-Greedy Exploration

**Hyperparameters**:
- `epsilon` (exploration rate): Starts at 1.0, decreases by 0.005 every 10 games
- `gamma` (discount factor): 0.1
- `alpha` (learning rate): 0.05

**Training**:
- 1000 episodes of self-play
- Agent learns optimal action values Q(state, action)
- Gradually transitions from exploration to exploitation

## Usage

### Play Interactively

```bash
python blackjack_ui.py
```

Follow the prompts to hit (1) or stand (any other key).

### Train the Agent

```bash
python blackjack_rl.py
```

Trains the Q-learning agent for 1000 games and prints game progression with actions and states.

### Analyze Results

Open `blackjack_rl.ipynb` in Jupyter Notebook to view training analysis and performance visualizations.

## Requirements

- Python 3.x
- NumPy
- Matplotlib (for notebook visualizations)
- Jupyter (for notebook)

## How It Works

1. **Initialization**: Deck is shuffled and 2 cards dealt to player and dealer
2. **Game Loop**: Agent decides to hit or stand based on current state
3. **Q-Value Update**: After each action, Q-values are updated using the reward and next state
4. **Exploration Decay**: As training progresses, agent relies less on random exploration
